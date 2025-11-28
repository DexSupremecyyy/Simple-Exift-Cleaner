# Hanya projek simple hehe ^_^
# Projek untuk menghilangkan informasi metadata dari gambar

from PIL import Image
from PIL.ExifTags import TAGS
import sys
import os

def remove_exif(input_path):
    try:
        # 1. Buka gambar (Pillow otomatis tau ini JPG, PNG, atau WebP)
        image = Image.open(input_path)
        print(f"[+] Memproses: {input_path}")
        
        # Kita pecah: "foto.png" jadi ("foto", ".png")
        file_name, extension = os.path.splitext(input_path)
        
        # Bikin nama output: "foto_cleaned.png"
        output_path = f"{file_name}_cleaned{extension}"
        
        # Cek Metadata
        exif_data = image.getexif()
        if not exif_data:
            print("[!] Tidak ada EXIF standard (Mungkin PNG/WebP atau sudah bersih).")
        else:
            print("[*] Mendeteksi Metadata...")


        # 2. Proses Pembersihan (Sanitizing)
        # Copy pixel data ke canvas baru dengan Mode yang sama
        # (kalau PNG transparan, tetep transparan)
        data = list(image.getdata())
        image_clean = Image.new(image.mode, image.size)
        image_clean.putdata(data)
        
        
        # 3. Save sesuai ekstensi aslinya
        image_clean.save(output_path)
        print(f"[SUCCESS] File bersih disimpan: {output_path}")
        print("------------------------------------------------")
        
    except Exception as e:
        print(f"[ERROR] Gagal: {e}")

if __name__ == "__main__":
    try:
        target = input("Masukkan nama file (contoh: gambar.png): ")
        
        # Cek file
        if os.path.exists(target):
            remove_exif(target)
        else:
            print("[!] File tidak ditemukan, mohon di cek lagi.")
            
    except KeyboardInterrupt:
        print("\n[!] Keluar.")