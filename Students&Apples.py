# N students take K apples and distribute them among each other evenly. The
# remaining (the indivisible) part remains in the basket. How many apples will each
# single student get? How many apples will remain in the basket?


n = int(input('Enter no.of students'))
k = int(input('Enter no.of apples'))

print('apple per students : ',k // n)  
print('apple remaining : ',k % n)    