#prime number generator
def prime_number(n):
	if number < 0:
		return "Only positive numbers allowed."
    return(len([i for i in range(1,n+1) if n%i == 0])==2)
max = int(input())
for i in range(1,max+1):
    if prime_number(i):
        print(i)
       