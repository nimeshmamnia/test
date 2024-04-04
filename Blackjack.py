import random, sys
HEARTS = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES = chr(9824) # Character 9824 is '♠'.
CLUBS = chr(9827) # Character 9827 is '♣'.
BACKSIDE = 'backside'


def getHandvalue(cards):
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

    value = 0
    NumberofAces = 0
    for card in cards:
        rank = card[0]
        if rank == 'A':
            NumberofAces += 1
            value += 1
        else:
            value += card_values[rank]

    for i in range(NumberofAces):
        if value + 10 <= 21:
            value += 10
    return value

def displayCards(cards):
    for i, card in enumerate(cards):
        if card == BACKSIDE:
            print(i, 'backside')
        else:
            print(i, card)
def getBet(maxBet):
    while True:
        bet = input('How much do you want to bet? ($1-$5000) or QUIT: ')
        if bet == 'QUIT':
            print('Thanks for playing')
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, show):
    if show:
        print('Dealer Hand:', getHandvalue(dealerHand))
        displayCards(dealerHand)
    else:
        print('Dealer Hand: ???')
        displayCards([BACKSIDE] + dealerHand[1:])

    print('Player Hand:', getHandvalue(playerHand))
    displayCards(playerHand)


print('''Welcome to Blackjack: Rules are -->
Try to get as close to 21 without going over. 
Kings, Queens, Jacks are worth 10 points.
Aces are worth either 1 or 11 points.
Cards 2 to 10 are worth their face values.
(H)it to hit another card
(S)tand to stop taking cards.
D(ouble) down to increase your bet.
In case of a tie, the bet is returned to the player.
The dealer stops hitting at 17.''')
money = 5000
while money > 0:
    print('Money =', money)
    bet = getBet(money)
    deck = getDeck()
    dealerHand = [deck.pop(), deck.pop()]
    playerHand = [deck.pop(), deck.pop()]
    print('Bet =', bet)
    while True:
        print(displayHands(playerHand, dealerHand, False))
        if getHandvalue(playerHand) > 21:
            break

        move = input("Enter your move (H)it or (S)tand or (D)ouble: ")
        if move == 'D':
            additionalbet = getBet(min(bet, money - bet))
            bet += additionalbet
            print('Total Bet increased to', bet)

        if move in ('H', 'D'):
            newCard = deck.pop()
            rank, suit = newCard
            print('You picked up', rank, 'of', suit)
            playerHand.append(newCard)
            if getHandvalue(playerHand) > 21:
                print("You are busted")
                sys.exit()

        if move in ('S', 'D'):
            break

    if getHandvalue(playerHand) <= 21:
        while getHandvalue(dealerHand) < 17:
            print("Dealer hits: ")
            dealerHand.append(deck.pop())
            displayHands(playerHand, dealerHand, False)
            if getHandvalue(dealerHand) > 21:
                break
            input("Press Enter to continue")
            print("\n\n")

            displayHands(playerHand, dealerHand,True)
            playervalue = getHandvalue(playerHand)
            dealervalue = getHandvalue(dealerHand)

            if dealervalue > 21:
                print('Dealer is busted. You win', bet, 'money')
                money += bet
            elif playervalue > 21 or playervalue < dealervalue:
                print('You lost, dealer wins')
                money -= bet
            elif playervalue > dealervalue:
                print('You win', bet, 'money')
                money += bet
            elif playervalue == dealervalue:
                print("It's a tie")

            input("Press Enter to continue")
            print("\n\n")





