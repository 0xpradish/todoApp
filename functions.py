
def get_todo(file_path):
    """ Read a text file a return list to to-do items """
    with open(file_path,'r') as file:
        to_do =  file.readlines()
    return to_do

def write_todo(file_path,to_do):
    """ Write the to-do item list in text file """
    with open(file_path,'w') as file:
         file.writelines(to_do) 