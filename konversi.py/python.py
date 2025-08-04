def konversi_suhu(nilai, dari, ke):
    # Ubah ke Celcius
    if dari == "fahrenheit":
        celcius = (nilai - 32) * 5/9
    elif dari == "reamur":
        celcius = nilai * 5/4
    elif dari == "kelvin":
        celcius = nilai - 273.15
    else:
        celcius = nilai

    # Ubah ke tujuan
    if ke == "fahrenheit":
        return (celcius * 9/5) + 32
    elif ke == "reamur":
        return celcius * 4/5
    elif ke == "kelvin":
        return celcius + 273.15
    else:
        return celcius


# Input user
nilai = float(input("Masukkan nilai suhu: "))
dari = input("Dari (celcius/fahrenheit/reamur/kelvin): ").lower()
ke = input("Ke (celcius/fahrenheit/reamur/kelvin): ").lower()

# Proses & Output
hasil = konversi_suhu(nilai, dari, ke)
print(f"Hasil konversi: {round(hasil, 2)} {ke.capitalize()}")