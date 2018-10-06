SERVICE_CHARGE = 2
TICKET_PRICE = 10
tickets_remaining = 100

calculate_price(number_of_tickets):
    return((number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE)

while tickets_remaining:
    print("There are {} tickets remaning".format(tickets_remaining))
    name = input("What's your name ? ")
    try:
        num_tickets = int(input("How many tickets would you like, {}? ".format(name)))
        if num_tickets > tickets_remaining:
            raise ValueError("They are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue, please try again!")
    else:
        amount_due = calculate_price(num_tickets)
        print("The total due is {} . ".format(amount_due))
        should_process = prompt('Do you want processs ? Y/N ')
        if should_process.lower() == 'y':
            print("SOLD! ")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways, {}".format(name))
print("Sorry, the tickets are sold_out")
