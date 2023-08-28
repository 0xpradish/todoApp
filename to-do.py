#todo test app
file_path = 'todo.txt'

def read_write(file_path,operation,to_do):
    if operation == 'r':
        with open(file_path,'r') as file:
            to_do =  file.readlines()
        return to_do
    else:
        with open(file_path,'w') as file:
            file.writelines(to_do) 
        
        

while True:
    prompt = " Add , Show , Edit , Complete and Exit :"
    user_input = input(prompt).strip()
    
        
    if user_input.startswith("Add"):
        print('yes')
        add_todo=user_input[4:]
        
        to_do=read_write(file_path,'r','')
        
        to_do.append(add_todo+'\n')
        
        read_write(file_path,'w',to_do)
            
    elif user_input.startswith("Show"):
        to_do=read_write(file_path,'r','')
        
        for index,items in enumerate(to_do):
            items = items.strip('\n')
            row=f"{index} - {items}"
            print(row)
            
    elif user_input.startswith("Edit"):    
        try:
            number=int(user_input[5:])       
            to_do=read_write(file_path,'r','')
            
            the_edit = input("Please add you change: ")
            to_do[number] = the_edit + "\n"
            read_write(file_path,'w',to_do)
        
        except ValueError:
            print("Your command in not valid :(")
            continue
        
    elif user_input.startswith("Complete"):
        to_do=read_write(file_path,'r','')
        num = int(input("Number of the todo to complete: "))
        to_do.pop(num-1)
        read_write(file_path,'w',to_do)
            
    elif "Exit" in user_input:
        break
    
    
#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
