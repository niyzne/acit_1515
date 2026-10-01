# next quiz
# list of values
values = ["red", "blue"]
# take stuff from list, do smth to do with it. some stuff might be useles data. etc
values = ["red", "blue", False, 30.5]

# dont do smth like

def get_length(values):
    for val in values:
        print(len(val))

get_length(["red", "blue", False, 30.5])

# maybe, before this. we can only get the safe stuff.... so perhaos remove the non strings? yk...
# maybe you end up
def get_safe_values(values):
    # smth to do with type() operator
    pass

# so overall like
def get_safe_values(values):
    safe_values = []
    for val in values:
        if type(val) == str:
            # maybe then add to list of safe values?
            safe_values.append(val)

def get_length(values):
    for val in values:
        print(len(val))

# make sure you rmember how to detemrine odd/even
# smth % 2 == 0

get_length(get_safe_values(["red", "blue", False, 30.5]))

# quiz is one question. out of 5

