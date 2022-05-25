class parkingGarage():

    def __init__(self, tickets, spaces, currentTicket):
        self.tickets = tickets
        self.spaces = spaces
        self.currentTicket = currentTicket

    def takeTicket(self):
        self.tickets.pop()
        self.spaces.pop()
                
    def payForParking(self):
        self.tickets.insert()

    def leaveGarage(self):
        self.spaces.insert()



one_Garage = parkingGarage([1,2,3,4,5], [1,2,3,4,5], 2.50)

def two_Garage():

    while True:
        response = input("Welcome to the garage, choose 'take'/'pay for parking'/'ticket paid'/'leave garage': ")       

        if response == 'take':
            one_Garage.takeTicket()
            print("Here is your ticket.")

        elif response.lower() == "pay for parking":
            print("Please pay for your ticket.")
        
        elif response.lower() == "ticket paid":
            one_Garage.payForParking()
            print("Thank you. You have 15 minutes to exit the parking garage.")

        elif response.lower() == "leave garage":
            one_Garage.leaveGarage()
            print("Thank you for choosing our parking garage!")
            break

        else:
            print("Please select an option.")

two_Garage()

