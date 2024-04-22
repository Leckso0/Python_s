# დახურდავება
amount_due = 50 


while amount_due > 0:
    print("Amount Due: ", amount_due)
    # კითხე მომხმარებელს ჩააგდოს ხურდა
    coin = int(input("Insert coin: "))
    # შეამოწმე თუ ხურდა 25, 10 ან 5 თეთრია
    if coin in [25, 10, 5]:
        amount_due -= coin

change_owed = abs(amount_due)

print("Change Owed: ", change_owed)

