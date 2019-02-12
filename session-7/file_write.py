# Example of writting a file located
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


# OPEN FILE
f = open(NAME, 'a')

# WRITE FILE
f.write('Example.   You can read or write from and to the file with python programs as many times as you execute the programs.')

# CLOSE FILE
f.close()
print('The end.')
