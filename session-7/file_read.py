# Example of reading a file located
# in our local file system

NAME = 'mynotes.txt'

# OPEN FILE
myfile = open(NAME, 'r')  # 'myfile' is an OBJECT that may have attributes, etc.


print('File opened: {}'.format(myfile.name))

# READ FILE
contents = myfile.read()

# PRINT FILE
print('The file contents are: {}'.format(contents))

# CLOSE FILE
myfile.close()