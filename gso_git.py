#Fannar Hrafn Haraldsson
#25.1.17
#Git verkefni
nafn=input("Hvað heitir skráin?: ")
skraheiti=nafn+".txt"
skra = open(skraheiti,'w+')
skra.write('virkar\n')
skra.close()
