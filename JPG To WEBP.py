import os
from PIL import Image

def convert_to_webp(folder_path):
     
    file_list = os.listdir(folder_path)
    
    for file_name in file_list:
         
        if file_name.endswith('.jpg'):
             
            file_path = os.path.join(folder_path, file_name)
            
             
            image = Image.open(file_path)
            
             
            new_file_path = os.path.splitext(file_path)[0] + '.webp'
            image.save(new_file_path, 'WEBP')
            
            print(f"{file_name} başarıyla dönüştürüldü.")
            
    print("Tüm resimler başarıyla dönüştürüldü.")

# DOSYA KONUMUNU BU ŞEKİLDE GİR TAMAMEN İÇİNDEKİ TÜM JPG UZANTILARINI WEBP YE ÇEVİRİR
folder_path = r"C:\Users\Letrx Morrison\Desktop\X1"
convert_to_webp(folder_path)