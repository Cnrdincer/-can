print("""

___________Welcome___________

===============================
[1] + add
[2] – subtract
[3] × multiply
[4] ÷ divide
===============================
 """)

veri = input("işlem :")
if  veri == "1":
    x = input("first number :")
    x = float(x)
    y = input("second number :")
    y = float(y)
    print("result :",x + y)

elif veri == "2":
	x = input("first number  :")
    x = float(x)
    y = input("second number:")
    y = float(y)
    print("result :",x - y)

elif veri == "3":
	x = input("first number  :")
	x = float(x)
	y = input("second number")
	y = float(y)
	print("result :",x * y)

elif veri == "4":
	x = input("first number  :")
	x = float(x)
	y = input("secon number")
	y = (y)
	print("result :",x / y)

else :
	print("wrong data entry")
	quit()
