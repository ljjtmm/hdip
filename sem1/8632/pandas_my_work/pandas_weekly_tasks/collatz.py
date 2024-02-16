def collatz_fn(n):
    """
    Function to return a sequence of the desired values based on task description.
    """
    lst = [n]

    while n != 1:
        if n % 2 == 0:
            n = n //2
        
        else:
            n = (n * 3) + 1

        lst.append(n)

    return lst

def main():
    while True:
        try:
            val = int(input("Please enter a postive integer: "))

            if val >= 0:
                seq = collatz_fn(val)

                print(" ". join(map(str, seq)))
            
                break

            else:
                print("Value was not a positive integer. Please retry.")

        except ValueError as ve:
            print(ve)

if __name__ == '__main__':
    main()