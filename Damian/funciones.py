#ejercio 01
#       0         1         2         3
#       0123456789012345678901234567890123456789
frase1="LA MISMA CALLE ME HA ENSEÑADO A CUIDARME"
#mostrar el numero de ocurrencias de la vocal "A"
print("la vocal 'A' ocurre:", frase1.count("A")," veces")

#ejercio 02
#       0         1         2         3         4         5
#       012345678901234567890123456789012345678901234567890123
frase2="LA MENTE ES COMO UN PARACAIDAS, NO SIRVE SI NO SE ABRE"
print("la vocal 'E' ocurre:", frase2.count("E")," veces")

#ejercio 03
#       0         1         2         3         4         5
#       01234567890123456789012345678901234567890123456789012
frase3="NO SE CUENTAN LOS SEGUNDOS, SE CUENTAN HISTORIAS BABY"
print(frase3.lower())

#ejercio 04
#       0         1         2         3         4
#       012345678901234567890123456789012345678901234
frase4="POR LA SONRISA DE MI MADRE QUE VALE UN MILLON"
print(frase4.lower())
#ejercio 05
#       0         1         2         3
#       0123456789012345678901234567890123456789
frase5="cuando tu mundo se desmorone, ven al mio"
print(frase5.upper())

#ejercio 06
#       0         1         2         3         4
#       01234567890123456789012345678901234567890123456
frase6="no le hables de calle a la suela de mis zapatos"
print(frase6.upper())

#ejercio 07
#      0         1         2         3         4
#      0123456789012345678901234567890123456789012345678
frase7="CUIDADO CON LOS MIEDOS, LES ENCANTA ROBAR SUENIOS"
print(frase7.replace("MIEDOS","MEDIOS"))

#ejercio 08
#       0         1         2         3         4
#       0123456789012345678901234567890123456789012345
frase8="SOMOS LO QUE HACEMOS PARA CAMBIAR LO QUE SOMOS"
print(frase8.replace("HACEMOS","COGEMOS"))

#ejercio 09
#       0         1         2         3         4         5         6
#       0123456789012345678901234567890123456789012345678901234567890123456
frase9="              LAS TORMENTAS HACEN QUE LOS ARBOLES TENGAN LAS RAICES MAS PROFUNDAS                   "
print("#"*100)
print(frase9.rstrip())
print("#"*100)

#ejercio 10
#        0         1         2         3         4
#        0123456789012345678901234567890123456789012
frase10="                          CUANDO ESTA OSCURO PUEDES VER LAS ESTRELLAS   "
print("#"*50)
print(frase10.lstrip())
print("#"*50)

#ejercio 11
#        0         1         2         3         4         5
#        012345678901234567890123456789012345678901234567890
frase11="               LA UNICA DISCAPACIDAD EN LA VIDA ES LA MALA ACTITUD            "
print(frase11.rstrip())

#ejercio 12
#        0         1         2         3         4         5         6         7
#        01234567890123456789012345678901234567890123456789012345678901234567890123
frase12="TODO ES O UNA OPORTUNIDAD PARA CRECER O UN OBSTACULO QUE EVITA QUE CREZCAS"
print(frase12.split())

#ejercio 13
#        0         1         2         3         4         5         6
#        0123456789012345678901234567890123456789012345678901234567890
frase13="LA VIDA ES MUY SIMPLE, PERO  NOS EMPENIAMOS EN HACERLA DIFICIL"
print(frase13.isdigit())

#ejercio 14
#        0         1         2         3         4         5         6
#        0123456789012345678901234567890123456789012345678901234567890123
frase14="    EL VERDADERO ROMANCE SURGE CUANDO APRENDES A QUERERTE A TI MISMO    "
print(frase14.strip())

#ejercio 15
#        0         1         2         3         4         5         6
#        012345678901234567890123456789012345678901234567890123456789012345
frase15="LAS PERSONAS MAS IMPORTANTES NO SE BUSCAN, LA VIDA TE LAS PRESENTA"
print(frase15.isalnum())
