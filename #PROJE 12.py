#PROJE 12
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QMessageBox, QRadioButton, QButtonGroup, QComboBox
import sqlite3

class Kullanici:
    def __init__(self, ad, soyad, yas, cinsiyet):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.cinsiyet = cinsiyet

class SaglikKaydi:
    def __init__(self, kan_basinci, nabiz, kan_sekeri):
        self.kan_basinci = kan_basinci
        self.nabiz = nabiz
        self.kan_sekeri = kan_sekeri

class Egzersiz:
    def __init__(self, ad, süre, tekrar):
        self.ad = ad
        self.süre = süre
        self.tekrar = tekrar

class SaglikUygulamasi(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kişisel Sağlık Takip Uygulaması")
        self.setGeometry(50, 50, 500, 400)
        layout = QVBoxLayout()

        self.kullanici_baslik = QLabel("Kullanıcı Bilgileri")
        layout.addWidget(self.kullanici_baslik)

        self.ad_label = QLabel("Ad:")
        self.ad_input = QLineEdit()
        layout.addWidget(self.ad_label)
        layout.addWidget(self.ad_input)

        self.soyad_label = QLabel("Soyad:")
        self.soyad_input = QLineEdit()
        layout.addWidget(self.soyad_label)
        layout.addWidget(self.soyad_input)

        self.yas_label = QLabel("Yaş:")
        self.yas_input = QLineEdit()
        layout.addWidget(self.yas_label)
        layout.addWidget(self.yas_input)

        self.cinsiyet_label = QLabel("Cinsiyet:")
        self.erkek_radio = QRadioButton("Erkek")
        self.kadin_radio = QRadioButton("Kadın")
        self.cinsiyet_group = QButtonGroup(self)
        self.cinsiyet_group.addButton(self.erkek_radio)
        self.cinsiyet_group.addButton(self.kadin_radio)
        layout.addWidget(self.cinsiyet_label)
        layout.addWidget(self.erkek_radio)
        layout.addWidget(self.kadin_radio)

        self.kayit_ekle_btn = QPushButton("Kayıt Ekle")
        self.kayit_ekle_btn.clicked.connect(self.kayit_ekle)
        layout.addWidget(self.kayit_ekle_btn)

        self.saglik_kaydi_baslik = QLabel("Sağlık Kaydı")
        layout.addWidget(self.saglik_kaydi_baslik)

        self.kan_basinci_label = QLabel("Kan Basıncı:")
        self.kan_basinci_input = QLineEdit()
        layout.addWidget(self.kan_basinci_label)
        layout.addWidget(self.kan_basinci_input)

        self.nabiz_label = QLabel("Nabız:")
        self.nabiz_input = QLineEdit()
        layout.addWidget(self.nabiz_label)
        layout.addWidget(self.nabiz_input)

        self.kan_sekeri_label = QLabel("Kan Şekeri:")
        self.kan_sekeri_input = QLineEdit()
        layout.addWidget(self.kan_sekeri_label)
        layout.addWidget(self.kan_sekeri_input)

        self.saglik_kaydi_ekle_btn = QPushButton("Sağlık Kaydı Ekle")
        self.saglik_kaydi_ekle_btn.clicked.connect(self.saglik_kaydi_ekle)
        layout.addWidget(self.saglik_kaydi_ekle_btn)

        self.egzersiz_baslik = QLabel("Egzersiz Bilgileri")
        layout.addWidget(self.egzersiz_baslik)

        self.egzersiz_ad_label = QLabel("Egzersiz Adı:")
        self.egzersiz_ad_combobox = QComboBox()
        self.egzersiz_ad_combobox.addItems(["Pilates", "Yoga", "Koşu", "Yüzme", "Bisiklet", "Ağırlık Antrenmanı"])  
        layout.addWidget(self.egzersiz_ad_label)
        layout.addWidget(self.egzersiz_ad_combobox)

        self.egzersiz_sure_label = QLabel("Egzersiz Süresi:")
        self.egzersiz_sure_combobox = QComboBox()
        self.egzersiz_sure_combobox.addItems(["5-10 min", "10-15 min", "15-20 min", "20-30 min", "30-45 min", "45-60 min"])  
        layout.addWidget(self.egzersiz_sure_label)
        layout.addWidget(self.egzersiz_sure_combobox)

        self.egzersiz_tekrar_label = QLabel("Egzersiz Tekrarları:")
        self.egzersiz_tekrar_combobox = QComboBox()
        self.egzersiz_tekrar_combobox.addItems(["1 set", "2 set", "3 set", "4 set", "5 set", "6 set"])
        layout.addWidget(self.egzersiz_tekrar_label)
        layout.addWidget(self.egzersiz_tekrar_combobox)

        self.egzersiz_ekle_btn = QPushButton("Egzersiz Ekle")
        self.egzersiz_ekle_btn.clicked.connect(self.egzersiz_ekle)
        layout.addWidget(self.egzersiz_ekle_btn)

        self.rapor_olustur_btn = QPushButton("Rapor Oluştur")
        self.rapor_olustur_btn.clicked.connect(self.rapor_olustur)
        layout.addWidget(self.rapor_olustur_btn)

        self.setLayout(layout)
        self.veritabani_olustur()

    def rapor_olustur(self):
        ad = self.ad_input.text()
        soyad = self.soyad_input.text()
        yas = self.yas_input.text()
        if self.erkek_radio.isChecked():
            cinsiyet = "Erkek"
        elif self.kadin_radio.isChecked():
            cinsiyet = "Kadın"
        kan_basinci = self.kan_basinci_input.text()
        nabiz = self.nabiz_input.text()
        kan_sekeri = self.kan_sekeri_input.text()
        egzersiz_ad = self.egzersiz_ad_combobox.currentText()
        egzersiz_sure = self.egzersiz_sure_combobox.currentText()
        egzersiz_tekrar = self.egzersiz_tekrar_combobox.currentText()

        if ad and soyad and yas and cinsiyet and kan_basinci and nabiz and kan_sekeri and egzersiz_ad and egzersiz_sure and egzersiz_tekrar:
            kullanici = Kullanici(ad, soyad, yas, cinsiyet)
            saglik_kaydi = SaglikKaydi(kan_basinci, nabiz, kan_sekeri)
            egzersiz = Egzersiz(egzersiz_ad, egzersiz_sure, egzersiz_tekrar)
            self.veritabanina_kaydet(kullanici, saglik_kaydi, egzersiz)
            QMessageBox.information(self, "Başarılı", "Rapor oluşturuldu ve kaydedildi.")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun.")

    def kayit_ekle(self):
        ad = self.ad_input.text()
        soyad = self.soyad_input.text()
        yas = self.yas_input.text()
        if self.erkek_radio.isChecked():
            cinsiyet = "Erkek"
        elif self.kadin_radio.isChecked():
            cinsiyet = "Kadın"

        if ad and soyad and yas and cinsiyet:
            QMessageBox.information(self, "Başarılı", "Yeni kayıt eklendi.")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun.")

    def saglik_kaydi_ekle(self):
        kan_basinci = self.kan_basinci_input.text()
        nabiz = self.nabiz_input.text()
        kan_sekeri = self.kan_sekeri_input.text()
        if kan_basinci and nabiz and kan_sekeri:
            QMessageBox.information(self, "Başarılı", "Sağlık kaydı eklendi.")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun.")

    def egzersiz_ekle(self):
        egzersiz_ad = self.egzersiz_ad_combobox.currentText()
        egzersiz_sure = self.egzersiz_sure_combobox.currentText()
        egzersiz_tekrar = self.egzersiz_tekrar_combobox.currentText()
        if egzersiz_ad and egzersiz_sure and egzersiz_tekrar:
            QMessageBox.information(self, "Başarılı", "Egzersiz eklendi.")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun.")

    def veritabani_olustur(self):
        self.conn = sqlite3.connect('saglik_app.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Raporlar (Ad TEXT, Soyad TEXT, Yas INTEGER, Cinsiyet TEXT, KanBasinci TEXT, Nabiz TEXT, 
        KanSekeri TEXT, EgzersizAdi TEXT, EgzersizSuresi TEXT, EgzersizTekrarlari TEXT)''')
        self.conn.commit()

    def veritabanina_kaydet(self, kullanici, saglik_kaydi, egzersiz):
        self.cur.execute('''INSERT INTO Raporlar (Ad, Soyad, Yas, Cinsiyet, KanBasinci, Nabiz, KanSekeri, EgzersizAdi, EgzersizSuresi, EgzersizTekrarlari) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (kullanici.ad, kullanici.soyad, kullanici.yas, kullanici.cinsiyet, saglik_kaydi.kan_basinci, saglik_kaydi.nabiz, saglik_kaydi.kan_sekeri, egzersiz.ad, 
        egzersiz.süre, egzersiz.tekrar))
        self.conn.commit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = SaglikUygulamasi()
    pencere.show()
    sys.exit(app.exec_())
