# --- Python Devlog: Equality (==) vs. Identity (is) ---

# 1. Create two separate list objects with identical contents
list_a = [1, 2, 3]
list_b = [1, 2, 3]

print("--- Case 1: Separate Objects, Same Values ---")
# The == operator checks VALUE equality (Are the contents the same?)
print(f"list_a == list_b: {list_a == list_b}")  # True

# The 'is' operator checks IDENTITY (Are they the exact same memory address?)
print(f"list_a is list_b: {list_a is list_b}")  # False
print(f"Memory Addresses -> a: {id(list_a)}, b: {id(list_b)}\n")


# 2. Create a shared reference (Alias)
# This points list_c directly to the object list_a is already pointing to
list_c = list_a

print("--- Case 2: Shared Reference (Same Object) ---")
print(f"list_a == list_c: {list_a == list_c}")  # True
print(f"list_a is list_c: {list_a is list_c}")  # True
print(f"Memory Addresses -> a: {id(list_a)}, c: {id(list_c)}\n")


# 3. The danger of shared references with mutable objects (Lists)
print("--- Case 3: The Side Effect of Mutation ---")
# Modifying list_c will unexpectedly change list_a because they share an identity!
list_c.append(4)

print(f"list_c after append: {list_c}")
print(f"list_a automatically changes: {list_a}")
print(f"list_b remains untouched: {list_b}")