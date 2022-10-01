def read_file(filename):
    with open(filename) as file:
        content = file.readlines()
        print(content)
