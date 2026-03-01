import time
import multiprocessing  # digunakan untuk menjalankan proses paralel

def proses_berat(angka):
    time.sleep(1)  
    # simulasi proses berat
    return angka * angka

def proses_paralel(data):
    with multiprocessing.Pool() as pool:  
        # membuat pool (sekumpulan worker/process CPU)
        
        hasil = pool.map(proses_berat, data)  
        # membagi pekerjaan ke banyak proses secara bersamaan
        # setiap data diproses paralel
    
    return hasil  
    # mengembalikan hasil setelah semua proses selesai


# PROGRAM UTAMA
if __name__ == "__main__":  
    # wajib di Windows agar multiprocessing tidak error (spawn process)

    data = [1, 2, 3, 4, 5]

    waktu_mulai = time.time()  
    # mulai hitung waktu

    hasil_akhir = proses_paralel(data)  
    # menjalankan proses paralel

    waktu_selesai = time.time()  
    # selesai

    print("Hasil:", hasil_akhir)
    print("Waktu eksekusi:", waktu_selesai - waktu_mulai)
    # waktu lebih cepat karena proses berjalan bersamaan