import os
current_path = os.getcwd()
os.chdir(current_path)            # so the scrpit can find the accounts.txt text file

saved_accounts = open('accounts.txt', 'r').read()   
accounts_list = saved_accounts.split('\n')       # putting the contents of that text file in a list

print("\n", "*" * 5,"WELCOME", "*" *5,"\nXD--Secure Writing Project--XD","\nNOTE:\nWriting Ideas, Memories, Dreams or even Messeges\nis like saving your progress in a game")
print("-" * 10)
print("\nLog in OR make new account:")
user_choice = input("> ")
user_choice_list = list(user_choice.split(' '))


if "Log" in  user_choice_list or "log" in user_choice_list:
    Email = input("E-mail: ")
    
    password = input("Pass: ")
    
    while Email in accounts_list:      # cheching if email is correct
        try :
            E_index = accounts_list.index(Email)
            P_index = accounts_list.index(password)
            E_index == P_index -1         # make sure the entered pass is for this email .. open the accounts.txt to see what i mean
        except ValueError:
            print("1Sorry, Your Email or pass is incorrect"  )
            break
        print("Hi, You are successfully logged in")
        break
        
        
        
        
    else :
        print("Sorry, Your Email or pass is incorrect")
        
        
elif "new" in user_choice_list or "make" in user_choice_list:
    print("\n","/\\" * 10, "\nCreating new acount\n", "/\\" * 10)
    Name = input("\nName: ")
    
    Family_name = input("Family name: ")
    
    new_Email = input("E-mail: ")
    while (new_Email.find("@") == -1): # just for the style XD
        print("This E-mail is not valid, try another one")
        new_Email = input("E-mail: ")
    
    new_password = input("Password: ")
    re_password = input("Password again: ")
    while new_password != re_password:
        print("Passwords not matched, try again")
        new_password = input("Password: ")
        re_password = input("Password again: ")
    
    print("\n","-"*10,"Saving you information", "-"*10, "\n")
    
    accounts_list.append(new_Email) # adding new line with the new email
    accounts_list.append(new_password) # adding a line under the new email for the new pass
    new_contents = '\n'.join(accounts_list) # generating a string from the list 
    
    saved_accounts = open('Accounts.txt', 'r+', encoding = 'utf-8')
    saved_accounts.write(new_contents) # copying that string to the accounts.txt
    saved_accounts.close() # closing the file
    
    print("\nAccount created successfullyy", "\n", "*" * 10)    