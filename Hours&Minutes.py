# Given the integer N - the number of seconds that is passed since midnight -
# how many full hours and full minutes are passed since midnight?
# The program should print two numbers: the number of hours (between 0 and 23)
# and the number of minutes (between 0 and 1339).

# For example, if N = 4700, then 3900 seconds have passed since midnight.
# Therefore, the time now is 1:18am.
# So the program should print 1 78 - 1 full hour is passed since midnight, 78 full
# minutes passed since midnight.


T = int(input('Enter Time in seconds'))

print('hours :',T//60)//60)
print('minutes : ',T//60//60//60)