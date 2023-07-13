from datetime import datetime as dt
import os

class Menu:
    def __init__(self,idn,name,price):
        '''
        To generate Menu of the Hotel
        '''
        self.id = idn
        self.name = name
        self.price = price

    def show_menu(self):
        print('\n','-'*30,sep='')
        print('Pearls Restaurant Menu'.center(30))
        print('-'*30)
        print(f"No {' Name':<20}Price")
        print('-'*30)
        for obj in menu:
            print(f"{obj.id}. {obj.name:<20}{obj.price}")
            print('-'*30)
        print(end='\n')

class Table(Menu):
    def __init__(self):
        self.table = {'table':[2,2,4,4,6,8,8,12],'free':[False]*8}
        self.table_no = list(range(1,len(self.table['table'])+1))

    def allot_table(self,number):
        if all(self.table['free']):
            print('Please Wait all Tables are Full')
        else:
            for i in self.table_no:
                if number < 3 and i > 2:
                    print('Please wait Table is already fulled 1')
                    break
                elif number < 5 and i > 5:
                    print('Please wait Table is already fulled 2')
                    break
                elif number < 8  and i > 7:
                    print('Please wait Table is already fulled 3')
                    break
                elif number > 8 and self.table['free'][-1]:
                    print('Please wait Table is already fulled 4')
                    break
                elif (not self.table['free'][i-1]) and number <= self.table['table'][i-1]: 
                    self.allot = i
                    self.table['free'][i-1] = True
                    #print(self.table)
                    return self.allot

def clear(tab,cross_total,gst,tip=0,rate=''):
    f.write(f"{date[tab-1][:10]}\t{date[tab-1][11:]}\t{name_table[tab]}\t{tab}\t{waiter[tab]}\t{tip}\t{cross_total}\t{gst*2}\t{rate}\n")
    table.table['free'][tab-1] = False
    date[tab-1] = '00-00-0000 00:00:0000'
    del order_data[tab]
    del name_table[tab]

name_table = {}
def name_tab(allot_table,name):
    name_table[allot_table] = name

def rate_check(rate):
    if rate in range(0,6):
        return True
    else:
        return False

def feedback(tab):
    a = ''
    while True:
        a = input(f'{name_table[tab].capitalize()} are you willing to provide Feedback (Type Yes or Press enter to Exit) ')
        if a == '':
            break
        elif a.lower() == 'Yes'.lower() or a.lower() == 'Y'.lower():
            rate = input('Please Type Here ')
            print('Thanks for Your Valuable Feedback')
            return rate
    
def bill(tab,tip):
    if order_data.get(tab):
        print('='*100)
        print('Pearls Restaurant Bill'.center(100))
       # print('64, Indra Gandhi Nagar'.center(100))
        # print('Chennai Tamilnadu - 60028'.center(100))
        print('='*100)
        print(f"{'Name':>20} :- {name_table[tab]}")
        print(f"{'Table Number':>20} :- {tab}")
        print(f"{'Waiter ID':>20} :- {waiter[tab]}")
        print(f"{'Date':>20} :- {date[tab-1][:10]}")
        print(f"{'Time':>20} :- {date[tab-1][11:]}")
        print('='*100)
        print(f"{'No.':>12} {'Items':^34} {'Price':^12} {'Quantity':^12} {'Amount':>12}")
        print('-'*100)
        num = 1
        total = 0
        cross_total = 0
        gst = 0
        for i,j in order_data[tab].items():
            print(f"{num:>12} {food[i-1]:^34} {price[i-1]:^12} {j:^12} {(price[i-1]*j):>11}")
            total += price[i-1]*j
            print('-'*100)
        gst = round((total*0.09),2)
        print(f"{'Sub Total :':>77}{total:>8}")
        print(f"{'Tips :':>77}{tip:>8}")
        print(f"{'CGST (9%):':>77}{gst:>8}")
        print(f"{'SGST (9%):':>77}{gst:>8}")
        cross_total = total + (gst*2)+ tip
        print(f"{'':>77}{'-'*12}")
        print(f"{'Net Amount :':>77}{round(cross_total):>8}")
        print(f"{'':>77}{'-'*12}")
        print('\n\n')
        print('='*100)
        print('Thank You Visit Again'.center(100))
        print('='*100)
        clear(tab,cross_total,gst,tip=tip,rate=feedback(tab))
    else:
        print('Please Order some food and Then try to Generate Bill')
    
order_data = {}
def order(tab):
    menu_obj.show_menu()
    summary = [0]*len(food)
    a = ''
    count = ''
    while True:
        a = input("\nEnter Food number from menu(Press enter to Exit) ")
        if a == '':
            break
        elif not a.isdigit() or a == '0':
            print("Please Provide Valid Input Try to Enter Food Number")
            a = ''
        elif a.isdigit():
            a = int(a)
            if a<=len(food):
                count = ''
                while not count:
                    count = input(f"How many {food[a-1]} you want (Press enter to go Back) ")
                    if count == '':
                        break
                    try:
                        count = int(count)
                    except ValueError:
                        print('Invalid input Please Provide numbers only')
                        count = ''
            else:
                print("Please Provide Valid Input Try to Enter Food Number")
                a = ''
                count = ''
            if count:
                summary[a-1] += count
                table_order = order_data.setdefault(tab,{})
                if a in table_order:
                    table_order[a] = table_order[a] + count
                else:
                    table_order[a] = count
    if order_data.get(tab):
        print('\nPlease Verify Your Order Details')
        num = 1
        print(f"\nNo {' Name':<20}Quantity")
        print('-'*30)
        for i,j in enumerate(summary):
            if j > 0:
                print(f'{num}. {food[i]:<20}{j}')
                num += 1
                print('-'*30)
        flag = ''
        while not flag:
            flag = input('\nPress Y or Type "Yes" To confirm your Order (n or No to reorder) ')
            if flag.lower() == 'y' or flag.lower() == 'yes':
                now = dt.now()
                d = now.strftime('%d-%m-%Y %I:%M:%S%p')
                date[tab-1] = d
                print('\nYour Food will reach you soon, Enjoy your Food\n')
                break
            elif flag.lower() == 'n' or flag.lower() == 'no':
                table_order = order_data[tab]
                for i,j in enumerate(summary):
                    i = i+1
                    if i in table_order:
                        table_order[i] = table_order[i] - j
                        if table_order[i] == 0:
                            del table_order[i]
                order(tab)
                break
            else:
                print('Please provide Vaild Input')
                flag = ''
                continue
    

waiter = {1:'W101',2:'W102',3:'W101',4:'W102',5:'W103',6:'W104',7:'W105',8:'W106'}
waiter_details = {'W101':'Kamal','W102':'Simbu','W103':'Thanush','W104':'Surya','W105':'Vijay','W106':'Ajith'}
def allot_waiter(table):
    waiterid = waiter[table]
    print(f'Your Waiter name was {waiter_details[waiterid]}, he will reach you soon Please Wait')
    flag=''
    while not flag:
        flag = input('\nFor Order now press y, To go to main menu press n ')
        if flag.lower() == 'y' or flag.lower() == 'yes':
            order(table)
            break
        elif flag.lower() == 'n' or flag.lower() == 'no':
            break
        else:
            print('Please provide Vaild Input')
            flag = ''
            continue

           
food = ['Biryani','Chapati','Naan','Meals','Chilli Chicken','Pepper Chiceken','Grill Chicken',
        'Tandori','Green Chicken']
price = [150,15,20,100,120,130,320,180,170]
menu = []
for i,j,k in zip(range(1,len(food)+1),food,price):
    menu.append(Menu(i,j,k))

number = None
menu_obj = Menu(None,None,None)
table = Table()
if not os.path.isfile('Record.txt'):
    f = open('Record.txt','a+')
    f.write('Date\tTime\tName\tTable_No\tWaiter_id\tTips\tTotal\tGST\tFeedback\n')
else:
    f = open('Record.txt','a+')
date = ['00-00-0000 00:00:0000']*len(table.table['table'])
print('='*30)
print('Welcome to Pearls Restaurant')
print('='*30)
while True:
    print('1 - Book Table')
    print('2 - Show Menu')
    print('3 - Take Order')
    print('4 - Generate Bill')
    print('5 - Exit')
    i = input('\nHow can I Help you ')
    if i == '1':
        number = ''
        while not number:
            try:
                number = int(input('Enter Total number of persons '))
                name = input('Which Name You want to Book Table ')
                allot_table = table.allot_table(number)
                if allot_table:
                    print(f"\nThank you {name.capitalize()}, Table number {allot_table} is alloted for you")
                    allot_waiter(allot_table)
                    name_tab(allot_table,name)
            except ValueError:
                print('Please enter a valid Input')
                number = ''    
    elif i == '2':
        menu_obj.show_menu()
    elif i == '3':
        tab = ''
        temp = []
        while True:
            n = input('Please Enter Your Name ')
            if n == '':
                break
            if n in map(lambda x:x.lower(),name_table.values()):
                for key,value in name_table.items():
                    if value.lower() == n.lower():
                        temp.append(key)
                if len(temp)<2:
                    tab = temp[0]
                else:
                    tab = input('Please Enter your Table Number ')
                try:
                    tab = int(tab)
                    if tab > 0 and tab < 9:
                        if table.table['free'][tab-1] is True:
                            order(tab)
                        else:
                            print(f'Table Number {tab} is not alloted, So please use Option -1 to Book Table for you')
                        break
                    else:
                        print('Please provide Valid Table Number ')
                        tab = ''
                        continue
                except ValueError:
                    print('Please provide Valid Table Number ')
                    tab = ''
            else:
                print(f'No Table Booked in name as {n.capitalize()}, Please provide a Valid Name')        
    elif i == '4':
        tab = ''
        temp = []
        while True:
            n = input('Please Enter Your Name ')
            if n == '':
                break
            if n.lower() in map(lambda x:x.lower(),name_table.values()):
                for key,value in name_table.items():
                    if value.lower() == n.lower():
                        temp.append(key)
                if len(temp)<2:
                    tab = temp[0]
                else:
                    tab = input('Please Enter your Table Number ')
                try:
                    tab = int(tab)
                    if tab > 0 and tab < 9:
                        if table.table['free'][tab-1] is True:
                            tip = ''
                            if order_data.get(tab):
                                while True:
                                    tip = input(f"Do you willing to provide Tip to {waiter_details[waiter[tab]]} (Press Enter to skip) ")
                                    if tip == '':
                                        tip = 0
                                        break
                                    elif tip.isdigit():
                                        tip = int(tip)
                                        break
                                    else:
                                        print('Please Provide any valid Input')
                            bill(tab,tip)
                        else:
                            print(f'Table Number {tab} is not alloted, so Please provide Valid Table number')
                        break
                    else:
                        print('Please provide Valid Table Number ')
                        tab = ''
                        continue
                except ValueError:
                    print('Please provide Valid Table Number ')
                    tab = ''
            else:
                print(f'No Table Booked named as {n.capitalize()}, Please provide a Valid Name')

    elif i == '5':
        break
    else:
        print('='*59)
        print('! Please Provide any Valid Input (Only 1 to 4 is allowed) !')
        print('='*59)

f.close()
