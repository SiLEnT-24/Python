# nested dictionary - dictionary with inside dictionary is called nested dictionary

products={
    1:{"code":1, "name":"printer", "price":22000},
    2:{"code":2, "name":"printer", "price":22000},
    3:{"code":3, "name":"printer", "price":22000}
}
print(products)
products[1]["code"]=101
print(products)

products[3]["price"]=100000
print(products)

