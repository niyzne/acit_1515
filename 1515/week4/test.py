# https://x.com/realhughjackman
# Function composition

name = " hugh jackman "
# how do we get spaces (some spaces, like on left or right, could be accidents)
# maybe the one in the middle is like, unique
# either way, how can we like, handle it as a whole thing.... maybe like "hugh_jackman"
print(name)

name = name.strip()

print(name)

# maybe also like. someone wants everyone to be capitalized or lowercased
name = " hugh jaCKman "
print(name)

name = name.lower()

print(name)

# and then we can strip and loewrcase
name = " hugh jaCKman "
print(name)
name = name.strip().lower()
print(name)
# could also upper it
name = name.upper()
print(name)
