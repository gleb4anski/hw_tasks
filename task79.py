nums = []
z = input("Введите 1-ое число: ")
x = input("Введите 3-ое число: ")
c = input("Введите 2-ое число: ")
nums.append(z)
nums.append(x)
nums.append(c)
l = input("хотите ли вы оставить последнее число в списке? ")
if l == "no" :
    nums.pop()
    for y in nums:
     print(y)
elif l == "yes" :
    for y in nums:
     print(y)

