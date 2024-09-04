def read_file(file_name):
    with open(file_name, 'r') as file:
        contents = file.read()
        print(contents)
        return contents

def read_file_into_list(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return lines

def write_first_line_to_file(file_contents, output_filename):
    first_line = file_contents.split('\n', 1)[0]

    with open(output_filename, 'w') as file:
        file.write(first_line)

def read_even_numbered_lines(file_name):
    even_lines = []
    
    with open(file_name, 'r') as file:
        lines = file.readlines()
        even_lines = [line.strip() for idx, line in enumerate(lines) if idx % 2 != 0]
    return even_lines

def read_file_in_reverse(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        reversed_lines = list(reversed(lines))
        return reversed_lines

def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()
