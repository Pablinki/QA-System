from random import sample
 
def search(word):
    s = sample(range(10), len(word))
    print '-- SEARCH %-12s %68s %-60s' % (word, '', str(sorted(s)))
    return set(s)
 
def set_op(operator, set1, set2):
    if operator == 'AND':
        return set1 & set2
    if operator == 'OR':
        return set1 | set2
    return set()
 
def do_operations(operator,  operands, hits_buffer=set()):
    if len(operands) == 0: return set()
    combined = set(search(operands[0]))
    for word in operands[1:]:
        hits = search(word)
        combined = set_op(operator, combined, hits)
    if hits_buffer:
        combined = set_op(operator, combined, hits_buffer)
    return combined
 
def parse(query):
    print 'query: %s' % query
    hits_buffer = set()
    stack = []
    for item in query.split():
        print '- %-20s %-25s %s' % (item, list(hits_buffer), str(stack))
        if item in ['OR', 'AND']:
            stack.append(item)
        elif item == '(':
            continue
        elif item == ')':
            operands = []
            while stack and stack[-1] not in ['OR', 'AND']: 
                operands.append(stack.pop())
            operator = stack.pop()
            hits_buffer = do_operations(operator, operands, hits_buffer)
            print '-- %-19s %-40s' % (operator, list(hits_buffer))
        else:
            stack.append(item)
    return hits_buffer
            
if __name__ == '__main__':
    query = "OR ( AND ( maria sharapova ) tennis )"
    parse(query)
    
    print '-'*75
    query = "AND ( OR ( AND ( maria sharapova ) tennis ) soccer )"
    parse(query)
