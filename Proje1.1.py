from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QComboBox, QLineEdit

class Arac:
    def __init__(self, id, model, yil, km, durum):
        self.id = id
        self.model = model
        self.yil = yil
        self.km = km
        self.durum = durum

    def __str__(self):
        return f"{self.model} ({self.yil}) - {self.durum}"

# Araç verileri
arac_listesi = [
    Arac(1, "Toyota Corolla", 2019, 25000, "Müsait"),
    Arac(2, "Honda Civic", 2020, 30000, "Müsait"),
    Arac(3, "Ford Focus", 2018, 20000, "Kiralandı"),
    Arac(4, "Volkswagen Golf", 2017, 18000, "Müsait"),
    Arac(5, "Renault Megane", 2019, 22000, "Kiralandı")
]

app = QApplication([])

window = QWidget()
window.setWindowTitle("Araç Kiralama Sistemi")

label_adi = QLabel("Adınız:")
input_adi = QLineEdit()

label_soyadi = QLabel("Soyadınız:")
input_soyadi = QLineEdit()

label_telefon = QLabel("Telefon Numaranız:")
input_telefon = QLineEdit()

label_kredi_kart = QLabel("Kredi Kartı Bilgileriniz:")
input_kredi_kart = QLineEdit()

label_arac_sec = QLabel("Araç Seçimi:")
combo_arac_sec = QComboBox()
# Araç listesini combobox'a ekleyin
for arac in arac_listesi:
    if arac.durum == "Müsait":
        combo_arac_sec.addItem(str(arac), arac)

button_kiralama_yap = QPushButton("Kiralama Yap")
button_kiralama_iptal_et = QPushButton("Kiralama İptal Et")

layout = QVBoxLayout()
layout.addWidget(label_adi)
layout.addWidget(input_adi)
layout.addWidget(label_soyadi)
layout.addWidget(input_soyadi)
layout.addWidget(label_telefon)
layout.addWidget(input_telefon)
layout.addWidget(label_kredi_kart)
layout.addWidget(input_kredi_kart)
layout.addWidget(label_arac_sec)
layout.addWidget(combo_arac_sec)
layout.addWidget(button_kiralama_yap)
layout.addWidget(button_kiralama_iptal_et)

window.setLayout(layout)

# Fonksiyonlar ve Sinyal-Slot bağlantıları burada tanımlanabilir.
# Örneğin:
# def kiralamaYap():
#     secili_arac = combo_arac_sec.currentData()
#     # Kiralama işlemleri burada gerçekleştirilebilir.
# 
# button_kiralama_yap.clicked.connect(kiralamaYap)

window.show()

app.exec_()

