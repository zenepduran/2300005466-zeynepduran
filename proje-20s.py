#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QMessageBox


class VideoGameCollectionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.games = []
        self.players = []

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Video Oyunu Koleksiyonu")

        # Oyun ekleme arayüzü
        self.game_name_label = QLabel("Oyun Adı:")
        self.game_name_edit = QLineEdit()
        self.game_genre_label = QLabel("Türü:")
        self.game_genre_edit = QLineEdit()
        self.game_platform_label = QLabel("Platformu:")
        self.game_platform_edit = QLineEdit()
        self.add_game_button = QPushButton("Oyun Ekle")
        self.add_game_button.clicked.connect(self.add_game)

        game_layout = QVBoxLayout()
        game_layout.addWidget(self.game_name_label)
        game_layout.addWidget(self.game_name_edit)
        game_layout.addWidget(self.game_genre_label)
        game_layout.addWidget(self.game_genre_edit)
        game_layout.addWidget(self.game_platform_label)
        game_layout.addWidget(self.game_platform_edit)
        game_layout.addWidget(self.add_game_button)

        # Oyuncu ve koleksiyon arayüzü
        self.player_name_label = QLabel("Oyuncu Adı:")
        self.player_name_edit = QLineEdit()
        self.played_games_list = QListWidget()
        self.add_to_favorite_button = QPushButton("Favoriye Ekle")
        self.add_to_favorite_button.clicked.connect(self.add_to_favorite)

        self.favorite_games_list = QListWidget()
        self.add_player_button = QPushButton("Oyuncu Ekle")
        self.add_player_button.clicked.connect(self.add_player)

        player_layout = QVBoxLayout()
        player_layout.addWidget(self.player_name_label)
        player_layout.addWidget(self.player_name_edit)
        player_layout.addWidget(QLabel("Oynadığı Oyunlar:"))
        player_layout.addWidget(self.played_games_list)
        player_layout.addWidget(self.add_to_favorite_button)
        player_layout.addWidget(QLabel("Favori Oyunlar:"))
        player_layout.addWidget(self.favorite_games_list)
        player_layout.addWidget(self.add_player_button)

        # Ana pencere düzeni
        main_layout = QHBoxLayout()
        main_layout.addLayout(game_layout)
        main_layout.addLayout(player_layout)

        self.setLayout(main_layout)

    def add_game(self):
        game_name = self.game_name_edit.text()
        game_genre = self.game_genre_edit.text()
        game_platform = self.game_platform_edit.text()
        if game_name and game_genre and game_platform:
            self.games.append((game_name, game_genre, game_platform))
            self.game_name_edit.clear()
            self.game_genre_edit.clear()
            self.game_platform_edit.clear()
            # Oyun listesine ekle
            item = QListWidgetItem(f"{game_name} - {game_genre} ({game_platform})")
            self.played_games_list.addItem(item)

    def add_to_favorite(self):
        selected_items = self.played_games_list.selectedItems()
        for item in selected_items:
            self.favorite_games_list.addItem(item.text())
            # Oynadığı oyunlar listesinden seçilen oyunu kaldır
            self.played_games_list.takeItem(self.played_games_list.row(item))

    def add_player(self):
        player_name = self.player_name_edit.text()
        if player_name:
            played_games = [self.played_games_list.item(i).text() for i in range(self.played_games_list.count())]
            favorite_games = [self.favorite_games_list.item(i).text() for i in range(self.favorite_games_list.count())]
            self.players.append({
                "name": player_name,
                "played_games": played_games,
                "favorite_games": favorite_games
            })
            self.player_name_edit.clear()
            self.played_games_list.clear()
            self.favorite_games_list.clear()

            # Bilgi ekranını göster
            self.show_player_info()

    def show_player_info(self):
        info_dialog = QMessageBox()
        info_dialog.setWindowTitle("Oyuncu Bilgileri")
        info_dialog_text = ""
        for player in self.players:
            info_dialog_text += f"Oyuncu Adı: {player['name']}\n"
            info_dialog_text += "Oynadığı Oyunlar:\n"
            for game in player['played_games']:
                info_dialog_text += f"- {game}\n"
            info_dialog_text += "Favori Oyunlar:\n"
            for fav_game in player['favorite_games']:
                info_dialog_text += f"- {fav_game}\n"
            info_dialog_text += "\n"
        info_dialog.setText(info_dialog_text)
        info_dialog.exec_()

    def show(self):
        super().show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game_collection_app = VideoGameCollectionApp()
    game_collection_app.show()
    sys.exit(app.exec_())


# In[ ]:




