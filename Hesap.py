print("""

___________Hoşgeldin___________

===============================
[1] Toplama
[2] çıkartma
[3] çarpma
[4] üssünü alma
[5] bölme
===============================
 """)

veri = input("işlem :")
if  veri =="1":
    x = input("ilk sayi :")
    x = float(x)
    y = input("ikinici sayi :")
    y = float(y)
    print("sonuç :",x + y)

elif veri == "2":
	x = input("ilk sayi :")
    x = float(x)
    y = input("ikinici sayi :")
    y = float(y)
    print("sonuç :",x - y)

elif veri == "3":
	x = input("ilk sayi :")
	x = float(x)
	y = input("ikinci sayı")
	y = float(y)
	print("sonuç :",x * y)

elif veri == "4":
	x = input("ilk sayı :")
	x = float(x)
	y = input("ikinci sayı")
	y = float(y)
	print("sonuç :",x ** y)

elif veri == "5":
	x = input("ilk sayı :")
	x = float(x)
	y = input("ikinici sayi")
	y = (y)
	print("sonuç :",x / y)

else :
	print("yanlış veri girişi yapıldı")
	print("program kapatılıyor")
	quit()
