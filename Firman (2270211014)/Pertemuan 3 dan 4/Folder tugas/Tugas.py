import time;
localtime = time.ctime()

print("●SELAMAT DATANG DI CAFE UNKRIS●")
print('HARAP MENGISI FORM DIBAWAH AGAR MEMUDAHKAN PELANGGAN ☟')
pembeli = input("✐ Masukkan nama Pembeli: ")
alamat = input("✉ Masukkan alamat Pembeli: ")
telepon = input("☏ Masukkan no telp Pembeli: ")

total1=0
jenis1=""
porsi=0
gelas=0

print("SILAHKAN MEMILIH MENU DIBAWAH INI 🡳")
def fungsimakanan():
   global total1
   global porsi
   global jenis1
   print ("\n~~~~Menu Makanan~~~~")
   print("1. nasi goreng - Rp15000")
   print("2. mie ayam - Rp13000")
   print("3. nasi ayam geprek - Rp15000")
   print("4. bakso - Rp12000")
   print("5. tenderloin steak - Rp26000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       total1=porsi*15000
       print (porsi," nasi goreng = Rp", total1)
       jenis1=("Nasi goreng")
   elif nomor==2:
       total1=porsi*13000
       print (porsi," mie ayam = Rp", total1)
       jenis1=("mie ayam")
   elif nomor==3:
       total1=porsi*15000
       print (porsi, " nasi + ayam geprek = Rp", total1)
       jenis1=("nasi ayam geprek")
   elif nomor==4:
       total1=porsi*12000
       print (porsi, " bakso = Rp", total1)
       jenis1=("bakso")
   elif nomor==5:
       total1=porsi*26000
       print (porsi, " tenderloin steak = Rp", total1)
       jenis1=("tenderloin steak")
   else:
      print("Pilihan tidak ada ☹, silahkan masukan lagi!!")
      fungsimakanan()


fungsimakanan()

total2=0
jenis2=""

def fungsiminuman():
   global total2
   global jenis2
   global gelas
   print("\n~~~~Menu Minuman~~~~")
   print("1. Es teh - Rp3000")
   print("2. Es jeruk - Rp3500")
   print("3. Es kopi - Rp4000")
   print("4. Es campur - Rp5000")
   print("5. teh tawar - Rp2000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       total2=gelas*3000
       print (gelas," Gelas Es Teh = Rp", total2)
       jenis2=("Es Teh")
   elif nomor==2:
       total2=gelas*3500
       print (gelas, " Gelas Es Jeruk = Rp", total2)
       jenis2=("Es Jeruk")
   elif nomor==3:
       total2=gelas*4000
       print (gelas, " Gelas Es Kopi = Rp", total2)
       jenis2=("Es Kopi")
   elif nomor==4:
       total2=gelas*7000
       print (gelas, " Gelas Es Campur = Rp", total2)
       jenis2=("Es Campur")
   elif nomor==5:
       total2=gelas*3000
       print (gelas, " Gelas Teh Tawar = Rp", total2)
       jenis2=("Teh Tawar")
   else:
      print("Pilihan tidak ada ☹, silahkan masukan lagi!!")
      fungsiminuman()


fungsiminuman()
    
totalsemua=0
totalsemua=total1+total2
print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp."))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("===================================")
data_pembeli = [pembeli, totalsemua, uang]
print(data_pembeli)
print("===================================")

print("\n=================================================")
print("========= S T R U K   P E M B E L I A N =========")
print("=================================================")
print (" Nama         :",pembeli)
print ("alamat        :",alamat)
print ("no.tlp        :",telepon)
print ("Membeli pada   :",localtime)
print (" Beli         :",porsi,jenis1,"-", total1)
print ("               ",gelas,jenis2,"-", total2)
print (" Tagihan      : Rp.",totalsemua)
print (" Uang         : Rp.",uang)
print (" Kembalian    : Rp.",kembalian)
print("==========TERIMA KASIH ATAS KUNJUNGAN ANDA===========")
print("☎ UNTUK DRIVE THRU BISA MENGHUBUNGI : 08953789122847")