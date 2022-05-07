#Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP). 


#Your parking garage class should have the following methods:
#takeTicket- list
    #This should decrease the amount of tickets available by 1
    #This should decrease the amount of parkingSpaces available by 1


#payForParking
    #Display an input that waits for an amount from the user and store it in a variable
    #If the payment variable is not empty then (meaning the ticket has been paid)
     # display a message to the user that their ticket has been paid and they have 15mins to leave
    #This should update the "currentTicket" dictionary key "paid" to True

# leaveGarage
    #If the ticket has been paid, display a message of "Thank You, have a nice day"
    #If the ticket has not been paid, display an input prompt for payment
    #Once paid, display message "Thank you, have a nice day!"
    #Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
    #Update tickets list to increase by 1 (meaning add to the tickets list)

#You will need a few attributes as well:
#tickets -> list
#parkingSpaces -> list
#currentTicket -> dictionary


from urllib import response


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



one_Garage = parkingGarage(20, 20, ['1:2.50', '2:5.00', '3:7.00'])

def run():

    while True:

        print("Welcome to our parking garage. Please take your ticket.")
        if response.lower == 'take':
            one_Garage.takeTicket()

        if response == 'Pay for parking':
            print("Choose 1, 2, or 3 hours of parking to pay for your ticket.")
        
        if response == {one_Garage.currentTicket.key}:
            print("Your total is: {one_Garage.currentTicket.value}")
            one_Garage.currentTicket()
            print("Thank you. You have 15 minutes to exit the parking garage.")

        if response == "Leave garage":
            one_Garage.leaveGarage()
            print("Thank you for choosing our parking garage!")

        else:
            print("Please select an option.")


run()



