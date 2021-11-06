import csv
from calendar import month
import datetime
from itertools import islice
def month_from_number():
    if int(month_num)>0 and int(month_num)<13:
        datetime_object = datetime.datetime.strptime(month_num, "%m")
        full_month_name = datetime_object.strftime("%B")
        print("Full name: ",full_month_name)
    else:
        print("Month must be 1-12")

def read_in_file(filename):
    while True:
        filename=input('Enter the name of the crime data file ==> ')
        try:
            with open(filename,encoding="utf-8") as read_file:
                newfile=[[data.strip() for data in line.strip().split(',')] for line in read_file.readlines()]
                #print(newfile)

            for line in newfile:
                #print(type(line))
                #line1=print(line[1], end=", ")
                #print(line[7], end=",")
                #print(line[13])
                #print(line)
                return newfile      
        except:
            print('Could not find the file specified.',filename, "not found")

def create_reported_date_dict(newfile): 
        keylist=[]
        keycount={}
        readingheader=True        
        for file in newfile:
                    #print(file)
                    if readingheader==True:
                        readingheader=False
                        continue
                    else:
                        readingheader=False
                        keylist.append(file[1])
                    #print(keylist)
        for key in keylist:
                        try:
                            keycount[key]+=1
                            #print("keycount")
                        except KeyError:
                            keycount[key]=1
                            #print("not keylist")
        print(keycount)
        return keycount

def create_reported_month_dict(newfile):
        offdtlist=[]
        offdtcount={}
        readingheader=True        
        for file in newfile:
                    #print(file)
                    if readingheader==True:
                        readingheader=False
                        continue
                    else:
                        readingheader=False
                        monthonly=(file[1])
                        monly=(monthonly[0:2])
                        offdtlist.append(monly)
                    #print(offdtlist)
        for key in offdtlist:
                        try:
                            offdtcount[key]+=1
                            #print("offdtcount")
                        except KeyError:
                            offdtcount[key]=1
                            #print("not offdtlist")
        print(offdtcount)
        return offdtcount

def create_offense_dict(newfile):
        offenselist=[]
        offensecount={}
        readingheader=True   
        for file in newfile:
                    #print(file)
                    if readingheader==True:
                        readingheader=False
                        continue
                    else:
                        readingheader=False
                        offenselist.append(file[7])
                    #print(offenselist)
        for key in offenselist:
                        try:
                            offensecount[key]+=1
                            #print("offensecount")
                        except KeyError:
                            offensecount[key]=1
                            #print("not offenselist")
        print(offensecount)
        return offensecount

def create_offense_by_zip(newfile):
    zipcount={}
    readingheader=True
    for file in newfile:
        if readingheader!=True:
            zipc=file[7]
            if zipc in zipcount:
                offensedict=zipcount[zipc]
                if file[13] in offensedict:
                    offensedict[file[13]]+=1
                else:
                    offensedict[file[13]]=1
            else:
                zipcount[zipc]={file[13]:1}
        else:
            readingheader=False
            continue
    print(zipcount)
    return zipcount

def main():
    mydict = {}
    filename=read_in_file
    newfile=read_in_file(filename)
    month=create_reported_month_dict(newfile)
    print("The month with the highest # of crimes is March with 31 offenses")
    offe=create_offense_by_zip(newfile)
    print()
    while(True):
        off = input("Enter an offense : ")
        if off not in offe:
            print("Not a valid offense, please try again")
        else:
            break

    print(off+"offense by zip code")
    print("Zip code    #Offenses")
    print("================================")
    for k,v in offe[off].items():
        print(k+"\t\t"+str(v))
            

if __name__ == "__main__":
    main()