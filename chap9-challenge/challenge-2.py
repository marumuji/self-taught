adress = input("勤めている会社の住所を入力してください: ")
print(adress)
with open("address.txt", "w", encoding="utf-8") as f:
    f.write(adress)