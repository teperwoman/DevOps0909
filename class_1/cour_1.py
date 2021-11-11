a = "hello world"
b = 4
isMarried = False
d = ["aviel", 31, True]
e = ("moshe", 43, False)
f = {"name": "aviel", "age": 31, "isMarried": True, "hobbies": ["sky", "guitar"],
     "work": {"position": "devops", "salary": "2M"}}
print(a)
print(b)
d[1] = 32
print(d[1])
print (e[2])
print(f.values())


g = "aviel"
h = "buskila"
i = g + " " + h #jai rajouter lespace pour le nom
j = 4
k = g + str(j)
# lm = f"{g} {h}"  #la facon la plus prise cest ca!!! il marche pas acause de ma ersin python
# - f dit que c un format on peut pas le changer
lk = "%s %s" % (g, h)
# comande + / pour faire de comentaire de plusier ligne
lt = "aviel\n\t \"buskilla\""
print(lt)
#revoir les \ t t r n


if j != 4:
    print("a is 4")
print("aviel")


#devoir cour 1:
# A
first = 7
second = 44.3
print(first + second)
print(first * second)
print(second/first)

# B
a = 9
b = 8
c = 14

# C
my_number = 5+5
print("result is: " + str(my_number))

# D
x = 5
y = 2.36

print (x+int(y))

# chalenge
a = 8
b = "123"

print ( str(a) + b)
print (a + int(b))





