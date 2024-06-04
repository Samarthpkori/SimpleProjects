print("Enter the Size: ")
n = int(input())


print("Enter " +str(n)+ " Elements: ")
G = []
for i in range(n):
    G.append(input())


print("Enter an Element to Search: ")
element = input()
check = 0


for i in range(n):
    if element==G[i]:
        index = i
        check = 1
        break


if check==1:
        print("\nElement Found at IndexNumber: " + str(index))
else:
            print("\nElement doesn't found!")