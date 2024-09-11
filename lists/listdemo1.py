# write an app that interacts with the user to add items to a list, remove an item 
# from the list, and print the list
def add_item(list_name, item):
    if not list_name:
        list_name = []
    list_name.apppend(item)
    return(list_name)
        
