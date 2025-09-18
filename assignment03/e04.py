# Sort and Print List

list = []

for i in range(5):
    print(f"Anna numero  + {i + 1}:")
    n = int(input())
    list.append(n)

list.sort #(reverse = True)
print(list)