import statistics

testscores=[]
assignments=[]

def addtest(testscores):
    addtestscore=float(input("Enter the New Test score 0-100 ==> "))
    if addtestscore<0:
        print("Enter a valid score.")
    else:
       testscores.append(addtestscore)
       #print(testscores)

def removetest(testscores):
    removetestscore=int(input("Enter the Test score to remove 0-100 ==> "))
    #testscores=addtest(number)
    if removetestscore not in testscores:
        print(removetestscore, " Could not find test score to remove.")
    else:
        testscores.remove(removetestscore)
        #print(testscores)

def addassgn(assignments):
    addassgnscore=float(input("Enter the New Assignment score 0-100 ==> "))
    if addassgnscore<0:
        print("Enter a valid score.")
    else:
        assignments.append(addassgnscore)
        #print(assignments)

def removeassgn(assignments):
    removeassgnscore=int(input("Enter the Assignment score to remove 0-100 ==> "))
    #testscores=addtest(number)
    if removeassgnscore not in assignments:
        print("Could not find assignment score to remove.")
    else:
        assignments.remove(removeassgnscore)
        #print(assignments)

def displayscores(testscores, assignments):
    if len(testscores)==0:
        numtest=len(testscores)
        mintest="n/a"
        maxtest="n/a"
        avgtest="n/a"
        stdtest="n/a"
    else:
        numtest=len(testscores)
        mintest=min(testscores)
        maxtest=max(testscores)
        avgtest=statistics.mean(testscores)
        stdtest=statistics.pstdev(testscores)
        stdtest="{:.2f}".format(stdtest)

    if len(assignments)==0:
        numprog=len(assignments)
        minprog="n/a"
        maxprog="n/a"
        avgprog="n/a"
        stdprog="n/a"
    else:
        numprog=len(assignments)
        minprog=min(assignments)
        maxprog=max(assignments)
        avgprog=statistics.mean(assignments)
        stdprog=statistics.pstdev(assignments)
        #print(assignments)
        #print(stdprog)
        stdprog="{:.2f}".format(stdprog)
        #print(stdprog)
        
    if len(testscores)==0 and len(assignments)==0:
        weightedscore="0.0"
    else:
        weightedscore=((avgtest*.6)+(avgprog*.4))


    print("Type             #          Min         Max         Avg         Std\n")
    print("===========================================================================\n")
    print("Test            ", numtest,"\t   ",mintest,"\t",maxtest,"\t   ",avgtest,"\t",stdtest)
    print("Programs        ",numprog,"\t   ",minprog,"\t",maxprog,"\t   ",avgprog,"\t",stdprog)

    print("\nThe weighted score is ", weightedscore)




playing=True
if __name__ == "__main__":
    while playing==True:
        number=input("\t\nGrade Menu\n1 - Add Test\n2 - Remove Test\n3 - Clear Tests\n4 - Add Assingmnet\n5 - Remove Assignment\n6 - Clear Assignments\nD - Display Scores\nQ - Quit\n\n==> ")
        if number=="1":
            addtest(testscores)
        elif number=="2":
            removetest(testscores)
        elif number=="3":
            testscores=[]
            print(testscores)
        elif number=="4":
            addassgn(assignments)
        elif number=="5":
            removeassgn(assignments)
        elif number=="6":
            assignments=[]
            print(assignments)
        elif number=="D" or number=="d":
            displayscores(testscores, assignments)
        elif number=="Q" or number=="q":
            break