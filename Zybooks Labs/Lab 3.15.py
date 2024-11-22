# https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/3/section/15 Musical note frequencies
#On a piano, a key has a frequency, say f0
#Each higher key (black or white) has a frequency of f0 * r^n, where n is the distance (number of keys) from that key, and r is 2^(1/12)
#Given an initial key frequency, output that frequency and the next 3 higher key frequencies
#Output each floating-point value with two digits after the decimal point, then the units ("Hz"), then a newline, using the following statement
#print(f'{your_value:.2f} Hz')
#input 440 | outputHz 440.00 \n 466.16Hz \n 493.88Hz\n 523.25Hz

Note = float(440)
R = pow(2,(1/12))

out1 = Note * pow(R, 0)
out2 = Note * pow(R, 1)
out3 = Note * pow(R, 2)
out4 = Note * pow(R, 3)

print(f'{out1:.2f} Hz')
print(f'{out2:.2f} Hz')
print(f'{out3:.2f} Hz')
print(f'{out4:.2f} Hz')
