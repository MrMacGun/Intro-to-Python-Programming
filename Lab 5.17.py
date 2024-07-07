#Golf scores record the number of strokes used to get the ball in the hole
#The expected number of strokes varies from hole to hole and is called par (i.e. 3, 4, or 5)
#Each score's name is based on the actual strokes taken compared to par
#"Eagle": number of strokes is two less than par
#"Birdie": number of strokes is one less than par
#"Par": number of strokes equals par
#"Bogey": number of strokes is one more than par
#Given two integers that represent par and the number of strokes used, write a program that prints the appropriate score name.
#Print "Error" if par is not 3, 4, or 5.
Par = int(2)
num_strokes = int(2)

if Par not in [3, 4, 5,]:
    print('Error') 
elif Par - num_strokes == 1:
    print('Birdie')
elif Par - num_strokes == 2:
    print('Eagle')
elif Par == num_strokes:
    print('Par')
elif Par < num_strokes:
    print('Bogey') 

else:
    print('Error') 

#FINALLY MADE WORKING CODE WITH MINIAL HELP =)!!!

