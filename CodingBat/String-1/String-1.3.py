#https://codingbat.com/prob/p132290
#The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text.
#In this example, the "i" tag makes <i> and </i> which surround the word "Yay".
#Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>

def make_tags(tag, word):
    return print(f'<{tag}>{word}<{tag}/>')

print("Enter an HTML tag and an word seperated via the Enter key")
print(make_tags((str(input())), (str(input()))))