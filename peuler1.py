#Project Euler

#Sum of 3, 5, 6 and 9 is 23.

three = 3
five = 5
six = 6
nine = 9

sums = three + five + six + nine

#Find the sum of all the multiples of 3 or 5 below 1000

num = 1000
lis = {}

for i in range(num):
	if i % 3 == 0:

		lis[i] =  i

	elif i % 5 == 0:

		lis[i] = i

lis = sorted(set(lis))
print lis
suml = sum(lis)
print suml
