# Write a Python program to test whether a passed letter is a vowel or not
vowel=['a','e','i','o','u']
cha=str(input('enter your letter : '))
for i in vowel:
    if (cha in vowel):
        
        print('The given letter present vowel group')
        break
    else:

        print('Given letter is costant')
        break