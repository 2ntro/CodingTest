import itertools

def solution(v):
    answer = []
    
    # x,y로 분류하여 저장하기
    v_x ,v_y = [],[]
    for vn in v:
        vn_x ,vn_y = vn[0], vn[1]
        
        v_x.append(vn_x)
        v_y.append(vn_y)
    
    #
    result_x = 0
    result_y = 0

    for vn_x in v_x:
        if v_x.count(vn_x) == 1:
            result_x = vn_x
            break
    for vn_y in v_y:
        if v_y.count(vn_y) == 1:
            result_y = vn_y
            break
    
    answer.append(result_x)
    answer.append(result_y)
    

    return answer

print(solution(v=[[1, 4], [3, 4], [3, 10]]))