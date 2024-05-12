from menuoptions import *

def user_interface():
    print("="*40)
    print("                  MENU                   ")
    print("="*40)

    print("1 - View Cities by Country")
    print("2 - Update City Population")
    print("3 - Add New Person")
    print("4 - Delete Person")
    print("5 - View Countries by population")
    print("6 - Show Twinned Cities")
    print("7 - Twin with Dublin")
    print("x - Exit")

def exit_application():
    print("Exiting the application.")
    exit()

def get_input():
    answer = input("Choice: ")

    return answer

def main():
    while True:
        user_interface()

        user_value = get_input()

        menu_options = {
            '1': view_cities_by_country,
            '2': update_city_pop,
            '3': add_new_person,
            '4': delete_person,
            '5': view_countries,
            '6': twinned_cities,
            '7': twinned_with_dublin,
            'x': exit_application
        }

        if user_value in menu_options:
            menu_options[user_value]()

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()

