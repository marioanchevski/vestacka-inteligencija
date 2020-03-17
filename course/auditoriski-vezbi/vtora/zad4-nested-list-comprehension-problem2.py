def multiply(elem,i,n):
    if i<n/2:
        return elem*2
    else:
        return elem*3

def resenie():
    n = int(input())
    m = int(input())
    row = []
    matrix = []

    for i in range(n):
        for j in range(m):
            row.append(int(input()))
        matrix.append(row)
        row = []

    res=[[multiply(matrix[i][j],i,n) for j in range(m) ] for i in range(n) ]
    print(res)

if __name__=="__main__":
    resenie()
