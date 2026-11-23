sqr={x:x**2 for x in range(1,6)}
print(sqr)

keys=["a","b","c"]
values=[11,12,13]
d1={k:v for k, v in zip(keys,values)}
print(d1)