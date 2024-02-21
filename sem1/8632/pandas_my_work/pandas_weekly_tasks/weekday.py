from datetime import datetime

def is_weekend(date):
    """
    Function to determine if the input day is a weekend day.
    """

    #Find the numerical value for the day of the week (count starts at 0 for Monday)
    day = date.date().weekday()

    #Check if the day number corresponds to a weekend day (where Saturday is 5)
    if day >= 5:
        return "It is the weekend, yay!"
    
    else:
        return "Yes, unfortunately today is a weekday."

def main():
    #Get today's date
    today = datetime.now()

    #Check if it's a weekend day
    print(is_weekend(today))

if __name__ == "__main__":
    main()
