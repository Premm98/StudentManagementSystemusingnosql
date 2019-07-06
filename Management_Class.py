

import Management_Database

class Management():

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def display_data(self):
        print("Name of the employee is: ", self.name)
        print("Address of the employee is: ", self.address)
        print("Phone number of the employee is: ", self.phone)

    def save_details(self):
        Management_Database.save_record(self.name, self.address, self.phone)
