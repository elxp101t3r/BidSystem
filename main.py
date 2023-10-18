import os
biding_list = []
def biding_system(name,bid):
    biding_list.append({name:bid})
choice = 'yes'
while choice == 'yes':
    name = input("Enter your name :\n")
    bid = input('What is your bid:\n$')
    if choice == 'yes':
        biding_system(name,bid)
    elif choice == 'no':
        break
    choice = input('Is there any other person wants to bid?"yes" or "no"\n')
    os.system('clear')
m_bid = 0
win_bid = ''
for i in biding_list:
    for name, bid in i.items():
        if int(bid) > m_bid:
            m_bid = int(bid)
            win_bid = name
print(f'The highest bid was ${m_bid} by {win_bid}')