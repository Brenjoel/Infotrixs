#import Statements
import pandas as pd
from colorama import Fore, Back, Style

#Class to process add functions add, search ,update, delete, print , save
class Contacts:
    df1=pd.read_csv("Contacts.csv")
    df1=df1.iloc[:,1:]
    c=df1.to_dict('list')
    # c={
    #     'Name':[],
    #     'Phno':[],
    #     "Mail":[]
    # }

    # Create a new Contact
    def Create(self):
        #Taking input
        while True:
            try: 
                Name=input("Enter Name to add: ")
                if Name in self.c['Name']:   
                    while True:
                        print(Name+" already exists, Do you want to update ?")
                        print("1.Yes \n2.No" )
                        try:
                            ch1=int(input("\nEnter your Choice( 1 or 2 ): "))
                            if ch1==1:
                                self.Update()
                                return
                            elif ch1==2:
                                try:
                                    Phno=input("Enter phone number: ")
                                    Mail=input("Enter Mail id: ")
                                    self.c['Name'].append(Name)
                                    self.c['Phno'].append(int(Phno))
                                    self.c['Mail'].append(Mail)
                                    self.save()
                                    #saving
                                    print(Fore.GREEN+"\nContact created Succesfully ")
                                    print(Style.RESET_ALL)
                                    return
                                except:
                                    print(Fore.RED+" Please Enter a valid Input")
                                    print(Style.RESET_ALL)
                                    continue
                            else:
                                print(Fore.RED+" Please choose either 1 or 2")
                                print(Style.RESET_ALL)
                                continue
                        except:
                            print(Fore.RED+" Please Enter a valid Input")
                            print(Style.RESET_ALL)
                            continue
                else:
                    self.c['Name'].append(Name)
                    try:
                        Phno=input("Enter phone number: ")
                        Mail=input("Enter Mail id: add : ")
                        self.c['Phno'].append(int(Phno))
                        self.c['Mail'].append(Mail)
                        self.save()
                        #saving
                    
                        print(Fore.GREEN+"\nContact created Succesfully ")
                        print(Style.RESET_ALL)
                        return
                    except:
                        print(Fore.RED+" Please Enter a valid Input")
                        print(Style.RESET_ALL)
                        continue
                    
            except:
                print(Fore.RED+" Please Enter a valid Input")
                print(Style.RESET_ALL)
                continue
                
        

    #Search for a contact
    def Search(self,Name):
        if Name in self.c['Name']:
                ind=self.c['Name'].index(Name)
                print(Fore.BLUE+ Name + " is found ")
                print("Name: " + self.c['Name'][ind] + "\nPhno: " + str(self.c['Phno'][ind]) + "\nE-Mail: " + self.c['Mail'][ind] )
                print(Style.RESET_ALL)
        else:
                print(Fore.YELLOW+"\nSorry "+ Name +" is not found !")
                print(Style.RESET_ALL)

    #Update a contact
    def Update(self):
        while True:
            try:
                #Taking input to update
                Name=input("Enter Name to be updated: ")
                if Name in self.c['Name']:
                    ind=self.c['Name'].index(Name)

                    Phno=input("Enter phone number: ")
                    Mail=input("Enter EMail id: ")
                    
                    #updating
                    self.c['Phno'][ind]=int(Phno)
                    self.c['Mail'][ind]=Mail
                    self.save()
                    print(Fore.GREEN+"\nUpdated contact Succesfully ")
                    print(Style.RESET_ALL)
                    return
                else:
                    print(Fore.YELLOW+"\n"+Name+" not found")
                    return
            except Exception as e:
                # print(e)
                print(Fore.RED+" Please Enter a valid Input")
                print(Style.RESET_ALL)
                continue
            
        

    #delete a contact
    def Delete(self):
        while True:
            try:
                Name=input("Enter Name to delete: ")
                if Name in self.c['Name']:
                    ind=self.c['Name'].index(Name)
                    del self.c['Name'][ind]
                    del self.c['Phno'][ind]
                    del self.c['Mail'][ind]
                    self.save()
                    print(Fore.GREEN+"\nContact Deleted Succesfully ")
                    print(Style.RESET_ALL)
                    break
                else:
                    print(Fore.YELLOW+"\n"+Name+" Not Found in Contacts")
                    print(Style.RESET_ALL)
                    break

            except :
                print(Fore.RED+" Please Enter a valid Input")
                print(Style.RESET_ALL)
                return
    
    #print Contacts
    def pr(self):
        dfp=pd.read_csv("Contacts.csv")
        print(Fore.BLUE)
        print(dfp.iloc[:,1:])
        print(Style.RESET_ALL)

        

    def save(self):
        df=pd.DataFrame(self.c)
        df=df.iloc[:,:]
        df.to_csv("Contacts.csv")
        
ch=1
co=Contacts()
while ch>0 :
    #MENU 
        print("\n----MENU----")
        print("1.Create a new Contact","2. Search for a contact","3.Update a contact","4.Delete a contatct","5.Print the contacts data","0.Exit",sep="\n")
        try:
            ch=int(input("\nEnter your Choice: "))
        except:
            print(Fore.RED+" Please Enter a valid Input")
            print(Style.RESET_ALL)
            continue
        match ch:
            case 0:
                print(Fore.GREEN+" Thank you ! \n")
                print(Style.RESET_ALL)
                exit()

            case 1:
                co.Create()

            case 2:
              try:   
                Name=input("Enter Name to search: ")
                co.Search(Name)
              except:
                print(Fore.RED+" Please Enter a valid Input")
                print(Style.RESET_ALL)
                continue
              
            case 3:
                co.Update()
                

            case 4:
                co.Delete()
                

            case 5:
                co.pr()

            case _:
                print(Fore.RED+"\n\nPlease Enter a number from the given MENU ")
                print(Style.RESET_ALL)


