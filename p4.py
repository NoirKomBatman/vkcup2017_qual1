line1 = input().split(' ')
n = int(line1[0])
k = int(line1[1])

seq = input().split(' ')
seq = [int(x) for x in seq]


count = 0

def numberOfSetBits(i):
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24

for i in range(n):
    for j in range(i+1,n):
        xor = seq[i] ^ seq[j]
        if numberOfSetBits(xor) == k:
            count+=1

print(count)
