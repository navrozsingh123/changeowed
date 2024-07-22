def change_owed(coins):

  # To count total numebr of coins:-
  counter = 0

  # Counter to count each coin:-
  counter_25 = 0
  counter_10 = 0
  counter_5 = 0
  counter_1 =0

  while (counter <= coins):

    # To count number of 25$ coins:
    if (coins >= 25):
      while (coins > 24):
        coins -= 25
        counter += 1
        counter_25 += 1
      print(counter_25,"coin/coins of 25$")

    # To count number of 10$ coins:
    if (coins >= 10):
      while (coins > 9):
        coins -= 10
        counter += 1
        counter_10 += 1
      print(counter_10,"coin/coins of 10$")

    # To count number of 5$ coins:
    if (coins >= 5):
      while (coins > 4):
        coins -= 5
        counter += 1
        counter_5 += 1
      print(counter_5,"coin/coins of 5$")

    # To count number of 1$ coins:
    if (coins >= 1):
      while (coins > 0):
        coins -= 1
        counter += 1
        counter_1 += 1
      print(counter_1,"coin/coins of 1$")

    # To print total number of coins:
    print("Total number of coins:", counter)

# To get input of coins:-
coins = int(input("Change Owed: "))

# Calling the function cahnge_owed:-
change_owed(coins)
