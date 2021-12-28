1

print("Hello world\nHello World\nHello World\nHello World\nI love python\nI love python\nI love python\nI love python")

month= input("Please enter a month 1-12: ")
months = int(month)
if months in (3,4,5):
    print("The season is Spring")
elif months in (6,7,8):
    print("The season is Summer")
elif months in (9,10,11):
    print("The season is Fall")
else:
    print("The season is Winter")
