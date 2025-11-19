#               for and if-elif-else practise

# -------------------------

# # 1. 1 dan 20 gacha bo‘lgan sonlardan faqat juftlarini chiqaring.

# for i in range(1,20):
#     if i % 2 == 0:
#         print(i)

# --------------------------

# 3. Foydalanuvchi 5 ta son kiritadi. Ularning ichidan faqat musbatlarini chiqarib bering.

# sonlar = []
# for i in range(5):
#     son = int(input("Son kiriting: "))
#     sonlar.append(son)

# print("Musbat sonlar: ", end=" ")
# for son in sonlar:
#     if son > 0:
#         print(son, end=" ")

# ---------------------------

# 4. 1 dan 15 gacha bo‘lgan har bir sonning kvadratini chiqaring.

# for i in range(1,16):
#     s = i ** 2
#     print(f"{i} ning kvadrati: {s}")

# ----------------------------

# 5. Ro‘yxatda berilgan ismlar ichidan “A” bilan boshlanadigan ismlarni chiqaring.

# name = ["Ali", "Vali", "Asad", "Kochavali", "Akmal", "Nodir", "Isoxon", "akbar"]
# print(name)
# print("Natija:", end=" ")

# for n in name:
#     if n.startswith("A"):
#         print(n, end=" ")

# ----------------------------

# 6. 1 dan 50 gacha bo‘lgan sonlardan faqat 5 ga bo‘linadigan sonlarni chiqaring.

# print("Natija:", end=" ")
# for i in range(1,51):
#     if i % 5 == 0:
#         print(i, end=" ")

# ----------------------------

# # 7. Foydalanuvchi 7 ta son kiritadi, juftlarini sanang.
# sonlar = []
# count = 0
# for i in range(7):
#     son = int(input("Son kiritng: "))
#     sonlar.append(son)
#     if son % 2 == 0:
#         count += 1

# print(f"Juft sonlar soni: {count} ta")

# ---------------------------

# # 8. Matndan iborat ro‘yxat berilgan. Uzunligi 3 ta harfdan uzun so‘zlarni chiqaring.

# matn = ["Salom", "Pdp", "Ikki", "Uch", "Tort", "Besh"]
# print(matn)
# print("Natija(3 ta xarfdan uzun):", end=" ")
# for i in matn:
#     if len(i) > 3:
#         print(i, end=" ")

# --------------------------

# 9. 1 dan 40 gacha bo‘lgan sonlardan som (3 ga bo‘linadiganlarini) chiqaring.

# print("\n Natija:", end=" ")
# for i in range(1,41):
#     if i % 3 == 0:
#         print(i, end=" ")
# print("\n")

# -----------------------

# 10. Foydalanuvchi 6 ta son kiritadi. Ulardan faqat manfiy sonlarni chiqaring.

# sonlar = []
# for i in range(6):
#     son = int(input("Son kiriting: "))
#     sonlar.append(son)
# print("Manfiy sonlar: ", end=" ")
# for son in sonlar:
#     if son < 0:
#         print(son, end=" ")
# print("\n")

# ------------------------

# 11. Ro‘yxatda berilgan 10 ta son ichidan eng kattasini toping.

# sonlar = [12, 45, 7, 23, 89, 34, 67, 90, 11, 5]
# print("\nSonlar ro'yxati:", sonlar)
# print("Eng katta son:", max(sonlar))
# print("\n")

# ------------------------

# 12. 1 dan 25 gacha sonlarni chiqarib bering. Agar son toq bo‘lsa → “toq”, juft bo‘lsa → “juft” deb yozing.

# for i in range(1,26):
#     if i % 2 == 0:
#         print(f"{i} juft")
#     else:
#         print(f"{i} toq")

# ------------------------

# 13. Foydalanuvchi 5 ta ism kiritadi. Oxiri “a” bilan tugaydigan ismlarni chiqarib bering.

# ismalar = []
# for i in range(5):
#     ism = input("Ism kiriting: ")
#     ismalar.append(ism)
# print("Oxiri 'a' bilan tugaydigan ismlar: ", end=" ")
# for ism in ismalar:
#     if ism.endswith("a"):
#         print(ism, end=" ")
# print("\n")

# ------------------------

# 14. 1 dan 30 gacha bo‘lgan sonlardan faqat 2 xonali sonlarni chiqaring.

# print("\nNatija:", end=" ")
# for i in range(1,150):
#     if 10 <= i <= 99:
#         print(i, end=" ")
# print("\n")

# ------------------------

# 15. 1 dan n gacha bo‘lgan sonlarda 5 bilan tugaydiganlarni toping.

# n = int(input("n ni kiriting: "))
# print(f"1 dan {n} gacha bo'lgan sonlarda 5 bilan tugaydiganlar: ", end=" ")
# for i in range(1,n+1):
#     if str(i).endswith("5"):
#         print(i, end=" ")
# print("\n")\

# ------------------------

# 16. Ro‘yxatda berilgan so‘zlardan ichida 'o' harfi bor so‘zlarni chiqarib bering.

# words = ["olma", "banan", "anor", "shaftoli", "nok", "o'rik", "gilos", "tarvuz"]
# print("So'zlar ro'yxati:", words)
# print("Ichida 'o' harfi bor so'zlar: ", end=" ")
# for word in words:
#     if 'o' in word:
#         print(word, end=" ")
# print("\n")

# # ------------------------

# 17. Foydalanuvchi 8 ta son kiritadi. Ulardan faqat 10 dan katta bo‘lganlarini chiqarib bering.

# sonlar = []
# print("8 ta son kiriting:")
# for i in range(8):
#     son = int(input(f"{i+1}-son: "))
#     sonlar.append(son)

# print("10 dan katta sonlar: ", end=" ")
# for son in sonlar:
#     if son > 10:
#         print(son, end=" ")
# print("\n")

# ------------------------

# 18. 1 dan 100 gacha bo‘lgan sonlardan faqat 3 ning ko‘paytmalarini chiqarib bering.

# print("\n1 dan 20 gacha sonlar ichida 3 ga karrali sonlar royxati:", end=" ")
# for i in range(1,101):
#     if i % 3 == 0:
#         print(i, end=" ")
# print("\n")

# ------------------------

# 19. 1 dan 550 gacha bo‘lgan sonlarda oxiri 0 bilan tugaydigan sonlarni toping.

# print("\n1 dan 550 gacha bo'lgan sonlarda oxiri 0 bilan tugaydigan sonlar:", end=" ")
# for i in range(10,551,10):  # 10 dan boshlab 10 qadam bilan yani 10 ning ko'paytmalari bu
#     print(i, end=" ")       #  usul sonni string ga otkizmasdan uni 0 bilan tugashini tekshiradi
# print("\n")

# 20. Foydalanuvchi 10 ta son kiritadi. Ulardan eng kichik sonni toping.

# sonlar = []
# for i in range(10):
#     son = int(input("Son kiriting: "))
#     sonlar.append(son)
# print("Eng kichik son:", min(sonlar))

# ------------------------

# ism = input("Ismingizni kiriting: ")
# if ism.lower() != "ali":
#     print(f"Uzur {ism.title()} biz Alini kutyanmiz!")
# else:
#     print("Salom, Ali!")

# ---------------------------

# login = input("Enter your login: ")
# if len(login) <= 5:
#     print("Login 5 ta harfdan ko'p bolishi kerak!!!")
# else:
#     print("Xush kelibsiz!!!")

# ---------------------------------

# year = int(input("Enter your year: "))
# if 2025-age < 18:
#     print(f"Yoshingiz {2025-year} da ekan")
#     print("Sizga kirish mumkin emas!")
# else:
#     print("Hush kelibsiz!")

# ---------------------------------------

# x, y = 70, 50
# print("x>y") if x>y else print("x<y")

# --------------------------------------


# kun = input("Bugun qanday kun? ")
# harorat = float(input("Havo harorati qanday? "))
#
# if kun == 'yakshanba' and harorat >= 30:
#     print("Ketdik chomilgani!")
# elif kun == 'yakshanba' and harorat < 30:
#     print("Bugun dam olamiz!")

# ----------------------------------

# kun = input("Bugun qanday kun? ")
# harorat = float(input("Bugun harorat necha gradus? "))
#
# if kun.lower() == 'yakshanba' or kun.lower() == 'shanba' and harorat >= 30:
#     print("Ketdik chomilishga bolla!")
# elif kun.lower() == 'yakshanba' or kun.lower() == 'shanba' and harorat < 30:
#     print("Bugun uyda dam olamiz chomilish atmen")

# ---------------------------------
