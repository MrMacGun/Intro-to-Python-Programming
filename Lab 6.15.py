#Program takes a password and modifies it
#Guess is that algorithm takes each ACII character in the string and subtracts by a different number
#chr(ord(ch)+2)

input_password = input()
password = input_password


def strengthen_password(password):
    replacements = {
        'i': '1',
        'a': '@',
        'm': 'M',
        'B': '8',
        's': '$'
    }
    
    strengthened_password = []
    
    for char in password:
        if char.lower() in replacements:
            strengthened_password.append(replacements[char.lower()])
        else:
            strengthened_password.append(char)
    
    strengthened_password.append('!')
    
    return ''.join(strengthened_password)

# Example usage:
output_password = strengthen_password(input_password)
print(output_password)

