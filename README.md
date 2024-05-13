16-17-18-19-20. projeler görev bölümünden bana düşen/benim projelerimdir. 

![p1](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/93835e2c-ad7e-4bb1-9e71-18e350d1c797)
![p5](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/e91a1333-3b89-41ea-833e-376997b28ddf)
![p4](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/f96f1a1f-abc9-431d-8ae7-4b9e130afb85)
![p3](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/4010b7ed-c932-46cf-b317-20df794bdf08)
![p2](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/eaeea892-2a3c-4129-b462-46cdc71f0515)
![p7](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/ce057343-b459-4def-9768-0316d699f5e7)
![p9](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/a7c3eedd-f53d-4cf4-9545-1128dbc12d4c)
![p8](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/4927d11b-2b53-4967-bd06-06b4f5b36830)
![p10](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/2f9ca7ea-8fc8-4176-9d54-7f053cd55d15)
![p11](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/898231df-7bed-4a49-851b-34e030907642)
![p12](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/de6a5f5c-0afc-407a-a820-6eb000c5cddc)
![p13](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/6a54f405-448a-489f-b234-8f27fc1e2d33)
![p14](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/dc237353-26a6-499f-ac54-cf7b8f543ec4)
![p15](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/f8d0b704-6c51-45b8-b309-f61d6e329b68)
![p16](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/9f99367d-ec6f-4b2d-9ab2-dc865aae4ee3)

Öncelikle tüm kodların çalıştırılması için python ve pyqt5 kurulu olmalıdır.
Kullanıcı adı ve şifreyi girdikten sonra giriş yap butonuna tıklayarak sisteme giriş yapabilirsiniz.Film adı alanına film ismi yazıp film ekle butonuna basarak izleme geçmişinize film ekleyin ve izleme geçmişinizdeki bir filme tıklayarak o filmi favorilerinize ekleyebilirsiniz.

Teknik Detaylar

Film Sınıfı (Film):

film_adı: Film adı.
film_yönetmeni: Film yönetmeni.
film_imdb: Film IMDb puanı.
süre: Film süresi .
film_türü: Film türü.

Kullanıcı Sınıfı (Kullanıcı):

kullanici_adi: Kullanıcı adı.
kullanici_sifre: Kullanıcı şifresi.
izleme_gecmisi: Kullanıcının izleme geçmişi.
favori_filmler: Kullanıcının favori filmleri listesi.

Film İzleme Servisi Sınıfı (FilmIzlemeServisi):

Arayüz ve iş mantığını bir araya getiren ana sınıf.
Kullanıcı girişini yönetir, film eklemesini sağlar, izleme geçmişini ve favori filmleri görüntüler.

![p17](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/eb075f47-8ec8-42c2-abba-d25eb950179d)

İstenilen bilgiler girilip kaydet butonuna basıldıktan sonra öğrencinin adı,soyadı, dersi, ders kaynağı ve öğretmeni bilgileri ekranda çıkar.

Teknik Detaylar

1.EgitimPlatformu sınıfı QMainWindow sınıfından türetilmiştir.
2.initUI metodu, arayüz öğelerini oluşturur ve pencereye yerleştirir.
3.kaydet metodu, kullanıcının girdiği bilgileri alır ve bu bilgileri ilgili QLabel'lar üzerinde görüntüler.
4.QPushButton ve QLineEdit gibi PyQt5 widget'ları kullanılarak arayüz öğeleri oluşturulur ve düzenlenir.
5.QVBoxLayout kullanılarak dikey bir düzen (layout) oluşturulur ve widget'lar bu düzene eklenir.

![p18](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/161f960c-7301-4232-972a-ba1035676faa)

Olay ekle, şahsiyet ekle,dönem ekle pencereleindeki girdileri kaydettikten sona kayıtları görüntüle butonuna basarak bilgilere toplu halde ulaşabilirsiniz.

Teknik Detaylar

Ana Pencere (AnaPencere)
Ana pencere, QTabWidget kullanarak üç farklı sekme içerir: Olay Ekle, Şahsiyet Ekle, ve Dönem Ekle.
Her sekme, kullanıcıdan bilgi girmesini ve bu bilgileri kaydetmesini bekler.
"Kayıtları Görüntüle" düğmesi, kaydedilen bilgileri görüntülemek için kullanılır.

Bilgi Giriş Pencereleri (OlayEklePenceresi, SahsiyetEklePenceresi, DonemEklePenceresi)
Her bilgi giriş penceresi, belirli türdeki bilgileri girmek için kullanılır (Olay, Şahsiyet, Dönem).
Bilgiler girildikten sonra "Kaydet" düğmesi ile ana pencereye bu bilgiler iletilir.

Kayıtları Görüntüleme Penceresi (GoruntulePenceresi)
"Kayıtları Görüntüle" düğmesine tıklandığında, bu pencere açılır.
Olaylar, Şahsiyetler ve Dönemler için ayrı ayrı listeler oluşturulur ve kullanıcının kaydedilen bilgileri görmesi sağlanır.

![p20s](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/d9bcb735-e266-4daf-a3a8-9c2e196589c9)

Oyun adı,türü ve platformunu girip oyun ekle'ye her bastığınızda 'oynadığı oyunlar kısmına bu oyunlar eklecektir. İçlerinden bir oyun seçip 'favoriye ekle'ye astığınızda 'favori oyunlar listesi' oluşur. Oyuncu adını girip oyuncu ekle'ye bastığınızda da oyuncunun adı,oynadığı oyunlar ve favori oyunlar taablosu sizi karşılar.

Teknik Detaylar

Uygulama, aşağıdaki bileşenlerden oluşur:

QApplication: PyQt5 uygulamasını temsil eden ana uygulama nesnesi.
QWidget: Ana pencereyi oluşturan ve temel işlevleri sağlayan PyQt5 bileşeni.
QVBoxLayout ve QHBoxLayout: Dikey ve yatay düzenler oluşturmak için kullanılan düzen nesneleri.
QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem: Arayüzde metin, düzenleme kutusu, düğme ve liste öğeleri oluşturmak için PyQt5 bileşenleri.
Ana Fonksiyonlar
add_game(): Oyun eklemek için kullanılan fonksiyon. Girilen oyun bilgilerini alır ve "Oynadığı Oyunlar" listesine ekler.
add_to_favorite(): Seçilen oyunları "Favori Oyunlar" listesine taşır.
add_player(): Yeni bir oyuncu eklemek için kullanılan fonksiyon. Oyuncunun adını, oynadığı ve favori oyunlarını kaydeder.
show_player_info(): Oyuncu bilgilerini içeren iletişim kutusunu görüntüler.
Uygulamanın Çalıştırılması
QApplication: PyQt5 uygulamasını başlatır.
VideoGameCollectionApp: Ana uygulama penceresini oluşturan ve başlatan sınıf.
show(): Ana pencereyi görüntüler.


![p19s](https://github.com/zenepduran/2300005466-zeynepduran/assets/148756307/32954303-709f-47ba-8372-2f3de0121fdc)

Restoran çalışanları yeni ürün bilgilerini girer ve "Ürünü Kaydet" düğmesine basarak kaydeder.
Bu ürünler "Ürün Adı - Fiyatı" formatında müşteri arayüzünde listelenir.Müşteriler listeden bir ürün seçer ve ad-soyad ile adres bilgilerini girerek "Sipariş Ver" düğmesine basar.
Seçilen ürün ve müşteri bilgileri sipariş detayları penceresinde görüntülenir.Sipariş detayları penceresinde müşteri bilgileri, sipariş edilen ürün ve toplam tutar bilgilerini gösterir.

RestaurantCustomerApp (Restoran Müşteri Uygulaması Sınıfı):

__init__: Ana pencere ve bileşenlerini oluşturur.
  Restoran ve Müşteri arayüzlerini hazırlar.
  Restoran arayüzüne ürün bilgileri girilip kaydedilebilir.
  Müşteri arayüzü, seçilen ürünle birlikte müşteri bilgilerini alarak siparişi tamamlamayı sağlar.
save_product: Restoran arayüzünden girilen ürün bilgilerini alıp listeye ekler.
show_order_details: Müşteri bilgileri ve seçilen ürünü içeren sipariş detaylarını göstermek için sipariş detayları penceresini açar.

OrderDetailsWindow (Sipariş Detayları Penceresi Sınıfı):

__init__: Sipariş detayları penceresini oluşturur.
display_order_details: Verilen sipariş detaylarını pencereye yazar.

