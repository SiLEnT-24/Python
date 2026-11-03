#packing in tuple
def demo(*x):
    print(sum(x), type(x))
demo(10)
demo(10, 20)
demo(10, 20, 30)
demo(10, 20, 30, 40)