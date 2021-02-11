n = int(input())
p = list()
pagrup = list()
na = 0
tot = 0
while n != 0:
    p.append(int(input()))
    n -= 1
for i in range(len(p)):
    pagrup.append(p[na:na+3])
    na += 3
    if na >= len(p):
        break
for i in range(len(pagrup)):
    if len(pagrup[i]) == 3:
        pagrup[i].sort(reverse=True)
        pagrup[i].pop()
        for u in range(len(pagrup[i])):
            tot += pagrup[i][u]
    else:
        for u in range(len(pagrup[i])):
            tot += pagrup[i][u]
print(tot)  

