#ejercio 01
#       0         1         2         3         4
#       0123456789012345678901234567890123456789012
frase1="YA LO PASADO PASADO NO ME INTERESA,EL AYER"
#mostrar el numero de ocurrencias de la vocal "A"
print("la vocal 'A' ocurre:", frase1.count("A")," veces")

##ejercio 02
#       0         1         2         3
#       0123456789012345678901234567890
frase2="DESDE QUE ESTABAMOS EN LA HIGH"
print("la vocal 'E' ocurre:", frase2.count("E")," veces")

#ejercio 03
#       0         1         2         3
#       0123456789012345678901234567890123
frase3="ESCRIBIAS MI NOMBRE EN TU CUADERNO"
print(frase3.lower())

#ejercio 04
#       0         1         2         3
#       0123456789012345678901234567890123
frase4="YO PIENSO EN TI CUANDO ESTOY HIGH"
print(frase4.lower())

#ejercio 05
#       0         1         2
#       012345678901234567890123456789
frase5="Y AHORA PICHEAS PARA COMERNOS"
print(frase5.upper())


#ejercio 06
#       0         1         2
#       012345678901234567890123
frase6="DAME UN RATITO Y MAS NA"
print(frase6.upper())

#ejercio 07
#       0         1         2         3
#       0123456789012345678901234567890123456789
frase7="DESPUES SI QUIERES NO TE ESCRIBO MAS NA"
print(frase7.replace("QUIERES","QUERES"))

#ejercio 08
#       0         1         2
#       012345678901234567890123
frase8="PAREZCO BOBO BUSCANDOTE"
print(frase8.replace("BOBO","IMBECIL"))

#ejercio 09
#       0         1         2         3         4         5         6
#       0123456789012345678901234567890123456789012345678901234567890123456
frase9="QUIERO HACER UNA SERIE QUE SE LLAME TODA LA NOCHE DANDOTE BABY"
print(frase9.rstrip())
print("#"*100)

#ejercio 10
#        0         1         2         3
#        012345678901234567890123456789012345678
frase10="DIME SI ANDAS CON ESE BOBO O ANDAS SOLA"
print("#"*50)
print(frase10.lstrip())
print("#"*50)

#ejercio 11
#        0         1         2         3         4
#        012345678901234567890123456789012345678901234
frase11="YO EN EL MERCEDES Y EL TE TIENE EN EL COROLLA"
print(frase11.rstrip())

#ejercio 12
#        0         1         2         3         4
#        0123456789012345678901234567890123456789012
frase12="SI UN DIA DE ESTOS,BABY,EL A TI TE DESCUIDA"
print(frase12.split(","))

#ejercio 13
#        0         1         2
#        012345678901234567890
frase13="YO VOY A HACERTE MIA X2"
print(frase13.isdigit())

#ejercio 14
#        0         1         2         3         4
#        01234567890123456789012345678901234567890
frase14="DIME CUANDO VAMOS A VERNOS PARA COMERNOS"
print(frase14.strip())

#ejercio 15
#        0         1         2         3
#        0123456789012345678901234567890123
frase15="SI SE TE OLVIDO YO TE LO RECUERDO"
print(frase15.isalnum())
