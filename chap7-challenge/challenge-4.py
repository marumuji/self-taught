while True:
  num = input("数字を入力してください: ")  
  answer = {"1", "2", "3", "4", "5"}
  if num == "q":
    quit()
  elif num in answer:
    print("正解")
  elif num.isdecimal() and num not in answer:
    print("不正解")
  else: 
    print("数字を入力するか、qで終了します")
  

