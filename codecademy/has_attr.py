can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for item in can_we_count_it:
  if hasattr(item, 'count'):
    print(str(type(item
    )) + " has the count attribute!")
  else:
    print(str(type(item)) + " does not have the count attribute :(")

# hasattr(element, attribute)
# getattr(element, attribute, default)