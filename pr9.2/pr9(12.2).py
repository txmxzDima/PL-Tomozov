import random
def create_matrix(rows, columns):
matrix = []
x=[]
n=0
with open('TomozovDmitriyYurievich_UB22_vvod.txt','r') as file1:
    for line in file1:
        x.append( list(map(int, line.split() )))
        n+=1
        for i in range(0, rows):
            inner_list = []
            for j in range(0, columns):
                inner_list.append(round(random.uniform(-10, 10), 2))
            matrix.append(inner_list)
file1.close()
with open('TomozovDmitriyYurievich_UB22_vivod.txt','w') as file2:
print(file2.write("new matrix\n"))
def spec_subtract(matrix):
    for i in range(0, len(matrix) - 1):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = matrix[i][j] - matrix[len(matrix) - 1][j]
def print_matrix(matrix):
    print('\n'.join([''.join([' {:.2f}'.format(item) for item in row]) for row in matrix]))
file2.close()