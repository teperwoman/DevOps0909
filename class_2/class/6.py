names = ["ariel", "adi", "eran", "adir", "shahar"]
string_to_print = "hello world!"
for i in range(5):
    print(names[i])
#revoir i !!!!!!
for i in range(len(names)):
    print(names[i])
#len me di combien la lliste fai


for name in names:
    print(name)

a= 0
while a < 10:
    a = a + 1
    if a == 5:
        continue
    print(a)


for i in range(1, 101):
    if i % 7 == 0 or "7" in str(i):
        continue
    print(i)
