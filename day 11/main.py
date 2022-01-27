from art import logo
import random


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def compare_score(u,c):
  if u>21 and c>21:
    return "You lose"
  if u==c:
    return "Draw"
  elif u>21:
    return "you lose"
  elif c>21:
    return "Computer loses"
  elif u>c:
    return "You win"
  elif c>u:
    return "Computer wins"
  else:
    return "You lose"

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

print(logo)

def play_game():
  L = []
  C = []
  done = False

  for _ in range(2):
    L.append(deal_card())
    C.append(deal_card())

  while not done:
    user_score = calculate_score(L)
    computer_score = calculate_score(C)
    print("Your cards:",L,"current score:",user_score)
    print("Computer's first card:",C[0])

    if user_score == 0 or computer_score == 0 or user_score > 21:
      done = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        L.append(deal_card())
      else:
        done = True

  while computer_score != 0 and computer_score < 17:
    C.append(deal_card())
    computer_score = calculate_score(C)

  print("Your final hand:",L,"final score:",user_score)
  print("Computer's final hand:",C,"final score:",computer_score)
  print(compare_score(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()




