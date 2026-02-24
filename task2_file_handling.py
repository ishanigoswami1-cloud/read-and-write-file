fh=open("output.txt",'at')
fh.write("Enter text to write to the file: Hello, Python!.\n")
fh.write("Data successfully written to output.txt.\n")
fh.write("Enter additional text to append: Learning file handling in Python.\n")
fh.write ("Data successfully appended.\n")
fh.write("Final content of output.txt.\n")
fh.write("Hello, Python!.\n")
fh.write("Learning file handling in Python.\n")
fh.close()
with open("output.txt", "r") as file:
    print(file.read())

''' Output : Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.
Enter additional text to append: Learning file handling in Python.
Data successfully appended.
Final content of output.txt:
Hello, Python!
Learning file handling in Python.'''
