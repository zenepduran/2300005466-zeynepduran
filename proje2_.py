class Doktor:
    def __init__(self, isim, uzmanlik_alani):
        self.isim = isim
        self.uzmanlik_alani = uzmanlik_alani
        self.musaitlik_durumu = True  # Başlangıçta doktor müsait kabul edilir

    def musait_mi(self):
        return self.musaitlik_durumu

    def randevu_ayarla(self):
        self.musaitlik_durumu = False

    def randevu_iptal(self):
        self.musaitlik_durumu = True


class Hasta:
    def __init__(self, tc, ad_soyad, dogum_tarihi, sigorta_durumu, sigorta_numarasi=None):
        self.tc = tc
        self.ad_soyad = ad_soyad
        self.dogum_tarihi = dogum_tarihi
        self.sigorta_durumu = sigorta_durumu
        self.sigorta_numarasi = sigorta_numarasi
        self.randevu_gecmisi = []

    def randevu_ekle(self, randevu):
        self.randevu_gecmisi.append(randevu)


class Randevu:
    def __init__(self, tarih, doktor, hasta):
        self.tarih = tarih
        self.doktor = doktor
        self.hasta = hasta


def randevu_al(doktorlar, hasta):
    musait_doktorlar = [doktor for doktor in doktorlar if doktor.musait_mi()]
    if not musait_doktorlar:
        print("Şu anda müsait doktor bulunmamaktadır.")
        return

    print("Müsait doktorlar:")
    for idx, doktor in enumerate(musait_doktorlar):
        print(f"{idx + 1}. {doktor.isim} - {doktor.uzmanlik_alani}")

    try:
        secim = int(input("Randevu almak istediğiniz doktorun numarasını girin: ")) - 1
        if 0 <= secim < len(musait_doktorlar):
            tarih = input("Randevu tarihi girin (GG/AA/YYYY): ")
            yeni_randevu = Randevu(tarih, musait_doktorlar[secim], hasta)
            musait_doktorlar[secim].randevu_ayarla()
            hasta.randevu_ekle(yeni_randevu)
            print(f"Randevunuz {tarih} tarihine alındı.")
        else:
            print("Geçersiz seçim.")
    except ValueError:
        print("Lütfen geçerli bir numara girin.")


def randevu_iptal(hasta):
    if not hasta.randevu_gecmisi:
        print("Hiç randevunuz bulunmamaktadır.")
        return

    for idx, randevu in enumerate(hasta.randevu_gecmisi):
        print(f"{idx + 1}. {randevu.tarih} - {randevu.doktor.isim}")

    try:
        secim = int(input("İptal etmek istediğiniz randevunun numarasını girin: ")) - 1
        if 0 <= secim < len(hasta.randevu_gecmisi):
            iptal_edilen = hasta.randevu_gecmisi.pop(secim)
            iptal_edilen.doktor.randevu_iptal()
            print("Randevunuz iptal edildi.")
        else:
            print("Geçersiz seçim.")
    except ValueError:
        print("Lütfen geçerli bir numara girin.")

# Örnek kullanım:
doktorlar = [Doktor("Ahmet Yılmaz", "Kardiyoloji"), Doktor("Elif Kaya", "Nöroloji")]
hasta = Hasta("12345678901", "Ayşe Demir", "01/01/1980", True, "1234")

randevu_al(doktorlar, hasta)
randevu_iptal(hasta)


#arayüz proje 2 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QLineEdit

class Doktor:
    def _init_(self, isim, uzmanlik_alani):
        self.isim = isim
        self.uzmanlik_alani = uzmanlik_alani
        self.randevular = []

    def randevu_ayarla(self):
        print(f"{self.isim} için yeni bir randevu ayarlandı.")

    def randevu_iptal(self):
        print(f"{self.isim} için bir randevu iptal edildi.")

class Hasta:
    def _init_(self, adi, soyadi, dogum_tarihi, telefon_numarasi, sigorta_numarasi):
        self.adi = adi
        self.soyadi = soyadi
        self.dogum_tarihi = dogum_tarihi
        self.telefon_numarasi = telefon_numarasi
        self.sigorta_numarasi = sigorta_numarasi
        self.randevu_gecmisi = []

    def randevu_ekle(self, randevu):
        self.randevu_gecmisi.append(randevu)
        print(f"{self.adi} {self.soyadi} için yeni bir randevu eklendi: {randevu.tarih}")

class Randevu:
    def _init_(self, tarih, doktor, hasta):
        self.tarih = tarih
        self.doktor = doktor
        self.hasta = hasta

class RandevuSistemi(QWidget):
    def _init_(self):
        super()._init_()
        self.doktorlar = [Doktor("Ahmet Yılmaz", "Kardiyoloji"), Doktor("Elif Kaya", "Nöroloji")]
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Hasta bilgileri
        self.adiLabel = QLabel("Adı:")
        self.layout.addWidget(self.adiLabel)

        self.adiLineEdit = QLineEdit()
        self.layout.addWidget(self.adiLineEdit)

        self.soyadiLabel = QLabel("Soyadı:")
        self.layout.addWidget(self.soyadiLabel)

        self.soyadiLineEdit = QLineEdit()
        self.layout.addWidget(self.soyadiLineEdit)

        self.dogumTarihiLabel = QLabel("Doğum Tarihi (GG/AA/YYYY):")
        self.layout.addWidget(self.dogumTarihiLabel)

        self.dogumTarihiLineEdit = QLineEdit()
        self.layout.addWidget(self.dogumTarihiLineEdit)
        
        self.telefonNumarasiLabel = QLabel("Telefon Numarası:")
        self.layout.addWidget(self.telefonNumarasiLabel)

        self.telefonNumarasiLineEdit = QLineEdit()
        self.layout.addWidget(self.telefonNumarasiLineEdit)

        self.sigortaNumarasiLabel = QLabel("Sigorta Numarası:")
        self.layout.addWidget(self.sigortaNumarasiLabel)

        self.sigortaNumarasiLineEdit = QLineEdit()
        self.layout.addWidget(self.sigortaNumarasiLineEdit)

        # Doktor seçimi
        self.doktorSecimLabel = QLabel("Doktor Seçiniz:")
        self.layout.addWidget(self.doktorSecimLabel)

        self.doktorSecimComboBox = QComboBox()
        for doktor in self.doktorlar:
            self.doktorSecimComboBox.addItem(doktor.isim + " - " + doktor.uzmanlik_alani)
        self.layout.addWidget(self.doktorSecimComboBox)

        # Randevu tarihi
        self.tarihLabel = QLabel("Randevu Tarihi (GG/AA/YYYY):")
        self.layout.addWidget(self.tarihLabel)

        self.tarihLineEdit = QLineEdit()
        self.layout.addWidget(self.tarihLineEdit)

        # Randevu butonları
        self.randevuAlButton = QPushButton("Randevu Al")
        self.randevuAlButton.clicked.connect(self.randevuAl)
        self.layout.addWidget(self.randevuAlButton)

        # Randevu iptal butonu işlevselliği için ekstra bir fonksiyon yazılmalıdır.
        
        #self.randevuIptalButton.clicked.connect(self.randevuIptal)
        
        #self.layout.addWidget(self.randevuIptalButton)

        self.setLayout(self.layout)
        self.setWindowTitle('Randevu Sistemi')
        self.show()

    def randevuAl(self):
        adi = self.adiLineEdit.text()
        soyadi = self.soyadiLineEdit.text()
        dogum_tarihi = self.dogumTarihiLineEdit.text()
        telefon_numarasi = self.telefonNumarasiLineEdit.text()
        # Create Randevu object
        randevu = Randevu(self.tarihLineEdit.text(), None, None)
        # Create Hasta object
        hasta = Hasta(adi, soyadi, dogum_tarihi, telefon_numarasi, None)
        hasta.randevu_ekle(randevu)

if _name_ == '_main_':
    app = QApplication(sys.argv)
    ex = RandevuSistemi()
    sys.exit(app.exec_())

