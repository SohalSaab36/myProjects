import random
import sys
dice = [1,2,3,4,5,6]
def roll():
    print(f"your dice no. is : {random.choice(dice)}")
def main():
    roll()
    a = input('do you want to continue (y/n) : ').lower()
    if a == "y":
        main()
    elif a == "n":
        sys.exit()
    else:
        main()
if __name__ == "__main__":
    main()

