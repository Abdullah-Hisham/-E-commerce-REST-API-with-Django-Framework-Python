def solution(array_a, array_b):
    y= 0
    
    n = 0 
    for i in range (len(array_a)):
        x = array_b[y]-array_a[y]
        if x<0:
            o = x*-1
            n += o*o
        else:
            n+=x*x
        y+=1
    return n/len(array_a) 
print(solution([10, 20, 10, 2], [10, 25, 5, -2]))