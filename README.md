# netflix_data_analysis
Netflix veri seti üzerinde keşifsel veri analizi (EDA) projesi. İzleyici davranışlarını ve içerik trendlerini anlamayı amaçlar.

Netflix Film & Dizi Analizi
📝 Proje Tanımı
Bu proje, Kaggle'dan elde edilen Netflix veri seti üzerinde keşifsel veri analizi (EDA) yapmayı amaçlamaktadır. Projenin temel amacı, Netflix platformundaki film ve dizilerle ilgili trendleri, içerik türlerini ve zaman serisi verilerini analiz ederek içgörüler elde etmektir.

🛠️ Kullanılan Teknolojiler
Python: Veri analizi ve modelleme için temel programlama dili.

Pandas: Veri manipülasyonu ve analizi için güçlü bir kütüphane.

Matplotlib & Seaborn: Veri görselleştirmesi ve grafik çizimleri için kullanılmıştır.

📁 Dosya Yapısı
Proje, kolay takip ve yönetim için aşağıdaki klasör yapısına sahiptir:

data/: Ham veri setinin (netflix_titles.csv) bulunduğu klasördür.

notebooks/: Veri analizi ve görselleştirme için kullanılan Jupyter Notebook dosyalarını içerir.

README.md: Projenin ana dokümantasyonunu ve genel bilgilerini barındırır.

🔍 Analiz ve Sonuçlar
1. Veri Temizleme ve İlk Gözlemler
Veri seti yüklendikten sonra, eksik ve hatalı veriler belirlenerek temizleme işlemleri gerçekleştirilmiştir. date_added sütunu düzenlenmiş ve bu veriler üzerinden aşağıdaki ilk gözlemler elde edilmiştir:

Yıllara Göre Trend: Netflix'e eklenen film ve dizi sayısının yıllar içinde dramatik bir şekilde arttığı gözlemlenmiştir. Özellikle 2017 ve sonrasında büyük bir büyüme yaşanmıştır.

2. Tür Bazlı Analizler
Veri setindeki listed_in (tür) sütunu analiz edilerek Netflix'teki en popüler film ve dizi türleri belirlenmiştir. Bu analiz, platformun hangi içeriklere daha fazla yatırım yaptığını anlamamızı sağlamıştır.

📌 Yol Haritası (Devam Eden Çalışmalar)
Ülke Bazlı Analizler: Yapımların hangi ülkelerden geldiğini ve coğrafi dağılımını incelemek.

Film/Dizi Karşılaştırması: Platformdaki film ve dizilerin süre, tür ve popülarite gibi metriklerini karşılaştırmak.
