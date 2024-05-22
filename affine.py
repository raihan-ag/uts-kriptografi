# Fungsi untuk menghitung gcd (greatest common divisor)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Fungsi untuk menghitung modular inverse
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Fungsi untuk enkripsi menggunakan Affine Cipher
def encrypt_affine(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            # Mengkonversi karakter menjadi angka (0-25)
            offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = (a * (ord(char) - offset) + b) % 26
            result += chr(encrypted_char + offset)
        else:
            result += char
    return result

# Fungsi untuk dekripsi menggunakan Affine Cipher
def decrypt_affine(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)  # Mencari modular inverse dari a
    if a_inv is None:
        return "Tidak ada inverse dari a, dekripsi tidak mungkin"
    for char in cipher:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = (a_inv * ((ord(char) - offset) - b)) % 26
            result += chr(decrypted_char + offset)
        else:
            result += char
    return result

# Fungsi untuk kriptoanalisis dengan brute force
def cryptanalysis_affine(cipher):
    for a in range(1, 26):
        if gcd(a, 26) == 1:  # Memastikan a coprime dengan 26
            for b in range(26):
                decrypted_text = decrypt_affine(cipher, a, b)
                print(f"Decrypting with a={a}, b={b}: {decrypted_text}")

# Program utama untuk menjalankan fungsi di atas
if __name__ == "__main__":
    plaintext = "RAIHAN"
    a = 5  # Kunci a
    b = 8  # Kunci b

    # Enkripsi
    encrypted_text = encrypt_affine(plaintext, a, b)
    print(f"Encrypted: {encrypted_text}")

    # Dekripsi
    decrypted_text = decrypt_affine(encrypted_text, a, b)
    print(f"Decrypted: {decrypted_text}")

    # Kriptoanalisis
    print("Cryptanalysis results:")
    cryptanalysis_affine(encrypted_text)
