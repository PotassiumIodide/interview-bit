 nrows = len(matrix)
        ncols = len(matrix[0])
        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j]==0:
                    matrix[i][j]='0'
                else:
                    pass
        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j]=='0':
                    matrix[i][j]=0
                    for k in range(nrows):
                        if (matrix[k][j] != '0'):
                            matrix[k][j] = 0
                    
                    for n in range(ncols):
                        if (matrix[i][n] != '0'):
                            matrix[i][n] = 0
