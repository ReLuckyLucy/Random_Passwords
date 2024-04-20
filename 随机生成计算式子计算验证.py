from random import*

n1 = randint(1, 10)
n2 = randint(1, 10)
op = choice(['+', '-', '*', '/'])
nub = str(n1) + op + str(n2)
print(nub)
ed = int(input("请输入计算结果: "))
print(n1, op, n2, '=', eval(str(n1) + op + str(n2)))
if ed == eval(str(n1) + op + str(n2)):
    print("正确")
else:
    print("错误")
