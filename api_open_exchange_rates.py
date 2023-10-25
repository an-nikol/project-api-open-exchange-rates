import requests
import json


def choice_01():
    json_dict_all_currencies = response.json()['rates']
    json_string_all_currencies = json.dumps(json_dict_all_currencies)
    python_dict_all_currencies = json.loads(json_string_all_currencies)
    for key in python_dict_all_currencies.keys():
        print(key, " - ", python_dict_all_currencies[key])

def choice_02():
    pass


def choice_03():
    pass


def choice_04():
    pass


def choice_05():
    pass


while True:
    response = requests.get('https://openexchangerates.org/api/latest.json?app_id=2a79f1183f864ff19561b6a9e9d09860')
    # i want users to click these icons
    print('Menu')
    print('Please choose one of the options below:')
    print('1. All current currency rates')
    print('2. A specific currency rate')
    print('3. Historical currency rates ')
    print('4. Convert from USD to another currency')
    print('5. Statistics for usage')
    print('6. Quit')

    choice = int(input('Enter your choice (1/2/3/4): '))
    if choice == 1:
        choice_01()
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass



