#https://codingbat.com/prob/p129981
#Given an "out" string length 4, such as "<<>>", and a word, return a new string
#where the word is in the middle of the out string, e.g. "<<word>>".

def make_out_word(out, word):
  outslice1 = out[0:2]
  outslice2 = out[2:4]
  return print(f'{outslice1}{word}{outslice2}')
  
print("Enter a surrounding bracket either <. (, {, or [ in a set of 4 <<>> )")
print("Then seperate via the enter key, enter a word")
print(make_out_word((str(input())), (str(input()))))