def append_and_verify(filename):
    with open(filename,'a') as file:
        file.write("Append")
    with open(filename,'r') as file:
        content=file.read()
        print(content)
append_and_verify("example.txt")