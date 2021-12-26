from random import uniform

num = [uniform(-100, 100) for i in range(10)]
print(num)
print(sorted(num, key=lambda x: abs(x - int(x))))