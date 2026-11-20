#this is about tuples basically

#here are the requirements to be a tuple:

#can't change or alter once created
#meaning it isn't immutable

# Standard tuple
coordinates = (34.05, -118.24)

# Tuple without parentheses (tuple packing)
user = "the-m-files", 14, "Software Engineer"

# Single-item tuple (requires a trailing comma)
single_item = ("retron",)

# Tuple unpacking into separate variables
lat, lon = coordinates
print(lat)  # Output: 34.05
