#generator is a special type of function that return values one ata time instead of returning multiple values.Generator use yield keyword instead of return
def demo():
    yield 10
    yield 24
    yield 34
x=demo()
# print(next(x))
# print(next(x))
# print(next(x))

for x in demo():
    print(x)