import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTextEdit, QMessageBox

class CRM(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Müşteri İlişkileri Yönetimi (CRM)")
        self.arayuz_olustur()
        self.veritabani_baglantisi_olustur()

    def arayuz_olustur(self):
        self.duzen = QVBoxLayout()

        # Customer (Müşteri) Section
        self.musteri_label = QLabel("Müşteri Adı:")
        self.musteri_input = QLineEdit()
        self.duzen.addWidget(self.musteri_label)
        self.duzen.addWidget(self.musteri_input)

        self.iletisim_label = QLabel("İletişim Bilgileri:")
        self.iletisim_input = QLineEdit()
        self.duzen.addWidget(self.iletisim_label)
        self.duzen.addWidget(self.iletisim_input)

        self.musteri_ekle_button = QPushButton("Müşteri Ekle")
        self.musteri_ekle_button.clicked.connect(self.musteri_ekle)
        self.duzen.addWidget(self.musteri_ekle_button)

        # Sale (Satış) Section
        self.satis_numarasi_label = QLabel("Satış Numarası:")
        self.satis_numarasi_input = QLineEdit()
        self.duzen.addWidget(self.satis_numarasi_label)
        self.duzen.addWidget(self.satis_numarasi_input)

        self.satilan_urunler_label = QLabel("Satılan Ürünler:")
        self.satilan_urunler_input = QLineEdit()
        self.duzen.addWidget(self.satilan_urunler_label)
        self.duzen.addWidget(self.satilan_urunler_input)

        self.satis_ekle_button = QPushButton("Satış Ekle")
        self.satis_ekle_button.clicked.connect(self.satis_ekle)
        self.duzen.addWidget(self.satis_ekle_button)

        # Support (Destek) Section
        self.destek_talebi_label = QLabel("Destek Talebi Detayları:")
        self.destek_talebi_input = QTextEdit()
        self.duzen.addWidget(self.destek_talebi_label)
        self.duzen.addWidget(self.destek_talebi_input)

        self.destek_talebi_ekle_button = QPushButton("Destek Talebi Oluştur")
        self.destek_talebi_ekle_button.clicked.connect(self.destek_talebi_olustur)
        self.duzen.addWidget(self.destek_talebi_ekle_button)

        self.setLayout(self.duzen)

    def veritabani_baglantisi_olustur(self):
        self.veritabani_baglantisi = sqlite3.connect('crm.db')
        self.cursor = self.veritabani_baglantisi.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Musteriler
                                (id INTEGER PRIMARY KEY,
                                ad TEXT,
                                iletisim TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Satislar
                                (id INTEGER PRIMARY KEY,
                                satis_numarasi INTEGER,
                                musteri_id INTEGER,
                                urunler TEXT,
                                FOREIGN KEY(musteri_id) REFERENCES Musteriler(id))''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS DestekTalepleri
                                (id INTEGER PRIMARY KEY,
                                musteri_id INTEGER,
                                detaylar TEXT,
                                FOREIGN KEY(musteri_id) REFERENCES Musteriler(id))''')
        self.veritabani_baglantisi.commit()

    def musteri_ekle(self):
        musteri_ad = self.musteri_input.text().strip()
        iletisim_bilgisi = self.iletisim_input.text().strip()

        if musteri_ad and iletisim_bilgisi:
            self.cursor.execute("INSERT INTO Musteriler (ad, iletisim) VALUES (?, ?)", (musteri_ad, iletisim_bilgisi))
            self.veritabani_baglantisi.commit()
            QMessageBox.information(self, "Başarılı", "Müşteri başarıyla eklendi!")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen müşteri adı ve iletişim bilgilerini girin.")

    def satis_ekle(self):
        satis_numarasi = self.satis_numarasi_input.text().strip()
        musteri_id = self.musteri_input.text().strip()
        urunler = self.satilan_urunler_input.text().strip()

        if satis_numarasi and musteri_id and urunler:
            self.cursor.execute("INSERT INTO Satislar (satis_numarasi, musteri_id, urunler) VALUES (?, ?, ?)", (satis_numarasi, musteri_id, urunler))
            self.veritabani_baglantisi.commit()
            QMessageBox.information(self, "Başarılı", "Satış başarıyla eklendi!")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen satış numarası, müşteri ID ve satılan ürünleri girin.")

    def destek_talebi_olustur(self):
        musteri_id = self.musteri_input.text().strip()
        detaylar = self.destek_talebi_input.toPlainText().strip()

        if musteri_id and detaylar:
            self.cursor.execute("INSERT INTO DestekTalepleri (musteri_id, detaylar) VALUES (?, ?)", (musteri_id, detaylar))
            self.veritabani_baglantisi.commit()
            QMessageBox.information(self, "Başarılı", "Destek talebi başarıyla oluşturuldu!")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen müşteri ID ve destek talebi detaylarını girin.")

    def closeEvent(self, event):
        self.veritabani_baglantisi.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CRM()
    window.show()
    sys.exit(app.exec_())


