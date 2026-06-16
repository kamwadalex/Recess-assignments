# Remove an item from a set
Cars = {"suzuki", "Honda", "subaru"}

Cars.remove("Honda")  # removes the item (error if not found)
print(Cars)

Cars.discard("suzuki")  # removes the item (no error if not found)
print(Cars)
