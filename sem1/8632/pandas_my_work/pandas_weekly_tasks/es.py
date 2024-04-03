import sys

def count(file_name):
    """
    Function which takes an input of a file name, and returns an output of number of times 'e' appears in the file.
    """

    try:
        #Open the file, read the amount of times 'e' appears in the file
        with open(file_name, 'r') as file:
            txt = file.read()
            count = txt.count('e')

            return count
        
    #Deal with case where the file doesn't exist.
    except FileNotFoundError:
        print("Error: File doesn't exist.")

    #Deal with case where the provided argument isn't a filename, but a directory.
    except IsADirectoryError:
        print("Error: The provided file name is actually a directory.")

    #Deal with case where the file isn't in a text file, and thus can't be read.
    except IOError:
        print("Error: Unable to read the provided file.")

    #Deal with other errors.
    except Exception as e:
        print("Unexpected error occurred:", e)

def main():
    if len(sys.argv) != 2:
        print("python3 es.py <filename>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    
    #Assuming we only want to be checking .txt files here.
    if not file_name.endswith(".txt"):
        print("Error: The file isn't a text file.")
        sys.exit(1)

    count_e = count(file_name)

    #Not providing if/else logic here, as I'm assuming we'll get some value if the file is a text file.
    print(count_e)

if __name__ == '__main__':
    main()