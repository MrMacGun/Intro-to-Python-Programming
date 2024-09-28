Line1str = str()

while Line1str != str(quit):
    Line1str = str(input())
    Line1strslice = Line1str[-1]
    NewLinestr = Line1str.split()

    print(f"Eating {Line1strslice} {NewLinestr[0]} a day keeps the doctor away.")