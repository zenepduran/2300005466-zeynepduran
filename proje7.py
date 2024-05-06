import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTextEdit, QMessageBox, QComboBox

class SporTakipUygulamasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spor Takip Uygulaması")
        self.arayuz_olustur()
        self.veritabani_baglantisi_olustur()

    def arayuz_olustur(self):
        self.duzen = QVBoxLayout()

        # Sporcu
        self.sporcu_label = QLabel("Sporcu Adı:")
        self.sporcu_input = QLineEdit()
        self.duzen.addWidget(self.sporcu_label)
        self.duzen.addWidget(self.sporcu_input)

        self.spor_dali_label = QLabel("Spor Dalı:")
        self.spor_dali_input = QLineEdit()
        self.duzen.addWidget(self.spor_dali_label)
        self.duzen.addWidget(self.spor_dali_input)

        # Adding sports options
        self.spor_dali_label = QLabel("Spor Dalı Seçin:")
        self.spor_dali_combobox = QComboBox()
        self.spor_dali_combobox.addItems(["Futbol", "Voleybol", "Basketbol", "Fitness", "Golf", "Masa Tenisi", "Jimnastik"])
        self.duzen.addWidget(self.spor_dali_label)
        self.duzen.addWidget(self.spor_dali_combobox)

        # Antrenman
        self.antrenman_label = QLabel("Antrenman Adı:")
        self.antrenman_input = QLineEdit()
        self.duzen.addWidget(self.antrenman_label)
        self.duzen.addWidget(self.antrenman_input)

        self.antrenman_detay_label = QLabel("Antrenman Detayları:")
        self.antrenman_detay_input = QTextEdit()
        self.duzen.addWidget(self.antrenman_detay_label)
        self.duzen.addWidget(self.antrenman_detay_input)

        # Takip
        self.antrenman_kaydet_button = QPushButton("Antrenmanı Kaydet")
        self.antrenman_kaydet_button.clicked.connect(self.antrenman_kaydet)
        self.duzen.addWidget(self.antrenman_kaydet_button)

        self.antrenman_listesi_label = QLabel("Antrenman Listesi:")
        self.antrenman_listesi = QListWidget()
        self.duzen.addWidget(self.antrenman_listesi_label)
        self.duzen.addWidget(self.antrenman_listesi)

        self.ilerleme_label = QLabel("İlerleme Kaydı:")
        self.ilerleme_input = QTextEdit()
        self.duzen.addWidget(self.ilerleme_label)
        self.duzen.addWidget(self.ilerleme_input)

        self.ilerleme_kaydet_button = QPushButton("İlerlemeyi Kaydet")
        self.ilerleme_kaydet_button.clicked.connect(self.ilerleme_kaydet)
        self.duzen.addWidget(self.ilerleme_kaydet_button)

        self.setLayout(self.duzen)

    def veritabani_baglantisi_olustur(self):
        self.veritabani_baglantisi = sqlite3.connect('spor_takip.db')
        self.cursor = self.veritabani_baglantisi.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Sporcular
                                (id INTEGER PRIMARY KEY,
                                ad TEXT,
                                spor_dali TEXT)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Antrenmanlar
                                (id INTEGER PRIMARY KEY,
                                sporcu_id INTEGER,
                                antrenman_adi TEXT,
                                antrenman_detay TEXT,
                                FOREIGN KEY(sporcu_id) REFERENCES Sporcular(id))''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Takip
                                (id INTEGER PRIMARY KEY,
                                sporcu_id INTEGER,
                                ilerleme_detayi TEXT,
                                FOREIGN KEY(sporcu_id) REFERENCES Sporcular(id))''')

        self.veritabani_baglantisi.commit()

    def antrenman_kaydet(self):
        sporcu_adi = self.sporcu_input.text().strip()
        spor_dali = self.spor_dali_combobox.currentText()
        antrenman_adi = self.antrenman_input.text().strip()
        antrenman_detay = self.antrenman_detay_input.toPlainText().strip()

        if sporcu_adi and spor_dali and antrenman_adi and antrenman_detay:
            self.cursor.execute("INSERT INTO Sporcular (ad, spor_dali) VALUES (?, ?)", (sporcu_adi, spor_dali))
            sporcu_id = self.cursor.lastrowid
            self.cursor.execute("INSERT INTO Antrenmanlar (sporcu_id, antrenman_adi, antrenman_detay) VALUES (?, ?, ?)", 
                                (sporcu_id, antrenman_adi, antrenman_detay))
            self.veritabani_baglantisi.commit()
            self.antrenman_listesini_yukle()
            QMessageBox.information(self, "Başarılı", "Antrenman başarıyla kaydedildi!")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen sporcu adı, spor dalı, antrenman adı ve detayları girin.")

    def antrenman_listesini_yukle(self):
        self.antrenman_listesi.clear()
        sporcu_adi = self.sporcu_input.text().strip()
        self.cursor.execute("SELECT id FROM Sporcular WHERE ad = ?", (sporcu_adi,))
        sporcu_id = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT antrenman_adi FROM Antrenmanlar WHERE sporcu_id = ?", (sporcu_id,))
        antrenmanlar = self.cursor.fetchall()
        for antrenman in antrenmanlar:
            self.antrenman_listesi.addItem(antrenman[0])

    def ilerleme_kaydet(self):
        sporcu_adi = self.sporcu_input.text().strip()
        ilerleme_detayi = self.ilerleme_input.toPlainText().strip()

        if sporcu_adi and ilerleme_detayi:
            self.cursor.execute("SELECT id FROM Sporcular WHERE ad = ?", (sporcu_adi,))
            sporcu_id = self.cursor.fetchone()[0]
            self.cursor.execute("INSERT INTO Takip (sporcu_id, ilerleme_detayi) VALUES (?, ?)", (sporcu_id, ilerleme_detayi))
            self.veritabani_baglantisi.commit()
            QMessageBox.information(self, "Başarılı", "İlerleme kaydedildi!")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen sporcu adı ve ilerleme detayları girin.")

    def closeEvent(self, event):
        self.veritabani_baglantisi.close()
        event.accept()

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = SporTakipUygulamasi()
    pencere.show()
    sys.exit(uygulama.exec_())
