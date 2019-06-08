names = " John, Jennie, Jim, Jack, Joe"

#idx = names.index("h")
idx = names.index("Jennie")
print(idx)

newNames = names.replace('J', 'K')
print(names)
print(newNames)

print()

num = names.count("John", 0, len(names))
print(num)

data = names.split(",")
print(data, type(data))
print()

for n in data:
    print(n)
