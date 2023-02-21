altura = int(input("Introduce la altura del árbol: "))

for i in range(altura):
    for j in range(altura-i):
        print(" ", end="")
    for k in range(2*i+1):
        print("*", end="")
    print()

for i in range(2):
    for j in range(altura-1):
        print(" ", end="")
    print("| |")
