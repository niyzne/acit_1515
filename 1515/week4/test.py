# https://x.com/realhughjackman
# Function composition

name = " hugh jaCKman "

def create_username(name):
    print("@" + name.replace(" ", "_"))
    # or we can do
    # print(f'@{(name.replace(" ", "_"))}')

def clean_name(name):
    return name.strip().lower()

cleaned_name = clean_name(name)
create_username(cleaned_name)
