import random
from time import sleep


def main():
    # player_count=1
    player_count = int(input("enter the number of player: "))
    # print(player_count)
    info = {}
    total={}
    for i in range(0, player_count):
        info[f'player{i+1}'] = input(f'Enter the Player Name{i+1}: ')
    print("\n")
    dice_rolls = int ( input("Enter the No of dice Roles: "))
    print("\n")
    sleep(1)
    for k, v in info.items():
        print(f'Player: {v} is rolling ......')
       
        # dice_rolls = 1
        dice_sum = 0
        for i in range(0, dice_rolls):
            sleep(1)
            roll = random.randint(1, 6)
            dice_sum = dice_sum + roll
            # Note that the beginning and the end of the range are inclusive bounds. That is, 1 and 6 are possible values, along with integers between them.
            if roll == 1:
                print(f'You rolled a {roll}! Critical Fail')
            elif roll == 6:
                print(f'You rolled a {roll}! Critical Success!')
            else:
                print(f'You rolled a {roll}')
        sleep(1)
        print(f'{v} have rolled a total of {dice_sum}')
        total[v]=dice_sum
        print("\n")
    
    max=-1;
    winner="Draw"
    count=0
    for k,v in total.items():
      if v==max :
        count=count+1
        max=v
        winner=k
      elif v>max :
        count=1
        max=v
        winner=k
    sleep(1)
    print("And the Winner is....")
    sleep(3)
    if count>1 :
      print("Game Draw !!!")
    else :
      print(f'Winner Of the Game is: {winner}')


if __name__ == "__main__":
    main()
