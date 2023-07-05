def begin_auction():
    # Create dictonary for storing the name and bid for each participant
    participants = {}
    cont = "yes"
    print("Welcome to the auction!")
    # Fill out each partcipant's information into the dictionary
    while cont == "yes":
        name = str(input("What is your name?: "))
        bid = int(input("How much will you bid?: "))
        participants[name] = bid
        cont = str(input("Are there any other bidders?: ")).lower()

    # to retreive max bid, check each particpant's bid and adjust the max bid
    max_bid = -1
    for key in participants:
        if participants[key] > max_bid:
            max_bid = participants[key]
    key_list = list(participants.keys())
    value_list = list(participants.values())
    index = value_list.index(max_bid)
    print(f"The winner of the auction is {key_list[index]} with a bid of ${max_bid}!")

begin_auction()