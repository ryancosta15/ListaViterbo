n = int(input())
div = []
sum = 0
for i in range(1,n):
    if n  %i == 0:
        div.append(i)
        sum+=i
div = str(div).replace(",", " + ").strip("[]")
if sum == n:
    print(f"{n} é um número perfeito")

else:
    print(f"{n} não é um número perfeito")
print(f"{div} = {sum}")
