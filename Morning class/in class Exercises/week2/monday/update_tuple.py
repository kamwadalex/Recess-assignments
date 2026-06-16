# How a tuple can be updated

colors = ("red", "green", "blue")
print("Original:", colors)

# Method 1: Create a new tuple
colors = colors + ("yellow",)
print("After adding:", colors)

# Method 2: Convert to list, update, convert back to tuple
colors_list = list(colors)
colors_list[1] = "orange"
colors = tuple(colors_list)
print("After changing index 1:", colors)
