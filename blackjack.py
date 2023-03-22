import random

def bet():
  pass

def build_deck():
  my_deck = []
  
  for suit in range(4):
    for num in range(2,10):
      my_deck.append(num)
    for face  in ["T", "J", "Q", "K", "A"]:
      my_deck.append(face)
  return my_deck

def draw_card(deck):  
  card = random.choice(deck)
  deck.remove(card)
  return card

def deal_hand(my_deck):
  hand = []
  hand.append(draw_card(my_deck))
  hand.append(draw_card(my_deck))
  print(f"{hand=}")
  return hand

def print_hand(hand):
  horizontal_line = " --" * len(hand)
  print(horizontal_line)
  print_row = "| "
  for card in hand:
      cardname = str(card)
      print_row += (cardname)
      print_row += "| "
  print(print_row)
  print(horizontal_line)

def hit_player(player, hand):
  pass

def hit_dealer(dealer, hand):
  pass

def score_hand(hand):
    score = 0
    if len(hand) > 5:
        return "Invalid"

    num_aces = 0
    
    for card in hand:
        if card in ["T", "J", "Q", "K"]:
            score += 10
        elif card == "A":
            num_aces += 1
        else:
            score += card

        if score > 21:
            return "Bust"
    
    # at most 1 ace can be 11, the rest must be 1
    if num_aces > 0:
        temp_score  = score + 11 + (num_aces - 1)
        if temp_score > 21:
            score = score + num_aces
        else:
            score = temp_score

    if score > 21:
        return "Bust"  

    print(f"{score=}")
    return score

def declare_winner(hands):
  pass

def pay_out(bet, winner):
  pass

def game(): 
  game_board = (build_deck())
  player_hand = deal_hand(game_board)
  player_score = score_hand(player_hand)
  print_hand(player_hand)

game()