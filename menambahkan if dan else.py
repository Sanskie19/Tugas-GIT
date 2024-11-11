        if password_input == password_benar:
            print("Login berhasil! Selamat datang.")
            return 
        else:
            kesempatan -= 1
            print(f"Password salah. Anda memiliki {kesempatan} kesempatan tersisa.")
