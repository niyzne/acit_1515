# https://x.com/realhughjackman
# Function composition

name = " hugh jaCKman "
print(name)

def create_username(name):
    return f"@{(name.replace(" ", "_"))}"

def clean_name(name):
    return name.strip().lower()

def create_url(username):
    return f"https://x.com/{username[1:]}"

print(create_url(create_username(clean_name(name))))
