#PROJE 13
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox, QComboBox

class BiletSatisPlatformu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Etkinlik ve Bilet Satış Platformu")
        self.setGeometry(100, 100, 300, 250)
        self.arayuz_olustur()
        self.veritabani_baglantisi_kur()

    def arayuz_olustur(self):
        layout = QVBoxLayout()

        # Kullanıcı
        self.ad_label = QLabel("Ad:")
        self.ad_input = QLineEdit()
        layout.addWidget(self.ad_label)
        layout.addWidget(self.ad_input)

        self.soyad_label = QLabel("Soyad:")
        self.soyad_input = QLineEdit()
        layout.addWidget(self.soyad_label)
        layout.addWidget(self.soyad_input)

        self.eposta_label = QLabel("E-Posta:")
        self.eposta_input = QLineEdit()
        layout.addWidget(self.eposta_label)
        layout.addWidget(self.eposta_input)
        self.setLayout(layout)

        # Etkinlik
        self.etkinlik_ad_label = QLabel("Etkinlik:")
        self.etkinlik_ad_combobox = QComboBox()
        self.etkinlik_ad_combobox.addItems(["Müzik" ,"Konser", "Festival"]) 
        layout.addWidget(self.etkinlik_ad_label)
        layout.addWidget(self.etkinlik_ad_combobox)

        self.etkinlik_tarih_label = QLabel("Tarih:")
        self.etkinlik_tarih_combobox = QComboBox()
        self.etkinlik_tarih_combobox.addItems(["15 Mayıs Çarşamba", "24 Mayıs Cuma"]) 
        layout.addWidget(self.etkinlik_tarih_label)
        layout.addWidget(self.etkinlik_tarih_combobox)

        self.etkinlik_mekan_label = QLabel("Mekan:")
        self.etkinlik_mekan_combobox = QComboBox()
        self.etkinlik_mekan_combobox.addItems(["Kültür Merkezi","Plaj Alanı"]) 
        layout.addWidget(self.etkinlik_mekan_label)
        layout.addWidget(self.etkinlik_mekan_combobox)

        self.ücret_label = QLabel("Ücret:")
        self.ücret_input = QLineEdit()
        layout.addWidget(self.ücret_label)
        layout.addWidget(self.ücret_input)

        self.kullanici_bilgisi_label = QLabel("Bilet Numarası:")
        self.kullanici_bilgisi_input = QLineEdit()
        layout.addWidget(self.kullanici_bilgisi_label)
        layout.addWidget(self.kullanici_bilgisi_input)

        self.kullanici_bilet_al_button = QPushButton("Bilet Satın Al")
        self.kullanici_bilet_al_button.clicked.connect(self.kullanici_bilet_al)
        layout.addWidget(self.kullanici_bilet_al_button)

    def veritabani_baglantisi_kur(self):
        self.baglanti = sqlite3.connect('bilet_satis_platformu.db')
        self.imlec = self.baglanti.cursor()
        self.imlec.execute('''CREATE TABLE IF NOT EXISTS Etkinlikler
                               (id INTEGER PRIMARY KEY,
                                ad TEXT,
                                tarih TEXT,
                                mekan TEXT)''')
        self.baglanti.commit()

    def etkinlik_olustur(self):
        etkinlik_ad = self.etkinlik_ad_input.text().strip()
        etkinlik_tarih = self.etkinlik_tarih_input.text().strip()
        etkinlik_mekan = self.etkinlik_mekan_input.text().strip()

        if etkinlik_ad and etkinlik_tarih and etkinlik_mekan:
            self.imlec.execute("INSERT INTO Etkinlikler (ad, tarih, mekan) VALUES (?, ?, ?)", (etkinlik_ad, etkinlik_tarih, etkinlik_mekan))
            self.baglanti.commit()
            self.etkinlik_listesi.addItem(f"{etkinlik_ad} - {etkinlik_tarih} - {etkinlik_mekan}")
            QMessageBox.information(self, "Başarılı", "Etkinlik başarıyla oluşturuldu!")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")

    def bilet_sat(self):
        bilet_numarasi = self.bilet_numarasi_input.text().strip()
        bilet_etkinlik_bilgisi = self.bilet_etkinlik_bilgisi_input.text().strip()

        if bilet_numarasi and bilet_etkinlik_bilgisi:
            QMessageBox.information(self, "Başarılı", "Bilet satışı başarıyla gerçekleştirildi!")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")

    def kullanici_bilet_al(self):
        ad = self.ad_input.text().strip()
        soyad = self.soyad_input.text().strip()
        eposta = self.eposta_input.text().strip()
        bilet_numarasi = self.kullanici_bilgisi_input.text().strip()

        if ad and soyad and eposta and bilet_numarasi:
            QMessageBox.information(self, "Başarılı", "Bilet alımı başarıyla gerçekleştirildi!")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")

    def closeEvent(self, event):
        self.baglanti.close()
        event.accept()

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = BiletSatisPlatformu()
    pencere.show()
    sys.exit(uygulama.exec_())
