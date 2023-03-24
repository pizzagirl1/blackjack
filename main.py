from helpers import build_deck, deal_hand, \
    score_hand, print_hand, print_dealer, \
    hit_player

def game(): 
    game_board = (build_deck())
    player_hand = deal_hand(game_board)
    dealer = deal_hand(game_board)
    print()
    print("DEALER:")
    print_dealer(dealer)
    dealer_score = score_hand(dealer)
    print()
    print("PLAYER:")
    print_hand(player_hand)
    player_score = score_hand(player_hand)
    print(f"{player_score=}")
    print()
    # ask if player wants to hit
    while player_score < 21:
        user_response = input("hit? ")
        if user_response == "y":
            hit_player(game_board, player_hand)
            print_hand(player_hand)
            player_score = score_hand(player_hand)
            print(f"{player_score=}")
        else:
            break

    if player_score > 21:
        print("BUST. You Lose.")
        quit()
    
    while dealer_score < 17:
        hit_player(game_board, dealer)
        dealer_score = score_hand(dealer)
    
    print()
    print("DEALER:")
    print_hand(dealer)
    print(f"{dealer_score=}")
    print()
    print("PLAYER:")
    print_hand(player_hand)
    print(f"{player_score=}")
    print()
    if dealer_score > 21:
        print("Dealer busts! You win!")
    elif dealer_score > player_score:
        print("You lose!")
    else:
        print("You win!")
    print()



game()