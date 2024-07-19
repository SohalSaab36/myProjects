n = int(input("Enter any number :- "))
y = []

def findMod(e, f):
    x = e % 2
    f.append(x)
    if e // 2 > 0:  # Use integer division to check the condition
        findMod(e // 2, f)

findMod(n, y)

# Reverse the list to get the correct binary order and join the elements to form a string
binary_representation = ''.join(map(str, y[::-1]))
print(binary_representation)
