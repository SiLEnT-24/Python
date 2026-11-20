try:
    d=("rio",345,"husk")
    # d.append(2,4)
except AttributeError:
    print("tuple is immutable")
else:
    a=list(d)
    a.append(54)
    d=tuple(a)
    print(d)