def solution(array, commands):
    
    answer = []
    for command in commands:
        start = command[0]
        end = command[1]
        sort = command[2]
        
        arr_slicing = array[start-1:end]
        arr_slicing.sort()
        answer.append(arr_slicing[sort-1])
    
    return answer