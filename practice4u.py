employee = {"name":"John", "eid":"john@example.com", "salary":30000}
print(employee, type(employee))
print()
print(len(employee))
print()

# max and min will work on keys not on values
print(max(employee))
print()
print(min(employee))
print()

# Update operation
employee["name"] = "John Watson"
print(employee)

keys = list(employee.keys())
values = list(employee.values())

print(keys, type(keys))
print(values, type(values))

# in dictonary we have keys as unique
# but values can be duplicates

for key in keys:
    print(key, employee[key])

