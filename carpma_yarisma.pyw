# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 22:48:04 2019

@author: Fatih Tosun
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *

import sys
import random
import time


class Pencere(QWidget):
    def __init__ (self):
        super().__init__()
        self.setUI()
        self.sayac=0
        self.a = 0
        self.b = 0
        self.c=""
        self.durum=True
        
        self.dogrular = ("Doğru bildin.", "Harikasın.", "Muhteşemsin.",
                    "Tamam bu iş oldu.", "Bravo!!!")
        self.yanlislar = ("Yanlış oldu tekrar dene.", "Olacak, hadi bir daha dene.",
                     "Az kaldı başaracaksın., bir daha dene.",
                     "Sana güveniyorum. Tekrar dene.")
        
        
    def setUI(self):
        self.setGeometry(300,85,600,650)
        self.setWindowIcon(QIcon("C:/Users/fatih/Desktop/Yeni klasör/Yeni klasör/logo.png"))
        
        self.setAutoFillBackground(True)
        self.p=self.palette()
        self.p.setColor(self.backgroundRole(),Qt.cyan)
        self.setPalette(self.p)
        
        self.media=QMediaPlayer()
        self.media.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/fatih/Desktop/Yeni klasör/Yeni klasör/Gong.mp3")))
        self.media1=QMediaPlayer()
        self.media1.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/fatih/Desktop/Yeni klasör/Yeni klasör/PING.mp3")))
        self.media2=QMediaPlayer()
        self.media2.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/fatih/Desktop/Yeni klasör/Yeni klasör/alkis1.wav")))
        self.media3=QMediaPlayer()
        self.media3.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/fatih/Desktop/Yeni klasör/Yeni klasör/yanlis.mp3")))
        self.media4=QMediaPlayer()
        self.media4.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/fatih/Desktop/Yeni klasör/Yeni klasör/basarisiz.mp3")))
        self.media5=QMediaPlayer()
        self.media5.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/fatih/Desktop/Yeni klasör/Yeni klasör/süre.mp3")))
        self.media.setVolume(50)
        self.media1.setVolume(50)
        self.media2.setVolume(50)
        self.media3.setVolume(50)
        self.media4.setVolume(50)
        self.media5.setVolume(50)
        
        self.setWindowTitle("Çarpım Tablosu Yarışması")
        self.isim=QLineEdit()                
        self.isimal=QPushButton("İsmim Doğru")
        self.hosgeldiniz=QLabel("""Çarpım Tablosu Öğreten Programa Hoşgeldiniz\nÖnce isminizi giriniz""")
        self.carpimlar=QLabel("")
        self.carpim_button=QPushButton("BAŞLA!!!")
        self.carpim_cevap=QLineEdit()
        self.cevap_ver=QPushButton("Cevap")
        self.mesaj=QLabel()
        self.sayac_say=QLabel()
        self.z_sayac=QLabel("Başladıktan sonra 60 saniye süren var")
        self.sıra_alan=QPushButton("skoru listeye ekle")
        self.sıra_göster=QPushButton("Sıramı öğren")
        self.listem=QListWidget()
        self.devam=QPushButton("Devam etmek için tıkla")
        self.cikalim=QPushButton("Çıkmak için tıkla")
        self.logo=QLabel()
        self.logo1=QLabel()
        sahip=QLabel()
        sahip.setText("""Fatih Tosun   f_tgs@hotmail.com
                     Beymelek İlkokulu Demre Antalya""")
        sahip.setFont(QFont("Comic Sans MS",8))
        self.logo.setPixmap(QPixmap("C:/Users/fatih/Desktop/Yeni klasör/Yeni klasör/logo.png"))
        self.logo.setAlignment(Qt.AlignRight)
        self.logo1.setPixmap(QPixmap("C:/Users/fatih/Desktop/Yeni klasör/Yeni klasör/okul_logo.jpeg"))
        self.logo1.setAlignment(Qt.AlignLeft)
        
        #setFont(QFont("Comic Sans MS",25))    
        self.hosgeldiniz.setFont(QFont("Comic Sans MS",25))
        self.z_sayac.setFont(QFont("Comic Sans MS",25))
        self.carpim_button.setFont(QFont("Comic Sans MS",25))
        self.isim.setFont(QFont("Comic Sans MS",25))
        self.carpimlar.setFont(QFont("Comic Sans MS",25))
        self.cevap_ver.setFont(QFont("Comic Sans MS",25))
        self.mesaj.setFont(QFont("Comic Sans MS",20))
        self.listem.setFont(QFont("Comic Sans MS",25))
        self.carpim_cevap.setFont(QFont("Comic Sans MS",25))
        
        
        self.mesaj.setAlignment(Qt.AlignCenter)
        self.sayac_say.setAlignment(Qt.AlignCenter)
        sahip.setAlignment(Qt.AlignRight)
         
        h_box=QHBoxLayout()
        h_box2=QHBoxLayout()
        h_box1=QHBoxLayout()
        h_box1.addWidget(self.logo1)
        
        h_box1.addWidget(self.logo)
        h_box.addWidget(self.isim)
        h_box.addWidget(self.isimal)
        h_box2.addWidget(self.carpimlar)
        h_box2.addWidget(self.carpim_cevap)
        h_box2.addWidget(self.cevap_ver)
        h_box.addWidget(self.sayac_say)
        
        
        

        v_box=QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addWidget(self.hosgeldiniz)
        v_box.addWidget(self.carpim_button)
        v_box.addLayout(h_box)
        v_box.addLayout(h_box2)
        v_box.addWidget(self.mesaj)
        v_box.addWidget(self.z_sayac)
        v_box.addWidget(self.sıra_alan)
        v_box.addWidget(self.sıra_göster)
        v_box.addWidget(self.devam)
        v_box.addWidget(self.cikalim)
        v_box.addWidget(self.listem)
        v_box.addWidget(sahip)
                
        self.isimal.clicked.connect(self.isim_al)
        self.carpim_button.clicked.connect(self.zamani_say)
        self.carpim_button.clicked.connect(self.carpma)
        self.isimal.clicked.connect(self.giris_muzik)
        
        #returnPressed.connect
        self.carpim_cevap.returnPressed.connect(self.sonuc_yaz)
        self.carpim_cevap.returnPressed.connect(self.zamani_bitir)
        self.cevap_ver.clicked.connect(self.sonuc_yaz)
        self.cevap_ver.clicked.connect(self.zamani_bitir)
        self.sıra_alan.clicked.connect(self.sira_al)
        self.sıra_göster.clicked.connect(self.sira_oku)
        self.cikalim.clicked.connect(self.cikis)
        self.devam.clicked.connect(self.pencere)
        
        self.setLayout(v_box)
        self.carpim_button.close() #yarışmayı başlatacak olan buton isim girilmeden görülmesin
        self.carpim_cevap.close()
        self.cevap_ver.close()
        self.sıra_alan.close()
        self.sıra_göster.close()
        self.listem.close()
        self.cikalim.close()
        self.devam.close()
        self.show()
        return self.carpim_cevap.text()
        
    def isim_al(self):
        self.ismim = self.isim.text()
        self.hosgeldiniz.setText("Hoş Geldin ***** {} *****. Başarılar Dilerim".format(self.ismim))
        self.isim.close()
        self.isimal.close()
        self.carpim_button.show() #isim girildikten sonra başlama butonu görünsün
        return self.ismim

        
    def carpma(self):
        self.a = random.randint(1, 10)
        self.b = random.randint(1, 10)
        self.c = self.a * self.b
        self.carpimlar.setText("{} kere {}  kaçtır?".format(self.a,self.b))
        self.carpim_button.close() # yarışma başladıktan sonra buton tekrar kaybolsun
        self.carpim_cevap.show()
        self.cevap_ver.show()
        self.logo.close()
        self.logo1.close()
        
    def sonuc_yaz(self):
        if self.carpim_cevap.text() == str(self.c):
            self.media1.play()
            self.mesaj.setText(random.choice(self.dogrular))
            self.sayac +=1
            self.sayac_say.setText(str(self.sayac) +"  doğrun var   {}".format(self.ismim))
            self.carpim_cevap.clear()
            
            if self.sayac==10:
                self.media2.play()
            
            self.carpma()
            
        elif self.carpim_cevap.text() != self.c:
            self.media3.play()
            self.mesaj.setText(random.choice(self.yanlislar))
            self.carpim_cevap.clear()
        
        
        
                
    def zamani_say(self):
        self.basla = time.time()
        self.z_sayac.setText("süren başladı")
        return self.basla

        
    def zamani_bitir(self):
        self.bitis=time.time()
        
                
        if self.bitis - self.basla > 60:
            self.z_sayac.setText("süre doldu")
            self.media5.play()
            self.carpim_cevap.close()
            self.cevap_ver.close()
            self.sayac_say.close()
            self.z_sayac.close()
            self.mesaj.close()
            self.carpimlar.close()
            self.hosgeldiniz.setText("{} bu yarışmada {} doğru yaptın".format(self.ismim,str(self.sayac)))
            self.hosgeldiniz.setFont(QFont("Comic Sans MS",25))
            self.sıra_alan.show()
            self.sıra_göster.show()

    def sira_al(self):
        self.cikalim.show()
        self.devam.show()
        self.sıra_alan.close()
        if self.sayac<10:
            self.mesaj.show()
            self.mesaj.setText("En az 10 doğru yapmalısın")
            self.media4.play()
        elif self.sayac>9:
            with open("sıra.txt","a+") as sıra:
                sıra.write("\n ")
                sıra.write(str( self.sayac))
                sıra.write("  doğruyla  ")
                sıra.write(str(self.ismim))
                sıra.write(" \n")
                sıra.close()
                self.media2.play()
    def sira_oku(self):
        self.logo.show()
        self.logo1.show()
        self.sıra_göster.close()
        self.listem.show()
        with open("sıra.txt","r") as sıra:
            sıra_liste=sıra.readlines()
            sıra_liste.sort(reverse=True)
            sıra_bölünen=sıra_liste[0:40]
            for i, value in enumerate(sıra_bölünen,1):
                self.listem.addItem("{} {}".format(i,value))
            sıra.close()
                           
    def giris_muzik(self):
        self.media.play()    
    
    def pencere(self):
         self.__init__()
         
                 
 
    def cikis(self):
        sys.exit() 
        
        
        
            

            
       
                
   
if __name__ ==  "__main__":
    app=QApplication(sys.argv)
    pencere=Pencere()
    sys.exit(app.exec())

    