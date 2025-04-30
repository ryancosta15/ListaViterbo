x = int(input())
y = int(input())
r = x
q = 0
x = r
#acaba quando resto não é divisível (menor que divisor)
while r >= y:
	r -= y
	q += 1
print(q)
print(r)
