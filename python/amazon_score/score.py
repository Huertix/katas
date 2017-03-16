# def totalScore(blocks, n):
#     # first clean previous value when Z
   
#     clean_list = []
#     for index in range(0, n):

#     	if str(blocks[index]) == 'Z':
#     		continue
    		
#     	if index < n-1 and str(blocks[index + 1]) == 'Z':
#     		continue

#         clean_list.append(str(blocks[index]))
    
#     total_score = 0
#     previous_score = 0
#     previous_score_2 = 0
#     for value in clean_list:
#         # calculate the sum of the dict
        
#         if value == 'X':
#             score = previous_score * 2
            
#         elif value == '+':
#             score = previous_score + previous_score_2
            
#         else:
#             score = int(value)
        
#         previous_score_2 = previous_score
#         previous_score = score
#         total_score = total_score + score

#     print total_score


def totalScore(blocks, n):
    
    total_score = 0
    last_score = 0
    last_score2 = 0
    for symbol in cleanList(blocks, n):
        score = symbolScore(symbol, last_score, last_score2 )
        last_score2 = last_score
        last_score = score
        total_score = total_score + score

    print total_score
    

def cleanList(blocks, n):
    clean_list = []
    for index in range(0, n):

    	if str(blocks[index]) == 'Z':
    		continue
    		
    	if index < n-1 and str(blocks[index + 1]) == 'Z':
    		continue

        clean_list.append(str(blocks[index]))
        
    return clean_list
        
def symbolScore(symbol, last_score, last_score2):
    if symbol == 'X':
        score = last_score * 2
        
    elif symbol == '+':
        score = last_score + last_score2
        
    else:
        score = int(symbol)
    
    return score


totalScore([5, -2, 4, 'Z', 'X', 9, '+','+'], 8)

totalScore([3, 5, 2, 'Z', 'Z'], 5)