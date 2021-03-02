#python final test 第三題
print("輸入字串:")
str=input()
print("輸入要取代的字串:")
ch=input()
print("輸入取代的字串:")
bh=input()
if ch in str:
    print(str.replace(ch,bh))
else:
    print("not found")
