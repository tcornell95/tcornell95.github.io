#----------------------------------------------------
# Author:   Tyler Cornell
# Creation: 03 March 2019
# Updated:  20 March 2023
#
# Description:
# Invoicing system for Davy's Auto Shop Services that
# takes user input of two services and outputs the 
# total cost to the user. The dictionary stores the possible services
# for the user to select from with their respective pricing.
#
# ASCII Art Generator: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
# ASCII Art Font: Standard
#----------------------------------------------------
import os

#Resize terminal window to display ASCII art banner correctly
cmd = 'mode 145, 40'
os.system(cmd)

#Dictionary containing services and their prices provided by the auto shop to the user
service_prices = {
    'oil change': 35,
    'tire rotation': 19,
    'car wash': 7,
    'car wax': 12,
    '-': 0
}

#Class containing user input for service and displaying it; and get service price
class Request:
    def __init__(self):
        while True:
            try:
                #Get user input and convert to lowercase
                self.service = input('Select a service: \n')
                self.service = self.service.lower()              
                
                #If service is greater than 0 print service name with cost
                if service_prices[self.service] > 0:
                    name = self.service
                    price = str(service_prices[self.service])
                    print(f"Service: {name} - ${price}")
                #if service is equal to 0 then print no service
                elif service_prices[self.service] == 0:
                    print("No service")
                break
            #if user select a service not in dictionary, ask to reselect
            except KeyError:
                print("Please select a valid service!")
                continue
                        
    def getPrice(self):
        return service_prices[self.service]

#ASCII art on initial start displaying the shops name
print(r"""
           _____                    _                     _           _____ _                    _____                 _               
          |  __ \                  ( )         /\        | |         / ____| |                  / ____|               (_)              
          | |  | | __ ___   ___   _|/ ___     /  \  _   _| |_ ___   | (___ | |__   ___  _ __   | (___   ___ _ ____   ___  ___ ___  ___ 
          | |  | |/ _` \ \ / / | | | / __|   / /\ \| | | | __/ _ \   \___ \| '_ \ / _ \| '_ \   \___ \ / _ \ '__\ \ / / |/ __/ _ \/ __|
          | |__| | (_| |\ V /| |_| | \__ \  / ____ \ |_| | || (_) |  ____) | | | | (_) | |_) |  ____) |  __/ |   \ V /| | (_|  __/\__ \
          |_____/ \__,_| \_/  \__, | |___/ /_/    \_\__,_|\__\___/  |_____/|_| |_|\___/| .__/  |_____/ \___|_|    \_/ |_|\___\___||___/
                               __/ |                                                   | |                                             
                              |___/                                                    |_|                                             """)

#Print list of auto shop services available for the user to select
print('\nPlease select services from the list below:')
print('Oil change    -- $35')
print('Tire rotation -- $19')
print('Car wash      -- $7')
print('Car wax       -- $12')
print('No service    -- Type \'-\'\n')

#Call function to get service requests and print them
service1 = Request()
service2 = Request()

#Print ASCCI art and the total cost to the user
print(r"""
           ____                    _          _         _          ____  _                   ___                 _          
          |  _ \  __ ___   ___   _( )___     / \  _   _| |_ ___   / ___|| |__   ___  _ __   |_ _|_ ____   _____ (_) ___ ___ 
          | | | |/ _` \ \ / / | | |// __|   / _ \| | | | __/ _ \  \___ \| '_ \ / _ \| '_ \   | || '_ \ \ / / _ \| |/ __/ _ \
          | |_| | (_| |\ V /| |_| | \__ \  / ___ \ |_| | || (_) |  ___) | | | | (_) | |_) |  | || | | \ V / (_) | | (_|  __/
          |____/ \__,_| \_/  \__, | |___/ /_/   \_\__,_|\__\___/  |____/|_| |_|\___/| .__/  |___|_| |_|\_/ \___/|_|\___\___|
                             |___/                                                  |_|                                     """)
print("Total: $", end='')
print(service1.getPrice() + service2.getPrice())

#Prevent terminal from closing automatically at end for particular launch cases
os.system("pause")