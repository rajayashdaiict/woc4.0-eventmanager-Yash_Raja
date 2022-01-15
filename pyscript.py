from collections import OrderedDict

from cv2 import FlannBasedMatcher

#functions for searching through dictonary 
def matchingKeys(dictionary, searchString):
    return [key for key,val in dictionary.items() if searchString in key]
def matchingnames(dictionary, searchString):
    return [key for key,val in dictionary.items() if searchString==key]

#function  to print dictonary in fashionable way
def print_out(dictonary) :
    for people , number in dictonary.items():
        print('name :',people,' , ','contact_number :',number ,'\n' )
    print('Thanks for using contact keeper :)')


# Main code starts from here 


d=OrderedDict() # This will be as key as name and value as a list of number 

var = True 
while var :
    print('\n')
    job=input('for insert data press 1 \nfor search data press 2 \nfor see entire database press 3 \nfor reading from a file press 4 \npress any other key to exit \n' )
    # code will check if name is already in dict or not ,  if its not then make a new key value pair , if it is then 
    # append value to number list 
    # this code takes input as lines so we can take multiple inputs in same job 
    if job=='1':
        print('please first input name and then 10 digit mobile number with space inbetween :')
        while True:
            line = input()
            if line :
                y=line.split()
                a=y[0]
                if len(y[1])!=10:
                    print('contact number only be 10 digit please try again with valid entries :(')
                    continue
                try :
                    b=int(y[1])
                except:
                    print('contact number is not in integer please try again with valid entries :(')
                    continue
                
                if a in d.keys() :
                    d[a].append(b)
                else :
                    d[a]=[b]
            else :
                break

    # For a given keyword this code will iterate over every key in dict and try to match        
    elif job=='2':
        fu=True
        while fu:
            x=input('enter 1 if you like to serach for a keyword \nenter 2 if you like to search for a name ')
            if x=='1':
                wh=input('\nenter the keyword :')
                l=matchingKeys(d,wh)
                for y in range(len(l)) :
                    print('name :',l[y],' , ','contact_number :',d[l[y]] ,'\n' )
                fu=False
            elif x=='2':
                wh=input('\nenter the name :')
                l=matchingnames(d,wh)
                for y in range(len(l)) :
                    print('name :',l[y],' , ','contact_number :',d[l[y]] ,'\n' )
                fu=False
            else :
                print('not recognized job , sorry please start again :(')
            

    # Showing whole dict
    elif job=='3':
        if(d):
            print_out(d)
        else :
            print('no contacts found :(')

    #reading from a file 
    elif job=='4':
        file1 = open("data.txt",'r')
        lines = file1.readlines()
        for line in lines :
            line = " ".join(line.split())
            y=line.split()
            a=y[0]
            if len(y[1])!=10:
                #print('contact number only be 10 digit please try again with valid entries :(')
                continue
            try :
                b=int(y[1])
            except:
                #print('contact number is not in integer please try again with valid entries :(')
                continue
            
            if a in d.keys() :
                d[a].append(b)
            else :
                d[a]=[b]

    # termination of code 
    else :
        print('peace out xD/n')
        var=False
