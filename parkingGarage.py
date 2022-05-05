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


from multiprocessing.context import SpawnProcess
from urllib import response


class parkingGarage():
    def __init__(self,tickets = 20 ,spaces = 20,currentTicket= {1:2.50, 2:5.00, 3:7.00}):
        self.tickets = tickets
        self.spaces = spaces
        self.currentTicket = currentTicket

        def takeTicket():
            while True:
                print("Welcome to our parking garage. Please take your ticket.")
                tickets.remove()
                spaces.remove()
                
        def payForParking():
            while True:
                print("Choose 1, 2, or 3 hours of parking to pay for your ticket.")
                if input == currentTicket.key:
                    return(currentTicket.value)
                print(currentTicket.value)
                print("Thank you. You have 15 minutes to exit the parking garage.")
                if input != currentTicket.key:
                    print("Please enter a valid number")


        def leaveGarage():
            if input(currentTicket.key) == True:
                tickets.add()
                spaces.add()
                print("Thank you, have a nice day!")
            if input(currentTicket.key) == False:
                print("Please pay for your ticket.")

        leaveGarage()
        payForParking()
        takeTicket()

parkingGarage()

                  