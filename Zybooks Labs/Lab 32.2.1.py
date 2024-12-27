
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

if __name__ == "__main__":
    in_str = input()
    result_str = reverse_string(in_str)
    print('Reverse of "' + in_str + '" is "' + result_str + '".')
