#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTabWidget, QLabel, QTextEdit, QDialog

class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tarihi Olaylar Veritabanı')
        self.layout = QVBoxLayout()
        self.tab_widget = QTabWidget()
        self.olaylar_listesi = []
        self.sahsiyetler_listesi = []
        self.donemler_listesi = []
        self.initUI()

    def initUI(self):
        self.tab_widget.addTab(OlayEklePenceresi(self), 'Olay Ekle')
        self.tab_widget.addTab(SahsiyetEklePenceresi(self), 'Şahsiyet Ekle')
        self.tab_widget.addTab(DonemEklePenceresi(self), 'Dönem Ekle')

        self.layout.addWidget(self.tab_widget)

        # Kayıtları görüntüle düğmesi
        self.goruntule_button = QPushButton('Kayıtları Görüntüle')
        self.goruntule_button.clicked.connect(self.kayitlari_goruntule)
        self.layout.addWidget(self.goruntule_button)

        self.setLayout(self.layout)

    def olay_bilgileri_ekle(self, olay_bilgileri):
        self.olaylar_listesi.append(olay_bilgileri)

    def sahsiyet_bilgileri_ekle(self, sahsiyet_bilgileri):
        self.sahsiyetler_listesi.append(sahsiyet_bilgileri)

    def donem_bilgileri_ekle(self, donem_bilgileri):
        self.donemler_listesi.append(donem_bilgileri)

    def kayitlari_goruntule(self):
        # Kayıtları görüntüleme penceresini oluştur
        goruntule_penceresi = GoruntulePenceresi(self.olaylar_listesi, self.sahsiyetler_listesi, self.donemler_listesi)
        goruntule_penceresi.exec_()  # exec_ kullanarak pencereyi modal olarak göster

class OlayEklePenceresi(QWidget):
    def __init__(self, ana_pencere):
        super().__init__()
        self.ana_pencere = ana_pencere
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Widgetler oluşturuluyor
        self.adi_label = QLabel('Olay Adı:')
        self.adi_edit = QTextEdit()

        self.tarih_label = QLabel('Tarihi:')
        self.tarih_edit = QTextEdit()

        self.aciklama_label = QLabel('Açıklama:')
        self.aciklama_edit = QTextEdit()

        self.layout.addWidget(self.adi_label)
        self.layout.addWidget(self.adi_edit)
        self.layout.addWidget(self.tarih_label)
        self.layout.addWidget(self.tarih_edit)
        self.layout.addWidget(self.aciklama_label)
        self.layout.addWidget(self.aciklama_edit)

        self.save_button = QPushButton('Kaydet')
        self.save_button.clicked.connect(self.kaydet)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)

    def kaydet(self):
        # Girdiler alınıyor
        olay_bilgileri = {
            'Olay Adı': self.adi_edit.toPlainText(),
            'Tarihi': self.tarih_edit.toPlainText(),
            'Açıklama': self.aciklama_edit.toPlainText()
        }

        # Ana pencereye bilgileri iletiliyor
        self.ana_pencere.olay_bilgileri_ekle(olay_bilgileri)
        self.clear_inputs()

    def clear_inputs(self):
        # Girdi kutuları temizleniyor
        self.adi_edit.clear()
        self.tarih_edit.clear()
        self.aciklama_edit.clear()

class SahsiyetEklePenceresi(QWidget):
    def __init__(self, ana_pencere):
        super().__init__()
        self.ana_pencere = ana_pencere
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.adi_label = QLabel('Şahsiyet Adı:')
        self.adi_edit = QTextEdit()

        self.dogum_label = QLabel('Doğum Tarihi:')
        self.dogum_edit = QTextEdit()

        self.olum_label = QLabel('Ölüm Tarihi:')
        self.olum_edit = QTextEdit()

        self.layout.addWidget(self.adi_label)
        self.layout.addWidget(self.adi_edit)
        self.layout.addWidget(self.dogum_label)
        self.layout.addWidget(self.dogum_edit)
        self.layout.addWidget(self.olum_label)
        self.layout.addWidget(self.olum_edit)

        self.save_button = QPushButton('Kaydet')
        self.save_button.clicked.connect(self.kaydet)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)

    def kaydet(self):
        # Girdiler alınıyor
        sahsiyet_bilgileri = {
            'Şahsiyet Adı': self.adi_edit.toPlainText(),
            'Doğum Tarihi': self.dogum_edit.toPlainText(),
            'Ölüm Tarihi': self.olum_edit.toPlainText(),
        }

        # Ana pencereye bilgileri iletiliyor
        self.ana_pencere.sahsiyet_bilgileri_ekle(sahsiyet_bilgileri)
        self.clear_inputs()

    def clear_inputs(self):
        # Girdi kutuları temizleniyor
        self.adi_edit.clear()
        self.dogum_edit.clear()
        self.olum_edit.clear()

class DonemEklePenceresi(QWidget):
    def __init__(self, ana_pencere):
        super().__init__()
        self.ana_pencere = ana_pencere
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.adi_label = QLabel('Dönem Adı:')
        self.adi_edit = QTextEdit()

        self.baslangic_label = QLabel('Başlangıç Tarihi:')
        self.baslangic_edit = QTextEdit()

        self.bitis_label = QLabel('Bitiş Tarihi:')
        self.bitis_edit = QTextEdit()

        self.layout.addWidget(self.adi_label)
        self.layout.addWidget(self.adi_edit)
        self.layout.addWidget(self.baslangic_label)
        self.layout.addWidget(self.baslangic_edit)
        self.layout.addWidget(self.bitis_label)
        self.layout.addWidget(self.bitis_edit)

        self.save_button = QPushButton('Kaydet')
        self.save_button.clicked.connect(self.kaydet)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)

    def kaydet(self):
        # Girdiler alınıyor
        donem_bilgileri = {
            'Dönem Adı': self.adi_edit.toPlainText(),
            'Başlangıç Tarihi': self.baslangic_edit.toPlainText(),
            'Bitiş Tarihi': self.bitis_edit.toPlainText(),
        }

        # Ana pencereye bilgileri iletiliyor
        self.ana_pencere.donem_bilgileri_ekle(donem_bilgileri)
        self.clear_inputs()

    def clear_inputs(self):
        # Girdi kutuları temizleniyor
        self.adi_edit.clear()
        self.baslangic_edit.clear()
        self.bitis_edit.clear()

class GoruntulePenceresi(QDialog):
    def __init__(self, olaylar_listesi, sahsiyetler_listesi, donemler_listesi):
        super().__init__()
        self.setWindowTitle('Kayıtlar')
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.create_table("Olaylar", olaylar_listesi))
        self.layout.addWidget(self.create_table("Şahsiyetler", sahsiyetler_listesi))
        self.layout.addWidget(self.create_table("Dönemler", donemler_listesi))

        self.setLayout(self.layout)

    def create_table(self, title, kayitlar_listesi):
        widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel(title)
        layout.addWidget(label)

        for kayit in kayitlar_listesi:
            kayit_text = ', '.join(f"{key}: {value}" for key, value in kayit.items())
            row_label = QLabel(kayit_text)
            layout.addWidget(row_label)

        widget.setLayout(layout)
        return widget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ana_pencere = AnaPencere()
    ana_pencere.show()
    sys.exit(app.exec_())


# In[ ]:




