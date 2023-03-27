import tkinter
import pymysql
from mysql.connector import MySQLConnection, Error
from aifc import Error
from tkinter.ttk import Treeview
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
from tkinter import IntVar
import mysql.connector

conn = pymysql.connect (host="localhost", user="root", password="Merveot", port=3306, database="bmh204")
cur = conn.cursor ( )

def isBlank (myString):
    return not (myString and myString.strip())

def isNotBlank (myString):
    return bool(myString and myString.strip())

# Müşteri SP işlemleri
def call_MusteriEkle_sp(ad, soyad, telefon, adres):
    try:
        cur.callproc ('MusteriEkle', ( ad, soyad, telefon, adres))
        data = cur.fetchall ( )
        if len (data) == 0:
            conn.commit ( )
            print ('Müşteri bilgileri başarıyla kaydedildi.:)')
        else:
            print ('error: ', str (data[0]))
    except Exception as e:
        print (e)

def call_Musterileri_getir_sp():
    try:
        cur.callproc ('Musterileri_getir')
        data = cur.fetchall ( )
        return data
    except Exception as e:
        print (e)

def call_Musteri_getir_musteri_id(musteri_id) :
    try:
        cur.callproc ('Musteri_getir_musteri_id',(musteri_id,))
        data = cur.fetchall ( )
        return data
    except Exception as e:
        print (e)

def call_MusteriGuncelle_sp(musteri_id, ad, soyad, telefon, adres):
    try:
        cur.callproc ('MusteriGuncelle', (musteri_id, ad, soyad, telefon, adres))
        data = cur.fetchall ( )
        if len (data) == 0:
            conn.commit ()
            print ('Müşteri bilgileri başarıyla güncellendi. :)')
        else:
            print ('error:', str (data[0]))
    except Exception as e:
        print (e)

def call_MusteriAra_telefon(liste, telefon):
    try:
        cur.callproc ('MusteriAra_telefon',(telefon,))
        data = cur.fetchall ( )
        index=0
        for x in data:
            liste.insert(parent='', index=index, iid=index, text='', values=x)
            index = index + 1
        if len (data) == 0:
            conn.commit ( )
        else:
            print ( str (data[0]))
    except Exception as e:
        print (e)

def call_MusteriSil_sp(musteri_id):
    msg = messagebox.askyesno ("Silme işlemi onayı", "Müşteriyi silmek istediğinizden emin misiniz?")
    if msg == True:
        try:
            cur.callproc ('MusteriSil', (musteri_id,))
            data = cur.fetchall()
            if len (data) == 0:
                conn.commit ( )
            else:
                print ('error: ', str (data[0]))
        except Exception as e:
            print (e)

# Ürün SP işlemleri
def call_UrunEkle_sp(urun_adi, aciklama, urun_fiyati):
    try:
        cur.callproc ('UrunEkle', ( urun_adi, aciklama, urun_fiyati))
        data = cur.fetchall ( )
        if len (data) == 0:
            conn.commit ( )
            print ('Ürün bilgileri başarıyla kaydedildi.:)')
        else:
            print ('error: ', str (data[0]))
    except Exception as e:
        print (e)

def call_UrunGuncelle_sp(urun_id,urun_adi,aciklama,urun_fiyati):
    try:
        cur.callproc ('UrunGuncelle', (urun_id,urun_adi,aciklama,urun_fiyati))
        data = cur.fetchall ( )
        if len (data) == 0:
            conn.commit ( )
            print ('Ürün bilgileri başarıyla güncellendi.')
        else:
            print ('error:', str (data[0]))
    except Exception as e:
        print (e)

def call_Urunleri_getir_sp():
    try:
        cur.callproc ('Urunleri_getir')
        data = cur.fetchall ( )
        return data
    except Exception as e:
        print (e)

def call_UrunAra_urun_adi(listeUrun,urun_adi):
    try:
        cur.callproc ('UrunAra_urun_adi',(urun_adi,))
        data = cur.fetchall ( )
        index = 0
        for x in data:
            listeUrun.insert (parent='', index=index, iid=index, text='', values=x)
            index = index + 1
        if len (data) == 0:
            conn.commit ( )
        else:
            print (str (data[0]))
    except Exception as e:
            print (e)

def call_UrunSil_sp(urun_id):
    msg = messagebox.askyesno ("Silme işlemi onayı", "Ürünü silmek istediğinizden emin misiniz?")
    if msg == True:
        try:
            cur.callproc ('UrunSil', (urun_id,))
            data = cur.fetchall ( )
            if len (data) == 0:
                conn.commit ( )
            else:
                print ('error: ', str (data[0]))
        except Exception as e:
            print (e)

# Veresiye SP işlemleri
def call_VeresiyeEkle_sp(musteri_id, borc_tutari, urun_id_list, urun_adet_list):
    try:
        cur.callproc ('VeresiyeEkle', (musteri_id, borc_tutari, urun_id_list, urun_adet_list))
        data = cur.fetchall ( )
        if len (data) == 0:
            conn.commit ( )
            print ('Veresiye bilgileri başarıyla kaydedildi.:)')
        else:
            print ('error: ', str (data[0]))
    except Exception as e:
        print (e)

def call_Veresiyeleri_getir_sp():
    try:
        cur.callproc ('Veresiyeleri_getir')
        data = cur.fetchall ( )
        return data
    except Exception as e:
        print (e)

def call_VeresiyeDetay_getir_veresiye_id(veresiye_id) :
    try :
        cur.callproc ('VeresiyeDetay_getir_veresiye_id', (veresiye_id,))
        data = cur.fetchall ( )
        return data
    except Exception as e :
        print (e)


def call_VeresiyeGuncelle_sp(veresiye_id,odeme_tipi):
    try:
        cur.callproc ('VeresiyeGuncelle', (veresiye_id,odeme_tipi))
        data = cur.fetchall ( )
        if len (data) == 0:
            conn.commit ( )
            print ('Veresiye bilgileri başarıyla güncellendi.')
        else:
            print ('error:', str (data[0]))
    except Exception as e:
        print (e)


def openMusteri():
    def MusteriAlanKontrol(ad, soyad, telefon, adres) :
        if isBlank (ad) :
            messagebox.showwarning ("Müşteri Bilgileri Kontrol", "Lütfen adınız kısmını boş bırakmayın")
            return False
        elif isBlank (soyad) :
            messagebox.showwarning ("Müşteri Bilgileri Kontrol", "Lütfen soyad kısmını boş bırakmayın")
            return False
        elif isBlank (telefon) :
            messagebox.showwarning ("Müşteri Bilgileri Kontrol", "Lütfen telefon kısmını boş bırakmayın")
            return False
        elif isBlank (adres) :
            messagebox.showwarning ("Müşteri Bilgileri Kontrol", "Lütfen adres kısmını boş bırakmayın")
            return False
        return True

    def MusteriListele():
        for i in liste.get_children ( ):
            liste.delete (i)
        data = call_Musterileri_getir_sp ()
        index = 0
        for x in data:
            liste.insert (parent='', index=index, iid=index, text='', values=x)
            index = index + 1

    def MusteriEkle(ad, soyad, telefon, adres):
        if MusteriAlanKontrol (ad, soyad, telefon, adres):
            call_MusteriEkle_sp (ad, soyad, telefon, adres)
        MusteriListele ()

    def MusteriGuncelle(musteri_id, ad, soyad, telefon, adres):
        if MusteriAlanKontrol (ad, soyad, telefon, adres):
            call_MusteriGuncelle_sp (musteri_id, ad, soyad, telefon, adres)
        MusteriListele ()

    def MusteriSil(musteri_id):
        call_MusteriSil_sp (musteri_id)
        MusteriListele ()

    def MusteriAra(telefon):
        for i in liste.get_children ( ):
            liste.delete (i)
        call_MusteriAra_telefon (liste,telefon)

    def MusteriAlanlariniDoldur(event):
        curItem = liste.focus ( )
        for x in liste.item (curItem).values():
            print (x)
        Mitext = liste.item (liste.selection ( )[0])['values'][0]
        Adtext = liste.item (liste.selection ( )[0])['values'][1]
        Sytext = liste.item (liste.selection ( )[0])['values'][2]
        Tltext = liste.item (liste.selection ( )[0])['values'][3]
        Adrtext = liste.item (liste.selection ( )[0])['values'][4]

        EMi.configure (state="normal")
        EMi.delete (0,tkinter.END)
        EMi.insert (0, Mitext)

        EAd.delete (0,tkinter.END)
        EAd.insert (0, Adtext)

        ESy.delete (0,tkinter.END)
        ESy.insert (0, Sytext)

        ETl.delete (0,tkinter.END)
        ETl.insert (0, Tltext)

        EAdr.delete (0,tkinter.END)
        EAdr.insert (0, Adrtext)

    def MusteriAlanlariniTemizle():
        EMi.delete (0,tkinter.END)
        EAd.delete (0, tkinter.END)
        ESy.delete (0, tkinter.END)
        ETl.delete (0, tkinter.END)
        EAdr.delete (0, tkinter.END)

    # noinspection PyShadowingNames
    openMusteri = tkinter.Tk ( )
    openMusteri.geometry ('1000x500')
    openMusteri.configure (background='light pink')
    openMusteri.title ("Müşteri İşlemleri")
    openMusteri.resizable (False, False)

    LMi = tkinter.Label(openMusteri, text="Müşteri id:").place (x=50, y=10)
    EMi = tkinter.Entry (openMusteri, bd=1, width=22)
    EMi.place (x=120, y=10)
    EMi.configure (state="disabled")
    EMi.update ( )

    LAd = tkinter.Label (openMusteri, text="Adı:").place (x=50, y=50)
    EAd = tkinter.Entry (openMusteri, bd=1, width=22)
    EAd.place (x=120, y=50)

    LSy = tkinter.Label (openMusteri, text="Soyadı:").place (x=50, y=90)
    ESy = tkinter.Entry (openMusteri, bd=1, width=22)
    ESy.place (x=120, y=90)

    LTl = tkinter.Label (openMusteri, text="Telefon:").place (x=50, y=140)
    ETl = tkinter.Entry (openMusteri, bd=1, width=22)
    ETl.place (x=120, y=140)

    LAdr = tkinter.Label (openMusteri, text="Adres:").place (x=50, y=190)
    EAdr = tkinter.Entry (openMusteri, bd=1, width=22)
    EAdr.place (x=120, y=190)

    buttonTumMusterileriGetir = tkinter.Button (openMusteri, text="Tüm Müşterileri Getir", command= lambda: MusteriListele())
    buttonTumMusterileriGetir.place (x=50, y=220)

    Ekle = tkinter.Button (openMusteri, text="Ekle", command= lambda: MusteriEkle(EAd.get(), ESy.get(), ETl.get(), EAdr.get()))
    Ekle.place (x=180, y=220)

    Guncelle = tkinter.Button (openMusteri, text="Güncelle", command=lambda :MusteriGuncelle(EMi.get(),EAd.get(),ESy.get(),ETl.get(),EAdr.get()))
    Guncelle.place (x=220, y=220)

    Ara =tkinter. Button (openMusteri, text="Ara", command=lambda :MusteriAra(ETl.get()))
    Ara.place (x=300, y=220)

    Sil =tkinter.Button (openMusteri, text="Sil", command=lambda :MusteriSil(EMi.get()))
    Sil.place (x=340, y=220)

    MusteriAlanlariniTemizlebtn=tkinter.Button(openMusteri,text='Müşteri Alanlarını Temizle', command=lambda :MusteriAlanlariniTemizle())
    MusteriAlanlariniTemizlebtn.place(x=370, y=220)

    liste = Treeview (openMusteri)
    liste["columns"] = ('id', 'ad', 'soyad', 'telefon', 'adres')
    liste.column ('#0', width=0)
    liste.place (x=0, y=270)
    liste.heading ('#0', text='')
    liste.heading ("id", text="Müşteri ID")
    liste.heading ("ad", text="Adı")
    liste.heading ("soyad", text="Soyadı")
    liste.heading ("telefon", text="Telefon")
    liste.heading ("adres", text="Adres")
    liste.bind ('<ButtonRelease-1>', MusteriAlanlariniDoldur)
    MusteriListele()

def openUrun():
    def UrunAlanKontrol(urun_adi, aciklama, urun_fiyati) :
        if isBlank (urun_adi) :
            messagebox.showwarning ("Ürün Bilgileri Kontrol", "Lütfen Ürün adını boş bırakmayın")
            return False
        elif isBlank (aciklama) :
            messagebox.showwarning ("Ürün Bilgileri Kontrol", "Lütfen açıklama kısmını boş bırakmayın")
            return False
        elif isBlank (urun_fiyati) :
            messagebox.showwarning ("Ürün Bilgileri Kontrol", "Lütfen fiyat kısmını boş bırakmayın")
            return False
        return True

    def UrunListele():
        for i in listeUrun.get_children():
            listeUrun.delete (i)
        data = call_Urunleri_getir_sp ()
        index = 0
        for x in data:
            listeUrun.insert (parent='', index=index, iid=index, text='', values=x)
            index = index + 1

    def UrunEkle(urun_adi, aciklama, urun_fiyati):
        if UrunAlanKontrol (urun_adi, aciklama, urun_fiyati):
            call_UrunEkle_sp (urun_adi, aciklama, urun_fiyati)
        UrunListele ()

    def UrunGuncelle(urun_id, urun_adi, aciklama, urun_fiyati):
        if UrunAlanKontrol (urun_adi, aciklama, urun_fiyati):
            call_UrunGuncelle_sp (urun_id,urun_adi,aciklama,urun_fiyati)
        UrunListele ()

    def UrunSil(urun_id):
        call_UrunSil_sp (urun_id)
        UrunListele ()

    def UrunAra(urun_adi):
        for i in listeUrun.get_children ( ):
            listeUrun.delete (i)
        call_UrunAra_urun_adi (listeUrun,urun_adi)

    def UrunAlanlariniDoldur(event):
        curItem = listeUrun.focus ( )
        for x in listeUrun.item (curItem).values ( ):
            print (x)

        Uitext = listeUrun.item (listeUrun.selection ( )[0])['values'][0]
        Uadtext = listeUrun.item (listeUrun.selection ( )[0])['values'][1]
        Actext = listeUrun.item (listeUrun.selection ( )[0])['values'][2]
        Uftext = listeUrun.item (listeUrun.selection ( )[0])['values'][3]


        EUri.configure (state="normal")
        EUri.delete (0, tkinter.END)
        EUri.insert (0, Uitext)

        EUAd.delete (0, tkinter.END)
        EUAd.insert (0, Uadtext)

        EAc.delete (0, tkinter.END)
        EAc.insert (0, Actext)

        EUf.delete (0, tkinter.END)
        EUf.insert (0, Uftext)

    def UrunAlanlariniTemizle():
        EUri.delete (0, tkinter.END)
        EUAd.delete (0, tkinter.END)
        EAc.delete (0, tkinter.END)
        EUf.delete (0, tkinter.END)

    # noinspection PyShadowingNames
    openUrun = tkinter.Tk ( )
    openUrun.geometry ('800x500')
    openUrun.configure (background='light pink')
    openUrun.title ("Ürün İşlemleri")
    openUrun.resizable (False, False)

    LUri = tkinter.Label (openUrun, text="Ürün id:").place (x=50, y=10)
    EUri = tkinter.Entry (openUrun, bd=1, width=22)
    EUri.configure (state="disabled")
    EUri.place (x=130, y=10)
    EUri.update ( )

    LUAd = tkinter.Label (openUrun, text="Ürün Adı").place (x=50, y=50)
    EUAd = tkinter.Entry (openUrun, bd=1, width=22)
    EUAd.place (x=130, y=50)

    LAc = tkinter.Label (openUrun, text="Açıklama:").place (x=50, y=90)
    EAc = tkinter.Entry (openUrun, bd=1, width=22)
    EAc.place (x=130, y=90)

    LUf = tkinter.Label (openUrun, text="Ürün Fiyatı:").place (x=50, y=140)
    EUf = tkinter.Entry (openUrun, bd=1, width=22)
    EUf.place (x=130, y=140)

    buttonTumUrunleriGetir = tkinter.Button (openUrun, text="Tüm Ürünleri Getir", command=lambda : UrunListele())
    buttonTumUrunleriGetir.place (x=30, y=220)

    Ekle = tkinter.Button (openUrun, text="Ekle", command=lambda:UrunEkle(EUAd.get(),EAc.get(),EUf.get()))
    Ekle.place (x=160, y=220)

    Guncelle = tkinter.Button (openUrun, text="Güncelle", command=lambda :UrunGuncelle(EUri.get(),EUAd.get(),EAc.get(),EUf.get()))
    Guncelle.place (x=220, y=220)

    Ara = tkinter.Button (openUrun, text="Ara", command=lambda:UrunAra(EUAd.get()))
    Ara.place (x=300, y=220)

    Sil = tkinter.Button (openUrun, text="Sil", command=lambda:UrunSil(EUri.get()))
    Sil.place (x=350, y=220)

    UrunAlanlariniTemizlebtn = tkinter.Button (openUrun, text="ürün Alanlarını Temizle", command=lambda :UrunAlanlariniTemizle())
    UrunAlanlariniTemizlebtn.place (x=380, y=220)

    listeUrun = Treeview (openUrun)
    listeUrun["columns"] = ('Ürün İD','Ürün Adı', 'Açıklama', 'Ürün Fiyatı')
    listeUrun.column ('#0', width=0)
    listeUrun.place (x=0, y=270)
    listeUrun.heading ('#0', text='')
    listeUrun.heading ("Ürün İD", text="Ürün id")
    listeUrun.heading ("Ürün Adı", text="Ürün Adı")
    listeUrun.heading ("Açıklama", text="Açıklama")
    listeUrun.heading ("Ürün Fiyatı", text="Ürün Fiyatı")
    listeUrun.bind ('<ButtonRelease-1>', UrunAlanlariniDoldur)
    UrunListele()

def openVeresiye():
    def SepetAlanKontrol(urun_id, urun_adet) :
            if isBlank (urun_id) :
                messagebox.showwarning ("Ürün Sepet  Kontrol", "Lütfen urun_id kısmını boş bırakmayın")
                return False
            elif isBlank (urun_adet) :
                messagebox.showwarning ("Ürün Sepet Kontrol", "Lütfen adet kısmını boş bırakmayın")
                return False
            return True

    def VeresiyeAlanKontrol(musteri_id, borc_tutari, sepetUrunSayisi) :
            if isBlank (musteri_id) :
                messagebox.showwarning ("Veresiye Bilgileri Kontrol", "Lütfen müsteri_id kısmını boş bırakmayın")
                return False
            elif sepetUrunSayisi==0:
                messagebox.showwarning ("Veresiye Bilgileri Kontrol", "Lütfen sepete ürün ekleyiniz")
                return False
            elif isBlank (borc_tutari) :
                messagebox.showwarning ("Veresiye Bilgileri Kontrol", "Lütfen borç kısmını boş bırakmayın")
                return False
            return True

    def VeresiyeListele():
        for i in listeVeresiye.get_children ( ):
            listeVeresiye.delete (i)
        data = call_Veresiyeleri_getir_sp ()
        index = 0
        for x in data:
            listeVeresiye.insert (parent='', index=index, iid=index, text='', values=x)
            index = index + 1

    def MusteriDoldur(combobox) :
        data = call_Musterileri_getir_sp ()
        cache = list ( )
        for x in data :
            cache.append (str(x[0]) + "-" + x[1] + "-" + x[2])
        combobox['values'] = cache

    def UrunSepeteEkle():
        value = comboboxUrunSec.get ( )
        urunAdet = entryUrunAdetKilo.get ( )
        if (SepetAlanKontrol(value, urunAdet)):
            toplamSepetTutar = float(ETt.get())
            split_string = value.split ("-")
            urunFiyat=float(split_string[2])
            urunToplamFiyat=urunFiyat*int(urunAdet)

            toplamSepetTutar = toplamSepetTutar + urunToplamFiyat

            ETt.delete(0, tkinter.END)
            ETt.insert(0, toplamSepetTutar)
            urunliste=(split_string[0], split_string[1], urunFiyat, urunAdet, urunToplamFiyat)
            listeSepet.insert (parent='', index=tkinter.END, text='', values=urunliste)

    def UrunleriDoldur(combobox) :
        data = call_Urunleri_getir_sp()
        cache = list ( )
        for x in data :
            cache.append (str(x[0]) + "-" + x[1]+ "-" + str(x[3]))
        combobox['values'] = cache

    def VeresiyeKapat(veresiye_id,odeme_tipi) :
            msg = messagebox.askyesno ("Borç kapama işlemi onayı", "Veresiyeyi kapatmak istediğinizden emin misiniz?")
            if msg == True :
                veresiye_id = EVi.get()
                odeme_tipi = EOtp.get()
                call_VeresiyeGuncelle_sp (veresiye_id, odeme_tipi)
                print("Borç kapandı")
            VeresiyeListele()

    def VeresiyeAlanlariniDoldur(event):
        veresiyeID = listeVeresiye.item(listeVeresiye.selection ( )[0])['values'][0]
        musteriID = listeVeresiye.item (listeVeresiye.selection ( )[0])['values'][1]
        ToplamSepetTutartext = listeVeresiye.item (listeVeresiye.selection ( )[0])['values'][3]
        Odemedurumutext = listeVeresiye.item (listeVeresiye.selection ( )[0])['values'][4]
        OdemeTipitext = listeVeresiye.item (listeVeresiye.selection ( )[0])['values'][6]

        musteri = call_Musteri_getir_musteri_id(musteriID)
        EMs.set(str(musteri[0][0]) + "-" + musteri[0][1] + "-" + musteri[0][2])
        EMs.configure (state="disabled")

        comboboxUrunSec.configure(state="disabled")
        entryUrunAdetKilo.configure(state="disabled")
        btnurunsepeteekle.configure(state="disabled")

        veresiyeDetay = call_VeresiyeDetay_getir_veresiye_id(veresiyeID)
        for i in listeSepet.get_children ( ):
            listeSepet.delete (i)
        for detay in veresiyeDetay:
            urunTutar = detay[7] * detay[3]
            detay2 = (detay[2], detay[5], detay[7], detay[3], urunTutar)
            listeSepet.insert (parent='', index=tkinter.END, text='', values=detay2)

        EVi.configure (state="normal")
        EVi.delete(0, tkinter.END)
        EVi.insert(0, veresiyeID)
        EVi.configure (state="disabled")

        ETt.delete (0, tkinter.END)
        ETt.insert (0, ToplamSepetTutartext)
        ETt.configure (state="disabled")

        EOd.delete (0, tkinter.END)
        EOd.insert (0, Odemedurumutext)
        EOd.configure (state="normal")

        EOtp.delete (0, tkinter.END)
        EOtp.insert (0, OdemeTipitext)
        EOtp.configure (state="normal")

    def VeresiyeUrunAlanlariniDoldur(ensert):
        global urunİD, urunFiyat, urunAdi
        curItem = listeSepet.focus ( )
        for x in listeSepet.item (curItem).values ( ) :
            print (x)
            call_MusteriEkle_sp(ad,soyad,telefon,adres)


    def VeresiyeAlanlariniTemizle():
        EMs.configure(state="normal")
        EMs.delete(0,tkinter.END)
        EVi.configure (state="normal")
        EVi.delete (0, tkinter.END)
        ETt.configure (state="normal")
        ETt.delete (0, tkinter.END)
        EOd.configure (state="normal")
        EOd.delete (0, tkinter.END)
        EOtp.configure (state="normal")
        EOtp.delete(0, tkinter.END)
        comboboxUrunSec.configure (state="normal")
        comboboxUrunSec.delete(0, tkinter.END)
        entryUrunAdetKilo.configure (state="normal")
        entryUrunAdetKilo.delete(0, tkinter.END)
        btnurunsepeteekle.configure (state="normal")
        for i in listeSepet.get_children ( ):
            listeSepet.delete (i)

    def VeresiyeEkle():
        seciliMusteri = EMs.get ( )
        toplamTutar = ETt.get ( )
        sepetUrunSayisi = len(listeSepet.get_children( ))
        if VeresiyeAlanKontrol(seciliMusteri, toplamTutar, sepetUrunSayisi) :
            musteriID = seciliMusteri.split("-")[0]
            urunIDList = ""
            urunAdetKiloList = ""
            for urun in listeSepet.get_children ( ):
                urunIDList = urunIDList = str(listeSepet.item(urun)['values'][0])
                urunAdetKiloList = urunAdetKiloList = str (listeSepet.item (urun)['values'][3])
            call_VeresiyeEkle_sp(musteriID, toplamTutar, urunIDList, urunAdetKiloList)
            VeresiyeListele()

    # noinspection PyShadowingNames
    openVeresiye = tkinter.Tk ( )
    openVeresiye.geometry ('1350x600')
    openVeresiye.configure (background='light pink')
    openVeresiye.title ("Veresiye İşlemleri")
    openVeresiye.resizable (False, False)



    LMs = tkinter.Label (openVeresiye, text="Müşteri Seç:").place (x=10, y=10)
    EMs = ttk.Combobox(openVeresiye, width=60)
    EMs.place (x=105, y=10)

    labelUrun = tkinter.Label (openVeresiye, text="Ürün Seç:").place (x=10, y=50)
    comboboxUrunSec = ttk.Combobox(openVeresiye)
    comboboxUrunSec.place (x=105, y=50)

    LVt = tkinter.Label (openVeresiye, text="Ürün Adet/Kilo:").place (x=260, y=50)
    entryUrunAdetKilo = tkinter.Entry (openVeresiye, bd=1, width=22)
    entryUrunAdetKilo.place (x=360, y=50)

    btnurunsepeteekle=tkinter.Button (openVeresiye, text="Ürün Sepete Ekle", command=UrunSepeteEkle)
    btnurunsepeteekle.place (x=400, y=90)

    LTt = tkinter.Label (openVeresiye, text="Toplam Tutar:").place (x=10, y=130)
    ETt = tkinter.Entry (openVeresiye, bd=1, width=22)
    ETt.place (x=105, y=130)

    LVi = tkinter.Label (openVeresiye, text="Veresiye İD:").place (x=260, y=130)
    EVi = tkinter.Entry (openVeresiye, bd=1, width=22)
    EVi.configure (state="disabled")
    EVi.place (x=360, y=130)

    LOd = tkinter.Label (openVeresiye, text="Ödeme Durumu").place (x=10, y=160)
    EOd= ttk.Combobox(openVeresiye)
    EOd['values']=('Ödendi','Ödenmedi')
    EOd.configure (state="disabled")
    EOd.place (x=105, y=160)

    LOtp = tkinter.Label (openVeresiye, text="Ödeme Tipi:").place (x=10, y=200)
    EOtp = ttk.Combobox (openVeresiye)
    EOtp['values'] = ('Nakit', 'Kredi/Banka Kart')
    EOtp.configure (state="disabled")
    EOtp.place (x=105, y=200)

    buttonTumVeresiyeleriGetir = tkinter.Button (openVeresiye, text="Tüm Veresiyeleri Getir", command=VeresiyeListele)
    buttonTumVeresiyeleriGetir.place (x=10, y=240)

    Ekle = tkinter.Button (openVeresiye, text="Veresiye Ekle", command=VeresiyeEkle)
    Ekle.place (x=150, y=240)

    Guncelle = tkinter.Button (openVeresiye, text="Veresiye Kapat", command=lambda :VeresiyeKapat(EVi.get(),EOtp.get()))
    Guncelle.place (x=250, y=240)

    VeresiyeAlanlariniTemizlebtn = tkinter.Button (openVeresiye, text="Veresiye Alanlarını Temizle",command=VeresiyeAlanlariniTemizle)
    VeresiyeAlanlariniTemizlebtn.place (x=350, y=240)

    listeVeresiye = Treeview(openVeresiye)
    listeVeresiye["columns"] = ('Veresiye İD', 'Müşteri İD', 'Veresiye Tarih', 'Borç Tutarı', 'Ödeme Durumu', 'Ödeme Tarihi','Ödeme Tipi')
    listeVeresiye.column ('#0', width=0)
    listeVeresiye.place(x=0, y=270)
    listeVeresiye.heading ('#0', text='')
    listeVeresiye.heading("Veresiye İD", text="Veresiye İD")
    listeVeresiye.heading("Müşteri İD", text="Müşteri İD")
    listeVeresiye.heading("Veresiye Tarih", text="Veresiye Tarih")
    listeVeresiye.heading("Borç Tutarı", text="Borç Tutarı")
    listeVeresiye.heading("Ödeme Durumu", text="Ödeme Durumu")
    listeVeresiye.heading("Ödeme Tarihi", text="Ödeme Tarihi")
    listeVeresiye.heading("Ödeme Tipi", text="Ödeme Tipi")
    listeVeresiye.bind ('<ButtonRelease-1>', VeresiyeAlanlariniDoldur)

    listeSepet= Treeview (openVeresiye)
    listeSepet["columns"] = ('Urun_ID', 'Urun_Adi','Urun_Fiyati','Urun_KiloAdet','Urun_Toplami')
    listeSepet.column ('#0', width=30)
    listeSepet.column ('Urun_ID', width=50)
    listeSepet.column ('Urun_Adi', width=100)
    listeSepet.column ('Urun_Fiyati', width=100)
    listeSepet.place (x=530, y=30)
    listeSepet.heading ('#0', text="")
    listeSepet.heading ("Urun_ID", text="Ürün ID")
    listeSepet.heading ("Urun_Adi", text="Ürün Adı")
    listeSepet.heading ("Urun_Fiyati", text="Ürün Fiyatı")
    listeSepet.heading ("Urun_KiloAdet", text="Ürün Kilo/Adet")
    listeSepet.heading ("Urun_Toplami", text="Ürün Tutarı")
    listeSepet.bind ('<ButtonRelease-1>', UrunSepeteEkle)

    MusteriDoldur(EMs)
    UrunleriDoldur(comboboxUrunSec)
    ETt.delete (0, tkinter.END)
    ETt.insert (0, 0)
    EOd.set("Ödenmedi")
    VeresiyeListele()

if __name__ == "__main__":
    site = tkinter.Tk ( )
    etiket = tkinter.Label (site, text='MENÜYE HOŞ GELDİNİZ')
    etiket.pack ( )
    etiket.configure (background='pink')

    btn = tkinter.Button (site, text='Müşteri İşlemleri', command=openMusteri)
    btn.pack (padx=20, pady=10)

    btn = tkinter.Button (site, text='Ürün  İşlemleri', command=openUrun)
    btn.pack (padx=20, pady=10)
    btn = tkinter.Button (site, text='Veresiye İşlemleri', command=openVeresiye)
    btn.pack (padx=20, pady=10)
    btn = tkinter.Button (site, text='Çıkış', command=site.quit)
    btn.pack (padx=20, pady=10)
    resim = ImageTk.PhotoImage (Image.open ('Resim.jpg'))
    buton = tkinter.Button (site, image=resim, activebackground='light blue')
    buton.pack()

    site.title ('Menü')
    site.geometry ('900x800')
    site.configure (background='light blue')
    site.mainloop()