import random

def play_again():
    
    while True:
        pa = input("Do you want to play again? ==> ")
        if pa == 'y' or pa == 'Y' or pa == 'yes' or pa == 'YES':
            return True
            break
        elif pa == 'n' or pa == 'N' or pa == 'no' or pa == 'NO':
            return False
            break
        else:
            print("You must enter Y/YES/N/NO to continue. Please try again")
            pass
        
        
     
def get_wager(bank : int):
    while True:
        b = int(input("How many chips do you want to wager? ==> "))
        if b <= 0:
            print("Too low a value, you can only choose 1 -", bank, "chips")
        elif b > bank:
            print("Too high a value, you can only choose 1 -", bank, "chips")
        elif b > 0 and b <= bank:
            break            
    return b

def get_slot_results():
    r1 = random.randint(1, 10)
    r2 = random.randint(1, 10)
    r3 = random.randint(1, 10)
    return r1, r2, r3
    

def get_matches(ra, rb, rc) -> int:
    if ra == rb and ra == rc:
        return 3
    elif ra == rb or ra == rc or rb == rc:
        return 2
    else:
        return 0

def get_bank():
    while True:
        bn = int(input("How many chips do you want to start with? ==>"))
        if bn <= 0:
            print("Too low a value, you can only choose 1 - 100 chips")
        elif bn > 100:
            print("Too high a value, you can only choose 1 - 100 chips")
        elif bn > 0 and bn <= 100:
            return bn
            break

def get_payout(wager, matches):
    if matches == 3:
        pay1 = (10 * wager) - wager
    elif matches == 2:
        pay1 = (3 * wager) - wager
    elif matches == 0:
        pay1 = - wager
    return pay1    


if __name__ == "__main__":
    playing = True
    wager = 0
    counter=0
    chipcount=0
    maxbn=0
    while playing:
        bank = get_bank()
        chipcount=bank
        maxbank=bank
        counter=0
        while bank >= wager:
            wager = get_wager(bank)
            get_slot_results()
            reel1, reel2, reel3 = get_slot_results()
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            if bank>maxbank:
                maxbank=bank
            else:
                ()

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            counter=counter+1
            
            


            
        
        
        print("You lost all", chipcount, "in", counter , "spins")
        print("The most chips you had was", maxbank)
        playing = play_again()