#Program by SUNIL SIR
#34.Wap to enter a number and print whether it is palindrome.

print('34.Wap to enter a number and print whether it is palindrome.\n')

n=int(input('Enter a no.: '))

if str(n)==str(n)[::-1]:
    print('The number is palindrome.')
else:
    print('The number is not palindrome.')