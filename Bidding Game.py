import os
#Welcome the user
print('Welcome to the Auction')

#Initiating the loop with the condition
another_bid = "yes"

#Create an empty dictionary to store all the bids
bids = {}
while another_bid == "yes":

    #Ask fo the name of the bidder
    bidder_name = input("Enter your name: ")

    #Ask for the bid price
    bid_price = float(input("Enter bid amount"))

    #Add the bidder name and the bid price to the empty dict
    bids[bidder_name] = bid_price

    #Ask if there are other users who want to bid
    another_bid = input("Are there any other users who want to bid? Yes or No: ").lower()

    #Lets clear the screen if theres another bid
    if another_bid == "yes":
        os.system("cls")
    
    #printing out the winner
max_value = max(bids.values())
max_bidder_list = [key for key, value in bids.items() if value == max_value]
max_bidder = "".join(max_bidder_list)

print(f"Thanks for all the bids. The winner of this bid round is {max_bidder}")


    
