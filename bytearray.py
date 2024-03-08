#Activité 1
liste_entiers = [10, 20, 30, 40, 50]
byte_array = bytearray(liste_entiers)
print("Bytearray original:", byte_array)

index_a_modifier = 2
nouvelle_valeur = 99 
if 0 <= nouvelle_valeur <= 255:
    byte_array[index_a_modifier] = nouvelle_valeur
    print("Bytearray modifié :", byte_array)
else:
    print("La nouvelle valeur doit être entre 0 et 255.")

# Activité 2


byte_array = bytearray([10, 50, 100, 150, 200, 250])

print("Bytearray original:")
for byte in byte_array:
    print(byte, end=' ')
print("\n")

print("Bytearray après ajout de 1 à chaque élément:")
for i in range(len(byte_array)):
    byte_array[i] = (byte_array[i] + 1) % 256 
    print(byte_array[i], end=' ')
