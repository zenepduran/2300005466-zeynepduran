#PROJE 14
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit

class IsTakipSistemi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('İş Takip ve Yönetim Sistemi')
        self.setGeometry(100, 100, 300, 250)
        self.layout = QVBoxLayout()

        # Proje oluşturma 
        self.proje_adi_label = QLabel('Proje Adı:')
        self.proje_adi_input = QLineEdit()
        self.baslangic_label = QLabel('Başlangıç Tarihi:')
        self.baslangic_input = QLineEdit()
        self.bitis_label = QLabel('Bitiş Tarihi:')
        self.bitis_input = QLineEdit()
        self.proje_olustur_button = QPushButton('Proje Oluştur')
        self.proje_olustur_button.clicked.connect(self.proje_olustur)

        self.layout.addWidget(self.proje_adi_label)
        self.layout.addWidget(self.proje_adi_input)
        self.layout.addWidget(self.baslangic_label)
        self.layout.addWidget(self.baslangic_input)
        self.layout.addWidget(self.bitis_label)
        self.layout.addWidget(self.bitis_input)
        self.layout.addWidget(self.proje_olustur_button)

        # Çalışan oluşturma 
        self.calisan_adi_label = QLabel('Çalışanın Adı:')
        self.calisan_adi_input = QLineEdit()
        self.calisan_departman_label = QLabel('Departman:')
        self.calisan_departman_input = QLineEdit()
        self.calisan_olustur_button = QPushButton('Çalışan Oluştur')
        self.calisan_olustur_button.clicked.connect(self.calisan_olustur)

        self.layout.addWidget(self.calisan_adi_label)
        self.layout.addWidget(self.calisan_adi_input)
        self.layout.addWidget(self.calisan_departman_label)
        self.layout.addWidget(self.calisan_departman_input)
        self.layout.addWidget(self.calisan_olustur_button)

        # Görev oluşturma 
        self.gorev_adi_label = QLabel('Görev Adı:')
        self.gorev_adi_input = QLineEdit()
        self.sorumlu_kisi_label = QLabel('Sorumlu Kişi:')
        self.sorumlu_kisi_input = QLineEdit()
        self.ilerleme_label = QLabel('İlerleme (%):')
        self.ilerleme_input = QLineEdit()
        self.gorev_olustur_button = QPushButton('Görev Oluştur')
        self.gorev_olustur_button.clicked.connect(self.gorev_olustur)

        self.layout.addWidget(self.gorev_adi_label)
        self.layout.addWidget(self.gorev_adi_input)
        self.layout.addWidget(self.sorumlu_kisi_label)
        self.layout.addWidget(self.sorumlu_kisi_input)
        self.layout.addWidget(self.ilerleme_label)
        self.layout.addWidget(self.ilerleme_input)
        self.layout.addWidget(self.gorev_olustur_button)
        self.setLayout(self.layout)
        self.show()

        # Veritabanı bağlantısı
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect('is_takip.db')
        self.cursor = self.baglanti.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS projeler (
                                proje_id INTEGER PRIMARY KEY,
                                proje_adi TEXT,
                                baslangic_tarihi DATE,
                                bitis_tarihi DATE)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS calisanlar (
                                calisan_id INTEGER PRIMARY KEY,
                                calisan_adi TEXT,
                                departman TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS gorevler (
                                gorev_id INTEGER PRIMARY KEY,
                                gorev_adi TEXT,
                                sorumlu_kisi TEXT,
                                ilerleme INTEGER)''')
        self.baglanti.commit()

    def proje_olustur(self):
        proje_adi = self.proje_adi_input.text()
        baslangic_tarihi = self.baslangic_input.text()
        bitis_tarihi = self.bitis_input.text()

        self.cursor.execute("INSERT INTO projeler (proje_adi, baslangic_tarihi, bitis_tarihi) VALUES (?, ?, ?)",
                            (proje_adi, baslangic_tarihi, bitis_tarihi))
        self.baglanti.commit()
        self.proje_adi_input.clear()
        self.baslangic_input.clear()
        self.bitis_input.clear()

    def calisan_olustur(self):
        calisan_adi = self.calisan_adi_input.text()
        departman = self.calisan_departman_input.text()

        self.cursor.execute("INSERT INTO calisanlar (calisan_adi, departman) VALUES (?, ?)", (calisan_adi, departman))
        self.baglanti.commit()
        self.calisan_adi_input.clear()
        self.calisan_departman_input.clear()

    def gorev_olustur(self):
        gorev_adi = self.gorev_adi_input.text()
        sorumlu_kisi = self.sorumlu_kisi_input.text()
        ilerleme = int(self.ilerleme_input.text())

        self.cursor.execute("INSERT INTO gorevler (gorev_adi, sorumlu_kisi, ilerleme) VALUES (?, ?, ?)",
                            (gorev_adi, sorumlu_kisi, ilerleme))
        self.baglanti.commit()
        self.gorev_adi_input.clear()
        self.sorumlu_kisi_input.clear()
        self.ilerleme_input.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    pencere = IsTakipSistemi()
    sys.exit(app.exec_())
