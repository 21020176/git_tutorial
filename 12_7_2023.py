def F(lst, N, X):
    sum =  0
    number = 0
    begin = 0
    end = 0
    for i in range(0, N): 
        if sum * (end - begin) >= X:
            number += 1
            sum = 0
            begin += 1
            i = begin
            break
        sum = lst[i + 1] - lst[i]
        end += 1
    return number
#print("commit")

lst = []

N = int(input())
X = int(input())

for i in range(0, N):
    ele = int(input())
    lst.append(ele)

print(F(lst, N, X))
