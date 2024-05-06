class Etkinlik:
    def __init__(self, adi, tarihi, yerleskeni, saati, fiyati):
        self.adi = adi
        self.tarihi = tarihi
        self.yerleskeni = yerleskeni
        self.saati = saati
        self.fiyati = fiyati

class Katilimci:
    def __init__(self, adi, soyadi, dogum_tarihi):
        self.adi = adi
        self.soyadi = soyadi
        self.dogum_tarihi = dogum_tarihi

class Bilet:
    def __init__(self, etkinlik, katilimci):
        self.etkinlik = etkinlik
        self.katilimci = katilimci
    
    def satin_al(self, kredi_karti_bilgileri):
        # Burada gerçek bir ödeme işlemi yapılacak.
        # Güvenlik nedeniyle bu adımı basitleştiriyoruz.
        print(f"{self.katilimci.adi} adına {self.etkinlik.adi} etkinliğine bilet satın alındı.")
class EtkinlikSistemi:
    def __init__(self):
        self.etkinlikler = []
        self.katilimcilar = []
    
    def etkinlik_ekle(self, etkinlik):
        self.etkinlikler.append(etkinlik)
    
    def katilimci_ekle(self, katilimci):
        self.katilimcilar.append(katilimci)
    
    def bilet_satin_al(self, etkinlik_adi, katilimci_adi, kredi_karti_bilgileri):
        etkinlik = next((e for e in self.etkinlikler if e.adi == etkinlik_adi), None)
        katilimci = next((k for k in self.katilimcilar if k.adi == katilimci_adi), None)
        
        if etkinlik and katilimci:
            bilet = Bilet(etkinlik, katilimci)
            bilet.satin_al(kredi_karti_bilgileri)
        else:
            print("Etkinlik veya Katılımcı bulunamadı.")
# Sistem oluşturma
sistem = EtkinlikSistemi()

# Etkinlikleri Ekleme
sistem.etkinlik_ekle(Etkinlik("Konser", "2023-06-15", "Stadyum", "20:00", 150))
sistem.etkinlik_ekle(Etkinlik("Tiyatro", "2023-06-20", "Kültür Merkezi", "19:00", 100))

# Katılımcıları Ekleme
sistem.katilimci_ekle(Katilimci("Ali", "Veli", "1990-01-01"))
sistem.katilimci_ekle(Katilimci("Ayşe", "Yılmaz", "1985-05-05"))

# Bilet Satın Alma
sistem.bilet_satin_al("Konser", "Ali", {"kart_numarasi": "1234-5678-9012-3456", "son_kullanma_tarihi": "06/25", "cvv": "123"})



#proje 4 arayüz


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QFormLayout, QMessageBox, QComboBox, QRadioButton

class EtkinlikSistemiGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Etkinlik Sistemi')
        self.setGeometry(100, 100, 280, 220)
        
        # Form Layout Oluştur
        layout = QFormLayout()
        
        # Kullanıcı Giriş Alanları
        self.etkinlikAdiInput = QLineEdit(self)
        self.etkinlikTurleri = QComboBox(self)
        self.etkinlikTurleri.addItems(['Spor', 'Müzik', 'Tiyatro'])
        
        self.katilimciAdiInput = QLineEdit(self)
        self.krediKartiBilgileriInput = QLineEdit(self)
        
        # Cinsiyet Seçimi
        self.cinsiyetSecimi = QRadioButton('Erkek', self)
        self.cinsiyetSecimi.setChecked(True)
        self.cinsiyetSecimi2 = QRadioButton('Kadın', self)
        
        # Giriş alanlarını layout'a ekle
        layout.addRow('Etkinlik Adı:', self.etkinlikAdiInput)
        layout.addRow('Etkinlik Türü:', self.etkinlikTurleri)
        layout.addRow('Katılımcı Adı:', self.katilimciAdiInput)
        layout.addRow('Kredi Kartı Bilgileri:', self.krediKartiBilgileriInput)
        layout.addRow('Cinsiyet:', self.cinsiyetSecimi)
        layout.addRow('', self.cinsiyetSecimi2)
        
        # Bilet Satın Al Butonu
        self.biletSatinAlBtn = QPushButton('Bilet Satın Al', self)
        self.biletSatinAlBtn.clicked.connect(self.biletSatinAl)
        
        layout.addWidget(self.biletSatinAlBtn)
        
        self.setLayout(layout)
    
    def biletSatinAl(self):
        etkinlikAdi = self.etkinlikAdiInput.text()
        secilenEtkinlikTuru = self.etkinlikTurleri.currentText()
        katilimciAdi = self.katilimciAdiInput.text()
        krediKartiBilgileri = self.krediKartiBilgileriInput.text()
        cinsiyet = 'Erkek' if self.cinsiyetSecimi.isChecked() else 'Kadın'
        
        # Basitçe bilgileri bir mesaj kutusunda göster
        QMessageBox.information(self, 'Bilet Satın Alındı', f"Etkinlik Adı: {etkinlikAdi}\nEtkinlik Türü: {secilenEtkinlikTuru}\nKatılımcı: {katilimciAdi}\nKredi Kartı Bilgileri: {krediKartiBilgileri}\nCinsiyet: {cinsiyet}", QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EtkinlikSistemiGUI()
    ex.show()
    sys.exit(app.exec_())

#2 arayü  

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QFormLayout, QMessageBox, QComboBox, QRadioButton, QLabel
 
class EtkinlikSistemiGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Etkinlik Sistemi')
        self.setGeometry(100, 100, 280, 320)
        
        # Form Layout Oluştur
        layout = QFormLayout()
        
        # Kullanıcı Giriş Alanları
        self.etkinlikAdiInput = QLineEdit(self)
        self.etkinlikTurleri = QComboBox(self)
        self.etkinlikTurleri.addItems(['Spor', 'Müzik', 'Tiyatro'])
        
        self.katilimciAdiInput = QLineEdit(self)
        self.krediKartiBilgileriInput = QLineEdit(self)
        
        self.etkinlikTarihiInput = QLineEdit(self)
        self.etkinlikSaatiInput = QLineEdit(self)
        self.katilimUcretiInput = QLineEdit(self)
        self.etkinlikYeriInput = QLineEdit(self)
        
        # Cinsiyet Seçimi
        self.cinsiyetSecimi = QRadioButton('Erkek', self)
        self.cinsiyetSecimi.setChecked(True)
        self.cinsiyetSecimi2 = QRadioButton('Kadın', self)
        
        # Giriş alanlarını layout'a ekle
        layout.addRow('Etkinlik Adı:', self.etkinlikAdiInput)
        layout.addRow('Etkinlik Türü:', self.etkinlikTurleri)
        layout.addRow('Katılımcı Adı:', self.katilimciAdiInput)
        layout.addRow('Kredi Kartı Bilgileri:', self.krediKartiBilgileriInput)
        
        layout.addRow('Etkinlik Tarihi:', self.etkinlikTarihiInput)
        layout.addRow('Etkinlik Saati:', self.etkinlikSaatiInput)
        layout.addRow('Katılım Ücreti:', self.katilimUcretiInput)
        layout.addRow('Etkinlik Yeri:', self.etkinlikYeriInput)
        
        layout.addRow('Cinsiyet:', self.cinsiyetSecimi)
        layout.addRow('', self.cinsiyetSecimi2)
        
        # Bilet Satın Al Butonu
        self.biletSatinAlBtn = QPushButton('Bilet Satın Al', self)
        self.biletSatinAlBtn.clicked.connect(self.biletSatinAl)
        
        layout.addWidget(self.biletSatinAlBtn)
        
        self.setLayout(layout)
    
    def biletSatinAl(self):
        etkinlikAdi = self.etkinlikAdiInput.text()
        secilenEtkinlikTuru = self.etkinlikTurleri.currentText()
        katilimciAdi = self.katilimciAdiInput.text()
        krediKartiBilgileri = self.krediKartiBilgileriInput.text()
        
        etkinlikTarihi = self.etkinlikTarihiInput.text()
        etkinlikSaati = self.etkinlikSaatiInput.text()
        katilimUcreti = self.katilimUcretiInput.text()
        etkinlikYeri = self.etkinlikYeriInput.text()
        
        cinsiyet = 'Erkek' if self.cinsiyetSecimi.isChecked() else 'Kadın'
        
        # Basitçe bilgileri bir mesaj kutusunda göster
        QMessageBox.information(self, 'Bilet Satın Alındı', f"Etkinlik Adı: {etkinlikAdi}\nEtkinlik Türü: {secilenEtkinlikTuru}\nKatılımcı: {katilimciAdi}\nKredi Kartı Bilgileri: {krediKartiBilgileri}\nEtkinlik Tarihi: {etkinlikTarihi}\nEtkinlik Saati: {etkinlikSaati}\nKatılım Ücreti: {katilimUcreti}\nEtkinlik Yeri: {etkinlikYeri}\nCinsiyet: {cinsiyet}", QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EtkinlikSistemiGUI()
    ex.show()
    sys.exit(app.exec_())
