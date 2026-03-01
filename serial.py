import time  # digunakan untuk mengukur waktu dan simulasi delay

def proses_berat(angka):
    time.sleep(1)  
    # simulasi proses berat (misalnya pengolahan data besar)
    return angka * angka  
    # operasi utama (contoh: kuadrat dari angka)

def proses_serial(data):
    hasil = []  
    # list untuk menyimpan hasil proses
    
    for item in data:  
        # looping data satu per satu (tidak paralel)
        
        output = proses_berat(item)  
        # memproses setiap data secara berurutan
        
        hasil.append(output)  
        # menyimpan hasil ke dalam list
    
    return hasil  
    # mengembalikan semua hasil


# PROGRAM UTAMA
data = [1, 2, 3, 4, 5]

waktu_mulai = time.time()  
# mencatat waktu mulai eksekusi

hasil_akhir = proses_serial(data)  
# menjalankan proses serial

waktu_selesai = time.time()  
# mencatat waktu selesai

print("Hasil:", hasil_akhir)
print("Waktu eksekusi:", waktu_selesai - waktu_mulai)
# total waktu = akumulasi semua proses (karena berurutan)