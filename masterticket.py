TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

def calculate_price(number_of_tickets):
    return (TICKET_PRICE * number_of_tickets) + SERVICE_CHARGE

while tickets_remaining > 0:
    print("There are {} tickets remaining".format(tickets_remaining))
    name = input("What's your name? ")

    try:
        number_of_tickets = int(input("Hello {}. How many tickets do you need? ".format(name)))
        if number_of_tickets > tickets_remaining:
            raise ValueError("Sorry, don't have this quantity available. Please chose a different quantity".format(tickets_remaining))
        elif number_of_tickets < 1:
            raise ValueError("The mininum amount for purchase is 1")
    except ValueError as err:
        print("That's not a valid value. ({}). Please try again.".format(err))
    else:
        amount_due = calculate_price(number_of_tickets)

        order_confirmed = input("Is this information correct? (Y/N)")
        if order_confirmed.lower() == "y":
            print("Thanks for shopping with us!")
            print("You are buying {} tickets and your total is ${}".format(number_of_tickets, amount_due))
            tickets_remaining -= number_of_tickets
        else:
            print("Thank you anyway, {}.".format(name))
print("Oh no, the tickets are sold out!")