import random

while True:
    # 提示使用者輸入選項
    print("請選擇剪刀(1)、石頭(2)、布(3)，或者輸入 q 退出遊戲")
    user_input = input()
    
    # 判斷使用者輸入的是哪一個選項
    if user_input == 'q':
        # 如果使用者輸入 q，退出遊戲
        break
    elif user_input not in ('1', '2', '3'):
        # 如果使用者輸入的不是有效的選項，重新提示輸入
        print("請輸入有效的選項")
        continue
    
    # 將使用者輸入的選項轉換為整數類型
    user_choice = int(user_input)
    
    # 產生電腦的選擇，使用亂數來實現
    computer_choice = random.randint(1, 3)
    
    # 顯示雙方的選擇
    print(f"你選擇了{user_choice}")
    print(f"電腦選擇了{computer_choice}")
    
    # 判斷輸贏情況
    if user_choice == computer_choice:
        print("平局")
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        print("你贏了！")
    else:
        print("你輸了。")
