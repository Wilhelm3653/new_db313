from animal import dog, cat

d = dog.Dog ##() <-> 2 варианта
print(type(d))

x = d()

print(type(x))
print(x.capture())