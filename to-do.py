#todo test app

while True:
    prompt = " Add , Show , Edit , Complete and Exit :"
    user_input = input(prompt).strip()
    
        
    if user_input.startswith("Add"):
        print('yes')
        add_todo=user_input[4:]
        
        with open('todo.txt','r') as file:
            to_do =  file.readlines()
        
        to_do.append(add_todo+'\n')
        
        with open('todo.txt','w') as file:
            file.writelines(to_do)
            
    elif user_input.startswith("Show"):
        with open('todo.txt','r') as file:
            to_do =  file.readlines()
        
        for index,items in enumerate(to_do):
            items = items.strip('\n')
            row=f"{index} - {items}"
            print(row)
            
    elif user_input.startswith("Edit"):    
        try:
            number=int(user_input[5:])       
            with open('todo.txt','r') as file:
                to_do =  file.readlines()
            
            the_edit = input("Please add you change: ")
            to_do[number] = the_edit + "\n"
            with open('todo.txt','w') as file:
                file.writelines(to_do)
        
        except ValueError:
            print("Your command in not valid :(")
            continue
        
    elif user_input.startswith("Complete"):
        with open('todo.txt','r') as file:
            to_do =  file.readlines()
        num = int(input("Number of the todo to complete: "))
        to_do.pop(num-1)
        with open('todo.txt','w') as file:
            file.writelines(to_do)
            
    elif "Exit" in user_input:
        break
    
    
#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
