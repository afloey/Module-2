class parkingGarage():

   def __init__(self, tickets, spaces, currentTicket):
        self.tickets = tickets
        self.spaces = spaces
        self.currentTicket = currentTicket

    def takeTicket():
        self.tickets.remove()
        self.spaces.remove()
                
    def payForParking():
        self.tickets.add()

    def leaveGarage():
        self.spaces.add()



one_Garage = parkingGarage(20, 20, 2.50)

def one_Garage():

    while True:
        response = input("Welcome to the garage, choose 'take'/'pay for parking'/'ticket paid'/'leave garage': ")        

        if response == 'take':
            one_Garage.takeTicket()

        elif response.lower == 'pay for parking':
            print("Please pay for your ticket.")
        
        elif response.lower == 'ticket paid':
              print("Thank you. You have 15 minutes to exit the parking garage.")
              one_Garage.payForParking()

        elif response.lower == "leave garage":
            print("Thank you for choosing our parking garage!")
            one_Garage.leaveGarage()
            break

        else:
            print("Please select an option.")


one_Garage.takeTicket()
one_Garage.payForParking()
one_Garage.leaveGarage()
