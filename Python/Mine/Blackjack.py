# Don't gamble. I bet on red, but it was black, and I lost 1,500,000 VND.
import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def create_deck():
    return [(rank, suit) for suit in suits for rank in ranks]

def deal_card(deck):
    return deck.pop()

def calculate_score(hand, is_player=True):
    score = 0
    aces = []
    
    for rank, suit in hand:
        if rank in ['J', 'Q', 'K']:
            score += 10
        elif rank == 'A':
            aces.append((rank, suit))  # Save to decide later
        else:
            score += int(rank)
    
    for ace in aces:
        if is_player:
            while True:
                try:
                    value = int(input(f"You got an Ace ({ace[0]} of {ace[1]}). Choose value (1 or 11): "))
                    if value in [1, 11]:
                        score += value
                        break
                    else:
                        print("Please choose 1 or 11.")
                except ValueError:
                    print("Please enter a number.")
        else:
            # Dealer logic: pick 11 if it doesn't bust, otherwise 1
            score += 11 if score + 11 <= 21 else 1

    return score

def show_hand(hand, name, is_player=True):
    formatted_cards = [f"{rank} of {suit}" for rank, suit in hand]
    cards_str = ', '.join(formatted_cards)
    score = calculate_score(hand, is_player)
    print(f"{name}'s hand: {cards_str}  |  Score: {score}")
    return score

def player_turn(deck):
    player_hand = [deal_card(deck), deal_card(deck)]

    while True:
        score = show_hand(player_hand, "Player", is_player=True)
        if score > 21:
            print("💥 Bust! You went over 21.")
            return player_hand, True
        choice = input("Do you want to Hit or Stand? (h/s): ").lower()
        if choice == 'h':
            player_hand.append(deal_card(deck))
        elif choice == 's':
            break
        else:
            print("Invalid choice. Please type 'h' or 's'.")
    return player_hand, False

def dealer_turn(deck):
    dealer_hand = [deal_card(deck), deal_card(deck)]
    print(f"Dealer's hand: {dealer_hand[0]} and [hidden]")
    while calculate_score(dealer_hand, is_player=False) < 17:
        dealer_hand.append(deal_card(deck))
    show_hand(dealer_hand, "Dealer", is_player=False)
    return dealer_hand

def blackjack_game():
    deck = create_deck()
    random.shuffle(deck)

    player_hand, busted = player_turn(deck)
    if busted:
        return "You busted! Dealer wins."

    dealer_hand = dealer_turn(deck)

    player_score = calculate_score(player_hand, is_player=True)
    dealer_score = calculate_score(dealer_hand, is_player=False)

    if dealer_score > 21:
        return "Dealer busted! You win."
    elif player_score > dealer_score:
        return "You win!"
    elif player_score == dealer_score:
        return "It's a tie!"
    else:
        return "Dealer wins!"

# Let's play!
print(blackjack_game())
