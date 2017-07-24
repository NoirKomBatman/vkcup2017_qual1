raw = input()
raw = raw.split(' ')
n = int(raw[0])
m = int(raw[1])
k = int(raw[2])

if k % 2 != 0:
    print('IMPOSSIBLE')
    quit()

trip_half = int(k/2)

result = ""
maze = [] # [row[col]]


# populate the maze and find position of X
x_col = 0 # x
x_row = 0 # y
temp_iter = 0
while temp_iter < n:
    temp = input()
    for i in range(m):
        if (temp[i] == "X"):
            x_col = i
            x_row = temp_iter
    maze.append(temp)
    temp_iter += 1

# start exploring possible paths
current_col = x_col
current_row = x_row

while trip_half > 0 :
    if current_row + 1 < n and (maze[current_row + 1][current_col] == "." or maze[current_row + 1][current_col] == "X"): # check down
        result+="D"
        current_row = current_row + 1
        trip_half -= 1
    elif current_col - 1 >= 0 and (maze[current_row][current_col - 1] == "." or maze[current_row][current_col - 1] == "X"): # check left
        result+="L"
        current_col = current_col - 1
        trip_half -= 1
    elif current_col + 1 < m and (maze[current_row][current_col + 1] == "." or maze[current_row][current_col + 1] == "X"): # check right
        result+="R"
        current_col = current_col + 1
        trip_half -= 1
    elif current_row - 1 >= 0 and (maze[current_row - 1][current_col] == "." or maze[current_row - 1][current_col] == "X"): # check up
        result+="U"
        current_row = current_row - 1
        trip_half -= 1
    else:
        print("IMPOSSIBLE")
        quit()

trip_half = int(k/2)
for i in range(trip_half - 1, -1, -1):
    if result[i] == 'D':
        result+='U'
    elif result[i] == 'U':
        result+='D'
    elif result[i] == 'L':
        result+='R'
    else:
        result+='L'
print(result)
