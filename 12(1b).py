def funk():
    a = int(input())
    if a == 0:
        return 0
    else:
        return max(a, funk())
        
print(funk())