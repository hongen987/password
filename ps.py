password = 'a123456'
y = 3
while True:
    x = input('請輸入密碼')
    if x == password:
        print('登入成功')
        break
    elif x != password and y==3 or y==2:
        y=y-1
        print('密碼錯誤!', '你還有',y,'次機會')
    elif x != password and y==1:
        print('沒有機會了')
        break

    