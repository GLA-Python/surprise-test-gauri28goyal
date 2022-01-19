#1 EXPANDING LIST
x=eval(input())
def abc(x):
    a=len(x)-1
    for i in range(a):
        if x[i]>x[i+1]:
            return False
            break
    else:
        return True
o=abc(x)
print(o)

