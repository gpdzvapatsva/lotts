entry1 = []
entry2 = []
entry3 = []

for x in range(18):
    no = input('select a number: ')
    if len(entry1) < 6:
        entry1.append(no)
    elif len(entry1) == 6 and len(entry2) < 6:
        entry2.append(no)
    else:
        entry3.append(no)


# no1=lotto.append(input("select a num: "))
# no2=lotto.append(input("select a num: "))
# no3=lotto.append(input("select a num: "))
# no4=lotto.append(input("select a num: "))
# no5=lotto.append(input("select a num: "))
# no6=lotto.append(input("select a num: "))
# no7=lotto.append(input("select a num: "))
# no8=lotto.append(input("select a num: "))
# no9=lotto.append(input("select a num: "))
# no10=lotto.append(input("select a num: "))
# no11=lotto.append(input("select a num: "))
# no12=lotto.append(input("select a num: "))
# no13=lotto.append(input("select a num: "))
# no14=lotto.append(input("select a num: "))
# no15=lotto.append(input("select a num: "))
# no16=lotto.append(input("select a num: "))

# if len(lotto) < 6:
#     lotto.append()
# elif len(lotto) == 6 and len(lotto2) < 6:
#     lotto2.append()
# else:
#     lotto3.append()



print(entry1)
print(entry2)
print(entry3)
#
# fname = "Abdullah"
# id = "9512285835083"
# username=fname[0:9]+id[0:6]
# print(username)





# last_name = input("what is your last name")
# def createUsername(first_name, last_name):
#     username = first_name + last_name
#     if len(username) > 15:
#         username = first_name + last_name[15 - len(first_name)]
#         # print(username)
import datetime
from datetime import *
