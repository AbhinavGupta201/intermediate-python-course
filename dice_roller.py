import random 

def main():
  dice_rolls=2
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    dice_sum = dice_sum + roll
    # Note that the beginning and the end of the range are inclusive bounds. That is, 1 and 6 are possible values, along with integers between them.

    print(f'You rolled a {roll}')

  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()