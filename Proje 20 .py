import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox, QDialog, QFormLayout
import sqlite3

class VideoOyunKoleksiyonu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Oyun Koleksiyonu Yönetimi")
        self.setGeometry(60, 60, 300, 200)

        self.baglanti_olustur()
        self.init_ui()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("video_oyun_koleksiyonu.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS oyunlar (id INTEGER PRIMARY KEY, ad TEXT, tur TEXT, platform TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS koleksiyonlar (id INTEGER PRIMARY KEY, oyuncu TEXT, oyun_id INTEGER, FOREIGN KEY(oyun_id) REFERENCES oyunlar(id))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS oyuncular (id INTEGER PRIMARY KEY, ad TEXT, favori_oyun TEXT, koleksiyon TEXT)")
        self.baglanti.commit()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.v_box = QVBoxLayout()
        self.central_widget.setLayout(self.v_box)

        # Oyun ekleme bölümü
        self.lbl_oyun_adı = QLabel("Oyun Adı:")
        self.txt_oyun_adı = QLineEdit()
        self.lbl_tur = QLabel("Tür:")
        self.txt_tur = QLineEdit()
        self.lbl_platform = QLabel("Platform:")
        self.txt_platform = QLineEdit()
        self.btn_oyun_ekle = QPushButton("Oyun Ekle")
        self.btn_oyun_ekle.clicked.connect(self.oyun_ekle)

        self.v_box.addWidget(self.lbl_oyun_adı)
        self.v_box.addWidget(self.txt_oyun_adı)
        self.v_box.addWidget(self.lbl_tur)
        self.v_box.addWidget(self.txt_tur)
        self.v_box.addWidget(self.lbl_platform)
        self.v_box.addWidget(self.txt_platform)
        self.v_box.addWidget(self.btn_oyun_ekle)

        # Oyuncu ekleme bölümü
        self.lbl_oyuncu_adı = QLabel("Oyuncu Adı:")
        self.txt_oyuncu_adı = QLineEdit()
        self.lbl_favori_oyun = QLabel("Favori Oyun:")
        self.txt_favori_oyun = QLineEdit()
        self.btn_koleksiyon_ekle = QPushButton("Koleksiyon Ekle")
        self.btn_koleksiyon_ekle.clicked.connect(self.koleksiyon_ekle)

        self.v_box.addWidget(self.lbl_oyuncu_adı)
        self.v_box.addWidget(self.txt_oyuncu_adı)
        self.v_box.addWidget(self.lbl_favori_oyun)
        self.v_box.addWidget(self.txt_favori_oyun)
        self.v_box.addWidget(self.btn_koleksiyon_ekle)

        # Oyuncu listesi
        self.liste_widget = QListWidget()
        self.v_box.addWidget(self.liste_widget)

        # Oyuncu bilgilerini yükleme
        self.yukle_oyuncular()

    def oyun_ekle(self):
        oyun_adı = self.txt_oyun_adı.text()
        tur = self.txt_tur.text()
        platform = self.txt_platform.text()

        self.cursor.execute("INSERT INTO oyunlar (ad, tur, platform) VALUES (?, ?, ?)", (oyun_adı, tur, platform))
        self.baglanti.commit()
        QMessageBox.information(self, "Bilgi", "Oyun başarıyla eklendi!")
        self.yukle_oyuncular()

    def koleksiyon_ekle(self):
        oyuncu_adı = self.txt_oyuncu_adı.text()
        favori_oyun = self.txt_favori_oyun.text()

        self.cursor.execute("INSERT INTO oyuncular (ad, favori_oyun) VALUES (?, ?)", (oyuncu_adı, favori_oyun))
        self.baglanti.commit()
        QMessageBox.information(self, "Bilgi", "Koleksiyon başarıyla eklendi!")
        self.yukle_oyuncular()

    def yukle_oyuncular(self):
        self.liste_widget.clear()
        self.cursor.execute("SELECT ad, favori_oyun FROM oyuncular")
        oyuncular = self.cursor.fetchall()
        for oyuncu in oyuncular:
            self.liste_widget.addItem(f"Oyuncu Adı: {oyuncu[0]} - Favori Oyun: {oyuncu[1]}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoOyunKoleksiyonu()
    window.show()
    sys.exit(app.exec_())
