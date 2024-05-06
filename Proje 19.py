import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox, QDialog, QFormLayout
import sqlite3

class RestoranSiparisSistemi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Restoran Sipariş ve Yönetim Sistemi")
        self.setGeometry(50, 50, 400, 200)

        self.baglanti_olustur()
        self.init_ui()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("restoran_veritabani.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS urunler (id INTEGER PRIMARY KEY, ad TEXT, fiyat REAL, stok INTEGER)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS siparisler (id INTEGER PRIMARY KEY, numara INTEGER, icerik TEXT, musteri TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS musteriler (id INTEGER PRIMARY KEY, ad TEXT, adres TEXT, siparis_gecmisi TEXT)")
        self.baglanti.commit()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.v_box = QVBoxLayout()
        self.central_widget.setLayout(self.v_box)

        self.lbl_urun_adı = QLabel("Ürün Adı:")
        self.txt_urun_adı = QLineEdit()
        self.lbl_fiyat = QLabel("Fiyatı:")
        self.txt_fiyat = QLineEdit()
        self.lbl_stok = QLabel("Stok Durumu:")
        self.txt_stok = QLineEdit()
        self.btn_urun_ekle = QPushButton("Ürün Ekle")
        self.btn_urun_ekle.clicked.connect(self.urun_ekle)

        self.v_box.addWidget(self.lbl_urun_adı)
        self.v_box.addWidget(self.txt_urun_adı)
        self.v_box.addWidget(self.lbl_fiyat)
        self.v_box.addWidget(self.txt_fiyat)
        self.v_box.addWidget(self.lbl_stok)
        self.v_box.addWidget(self.txt_stok)
        self.v_box.addWidget(self.btn_urun_ekle)

        self.lbl_siparis_numarası = QLabel("Sipariş Numarası:")
        self.txt_siparis_numarası = QLineEdit()
        self.lbl_icerik = QLabel("İçerik:")
        self.txt_icerik = QLineEdit()
        self.lbl_musteri = QLabel("Müşteri:")
        self.txt_musteri = QLineEdit()
        self.btn_siparis_al = QPushButton("Sipariş Al")
        self.btn_siparis_al.clicked.connect(self.siparis_al)

        self.v_box.addWidget(self.lbl_siparis_numarası)
        self.v_box.addWidget(self.txt_siparis_numarası)
        self.v_box.addWidget(self.lbl_icerik)
        self.v_box.addWidget(self.txt_icerik)
        self.v_box.addWidget(self.lbl_musteri)
        self.v_box.addWidget(self.txt_musteri)
        self.v_box.addWidget(self.btn_siparis_al)

        self.liste_widget = QListWidget()
        self.v_box.addWidget(self.liste_widget)

        self.yukle_urunler()

    def urun_ekle(self):
        urun_adı = self.txt_urun_adı.text()
        fiyat = float(self.txt_fiyat.text())
        stok = int(self.txt_stok.text())

        self.cursor.execute("INSERT INTO urunler (ad, fiyat, stok) VALUES (?, ?, ?)", (urun_adı, fiyat, stok))
        self.baglanti.commit()
        QMessageBox.information(self, "Bilgi", "Ürün başarıyla eklendi!")
        self.yukle_urunler()

    def siparis_al(self):
        siparis_numarası = int(self.txt_siparis_numarası.text())
        icerik = self.txt_icerik.text()
        musteri = self.txt_musteri.text()

        self.cursor.execute("INSERT INTO siparisler (numara, icerik, musteri) VALUES (?, ?, ?)", (siparis_numarası, icerik, musteri))
        self.baglanti.commit()
        QMessageBox.information(self, "Bilgi", "Sipariş başarıyla alındı!")
        self.yukle_siparisler()

    def yukle_urunler(self):
        self.liste_widget.clear()
        self.cursor.execute("SELECT ad FROM urunler")
        urunler = self.cursor.fetchall()
        for urun in urunler:
            self.liste_widget.addItem(urun[0])

    def yukle_siparisler(self):
        pass  # Buraya siparişlerin yüklendiği kod eklenecek.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RestoranSiparisSistemi()
    window.show()
    sys.exit(app.exec_())
