def main():
    text_list = read_file("provinces.txt")

    print(text_list)

    text_list.pop(0)

    print(text_list)

    text_list.pop()

    print(text_list)

    text_list = ["Alberta" if item == "AB" else item for item in text_list]

    print()

    print(text_list)

def read_file(filename):
  
    text_list = []
    
    with open(filename, "rt") as text_file:
        
        for line in text_file:

            clean_line = line.strip()

            text_list.append(clean_line)

    return text_list

if __name__ == "__main__":
    main()