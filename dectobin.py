n = int(input("Enter any number :- "))
y = []
def findMod(e, f):
    x = e % 2
    f.append(x)
    if e // 2 > 0: 
        findMod(e // 2, f)
findMod(n, y)
binary_representation = ''.join(map(str, y[::-1]))
print(binary_representation)
