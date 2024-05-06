import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QComboBox

class StokTakipSistemi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stok Takip Sistemi")
        self.arayuz_olustur()
        self.veritabani_baglantisi_olustur()

    def arayuz_olustur(self):
        self.duzen = QVBoxLayout()

        # Product (Ürün) Section
        self.urun_label = QLabel("Ürün Adı:")
        self.urun_input = QLineEdit()
        self.duzen.addWidget(self.urun_label)
        self.duzen.addWidget(self.urun_input)

        self.stok_label = QLabel("Stok Miktarı:")
        self.stok_input = QLineEdit()
        self.duzen.addWidget(self.stok_label)
        self.duzen.addWidget(self.stok_input)

        self.urun_ekle_button = QPushButton("Ürün Ekle")
        self.urun_ekle_button.clicked.connect(self.urun_ekle)
        self.duzen.addWidget(self.urun_ekle_button)

        # Stock (Stok) Section
        self.stok_listesi_label = QLabel("Stok Durumu:")
        self.stok_combobox = QComboBox()
        self.stok_combobox.addItems(["Var", "Az", "Bitmek Üzere", "Tükenmiş"])
        self.duzen.addWidget(self.stok_listesi_label)
        self.duzen.addWidget(self.stok_combobox)

        self.stok_guncelle_button = QPushButton("Stok Güncelle")
        self.stok_guncelle_button.clicked.connect(self.stok_guncelle)
        self.duzen.addWidget(self.stok_guncelle_button)

        # Order (Sipariş) Section
        self.siparis_label = QLabel("Sipariş Numarası:")
        self.siparis_input = QLineEdit()
        self.duzen.addWidget(self.siparis_label)
        self.duzen.addWidget(self.siparis_input)

        self.siparis_detay_label = QLabel("Sipariş Detayları:")
        self.siparis_detay_input = QTextEdit()
        self.duzen.addWidget(self.siparis_detay_label)
        self.duzen.addWidget(self.siparis_detay_input)

        self.siparis_olustur_button = QPushButton("Sipariş Oluştur")
        self.siparis_olustur_button.clicked.connect(self.siparis_olustur)
        self.duzen.addWidget(self.siparis_olustur_button)

        self.setLayout(self.duzen)

    def veritabani_baglantisi_olustur(self):
        self.veritabani_baglantisi = sqlite3.connect('stok_takip.db')
        self.cursor = self.veritabani_baglantisi.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Urunler
                                (id INTEGER PRIMARY KEY,
                                ad TEXT,
                                stok TEXT)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Siparisler
                                (id INTEGER PRIMARY KEY,
                                siparis_no TEXT,
                                detay TEXT)''')

        self.veritabani_baglantisi.commit()

    def urun_ekle(self):
        urun_adi = self.urun_input.text().strip()
        stok_durumu = self.stok_combobox.currentText()

        if urun_adi and stok_durumu:
            self.cursor.execute("INSERT INTO Urunler (ad, stok) VALUES (?, ?)", (urun_adi, stok_durumu))
            self.veritabani_baglantisi.commit()
            QMessageBox.information(self, "Başarılı", "Ürün başarıyla eklendi!")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen ürün adı ve stok durumu seçin.")

    def stok_guncelle(self):
        QMessageBox.warning(self, "Uyarı", "Stok güncelleme işlemi henüz eklenmedi.")

    def siparis_olustur(self):
        siparis_no = self.siparis_input.text().strip()
        siparis_detay = self.siparis_detay_input.toPlainText().strip()

        if siparis_no and siparis_detay:
            self.cursor.execute("INSERT INTO Siparisler (siparis_no, detay) VALUES (?, ?)", (siparis_no, siparis_detay))
            self.veritabani_baglantisi.commit()
            QMessageBox.information(self, "Başarılı", "Sipariş başarıyla oluşturuldu!")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen sipariş numarası ve detayları girin.")

    def closeEvent(self, event):
        self.veritabani_baglantisi.close()
        event.accept()

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = StokTakipSistemi()
    pencere.show()
    sys.exit(uygulama.exec_())

