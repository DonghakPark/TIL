num1, num2 = input().split()

num1 = list(num1)
num1.reverse()
num2 = list(num2)
num2.reverse()

num1 = int(''.join(num1))
num2 = int(''.join(num2))

print(max(num1, num2))
