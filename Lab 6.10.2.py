#This is an ititeration of Simon Says
#Simon outputs a sequnce of 10 characters (R, G, B,Y) and the user must repeat the sequnce
#Use a for loop that compares each character of the two strings
#For each matching character, add one point to user_score
#Upon a mismatch end the loop

user_score = 0
simon_pattern = input()
user_pattern = input()

for simon_char, user_char in zip(simon_pattern, user_pattern):
    if simon_char == user_char:
        user_score += 1
    else:
        break  # End the loop upon the first mismatch