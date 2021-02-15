x=int(input())
a = str(x)

if 0 < x <= (1 << 31)-1:
    print(int(a[::-1]))

elif (-1 << 31) <= x < 0:
     print(-(int(a[:-len(a):-1])))
else:
    print(0)
