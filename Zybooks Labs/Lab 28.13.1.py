#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/28/section/13

jpy1 = int(input("Enter player 1's jersey number:\n"))
jr1 = int(input("Enter player 1's rating:\n"))
print("")
jpy2 = int(input("Enter player 2's jersey number:\n"))
jr2 = int(input("Enter player 2's rating:\n"))
print("")
jpy3 = int(input("Enter player 3's jersey number:\n"))
jr3 = int(input("Enter player 3's rating:\n"))
print("")
jpy4 = int(input("Enter player 4's jersey number:\n"))
jr4 = int(input("Enter player 4's rating:\n"))
print("")
jpy5 = int(input("Enter player 5's jersey number:\n"))
jr5 = int(input("Enter player 5's rating:\n"))
print("")
roster = {jpy1:jr1, jpy2:jr2, jpy3:jr3, jpy4:jr4, jpy5:jr5}

print("ROSTER")
for key, value in roster:
    print(f"Jersey number: {key}, Rating: {value}")

print("")
print("MENUE")
print("a - Add player")
print("d - Remove player")
print("u - Update player rating")
print("r - Output players above a rating")
print("o - Output roster")
print("q - Quit")


def add_player(roster):
    jersey = int(input("Enter a new player's jersey number:\n"))
    rating = int(input("Enter the player's rating:\n"))
    print("")
    roster[jersey] = rating

def remove_player(roster):
    jersey = int(input("Enter a jersey number:\n"))
    if jersey in roster:
        del roster[jersey]
    else:
        print("Player not found.")
def update_player_rating(roster):
    jersey = int(input("Enter a jersey number:\n"))
    if jersey in roster:
        new_rating = int(input("Enter a new rating for player:\n"))
        roster[jersey] = new_rating
    else:
        print("Player not found.")

def output_players_above_rating(roster):
    rating = int(input("Enter a rating:\n"))
    print(f"ABOVE {rating}")
    for jersey, player_rating in roster.items():
        if player_rating > rating:
            print(f"Jersey number: {jersey}, Rating: {player_rating}")

def output_roster(roster):
    print("ROSTER")
    for jersey in sorted(roster.keys()):
        print(f"Jersey number: {jersey}, Rating: {roster[jersey]}")

choice = input("Choose an option:")
if choice == "a":
    add_player(roster)
elif choice == 'd':
    remove_player(roster)
elif choice == 'u':
    update_player_rating(roster)
elif choice == 'r':
    output_players_above_rating(roster)
elif choice == 'o':
    output_roster(roster)

    

