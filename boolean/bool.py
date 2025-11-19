
#     BOOLEAN - malumot turi.

# 1.
# narx = 15000  # mijoz breakfast uchun taom oldi
# choy = True   # choy ham oldi
# salat = False # lekn salat olmadi
#
# if choy or salat:
#     narx += 5000
# elif choy and salat:
#     narx -= 10000
# print(f"Sizdan jami {narx} boldi hurmatli mijoz.")

# ---------------------------------

# 2.
# price = 45000 # lunch uchun samarqand osh
# non = True    # true false orniga 1 0 qoyib ketsak xam boladi True = 1, False = 0.
# choy = False
# salat = True
# assorti = False
# kompot = True
#
# if non:
#     print("Mijoz non oldi!")
#     price += 5000
# if choy:
#     print("Mijoz choy oldi!")
#     price += 8000
# if salat:
#     print("Mijoz salat oldi!")
#     price += 10000
# if assorti:
#     print("Mijoz assorti oldi!")
#     price += 15000
# if kompot:
#     print("Mijoz kompot oldi!")
#     price += 3000 # PDP oshxonasida shunaqa narxi
#
# print(f"Hurmatli mijoz sizdan jami {price} ming som boldi!")
# print("To'lov usuli naqt or karta orqali/click?")

# ---------------------------------

#  IN - operatori

# menu = ["osh", "grechka", "xonim", "tiftel", "makaron"]
# ovqat = input("Nima ovqat yemoqchisz? ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi!")
# else:
#     print("Bizda bunday ovqat yo'q, UZUR!")

# -------------------------------

# menu = ["osh", "grechka", "xonim", "tiftel", "makaron", "kabob"]
# buyurtmalar = ["osh", "manti", "xonim", "tiftel", "makaron", "norin"]
#
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasz, menuda {taom} yoq")

###################################################

#    Practise (boolean,elif,in)

# 1. Son juftmi yoki toqmi?
# Foydalanuvchidan son ol va u juft yoki toq ekanini aniqlang.

# son = int(input("Son kiritng: "))
# if son % 2 > 0:
#     son = 'Musbat'
# elif son % 2 < 0:
#     son = 'Manfiy'
# else:
#     son = 'Nol'
# print(son)

# -----------------------------

# 2. Foydalanuvchining yoshi bo‘yicha kategoriya tanlang (elif).
# 0–2 → Chaqaloq
# 3–12 → Bola
# 13–18 → O‘spirin
# 19+ → Katta

# age = int(input("Yoshingizni kiritng: "))
# if age <= 2 and age > 0:
#     age = "Chaqaloq"
# elif age >= 3 and age < 12:
#     age = "Bola"
# elif age >= 13 and age < 20:
#     age = "O'spirin"
# elif age >= 19:
#     age = "Katta"
# print(f"Sizning statusingiz: {age}")

# -----------------------------

# 3. Ro‘yxatda "python" so‘zi bormi? (in)
# Berilgan ro‘yxat: ["java", "c++", "python", "html"]
#
# royxat = ["java", "c++", "python", "html"]
#
# if "python" in royxat:
#     print("Python prictise")
# -----------------------------

# 4. Matnda "salom" so‘zi ishtirok etganmi?
# Matn o‘zingiz yozing, ichida "salom" bor-yo‘qligini tekshiring.

# matn =input("Matn kiriting: ")
# if "salom" in matn:
#     print("Tabriklaymiz!")
# else:
#     print("Matnda 'salom' yoq!!!")

# -----------------------------

# 5. 2 shartni tekshirish (and).
# Yosh ≥ 18 va pasport bor bo‘lsa, "Kirish mumkin" deyilsin.
#
# age = int(input("Yoshingizni kiriting: "))
# pasport = 1
# if age >= 18 and pasport:
#     print("Kirish mumkin")
# else:
#     print("Kirish mumkin emas")

# -----------------------------

# 6. Online bo‘lmasa, "Offline" chiqsin (not).
# online = False berilgan.

# online = 0
# if online != 1:
#     print("Offline")
# else:
#     print("Online")

# -----------------------------

# 7. Lug‘atda "id" degan kalit bormi? (dict + in)
# dict: {"name": "Ali", "age": 20}

# dict = {"name": "Ali", "age": 20}
# if id in dict:
#     print("Id mavjud emas!")
# else:
#     print("Id mavjud!")

# -----------------------------

# 8. Tog‘/musbat/juft bo‘yicha tarmoqlash.
# Son musbatmi yoki manfiy?
# Agar musbat bo‘lsa, juft/toqligini ham tekshiring.

# son = float(input("Son kiriting: "))
# if son > 0 and son % 2 == 0:
#     son = "Musbat va juft"
# elif son > 0 and son % 2 == 1:
#     son = "Musbat va toq"
# elif son < 0 and son % 2 == 0:
#     son = "Manfiy va juft"
# elif son < 0 and son % 2 == 1:
#     son = "Manfiy va toq"
# else:
#     son = "Nol"
# print(f"Siz kiritgan son: {son}")

# -----------------------------

# 9. Foydalanuvchi ro‘yxatida login bor-yo‘qligini aniqlang.

# users = ["ali", "sardor", "nodir"]
# login = input("Login kiriting: ")
# if login.lower() in users:
#     print("Bu login mavjud!")
# else:
#     print("Login mavjud emas!")

# -----------------------------

# 10. Haftaning kuni bo‘yicha (elif) nom chiqarish.
# 1 – Dushanba, 2 – Seshanba, ... 7 – Yakshanba.

hafta = input("Enter[1-7]: ")
if hafta == "1":
    print("Dushanba")
elif hafta == "2":
    print("Seshanba")
elif hafta == "3":
    print("Chorshanba")
elif hafta == "4":
    print("Payshanba")
elif hafta == "5":
    print("Juma")
elif hafta == "6":
    print("Shanba")
elif hafta == "7":
    print("Yakshanba")
else:
    print("ERROR")

# -----------------------------
