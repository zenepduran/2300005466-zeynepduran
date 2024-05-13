#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QListWidget, QListWidgetItem, QMessageBox
from PyQt5.QtCore import Qt

class RestaurantCustomerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Restoran Sipariş Uygulaması")

        # Restoran Arayüzü
        self.restaurant_widget = QWidget()
        self.restaurant_layout = QVBoxLayout()

        self.product_name_label = QLabel("Ürün Adı:")
        self.product_name_edit = QLineEdit()
        self.stock_label = QLabel("Stok Miktarı:")
        self.stock_edit = QLineEdit()
        self.price_label = QLabel("Fiyatı:")
        self.price_edit = QLineEdit()

        self.save_button = QPushButton("Ürünü Kaydet")
        self.save_button.clicked.connect(self.save_product)

        self.restaurant_layout.addWidget(self.product_name_label)
        self.restaurant_layout.addWidget(self.product_name_edit)
        self.restaurant_layout.addWidget(self.stock_label)
        self.restaurant_layout.addWidget(self.stock_edit)
        self.restaurant_layout.addWidget(self.price_label)
        self.restaurant_layout.addWidget(self.price_edit)
        self.restaurant_layout.addWidget(self.save_button)

        self.restaurant_widget.setLayout(self.restaurant_layout)

        # Müşteri Arayüzü
        self.customer_widget = QWidget()
        self.customer_layout = QVBoxLayout()

        self.product_list_label = QLabel("Ürün Adı - Fiyatı:")
        self.product_list = QListWidget()
        self.customer_layout.addWidget(self.product_list_label)
        self.customer_layout.addWidget(self.product_list)

        self.name_label = QLabel("İsim:")
        self.name_edit = QLineEdit()
        self.address_label = QLabel("Adres:")
        self.address_edit = QLineEdit()

        self.customer_layout.addWidget(self.name_label)
        self.customer_layout.addWidget(self.name_edit)
        self.customer_layout.addWidget(self.address_label)
        self.customer_layout.addWidget(self.address_edit)

        self.order_button = QPushButton("Sipariş Ver")
        self.order_button.clicked.connect(self.show_order_details)

        self.customer_layout.addWidget(self.order_button)

        self.customer_widget.setLayout(self.customer_layout)

        # Ana Layout
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.restaurant_widget)
        self.main_layout.addWidget(self.customer_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)

        self.setCentralWidget(self.central_widget)

        # Sipariş Detayları Penceresi
        self.order_details_window = OrderDetailsWindow()

    def save_product(self):
        product_name = self.product_name_edit.text()
        stock = self.stock_edit.text()
        price = self.price_edit.text()

        item = QListWidgetItem(f"{product_name} - {price}")
        item.setData(1000, (product_name, price))
        self.product_list.addItem(item)

        self.product_name_edit.clear()
        self.stock_edit.clear()
        self.price_edit.clear()

    def show_order_details(self):
        customer_name = self.name_edit.text()
        customer_address = self.address_edit.text()

        selected_item = self.product_list.currentItem()
        if selected_item:
            product_name, price = selected_item.data(1000)
            order_info = f"Sipariş Edilen Ürün: {product_name} - Fiyatı: {price}"
            total_amount = price  # Burada daha karmaşık hesaplamalar yapılabilir

            order_details = f"{customer_name}, {customer_address}\n{order_info}\nToplam Tutar: {total_amount}"
            self.order_details_window.display_order_details(order_details)
            self.order_details_window.show()

class OrderDetailsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sipariş Detayları")
        self.setGeometry(100, 100, 400, 300)

        self.order_details_label = QLabel()
        self.order_details_label.setAlignment(Qt.AlignTop)
        
        layout = QVBoxLayout()
        layout.addWidget(self.order_details_label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def display_order_details(self, order_details):
        self.order_details_label.setText(order_details)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RestaurantCustomerApp()
    window.show()
    sys.exit(app.exec_())

