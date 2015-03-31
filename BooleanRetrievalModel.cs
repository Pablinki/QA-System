using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace BooleanRetrievalModel
{
    /// <summary>
    /// Implementation Simple Boolean Retrieval Model
    /// DPK 'SAMIR'
    /// </summary>
    
    class BooleanRetrievalModel
    {
        //stores distinct terms
        public static HashSet<string> distinctTerm = new HashSet<string>();
        //stores document id and its contents without splitting
        public static Dictionary<int, string> documentContentList = new Dictionary<int, string>();
        //stores document and its terms collection
        public static Dictionary<string, List<string>> documentCollection = new Dictionary<string, List<string>>();
        public static Dictionary<string, List<int>> termDocumentIncidenceMatrix = new Dictionary<string, List<int>>();
        //stop words collection
        public static List<string> stopWords = new List<string> {"ON","OF","THE","AN","A" };
        //boolean operators list
        public static string[] booleanOperator = new string[] { "AND", "OR", "NOT" };
        static void Main(string[] args)
        {
            int count = 0;
            //read all the text document on the specified directory; change this directory based on your machine
            foreach (string file in Directory.EnumerateFiles(@"C:/PruebaIRBooleano", "*.txt", SearchOption.TopDirectoryOnly))
            {
                string contents = File.ReadAllText(file);
                String[] termsCollection = RemoveStopsWords(contents.ToUpper().Split(' '));
                foreach (string term in termsCollection)
                {
                    //prepeare distinct terms collection
                    //remove stop words
                    if (!stopWords.Contains(term)) 
                    {
                        distinctTerm.Add(term);
                    }
                }

                //add document and their terms collection
                documentCollection.Add(file, termsCollection.ToList());
                //add document and its content for displaying the search result
                documentContentList.Add(count, contents);
                count++;
            }

            termDocumentIncidenceMatrix = GetTermDocumentIncidenceMatrix(distinctTerm, documentCollection);
            Console.WriteLine("Enter your boolean query");
            do{
                string query = Console.ReadLine();
                List<int> lst = ProcessQuery(query);
                count = 0;
                if (lst!=null)
                {
                    foreach (int a in lst)
                    {
                        if (a == 1)
                        {
                            Console.WriteLine(documentContentList[count]);
                        }
                        count++;
                    }
                }
                else
                {
                    Console.WriteLine("No search result found");
                }
            
            }  while(1==1);
        }

        /// <summary>
        /// Removes the query terms that doesnot appears on document
        /// </summary>
        /// <param name="str"></param>
        private static void FilterQueryTerm(ref string[] str)
        {
            List<string> _queryTerm = new List<string>();

            
            foreach (string queryTerm in str) 
            {
                if (queryTerm.ToUpper().Equals("BUT") || termDocumentIncidenceMatrix.ContainsKey(queryTerm.ToUpper()) || booleanOperator.Contains(queryTerm))
                {
                    _queryTerm.Add(queryTerm);
                   
                }
            }

            str = _queryTerm.ToArray();
        }

        //prepares Term Document Incidence Matrix
        public static Dictionary<string, List<int>> GetTermDocumentIncidenceMatrix(HashSet<string> distinctTerms,Dictionary<string,List<string>> documentCollection)
        {
            Dictionary<string, List<int>> termDocumentIncidenceMatrix = new Dictionary<string, List<int>>();
            List<int> incidenceVector = new List<int>();
            foreach (string term in distinctTerms)
            {
                //incidence vector for each terms
                incidenceVector = new List<int>();
                foreach(KeyValuePair<string ,List<string>> p in documentCollection)
                {
                    
                    if (p.Value.Contains(term))
                    {
                        //document contains the term
                        incidenceVector.Add(1); 

                    }
                    else
                    {
                        //document do not contains the term
                        incidenceVector.Add(0); 
                    }
                }
                termDocumentIncidenceMatrix.Add(term, incidenceVector);

            }
            return termDocumentIncidenceMatrix;
        }


        //removes all stop words
        public static string[] RemoveStopsWords(string[] str)
        {
            List<string> terms = new List<string>();
            foreach (string term in str)
            {
                if (!stopWords.Contains(term))
                {
                    terms.Add(term);
                }
            }
            return terms.ToArray();
        }

        //process the boolean query
        public static List<int> ProcessQuery(string query)
        {

            //query boolean operator
            string bitWiseOp = string.Empty;
            string[] queryTerm = RemoveStopsWords(query.ToUpper().Split(' '));

            //remove query term that doesnot appears on document collection
            FilterQueryTerm(ref queryTerm);
            List<int> previousTermIncidenceV = null;
            List<int> nextTermsIncidenceV = null;
            //holds the bitwise operation result
            List<int> resultSet = null;
            //suppose on query X AND Y, X is previousTerm term and Y is nextTerm
            Boolean hasPreviousTerm = false; 
            Boolean hasNotOperation = false;
            foreach (string term in queryTerm)
            {
                //is a term
                if (!booleanOperator.Contains(term)&&!term.Equals("BUT"))
                {
                    //query case: structure AND NOT analysis
                    if (hasNotOperation) 
                    {
                        
                        if (hasPreviousTerm)
                        {
                            nextTermsIncidenceV = ProcessBooleanOperator("NOT", GetTermIncidenceVector(term), nextTermsIncidenceV);
                        }
                        //query case: eg.NOT analysis
                        else 
                        {
                            previousTermIncidenceV = ProcessBooleanOperator("NOT", GetTermIncidenceVector(term), nextTermsIncidenceV);
                            resultSet = previousTermIncidenceV; 
                        }
                        hasNotOperation = false;
                    }
                    else if (!hasPreviousTerm)
                    {
                        previousTermIncidenceV = GetTermIncidenceVector(term);
                        resultSet = previousTermIncidenceV;
                        hasPreviousTerm = true; //
                    }
                    else
                    {
                        
                        nextTermsIncidenceV = GetTermIncidenceVector(term);
                    }
                }
                else if (term.Equals("NOT"))
                {
                    //indicates that the  term in the next iteration should be complemented.
                    hasNotOperation = true;
                }
                else
                {
                    //'BUT' also should be evaluated as AND eg. structure BUT NOT semantic should be evaluated as structure AND NOT semantic
                    if (term.Equals("BUT")) 
                    {
                        bitWiseOp = "AND";
                    }
                    else
                    bitWiseOp = term;
                }

                if (nextTermsIncidenceV != null && !hasNotOperation)
                {
                    resultSet = ProcessBooleanOperator(bitWiseOp, previousTermIncidenceV, nextTermsIncidenceV);
                    previousTermIncidenceV = resultSet;
                    hasPreviousTerm = true;
                    nextTermsIncidenceV = null;
                }
            }

            return resultSet;
        }

        public static List<int> ProcessBooleanOperator(string op,List<int> previousTermV,List<int> nextTermV)
        {
            List<int> resultSet = new List<int>();
            if(op.Equals("NOT"))
            {
                foreach(int a in previousTermV)
                {
                    if (a == 1)
                    {
                        resultSet.Add(0);
                    }
                    else
                    {
                        resultSet.Add(1);
                    }
                }
            }
            else if (op.ToUpper().Equals("AND")) //bitwise AND operation
            {
                for (int a = 0; a < previousTermV.Count; a++)
                {
                    if (previousTermV[a] == 1 && nextTermV[a] == 1)
                    {
                        resultSet.Add(1);
                    }
                    else
                    {
                        resultSet.Add(0);
                    }
                }
            }
            else if (op.ToUpper().Equals("OR")) //bitwise OR operation
            {
                for (int a = 0; a < previousTermV.Count; a++)
                {
                    if (previousTermV[a] == 0 && nextTermV[a] == 0)
                    {
                        resultSet.Add(0);
                    }
                    else
                    {
                        resultSet.Add(1);
                    }
                }
            }
            return resultSet;
        }


        //returns term incidence vector
        public static List<int> GetTermIncidenceVector(string term)
        {
            return termDocumentIncidenceMatrix[term.ToUpper()];
            
        }
    }


    //class for multidimensional dictionary
    public class MultiDimDictList : Dictionary<string, List<int>> { }
    public class MultiDimDictStringList : Dictionary<string, List<String>> { }
}
