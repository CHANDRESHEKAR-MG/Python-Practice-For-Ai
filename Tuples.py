purple = (128, 0, 128)
print(purple[0])
print(purple[1])
print(purple[2])

# Tuples are immutable, so we cannot change an item directly.
# To update the value, create a new tuple instead.
purple = (255, 0, 128)
print(purple[0])

r,g,b=purple
print(r)
print(g)
print(b)

yellow = (255, 255, 0)
mixed=((purple[0]+yellow[0])//2, (purple[1]+yellow[1])//2, (purple[2]+yellow[2])//2)
print(mixed) 