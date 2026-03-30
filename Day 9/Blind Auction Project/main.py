  # TODO-1: Ask the user for input
import art
print(art.logo)
print("Welcome to the secret auction program")


bidding = {}
# TODO-2: Save data into dictionary {name: price}
def find_highest_bidding(bidding_dict):
    winner =""
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with highest bid ${highest_bid}")

# TODO-3: Whether if new bids need to be added


continue_bidding = True
while continue_bidding:
    name = input("Enter your name:")
    bid = int(input("enter your bid:$"))

    bidding[name] = bid
    continue_or_not = input("Are there any other bit{type yes if there")
    if continue_or_not == "no":
        continue_bidding = False
        find_highest_bidding(bidding)
    elif continue_or_not == "yes":
        print("\n"*100)

# TODO-4: Compare bids in dictionary


