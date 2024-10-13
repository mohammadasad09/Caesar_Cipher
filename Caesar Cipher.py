
def encryption(letter, shift):
    encrypted_code = ""
    for x in letter:
        ascii_values.append(ord(x))
    
    for x in range(len(ascii_values)):
        if ascii_values[x] == 32:
            ascii_values[x] = " "
        
        elif ascii_values[x] + shift > 122:
            ascii_values[x] = chr((ascii_values[x] + shift) - 26)
            
        else:
            ascii_values[x] = chr(ascii_values[x] + shift)
    
        encrypted_code += ascii_values[x]
    print(encrypted_code)

def decryption(letter, shift):
    decrypted_code = ""
    for x in letter:
        ascii_values.append(ord(x))
    
    for x in range(len(ascii_values)):
        if ascii_values[x] == 32:
            ascii_values[x] = " "
                
        elif ascii_values[x] - shift < 97:
            ascii_values[x] = chr((ascii_values[x] - shift) + 26)
            
        else:
            ascii_values[x] = chr(ascii_values[x] - shift)
    
        decrypted_code += ascii_values[x]
    print(decrypted_code)


continuation = "yes"
while continuation == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    string_input = input("Input a string: ").lower()
    shift_number = int(input("Input a shift number: "))
    
    ascii_values = []
    
    if direction == "encode":
        encryption(string_input, shift_number)
    else:
        decryption(string_input, shift_number)
    
    continuation = str(input("Would you like to continue? Enter 'Yes' or 'No': ")).lower()
