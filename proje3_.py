class Kitap:
    def __init__(self, kitap_id, ad, yazar, yil, kategori):
        self.kitap_id = kitap_id
        self.ad = ad
        self.yazar = yazar
        self.yil = yil
        self.kategori = kategori
        self.durum = 'Mevcut'  # Başlangıç durumu

    def durum_guncelle(self, yeni_durum):
        self.durum = yeni_durum
        print(f"{self.ad} kitabının durumu '{yeni_durum}' olarak güncellendi.")

class Uye:
    uye_listesi = {}  # Tüm üyeleri tutan sınıf değişkeni

    def __init__(self, uye_id, ad, soyad, uye_oldugu_yil):
        self.uye_id = uye_id
        self.ad = ad
        self.soyad = soyad
        self.uye_oldugu_yil = uye_oldugu_yil
        self.once_alinan_kitaplar = []
        Uye.uye_listesi[uye_id] = self  # Üye oluşturulduğunda listeye eklenir

    def kitap_ekle(self, kitap):
        self.once_alinan_kitaplar.append(kitap)
        print(f"{kitap.ad}, {self.ad} {self.soyad} tarafından daha önce ödünç alındı.")
    
    @classmethod
    def uye_bilgisi_getir(cls, uye_id):
        uye = cls.uye_listesi.get(uye_id, None)
        if uye:
            print(f"Üye ID: {uye.uye_id}, Ad: {uye.ad}, Soyad: {uye.soyad}, Üyelik Yılı: {uye.uye_oldugu_yil}")
            for kitap in uye.once_alinan_kitaplar:
                print(f"Ödünç Alınan Kitap: {kitap.ad}")
        else:
            print("Bu ID'ye sahip bir üye bulunamadı. Lütfen üye olunuz.")

class Odunc:
    def __init__(self):
        self.odunc_listesi = []

    def odunc_al(self, uye, kitap):
        if kitap.durum == 'Mevcut':
            kitap.durum_guncelle('Ödünç Alındı')
            uye.kitap_ekle(kitap)
            self.odunc_listesi.append((uye, kitap))
            print(f"{kitap.ad} kitabı {uye.ad} {uye.soyad} tarafından ödünç alındı.")
        else:
            print(f"{kitap.ad} kitabı şu anda mevcut değil.")

    def iade_et(self, uye, kitap):
        if (uye, kitap) in self.odunc_listesi:
            kitap.durum_guncelle('Mevcut')
            self.odunc_listesi.remove((uye, kitap))
            print(f"{kitap.ad} kitabı {uye.ad} {uye.soyad} tarafından iade edildi.")
        else:
            print("Bu ödünç kaydı bulunamadı.")

    def odunc_bilgisi(self):
        for uye, kitap in self.odunc_listesi:
            print(f"{uye.ad} {uye.soyad}, {kitap.ad} ({kitap.yazar}) kitabını ödünç aldı.")

#Arayüz proje 3 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox

class LibraryGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Kütüphane Yönetim Sistemi')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.uyeIdInput = QLineEdit(self)
        self.uyeIdInput.setPlaceholderText('Üye ID')
        layout.addWidget(self.uyeIdInput)

        self.uyeAdiInput = QLineEdit(self)
        self.uyeAdiInput.setPlaceholderText('Üye Adı')
        layout.addWidget(self.uyeAdiInput)

        self.uyeSoyadiInput = QLineEdit(self)
        self.uyeSoyadiInput.setPlaceholderText('Üye Soyadı')
        layout.addWidget(self.uyeSoyadiInput)

        self.kitapIdInput = QLineEdit(self)
        self.kitapIdInput.setPlaceholderText('Kitap ID')
        layout.addWidget(self.kitapIdInput)

        self.kitapAdiInput = QLineEdit(self)
        self.kitapAdiInput.setPlaceholderText('Kitap Adı')
        layout.addWidget(self.kitapAdiInput)

        uyeEkleBtn = QPushButton('Üye Ekle', self)
        uyeEkleBtn.clicked.connect(self.uyeEkle)
        layout.addWidget(uyeEkleBtn)

        kitapEkleBtn = QPushButton('Kitap Ekle', self)
        kitapEkleBtn.clicked.connect(self.kitapEkle)
        layout.addWidget(kitapEkleBtn)

        oduncAlBtn = QPushButton('Ödünç Al', self)
        oduncAlBtn.clicked.connect(self.oduncAl)
        layout.addWidget(oduncAlBtn)

        iadeEtBtn = QPushButton('Kitabı İade Et', self)
        iadeEtBtn.clicked.connect(self.iadeEt)
        layout.addWidget(iadeEtBtn)

        self.setLayout(layout)

    def uyeEkle(self):
        # Buraya üye ekleme işlevi kodları gelecek
        QMessageBox.information(self, 'Bilgi', 'Üye Eklendi')

    def kitapEkle(self):
        # Buraya kitap ekleme işlevi kodları gelecek
        QMessageBox.information(self, 'Bilgi', 'Kitap Eklendi')

    def oduncAl(self):
        # Buraya ödünç alma işlevi kodları gelecek
        QMessageBox.information(self, 'Bilgi', 'Kitap Ödünç Alındı')

    def iadeEt(self):
        # Buraya kitap iade işlevi kodları gelecek
        QMessageBox.information(self, 'Bilgi', 'Kitap İade Edildi')

def main():
    app = QApplication(sys.argv)
    ex = LibraryGUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
