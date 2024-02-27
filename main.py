def binary_to_octal(binary_string):
    # İlk adım olarak, ikilik tabandaki sayıyı ondalık tabana çeviriyoruz.
    decimal_value = int(binary_string, 2)

    # İkinci adım olarak, ondalık sayıyı sekizlik tabana çeviriyoruz.
    octal_value = oct(decimal_value)

    # '0o' öneki kaldırılıyor.
    return octal_value[2:]


# Kullanıcıdan ikilik tabandaki bir sayı alalım.
binary_string = input("Please enter a binary number: ")

# Fonksiyonu çağırıp sonucu yazdıralım.
octal_string = binary_to_octal(binary_string)
print("Octal representation: ", octal_string)

