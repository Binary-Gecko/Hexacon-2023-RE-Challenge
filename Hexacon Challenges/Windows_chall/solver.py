keys= '-muyx_vbm8cip2n9iv05c0'
enc = [-18100,-16825,-31627,-28850,-30653,-22686,-30897,-29844,-17585,-31134,-17812,-29609,-17848,-19095,-30861,-28057,-28558,-26033,-31378,-30093,-20176,-32256]
flag1=""
c = 0
for i in range(len(enc)):
    flag1+=chr(enc[i] & 0xFF)
    enc[i]=enc[i]-(enc[i] & 0xFF)
flag2=""
c=0
for i in range(len(enc)):
    flag2+= chr((~(enc[i]))>>8)
    c+=2
flag=""
for i in range(len(flag1)):
    flag+=flag2[i]+flag1[i]
print(flag)
#cipher[j] = ((~(flag[i] ^ i ^ reference_string[rand() % (len(reference_string) - 1)])) << 8) + flag[i + 1];
#FLAG{upNwCXbxOtlDOybElsWEHJixsmgoreOznusN0}'''
'''
import random

ciphered_flag = [-9652,-28345,-6283,-7090,-6077,-10142,-7345,-916,-31153,-5022,-11156,-15017,-13752,-9879,-3725,-4505,-32654,-10929,-27026,-27533,-21968,-13568]
random_string = "-muyx_vbm8cip2n9iv05c0"

# Reverse the ciphered_flag to obtain the original flag
flag = []

for cipher_value in ciphered_flag:
    # Extract the second byte of cipher_value
    flag.append(cipher_value & 0xFF)

# Reverse the encryption process
original_flag = []
for i in range(len(flag)):
    # Extract the corresponding character from the random string
    random_char = random_string[i % len(random_string)]
    # Reverse the XOR operation
    original_char = chr(flag[i] ^ i ^ ord(random_char))
    original_flag.append(original_char)

# Convert the list of characters to a string
original_flag_str = ''.join(original_flag)
print("Original Flag:", original_flag_str)
'''