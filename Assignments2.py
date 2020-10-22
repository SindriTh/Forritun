def add_to_dict(mydict):
    key = input("Key: ")
    value = input("Value: ")
    if key not in mydict:
        mydict[key] = value
    else:
        print("Error. Key already exists.")
    return mydict

def remove_from_dict(mydict):
    key = input("Key to remove: ")
    if key in mydict:
        del mydict[key]
    else:
        print("Key not found.")
    return mydict

def find_key(mydict):
    key = input("Key to locate: ")
    if key in mydict:
        print("Value: {}".format(mydict[key]))
    else:
        print("Key not found.")
    return mydict

def menu_selection():
    print("Menu:") 
    userinput = input("(a)dd, (r)emove, (f)ind: ")
    return userinput

def execute_selection(userinput, mydict):
    if userinput.lower() == 'a':
        mydict = add_to_dict(mydict)
    elif userinput.lower() == 'r':
        mydict = remove_from_dict(mydict)
    elif userinput.lower() == 'f':
        mydict = find_key(mydict)
    else:
        print("Invalid choice.")

def dict_to_tuples(mydict):
    listi = []
    for items in mydict.items():
        listi.append(items)
    return listi

def main():
    more_input = True
    a_dict = {}
    
    while more_input:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more_input = again.lower() == 'y'
    
    tuple_list = dict_to_tuples(a_dict)
    print(sorted(tuple_list))

main()