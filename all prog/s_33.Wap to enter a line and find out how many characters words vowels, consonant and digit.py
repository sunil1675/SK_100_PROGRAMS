#Program by SUNIL SIR
#33.Wap to enter a line and find out how many characters words vowels, consonant and digit.

print('33.Wap to enter a line and find out how many characters words vowels, consonant and digit.\n')
import string
l=input('ENTER LINE: ')

print('WORDS: ')
w=l.split(' ')
print(len(w))

print('CHARACTERS: ')
c=l.replace(' ','')
print(len(c))

print('VOWELS: ')
v=('a','e','i','o','u','A','E','I','O','U')
v1=0
for i in l:
    if i in v:
        v1=v1+1
print(v1)

print('CONSONENTS: ')
co=('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z')
co1=0
for i in l:
    if i in co:
        co1=co1+1
print(co1)

print('DIGITS: ')
d=('1','2','3','4','5','6','7','8','9','0')
d1=0
for i in l:
    if i in d:
        d1=d1+1
print(d1)