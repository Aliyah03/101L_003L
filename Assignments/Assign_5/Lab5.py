import string

def character_value(charac : str) -> int:
    #print("checking character_value")
    #print(charac)
    newcharac=string.ascii_uppercase.index(charac)
    #print(newcharac)
    return string.ascii_uppercase.index(charac)

    


def get_check_digit(card_num : str) -> int:
    #print("checking get_check_digit")
    Total=0
    for card_num,ch in enumerate(card_num[0:5],1):
        #print(ch)
        Total=Total+(card_num+1)*character_value(ch)
        #print(Total)
    #for card_num,ch in enumerate(card_num[5:10],5):
        #Total=Total+(card_num+1)*ch
        #print(ch)
    return Total%10
     

def is_valid(card_num : str) -> tuple:
    #print("checking is_valid")
    if len(card_num)!=10:
        return False, "The length of the number given must be 10"
    elif len(card_num)==10:
        return True 
    print(is_valid)

def check_characters(card_num : str) -> tuple:
        for i in range(5):
            if card_num[i] not in string.ascii_uppercase:
                print("The first 5 characters must be A-Z, the invalid character is at ", i)
            break 
        else:
            print("Charaters valid")
    


def check_numbers(card_num : str) -> tuple:
        #print("checking check_numbers")
        for i in range(7,10):
            if card_num[i] not in string.digits:
                print("The last 3 digits must be 0-9, the invalid character is at ", i)
            break
        else:
            print("Characters valid")


def verify_check_digit(results : str) -> tuple:
    #print("checking verify_check_digit")
    res=is_valid(results)
    #print(res)
    if res==True:
        check_digit=int(is_valid(results))
        #print(check_digit)
        calculated_digit=get_check_digit(results)
        if check_digit!=calculated_digit:
            #print(calculated_digit)
            return False
        else:
            return True, ""
    else:
        return False, results
    


def get_school(card_num : str) -> str:
    #print("checking get_school")
    school=card_num[5]
    if school=="1":
        print("School of Computing and Engineering SCE")
    elif school=="2":
        print("School of Law")
    elif school=="3":
        print("College of Arts and Science")
    else:
        print("Invalid School")

def get_grade(gradelevel : str) -> str:
    #print("checking get_grade")
    gradelevel=card_num[6]
    if gradelevel=="1":
        print("Freshman")
    elif gradelevel=="2":
        print("Sophomore")
    elif gradelevel=="3":
        print("Junior")
    elif gradelevel=="4":
        print("Senior")
    else:
        print("Invalid Grade")


if __name__=="__main__":
    print("Linda Hall")
    print("Linda Hall Card Check")
    while True:
        print()
        card_num=input("Enter Library Card. Hit enter to Exit ==>").upper().strip()
        if card_num=="":
            break
        else:
            result = (verify_check_digit(card_num))
            check = (check_characters(card_num))
            nums = (check_numbers(card_num))
            digit = (get_check_digit(card_num))
            valid = (is_valid(card_num))
            school = (get_school(card_num))
            grade = (get_grade(card_num))


            if result==True:
                print("Library card is invalid")
                print("The card belongs to a student in()".format(get_school(card_num)))
                print("The card belongs to a ()".format(get_grade(card_num)))
            else:
                print("Library card is valid")
                
        