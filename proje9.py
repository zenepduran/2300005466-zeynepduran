import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTextEdit, QMessageBox, QComboBox

class SeyahatPlanlama(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seyahat Planlama Uygulaması")
        self.arayuz_olustur()
        self.veritabani_baglantisi_olustur()

    def arayuz_olustur(self):
        self.duzen = QVBoxLayout()

        # Travel (Seyahat) Section
        self.seyahat_rota_label = QLabel("Seyahat Rotası:")
        self.seyahat_rota_combobox = QComboBox()
        self.seyahat_rota_combobox.addItems(["İstanbul - Ankara", "İzmir - Antalya", "Bodrum - Kapadokya", "Bursa - Trabzon", "Eskişehir - Diyarbakır"])
        self.duzen.addWidget(self.seyahat_rota_label)
        self.duzen.addWidget(self.seyahat_rota_combobox)

        # Accommodation (Konaklama) Section
        self.konaklama_label = QLabel("Konaklama Tesis Adı:")
        self.konaklama_input = QLineEdit()
        self.duzen.addWidget(self.konaklama_label)
        self.duzen.addWidget(self.konaklama_input)

        self.fiyat_label = QLabel("Fiyat:")
        self.fiyat_input = QLineEdit()
        self.duzen.addWidget(self.fiyat_label)
        self.duzen.addWidget(self.fiyat_input)

        self.konaklama_sec_button = QPushButton("Konaklama Seç")
        self.konaklama_sec_button.clicked.connect(self.konaklama_sec)
        self.duzen.addWidget(self.konaklama_sec_button)

        # Route (Rota) Section
        self.rota_detay_label = QLabel("Seyahat Rota Detayları:")
        self.rota_detay_input = QTextEdit()
        self.duzen.addWidget(self.rota_detay_label)
        self.duzen.addWidget(self.rota_detay_input)

        self.rota_ekle_button = QPushButton("Rota Ekle")
        self.rota_ekle_button.clicked.connect(self.rota_ekle)
        self.duzen.addWidget(self.rota_ekle_button)

        # Plan List Section
        self.plan_listesi_label = QLabel("Seyahat Planı:")
        self.plan_listesi = QListWidget()
        self.duzen.addWidget(self.plan_listesi_label)
        self.duzen.addWidget(self.plan_listesi)

        self.setLayout(self.duzen)

    def veritabani_baglantisi_olustur(self):
        self.veritabani_baglantisi = sqlite3.connect('seyahat_planlama.db')
        self.cursor = self.veritabani_baglantisi.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Rotalar
                                (id INTEGER PRIMARY KEY,
                                rota TEXT,
                                konaklama TEXT,
                                fiyat INTEGER)''')

        self.veritabani_baglantisi.commit()

    def rota_ekle(self):
        rota = self.seyahat_rota_combobox.currentText()
        konaklama = self.konaklama_input.text().strip()
        fiyat = self.fiyat_input.text().strip()
        rota_detay = self.rota_detay_input.toPlainText().strip()

        if rota and konaklama and fiyat and rota_detay:
            self.cursor.execute("INSERT INTO Rotalar (rota, konaklama, fiyat) VALUES (?, ?, ?)", (rota, konaklama, fiyat))
            self.veritabani_baglantisi.commit()
            self.plan_listesini_yukle()
            QMessageBox.information(self, "Başarılı", "Rota başarıyla eklendi!")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen rota, konaklama, fiyat ve rota detay bilgilerini girin.")

    def konaklama_sec(self):
        selected_item = self.plan_listesi.currentItem()
        if selected_item:
            konaklama_bilgisi = selected_item.text().split(' - ')[1]
            self.konaklama_input.setText(konaklama_bilgisi)
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir konaklama seçeneği seçin.")

    def plan_listesini_yukle(self):
        self.plan_listesi.clear()
        self.cursor.execute("SELECT rota, konaklama, fiyat FROM Rotalar")
        rotalar = self.cursor.fetchall()
        for rota in rotalar:
            self.plan_listesi.addItem(f"Rota: {rota[0]} - Konaklama: {rota[1]} - Fiyat: {rota[2]}")

    def closeEvent(self, event):
        self.veritabani_baglantisi.close()
        event.accept()

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = SeyahatPlanlama()
    pencere.show()
    sys.exit(uygulama.exec_())

