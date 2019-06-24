from sys import argv

script, filename = argv

f = open(filename, 'r')

contents = f.read()

print(contents)

f.close()
