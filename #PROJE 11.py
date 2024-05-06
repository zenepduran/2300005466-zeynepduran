#PROJE 11 
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QListWidget, QComboBox
import sqlite3

class Enstruman:
    def __init__(self, ad, stok, durum):
        self.ad = ad
        self.stok = stok
        self.durum = durum

class Satis:
    def __init__(self, siparis_no, enstruman):
        self.siparis_no = siparis_no
        self.enstruman = enstruman

class MuzikDukkani(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Müzik Enstrümanı Dükkanı Yönetimi")
        self.setGeometry(100, 100, 350, 200)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.veritabani_baglantisi_olustur()
        self.tabloları_olustur()
        self.init_ui()

    def veritabani_baglantisi_olustur(self):
        self.conn = sqlite3.connect('muzik_dukkani.db')
        self.cur = self.conn.cursor()

    def tabloları_olustur(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS enstrumanlar (
                            id INTEGER PRIMARY KEY,
                            ad TEXT,
                            stok INTEGER,
                            durum TEXT
                            )''')

        self.conn.commit()

    def init_ui(self):
        # Enstrüman Bilgileri Bölümü
        self.layout.addWidget(QLabel("Enstrüman Bilgileri"))
        self.enstruman_ad_input = QLineEdit()
        self.enstruman_stok_input = QLineEdit()
        self.enstruman_durum_combobox = QComboBox()
        self.enstruman_durum_combobox.addItems(["Var", "Yok"])

        enstruman_ekle_layout = QHBoxLayout()
        enstruman_ekle_layout.addWidget(QLabel("Ad:"))
        enstruman_ekle_layout.addWidget(self.enstruman_ad_input)
        enstruman_ekle_layout.addWidget(QLabel("Stok Miktarı:"))
        enstruman_ekle_layout.addWidget(self.enstruman_stok_input)
        enstruman_ekle_layout.addWidget(QLabel("Durum:"))
        enstruman_ekle_layout.addWidget(self.enstruman_durum_combobox)
        self.layout.addLayout(enstruman_ekle_layout)

        enstruman_ekle_button = QPushButton("Enstrüman Ekle")
        enstruman_ekle_button.clicked.connect(self.enstruman_ekle)
        self.layout.addWidget(enstruman_ekle_button)

        # Satış Bölümü
        self.layout.addWidget(QLabel("Satış Bilgileri"))
        self.satis_siparis_input = QLineEdit()
        self.layout.addWidget(QLabel("Sipariş No:"))
        self.layout.addWidget(self.satis_siparis_input)

        self.enstrumanlar_listesi = QListWidget()
        self.layout.addWidget(QLabel("Satılan Enstrümanlar"))

        self.satis_enstruman_combobox = QComboBox()
        self.satis_enstruman_combobox.addItems(["Piyano", "Gitar", "Flüt", "Saksafon"])
        self.layout.addWidget(self.satis_enstruman_combobox)

        satis_ekle_button = QPushButton("Satış Yap")
        satis_ekle_button.clicked.connect(self.satis_ekle)
        self.layout.addWidget(satis_ekle_button)

        # Destek Bölümü
        self.layout.addWidget(QLabel("Destek Bilgileri"))
        self.destek_talep_input = QLineEdit()
        self.layout.addWidget(QLabel("Talep No:"))
        self.layout.addWidget(self.destek_talep_input)

        destek_ekle_button = QPushButton("Destek Oluştur")
        destek_ekle_button.clicked.connect(self.destek_ekle)
        self.layout.addWidget(destek_ekle_button)

    def enstruman_ekle(self):
        ad = self.enstruman_ad_input.text()
        stok = self.enstruman_stok_input.text()
        durum = self.enstruman_durum_combobox.currentText()

        if ad and stok:
            self.cur.execute("INSERT INTO enstrumanlar (ad, stok, durum) VALUES (?, ?, ?)", (ad, stok, durum))
            self.conn.commit()
            QMessageBox.information(self, "Başarılı", "Enstrüman başarıyla eklendi.")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen enstrüman adı, stok miktarı ve durumunu giriniz.")

    def satis_ekle(self):
        siparis_no = self.satis_siparis_input.text()
        enstruman = self.satis_enstruman_combobox.currentText()

        if siparis_no and enstruman:
            self.cur.execute("INSERT INTO satislar (siparis_no, enstruman) VALUES (?, ?)", (siparis_no, enstruman))
            self.conn.commit()
            QMessageBox.information(self, "Başarılı", "Satış başarıyla eklendi.")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen sipariş numarası ve enstrüman seçiniz.")

    def destek_ekle(self):
        talep_no = self.destek_talep_input.text()

        if talep_no:
            self.cur.execute("INSERT INTO destek (talep_no) VALUES (?)", (talep_no,))
            self.conn.commit()
            QMessageBox.information(self, "Başarılı", "Destek talebi başarıyla oluşturuldu.")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen talep numarasını giriniz.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MuzikDukkani()
    window.show()
    sys.exit(app.exec_())

