#https://codingbat.com/prob/p195669
#When squirrels get together for a party, they like to have cigars.
#A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
#Unless it is the weekend, in which case there is no upper bound on the number of cigars.
#Return True if the party with the given values is successful, or False otherwise.

def cigar_party(cigars, is_weekend):
    # If it's the weekend, cigars can be 40 or more
    if is_weekend.lower() == 'yes':
        return cigars >= 40
    # Otherwise, cigars must be between 40 and 60, inclusive
    else:
        return 40 <= cigars <= 60

print("You have a group of sqirrels that are 21 years of squireel age")
print("They party and smoke cigars but they have an overly technical way of analyzing parties")
print("If they have between 40 and 60 CIGARS, it's a good party.. I guess")
print("BUT if it's the weekend, they can have as many as they want and sill have a good party")
print("")
print("Enter the number of cigars the squirrels have")
cigars = int(input())
print("Then enter if it is the weekend enter Yes no No")
is_weekend = input()
print(cigar_party((cigars), (is_weekend)))

