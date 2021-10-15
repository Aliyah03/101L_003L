import string
string.ascii_uppercase
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
space=' '

def encrypt_string(state):
    script=input("Enter (brief) text to encrypt: ").upper()
    shift=int(input("Enter the number to shift letters by: "))
    print("Encrypted: ", end='')
    for i in script:
        ch="script"
        ch_value=ord(i)
        #print(i)
        #print(ch_value)
        chn=ch_value+shift
        if chn>90 or chn<65:
            #print(chn)
            chn=chn-26
        else:
            pass
        ch_new=chr(chn)
        ch_news=ch_new.upper()
        if ch_news not in letters:
            print(space, end='')
        elif ch_news in letters:
            print(*ch_news, end='') 

def decrypt_string(state):
    script=input("Enter (brief) text to decrypt: ").upper()
    shift=int(input("Enter the number to shift letters by: "))
    print("Decrypted: ", end='')
    for i in script:
        ch="script"
        ch_value=ord(i)
        chn=ch_value-shift
        if chn>90 or chn<65:
            chn=chn+26
        else:
            pass
        ch_new=chr(chn)
        ch_news=ch_new.upper()
        if ch_news not in letters:
            print(space, end='')            
        elif ch_news in letters:
            print(*ch_news, end='')



if __name__ == "__main__":
    playing = True
    while playing:
        print("\nMAIN MENU:\n1) Encode a string\n2) Decode a string\nQ) Quit")
        state=input("Enter your selection ==> ")
        if state=="1":
            encrypt_string(state)
            print()
        elif state=="2":
            decrypt_string(state)
            print()
        elif state=="Q" or state=="q":
            break
        elif state != "1" and "2" and "Q" and "q":
            print("Invalid Entry. RETRY.")