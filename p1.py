n = int(input())
courses = input().split(' ')
courses = [int(x) for x in courses]

mi = float('inf')
ma = float('-inf')

for n in courses:
    if n < mi:
        mi = n
    if n > ma:
        ma = n

ans = int((ma - mi) / 2) + mi
print(ans)
