def main():
    while True:
        try:
            amount1 = int(input("Enter amount1 (in cents):"))
            amount2 = int(input("Enter amount2 (in cents):"))

            total_cents = amount1 + amount2

            euro_value = total_cents // 100
            cent_value = total_cents % 100

            res_str = "The sum of these is €" + str(euro_value) + "." + str(cent_value)

            print(res_str)

        except ValueError:
            print("Please enter an integer value.")
            continue

        break
        
if __name__ == '__main__':
    main()