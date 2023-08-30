#todo test app

from functions import get_todo,write_todo

file_path = 'todo.txt'


while True:
    prompt = " Add , Show , Edit , Complete and Exit :"
    user_input = input(prompt).strip()
    
        
    if user_input.startswith("Add"):
        add_todo=user_input[4:]
        
        to_do=get_todo(file_path)
        
        to_do.append(add_todo+'\n')
        
        write_todo(file_path,to_do)
            
    elif user_input.startswith("Show"):
        to_do=get_todo(file_path)
        
        for index,items in enumerate(to_do):
            items = items.strip('\n')
            row=f"{index} - {items}"
            print(row)
            
    elif user_input.startswith("Edit"):    
        try:
            number=int(user_input[5:])       
            to_do=get_todo(file_path)
            
            the_edit = input("Please add you change: ")
            to_do[number] = the_edit + "\n"
            write_todo(file_path,to_do)
        
        except ValueError:
            print("Your command in not valid :(")
            continue
        
    elif user_input.startswith("Complete"):
        to_do=get_todo(file_path)
        num = int(input("Number of the todo to complete: "))
        to_do.pop(num-1)
        write_todo(file_path,to_do)
            
    elif "Exit" in user_input:
        break
    
    
#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
