#  ATM Stimulation Program
from datetime import datetime
pin = 7717
account_balance = 10000
# Ask the user to enter PIN 
check_pin = int(input('Enter your PIN: '))
if pin == check_pin:
    print('Login successful ✅')
else:
    print('Incorrect pin ❌\nLogin denied!')
    exit()
while True:
    print(f'----- ATM MENU ----- \n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4.View Transaction History\n5. Exit')
    user_choice = input('Enter your choice: ')

    if user_choice == '1':
        def check_balance():
            print(f'Current Balance: {account_balance}')
        check_balance()

    elif user_choice == '2':
        def deposit_money():
            global account_balance
            deposit = int(input('Enter amount to deposit: '))
            account_balance+=deposit
            print( f'💵 Rs{deposit} deposited successfully✅')
            current_time = datetime.now().strftime('%Y-%m-%d')
            with open('transaction.txt','a') as file:
                file.write(f'Date & Time: {current_time}\n')
                file.write(f'Deposited: Rs{deposit}\nNew Balance: Rs{account_balance}\n')
        deposit_money()

    elif user_choice == '3':
        def withdraw_money():
            global account_balance
            withdraw = int(input('Enter amount for withdrawl: '))
            if withdraw <= account_balance:
                print( f'Rs{withdraw} debited from your account successfully ✅')
                current_time = datetime.now().strftime('%Y-%m-%d')
                account_balance-=withdraw
                with open('transaction.txt','a') as file:
                    file.write(f'Date & Time: {current_time}\n')
                    file.write(f'Withraw Amount: Rs{withdraw}\nRemaining Balance: Rs{account_balance}')
                    
            else:
                print( 'Insufficient Balance!')
        withdraw_money()
    elif user_choice == '4':
        def view_transaction_history():
            global account_balance
            with open('transaction.txt','r') as file:
                content = file.read()
                print(content)
        view_transaction_history() 

    elif user_choice== '5':
        print('Thanks for taking services from us.')
        break

    else:
        print('Invalid Choice')