# https://x.com/realhughjackman
# Function composition

name = " hugh jaCKman "
print(name)

def create_username(name):
    # return "@" + name.replace(" ", "_")
    # or
    return f"@{(name.replace(" ", "_"))}"

def clean_name(name):
    return name.strip().lower()

def create_url(username):
    return f"https://x.com/{username[1:]}"

cleaned_name = clean_name(name)
usernamed = create_username(cleaned_name)
urled = create_url(usernamed)

print(cleaned_name)
print(usernamed)
print(urled)
