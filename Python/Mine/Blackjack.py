# Don't gamble. I bet on red, but it was black, and I lost 1,500,000 VND.
import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [(rank, suit) for suit in suits for rank in ranks]

random.shuffle(deck)

def deal_card(deck):
    return deck.pop()

# Deal 2 cards
card1 = deal_card(deck)
card2 = deal_card(deck)

def calculate_score(hand):
    score = 0
    aces = 0

    for rank, suit in hand:
        if rank in ['J', 'Q', 'K']:
            score += 10
        elif rank == 'A':
            aces += 1
            score += 11
        else:
            score += int(rank)
    
    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score

def show_hand(hand, name):
    # Format each card like "3 of Clubs"
    formatted_cards = [f"{rank} of {suit}" for rank, suit in hand]
    cards_str = ', '.join(formatted_cards)
    score = calculate_score(hand)
    print(f"{name}'s hand: {cards_str}  |  Score: {score}")

def player_turn(deck):
    # Start with 2 cards
    player_hand = [deal_card(deck), deal_card(deck)]

    while True:
        show_hand(player_hand, "Player")
        if calculate_score(player_hand) > 21:  # Check if busted
            print("💥 Bust! You went over 21.")
            return player_hand, True  # Return True for bust
        
        choice = input("Do you want to Hit or Stand? (h/s): ").lower()

        if choice == 'h':
            player_hand.append(deal_card(deck))
        elif choice == 's':
            break
        else:
            print("Invalid choice. Please type 'h' or 's'.")

    return player_hand, False  # False means still in the game

# Reset deck first (so you’re not playing with 48 cards left)
deck = [(rank, suit) for suit in suits for rank in ranks]
random.shuffle(deck)

player_hand, busted = player_turn(deck)
if not busted:
    print("You ended your turn with:", calculate_score(player_hand))

def dealer_turn(deck):
    # Dealer starts with 2 cards
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    # Show dealer's hand (but hide one card)
    print(f"Dealer's hand: {dealer_hand[0]} and [hidden]")
    
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))  # Dealer keeps hitting if score < 17
    
    # Now reveal the full dealer hand
    show_hand(dealer_hand, "Dealer")
    return dealer_hand

def blackjack_game():
    # Reset deck
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)

    # Player's turn
    player_hand, busted = player_turn(deck)
    if busted:
        return "You busted! Dealer wins."  # If busted, end game here

    # Dealer's turn
    dealer_hand = dealer_turn(deck)

    # Compare scores
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if dealer_score > 21:
        return "Dealer busted! You win."
    elif player_score > dealer_score:
        return "You win!"
    elif player_score == dealer_score:
        return "It's a tie!"
    else:
        return "Dealer wins!"

print(blackjack_game())