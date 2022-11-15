x=[]
arr=0
with open('TomozovDmitriyYurievich_UB22_vvod.txt','r') as file1:
    for line in file1:
        x.append( list(map(int, line.split() )))
        arr+=1
n = 4
arr_rev = list(map(list,zip(*arr)))
for i in range(n) :
    for j in range(n) :
        if arr[i] == arr_rev[j] :
              print(i + 1, 'строка и ', j + 1, 'столбец равны')
file1.close()
with open('TomozovDmitriyYurievich_UB22_vivod.txt','w') as file2:
        print(file1.write(i+1, 'строка и ', j+1, 'столбец равны'))
        print(file1.write('\n'))
file2.close()
