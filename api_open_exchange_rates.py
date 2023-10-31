import requests
import json
from datetime import datetime


class Currency:
    def __init__(self):
        self.api_key = open('api_key').readline().strip()
        self.url = f'https://openexchangerates.org/api/latest.json?app_id={self.api_key}'
        self.output = ''

    def do_request_01(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.output = response.json()['rates']
            str_response = json.dumps(self.output)
            dict_response = json.loads(str_response)
            final_list = []
            for key in dict_response.keys():
                print(key, "     -     ", dict_response[key])
        else:
            return f'Unexpected error. Type of error: {response.status_code}'


while True:
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
        # call object
        current_date = datetime.now().strftime('%d %b %Y')
        print()
        print(f'The date of the request: {current_date}')
        print('Currency - Corresponding rate per 1 USD')
        choice_01 = Currency()
        choice_01.do_request_01()
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
