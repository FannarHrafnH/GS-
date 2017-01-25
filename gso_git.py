#Fannar Hrafn Haraldsson
#25.1.17
#Git verkefni
#spyr um nafn
nafn=input("Hvað heitir skráin?: ")
#bæti við .txt
skraheiti=nafn+".txt"
#opna skrá með w+ til að búa hana til
skra = open(skraheiti,'w+')
#skrifa í skrá \n gerir nýja línu
skra.write('Þetta virkar\n')
#loka skrá
skra.close()
#opna skrá aftur
skra = open(skraheiti,'a')
#skrifa aftur í skrá, þessi kóði lítur ekkert sérstaklega vel út
skra.write('Alveg heilar\nþrjár\nlínur')
#loka skrá
skra.close()
#opna skrá aftur en með r því ég þarf bara að lesa hana
skra = open(skraheiti,'r')
#geri innihald að hverju sem er í skránni
innihald = skra.read()
#prenta innihald skráarinnar
print(innihald)
#loka skrá
skra.close()