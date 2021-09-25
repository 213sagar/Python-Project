def ComputeGCD(a,b):
    if b==0:
        return a
    else:
        return ComputeGCD(b,a%b)
a=int(input('Enter your first no : '))
b=int(input('Enter your 2nd num : '))
print(ComputeGCD(a,b))
