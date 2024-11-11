        if password_input == password_benar:
            print("Login berhasil! Selamat datang.")
            return 
        else:
            kesempatan -= 1
            print(f"Password salah. Anda memiliki {kesempatan} kesempatan tersisa.")
  print("Anda telah memasukkan password yang salah sebanyak 3 kali. Akses ditolak.")

menu_login()   
