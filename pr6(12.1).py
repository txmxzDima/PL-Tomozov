list_even = [ int(i) for i in input().split() if int(i)%2]
print(min(list_even) if list_even else 0)