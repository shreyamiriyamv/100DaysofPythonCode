from art import logo
print(logo)

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        if bidding_dictionary[bidder] > highest_bid:
            highest_bid = bidding_dictionary[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


blind_auction = {}
auction_running = True
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
while auction_running:
    name = input("What is your name?:  ")
    bid = int(input("What is your bid?: $ "))
    blind_auction[name] = bid
    question = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    print("\n" * 100)
    if question == "no":
        auction_running = False
        find_highest_bidder(blind_auction)