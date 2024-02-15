def main():
    acc = ""

    while True:
        acc = str(input("Please enter a 10 digit account number:"))

        if len(acc) == 10:
            print("XXXXXX" + acc[-4:])
            break
        
        else:
            print("Input is incorrect length.")
        
if __name__ == '__main__':
    main()