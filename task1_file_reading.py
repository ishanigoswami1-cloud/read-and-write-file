# Reading File Content
# Line1 : This is a sample text file.
# Line2 : it contains multiple lines.
file_handler =open("Sample.txt",'rt')
# read the content of the file as str
content=file_handler.read()
# closing the file
file_handler.close()
print(content)
print(type(content))
'''output: Python file reading test
# Reading File Content
# Line1 : This is a sample text file.
# Line2 : it contains multiple lines.
<class 'str'>'''

try:
    with open("sample.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print(f"Error: The file Sample.txt was not found.")
  
'''output:Error: The file Sample.txt was not found.'''
