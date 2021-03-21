############### The Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
#from replit import clear
import os
 


cards_list = [11, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check(user_cards, computer_cards):
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  if computer_score > user_score:
    return "Computer"
  else:
    return "You"
  

def calculate_score(cards):
  sum1 = 0
  sum2 = 0
  for i in range(0, len(cards)):
    sum1 += cards[i]
  if 11 in cards:
    sum2 = sum1 - 10
    if sum1 > 21 :
      return sum2
    else:
      return max(sum1, sum2)
  else:
    return sum1
  


def start():
  print(logo)
  #computer
  computer_cards = []
  computer_cards.append(cards_list[random.randint(0,11)])
  computer_cards.append(cards_list[random.randint(0,11)])

  #User
  user_cards = []
  user_cards.append(cards_list[random.randint(0,11)])
  user_cards.append(cards_list[random.randint(0,11)])

  print(f"Your Cards are : [{user_cards[0]}, {user_cards[1]}]")
  print(f"Computer has revealed the Card : [{computer_cards[0]}]")
  score = calculate_score(user_cards)
  print(f"Your current score is : {score}")

  #computer_cards
  if calculate_score(computer_cards) < 17:
    computer_cards.append(cards_list[random.randint(0,11)])
  # if calculate_score(computer_cards) > 21:
    # print("Computer Lose")
    # return
    

  #user
  def more():
    choice = input("Would you like another card? : ").lower()
    if choice == "yes":
      user_cards.append(cards_list[random.randint(0,11)])
      score = calculate_score(user_cards)
      print(f"Your current score is : {score}")
      if score <= 21:
        more()
      else:
        print("You Lose")
        return
    else:
      print("We will reveal the cards now!")
      user_score = calculate_score(user_cards)
      print(f"Your score is {user_score}")
      computer_score = calculate_score(computer_cards)
      print(f"Computer's score is {computer_score}")
      if user_score > 21:
        print("You Lose")
        return
      else:
        winner = check(user_cards, computer_cards)
        if calculate_score(computer_cards) > 21:
          print("You won!")
        elif calculate_score(computer_cards) == calculate_score(user_cards):
          print("Draw!")
        else:
          print(f"{winner} won!")
        greet()
  more()

      

def greet():
  start_game = input("Would you like to play? : ").lower()
  if start_game == "yes":
    # clear()
    os.system('cls')
    start()
  else:
    # clear()
    os.system('cls')
    print("Goodbye!")

greet()
  
