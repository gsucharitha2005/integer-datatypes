num=1233
print(num)
print("number type:", type(num))
binary=bin(num)
print(binary)

print("hello")

num=1233
print(num)
print("number type:", type(num))
octal=oct(num)
print(octal)

print(".........")

num=1233
print(num)
print("number type:", type(num))
hex=hex(num)
print(hex)

print("..........")

num=0x6ab
print(num)
print("number type:",type(num))
binary=bin(num)
print(binary)

decimal=int(binary,2)
print(decimal)
octal=oct(decimal)
print(octal)

print("................")

num=50.7
print(num)
print("number type:",type(num))

print("")
 
complex=3+5j
print(complex)
print("number type:",type(complex))

complex=["chairs","tables",'45']
print(complex)
print("number type:",type(num))

print("")

tree=("leafs","branches","animals",'34')
print(tree)
print(type(tree))

print(".......")

data=range(10)
print(data)
print(type(data))

for x in range(10):
          print(x)
print(type(x))

set_dt={1,2.5,"3+4j",1,5.6}
print(set_dt)
print(type(set_dt))

froz=frozenset(set_dt)
print(froz)
print(type(froz))

print("")

bl=True
print(bl)
print(type(bl))

std={237813250:"suchi",237813207:"suchi"}
print(std)
print(type(std))

str="bhanu"
print(str)
print(type(str))
