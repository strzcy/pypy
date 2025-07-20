import random

def main():
    print("=== Game Tebak Angka ===")
    print("Saya sudah memilih angka antara 1 sampai 10.")
    print("Kamu punya 5 kesempatan untuk menebaknya!")

    angka_rahasia = random.randint(1, 10)
    percobaan = 0
    max_percobaan = 5

    while percobaan < max_percobaan:
        try:
            tebakan = int(input(f"Tebakan ke-{percobaan + 1}: "))
            percobaan += 1

            if tebakan == angka_rahasia:
                print(f"🎉 Selamat! Kamu benar dalam {percobaan} percobaan.")
                break
            elif tebakan < angka_rahasia:
                print("Terlalu kecil!")
            else:
                print("Terlalu besar!")
        except ValueError:
            print("Masukkan angka yang valid!")

    else:
        print(f"😢 Kesempatan habis. Angka yang benar adalah {angka_rahasia}.")

if __name__ == "__main__":
    main()
