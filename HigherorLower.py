import random
from Data_for_higher_Lower import data
print("Welcome to guessing the Higher or Lower according their number of followers!!!")
def random_celeb(data_list):
    return random.choice(data)
def format_data(acc):
    name = acc["name"]
    followers = acc["follower_count"]
    description = acc["description"]
    country = acc["country"]
    print(f"{name}, {description}, {country}")
guess = True
points = 0
return_data_NoFromat_A = random_celeb(data)
return_data_NoFromat_B = random_celeb(data)
while guess:
    A = return_data_NoFromat_A["follower_count"]
    B = return_data_NoFromat_A["follower_count"]
    while(A == B):
        return_data_NoFromat_B = random_celeb(data)
        B = return_data_NoFromat_B["follower_count"]
    print(f"Compare A: ")
    format_data(return_data_NoFromat_A)
    print(f"Compare B: ")
    format_data(return_data_NoFromat_B)
    while(A == B):
        return_data_NoFromat_B = random_celeb(data)
        B = return_data_NoFromat_B["follower_count"]
    decision = input("Who has higher follwers 'A' or 'B':")
    while(A == B):
        return_data_NoFromat_B = random_celeb(data)
    if(decision == "A"):
        if(A > B):
            points += 1
            print(f"You guessed correct and you score is {points}")
            return_data_NoFromat_B = random_celeb(data)
        else:
            print(f"You guessed wrong Game over")
            guess = False
    elif(decision == "B"):
        if(B > A):
            points += 1
            print(f"You guessed correct and you score is {points}")
            return_data_NoFromat_A = return_data_NoFromat_B
        else:
            points -= 1
            print("You guessed wrong Game Over")
            guess = False


