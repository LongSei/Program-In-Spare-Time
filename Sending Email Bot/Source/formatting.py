msg_template = """
Dear {name}, 
bla bla bla
""" 

def format_msg(my_name=None, my_website=None):
    my_msg = msg_template.format(name=my_name)
    return my_msg

    