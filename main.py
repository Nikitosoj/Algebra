global k
n = 2
def quadr(x):
    if x == 0:
        return(1)
    else:
        return( (x*x) % k)
def minus(x,y):
    if x >= y:
        return(x-y)
    else:
        return(k-(y-x))
def VV(x,y):
    if max(x,y)+ 1 >= k:
        return((max(x,y)+ 1) % k)
    else:
        return(max(x,y) + 1)
def imp(x,y):
    if x <= y:
        return(k-1)
    else:
        return( (k-1) - x + y)
def minum(x,y):
    if x <= y:
        return(0)
    else:
        return(x-y)
def plus(x,y):
    if x + y >= k:
        return((x + y) % k)
    else:
        return(x+y)
def mult(x,y):
    if x * y >= k:
        return((x * y) % k)
    else:
        return(x*y)
def J(i,x):
    if x == i:
        return(1)
    else:
        return(0)
def I(i,x):
    if x == i:
        return(k-1)
    else:
        return(0)
def post(x):
    if x + 1 == k:
        return(0)
    else:
        return(x + 1)
def max(x,y):
    if x > y:
        return(x)
    if y >= x:
        return(y)
def min(x,y):
    if x < y:
        return(x)
    if y <= x:
        return(y)
def tilda(x):
    return((k-1)-x)
k = int(input())
x1 = []
y1 = []
for i in range(k):
    for l in range(k):
        x1.append(i)

for i in range(k):
    for l in range(k):
        y1.append(l)
# print("x | y | max(x,y) | min(x,y) |   x*y   | tilda(x) | post(x)| I3(x)| J3(x)| x + y| x * y| minum(*_)| imp(x,y)| VV(x,y)| x -y ")


result = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

final = []
# for i in range(k*k):
#     print(x1[i]," ", y1[i] ,"    ", max(x1[i], y1[i]),"      ", min(x1[i], y1[i]),"         ",
#     mult(x1[i], y1[i]) , "          ", tilda(x1[i]), "        ", post(x1[i]), "    ",I(2,x1[i]),
#     "    ",J(2,x1[i]), "   ", plus(x1[i],y1[i]), "   ", mult(x1[i],y1[i]), "     ", minum(x1[i],y1[i]), "           ",
#      imp(x1[i],y1[i]), "     ", VV(x1[i],y1[i]), "     ", minus(x1[i],y1[i]) )
# for i in range(k*k):
#     result[0].append(post(x1[i]))
# print(result[0])
# for i in range(k*k):
#     result[1].append(plus(result[0][i],result[0][i]))
# print(result[1])
# result[0] = []
# for i in range(k*k):
#     result[0].append(tilda(result[1][i]))
# print(result[0])
# result[1] = []
# for i in range(k*k):
#     result[1].append(mult(result[0][i],quadr(x1[i])))
# print(result[1])
def math(n,x,y):
    if n == 4: return(minus(x,y))
    elif n == 5: return(VV(x,y))
    elif n == 6: return(imp(x,y))
    elif n == 7: return(minum(x,y))
    elif n == 8: return(plus(x,y))
    elif n == 9: return(mult(x,y))
    elif n == 10: return(J(x,y))
    elif n == 11: return(I(x,y))
    elif n == 12: return(max(x,y))
    elif n == 13: return(min(x,y))
l = 3
def math2(n,x):
    if n == 1: return(quadr(x))
    elif n == 2: return(post(x))
    elif n == 3: return(tilda(x))
for i in range(k*k):
    if n >= 1 and n <= 3:
        result[l].append(math2(n,x1[i]))
    if n >=4 and n<=13:
        result[l].append(math(n,x1[i],y1[i]))
print(result[l])