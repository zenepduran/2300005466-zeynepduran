#PROJE 15
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
import sqlite3

class KitapUygulamasi(QWidget):
    def __init__(self):
        super().__init__()
        self.arayuzuOlustur()
        self.baglantiyiOlustur()
        self.tabloyuOlustur()

    def arayuzuOlustur(self):
        self.setWindowTitle('Çevrimiçi Kitap Okuma ve Paylaşım Platformu')
        self.setGeometry(100, 100, 400, 550)

        # Kullanıcı girişi 
        self.lbl_kullanici_adi = QLabel('Kullanıcı ID:', self)
        self.lbl_kullanici_adi.move(20, 20)
        self.txt_kullanici_adi = QLineEdit(self)
        self.txt_kullanici_adi.move(150, 20)

        self.lbl_sifre = QLabel('Şifre:', self)
        self.lbl_sifre.move(20, 60)
        self.txt_sifre = QLineEdit(self)
        self.txt_sifre.move(150, 60)
        self.txt_sifre.setEchoMode(QLineEdit.Password)

        self.btn_giris = QPushButton('Giriş Yap', self)
        self.btn_giris.move(150, 100)
        self.btn_giris.clicked.connect(self.girisYap)

        # Kitap ekleme 
        self.lbl_kitap_adi = QLabel('Kitap Adı:', self)
        self.lbl_kitap_adi.move(20, 150)
        self.txt_kitap_adi = QLineEdit(self)
        self.txt_kitap_adi.move(150, 150)

        self.lbl_yazar = QLabel('Yazar:', self)
        self.lbl_yazar.move(20, 190)
        self.txt_yazar = QLineEdit(self)
        self.txt_yazar.move(150, 190)

        self.lbl_yayinevi = QLabel('Yayınevi:', self)
        self.lbl_yayinevi.move(20, 230)
        self.txt_yayinevi = QLineEdit(self)
        self.txt_yayinevi.move(150, 230)

        self.btn_kitap_ekle = QPushButton('Kitap Ekle', self)
        self.btn_kitap_ekle.move(150, 270)
        self.btn_kitap_ekle.clicked.connect(self.kitapEkle)

        # Yorum ekleme 
        self.lbl_yorum = QLabel('Yorum Metni:', self)
        self.lbl_yorum.move(20, 320)
        self.txt_yorum = QTextEdit(self)
        self.txt_yorum.setGeometry(150, 320, 200, 100)

        self.btn_yorum_ekle = QPushButton('Yorum Ekle', self)
        self.btn_yorum_ekle.move(150, 480)
        self.btn_yorum_ekle.clicked.connect(self.yorumEkle)

    def baglantiyiOlustur(self):
        self.baglanti = sqlite3.connect('kitap_veritabani.db')
        self.cursor = self.baglanti.cursor()

    def tabloyuOlustur(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS kitaplar (
                            id INTEGER PRIMARY KEY,
                            ad TEXT,
                            yazar TEXT,
                            yayinevi TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS yorumlar (
                            id INTEGER PRIMARY KEY,
                            yorum TEXT,
                            yorum_yapan TEXT,
                            kitap_id INTEGER,
                            FOREIGN KEY(kitap_id) REFERENCES kitaplar(id))''')
        self.baglanti.commit()

    def girisYap(self):
        kullanici_adi = self.txt_kullanici_adi.text()
        sifre = self.txt_sifre.text()

        if kullanici_adi == "admin" and sifre == "admin":
            QMessageBox.information(self, 'Giriş Başarılı', 'Hoş geldiniz!')
        else:
            QMessageBox.warning(self, 'Hata', 'Geçersiz kullanıcı adı veya şifre!')

    def kitapEkle(self):
        kitap_adi = self.txt_kitap_adi.text()
        yazar = self.txt_yazar.text()
        yayinevi = self.txt_yayinevi.text()
        self.cursor.execute('''INSERT INTO kitaplar (ad, yazar, yayinevi) VALUES (?, ?, ?)''', (kitap_adi, yazar, yayinevi))
        self.baglanti.commit()
        self.txt_kitap_adi.clear()
        self.txt_yazar.clear()
        self.txt_yayinevi.clear()

    def yorumEkle(self):
        yorum = self.txt_yorum.toPlainText()
        yorum_yapan = self.txt_yorum_yapan.text()
        kitap_id = self.txt_secilen_kitap.text() 
        self.cursor.execute('''INSERT INTO yorumlar (yorum, yorum_yapan, kitap_id) VALUES (?, ?, ?)''', (yorum, yorum_yapan, kitap_id))
        self.baglanti.commit()
        self.txt_yorum.clear()
        self.txt_yorum_yapan.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = KitapUygulamasi()
    ex.show()
    sys.exit(app.exec_())
