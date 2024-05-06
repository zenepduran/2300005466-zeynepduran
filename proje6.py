import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox

class TarifUygulamasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tarif Uygulaması")
        self.arayuz_olustur()
        self.veritabani_baglantisi_olustur()

    def arayuz_olustur(self):
        self.duzen = QVBoxLayout()

        # Tarif
        self.tarif_ad_label = QLabel("Tarif Adı:")
        self.tarif_ad_input = QLineEdit()
        self.duzen.addWidget(self.tarif_ad_label)
        self.duzen.addWidget(self.tarif_ad_input)

        self.malzemeler_label = QLabel("Malzemeler:")
        self.malzemeler_input = QTextEdit()
        self.duzen.addWidget(self.malzemeler_label)
        self.duzen.addWidget(self.malzemeler_input)

        # Malzeme
        self.malzeme_ad_label = QLabel("Malzeme Adı:")
        self.malzeme_ad_input = QLineEdit()
        self.duzen.addWidget(self.malzeme_ad_label)
        self.duzen.addWidget(self.malzeme_ad_input)

        self.miktar_label = QLabel("Miktarı:")
        self.miktar_input = QLineEdit()
        self.duzen.addWidget(self.miktar_label)
        self.duzen.addWidget(self.miktar_input)

        self.tarif_label = QLabel("Tarif:")
        self.tarif_input = QTextEdit()
        self.duzen.addWidget(self.tarif_label)
        self.duzen.addWidget(self.tarif_input)

        self.tarif_ekle_button = QPushButton("Tarifi Ekle")
        self.tarif_ekle_button.clicked.connect(self.tarif_ekle)
        self.duzen.addWidget(self.tarif_ekle_button)

        # Kullanıcı
        self.kullanici_ad_label = QLabel("Kullanıcı Adı:")
        self.kullanici_ad_input = QLineEdit()
        self.duzen.addWidget(self.kullanici_ad_label)
        self.duzen.addWidget(self.kullanici_ad_input)

        self.sifre_label = QLabel("Şifre:")
        self.sifre_input = QLineEdit()
        self.sifre_input.setEchoMode(QLineEdit.Password)
        self.duzen.addWidget(self.sifre_label)
        self.duzen.addWidget(self.sifre_input)

        self.setLayout(self.duzen)

    def veritabani_baglantisi_olustur(self):
        self.veritabani_baglantisi = sqlite3.connect('tarifler.db')
        self.cursor = self.veritabani_baglantisi.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Tarifler
                                (tarif_id INTEGER PRIMARY KEY,
                                tarif_adi TEXT,
                                malzemeler TEXT,
                                tarif_metni TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Kullanicilar
                                (kullanici_id INTEGER PRIMARY KEY,
                                ad TEXT,
                                sifre TEXT)''')
        self.veritabani_baglantisi.commit()

    def tarif_ekle(self):
        tarif_ad = self.tarif_ad_input.text().strip()
        malzemeler = self.malzemeler_input.toPlainText().strip()
        tarif_icerik = self.tarif_input.toPlainText().strip()

        if tarif_ad and malzemeler and tarif_icerik:
            self.cursor.execute("INSERT INTO Tarifler (tarif_adi, malzemeler, tarif_metni) VALUES (?, ?, ?)",
                                (tarif_ad, malzemeler, tarif_icerik))
            self.veritabani_baglantisi.commit()
            QMessageBox.information(self, "Başarılı", "Tarif başarıyla eklendi!")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")

    def closeEvent(self, event):
        self.veritabani_baglantisi.close()
        event.accept()

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = TarifUygulamasi()
    pencere.show()
    sys.exit(uygulama.exec_())
