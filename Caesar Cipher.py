def caesar(letter, shift, cipher_direction):
    converted_code = ""

    for x in range(len(letter)):
        
        if letter[x].isalpha():
            
            if cipher_direction == "encode":
                if letter[x].islower():
                    if ord(letter[x]) + shift > 122:
                        converted_code += chr(ord(letter[x]) + shift - 26)
                    else:
                        converted_code += chr(ord(letter[x]) + shift)
                else:
                    
                    if ord(letter[x]) + shift > 90:
                        converted_code += chr(ord(letter[x]) + shift - 26)
                    else:
                        converted_code += chr(ord(letter[x]) + shift)    
                        
            else: 
                if letter[x].islower():
                    if ord(letter[x]) - shift < 97:
                        converted_code += chr(ord(letter[x]) - shift + 26)
                    else:
                        converted_code += chr(ord(letter[x]) - shift)
                        
                else:
                    if ord(letter[x]) - shift < 65:
                        converted_code += chr(ord(letter[x]) - shift + 26)
                    else:
                        converted_code += chr(ord(letter[x]) - shift)
                        
        else:
            converted_code += letter[x]
    print(f"Your {cipher_direction}d text is {converted_code}")

continuation = "yes"
while continuation == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    while direction not in ['decode', 'encode']:
        direction = input("Incorrect input. Please enter either 'encode' or 'decode': ").lower()
    string_input = input("Input a string: ")
    shift_number = int(input("Input a shift number: ")) % 26
    
    caesar(string_input, shift_number, direction)
    
    continuation = str(input("Would you like to continue? Enter 'Yes' or 'No': ")).lower()
    
    
