import os
print("Current directory:",os.getcwd())
os.mkdir('new_directory')
print("New directory:",os.listdir())
os.rename('new_directory','renamed')
os.rmdir('new_directory')