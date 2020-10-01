password = 'a123456'
print("你只有3次機會")
answer = input("請輸入密碼:")
x = 3
while x != 0:
	if answer != password:
		print("密碼錯誤! 還有", x-1,"次機會")
		x-=1
		answer = input("請輸入密碼:")
	else:
		print("登入成功!")
		break
