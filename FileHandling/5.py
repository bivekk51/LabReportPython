def write_list_to_file(filename,list):
    with open(filename, 'w') as file:
        for item in list:
            file.write(f"{item}\n")
write_list_to_file('fruits.txt',['apple','banana','mango'])