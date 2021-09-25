#  Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum
n1=int(input('1st no : '))
n2=int(input('2nd no : '))
n3=int(input('3rd no : '))
sa=n1+n2+n3
if (n1==n2==n3):
    print('three times of sum is : ',sa)
else:
    print(sa)

