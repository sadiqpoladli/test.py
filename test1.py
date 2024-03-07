# # num  = [1.5,7,8,4,13,24,32,12,22,21,]
# # toplamaq =sum(num)

# # print(toplamaq )
 

# # def myFunc(e):
# #   return len(e)
# # adlar = ['Nərmin', 'Sevda', 'Gülüstan', 'Lalə']
# # adlar.sort( key=myFunc)
# # print(adlar)           

# # fields = ['name', 'last_name', 'age', 'job']
# # values = ['John' 'Doe', '45', 'Python Developer']
# # a_dict = dict(zip(fields, values))

# # a_dict
# # print(a_dict)

# # liste = ["elma", "muz", "kiraz"]
# # liste.append("kavun")
# # print(liste)

# num  = [1.5,7,8,4,13,24,32,12,22,21,]
# num.index()
mehsul = []

for i in range(6):
   mehsulun_adi =input("mehsulun adin girin")
   qiymet =float(input("qiymetin girin :"))
   ortaq = {
      "mehsul_adi":mehsul,
      "qiymet":qiymet,
   }
   mehsul.append(ortaq)
   
   
   
print(f"{mehsul}: {qiymet} azn")

 
