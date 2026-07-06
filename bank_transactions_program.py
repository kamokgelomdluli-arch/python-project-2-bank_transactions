#banking system
clients={'name':['bruno','sesko','kobbie','casemiro'],
         'balance':[100,150,500,70],
         'pin':[1111,2222,3333,4444]}
num=0
while num<3:
    try:
        pin=int(input('enter your pin:'))
    except ValueError:
        print('pin should only be numbers restart the process')
        continue
    found=False 
    for c in range(len(clients['name'])):
        
            if pin== clients['pin'][c]:
                print(f'welcome {clients['name'][c]} choose how we may help you today from  the menu below')
                withdraw_cash=('1:withdraw')
                deposit_cash=('2:deposit')
                view_balance=('3:balance')
                print(withdraw_cash)
                print(deposit_cash)
                print(view_balance)
                try:
                    client_choice=int(input('enter one choice from the menu:'))
                except:
                    print('choice should be a number')
                    continue
                if client_choice == 1:
                    amount=int(input('enter amount you want to withdraw:'))
                    if amount> clients['balance'][c]:
                        print('insuffient funds')
                    else:
                        clients['balance'][c] -= amount
                        print(f"{amount} has been withdrawm from your account {clients['balance'][c]} is your available balance")
                    
                elif client_choice ==2:
                    deposit=int(input('enter the amount you want to deposit:'))
                    clients['balance'][c]+=deposit
                    print(f"{deposit} has been deposit from your account, your new balance is {clients['balance'][c]}")
                    
                else:
                    if client_choice==3:
                        print(clients['balance'][c])
                found=True
                break
    if found:
        break
    
    elif pin != clients['pin'][c]:
            num+=1
            print('wrong pin try again')
else:
    if num==3:
     print('account blocked')
    
        
            





