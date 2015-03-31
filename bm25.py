#package ivory.pwsim.score;

#public class Bm25 extends ScoringModel {

	k_1 = 1.2

	k_3 = 1000

	b = 0.75

	def computeScore( q_tf, doc_tf, q_len, doc_len) {

		# La definicion de K es diferente del standard BM25: hay un
		# d_tf adicional al final. Empiricamente el factor incrementa la efectividad.

		 K = k_1 * ((1 - b) + b * (doc_len / mAvgDocLength)) + doc_tf;
		 rsj = (float) Math.log((mDocCount - mDF + 0.5) / (mDF + 0.5));
		 val = ((k_1 + 1.0) * doc_tf / (K + doc_tf)) * ((k_3 + 1.0) * q_tf) / (k_3 + q_tf);

		return rsj * val;
	}

	def computeDocumentWeight(doc_tf, doc_len) {
		 K = k_1 * ((1 - b) + b * (doc_len / mAvgDocLength)) + doc_tf;
		 rsj = (float) Math.log((mDocCount - mDF + 0.5) / (mDF + 0.5));
		 val = ((k_1 + 1.0) * doc_tf / (K + doc_tf));

		return rsj * val;
	}
	
	def computeDocumentWeight(doc_tf, df, doc_len) {
		 K = k_1 * ((1 - b) + b * (doc_len / mAvgDocLength)) + doc_tf;
		 rsj = (float) Math.log((mDocCount - df + 0.5) / (df + 0.5));
		 val = ((k_1 + 1.0) * doc_tf / (K + doc_tf));

		return rsj * val;
	}

	def computeQueryWeight(q_tf, q_len) {
		return ((k_3 + 1.0) * q_tf) / (k_3 + q_tf);
	}

#}
