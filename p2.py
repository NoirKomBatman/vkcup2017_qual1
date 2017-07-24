n = int(input())
messages = input().split(' ')
messages = [int(x) for x in messages]

# if student 1 can't send any msgs
if messages[0] == 0:
    print(-1)
    quit()

# if total msg < n students
su = 0
for e in messages:
    su+=e

if su < n - 1:
    print(-1)
    quit()

# proceed
students = sorted(range(len(messages)), key=lambda k: messages[k], reverse=True)

tail = 1
count = 0
dic = {}
if students[0] != 0:
    messages[0] = messages[0] - 1
for st in students:

    while messages[st] > 0 and tail < n:
        if students[tail] == 0: # if we send to polycarp
            tail+=1
            continue
        dic[count] = (st + 1, students[tail] + 1)
        tail+=1
        messages[st]-=1
        count+=1

if students[0] != 0:
    print(count + 1)
    print(str(1) + ' ' + str(students[0] + 1))
else:
    print(count)

for c in range(count):
    temp = dic[c]
    print(str(temp[0]) + ' ' + str(temp[1]))
