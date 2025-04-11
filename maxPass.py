
def maxPathSum(m, n, tre): 
  
    for i in range(m-1, -1, -1): 
        for j in range(i+1): 

            if (tre[i+1][j] > tre[i+1][j+1]): 
                tre[i][j] += tre[i+1][j] 
            else: 
                tre[i][j] += tre[i+1][j+1] 
  

    return str(tre[0][0]) 
t = int(input())
for i in range(t):
    n = int(input())
    value=[] 
    for i in range(n): 
        col = [] 
        for j in range(n): 
            col.append(0) 
        value.append(col) 

    for i in range(n):
        char_in_line =input().split(" ")
        for j in range(len(char_in_line)):
            value[i][j] = int(char_in_line[j])

    print(maxPathSum(n-1, n-1, value))