Python Projeleri

Bu depo, iki farklı Python görevi için çözümler içermektedir: listeleri düzleştirme (flattening) ve iç içe geçmiş listeleri tersine çevirme.

Görev 1: Listeyi Düzleştirme (Flatten)

Amaç

Verilen çok katmanlı bir listeyi düzleştirerek tek boyutlu bir liste haline getiren bir fonksiyon yazmaktır. Liste elemanları non-scalar verilerden (örn. string, sayı) oluşabilir.

Fonksiyon: flatten_list(nested_list)

Bu fonksiyon, iç içe geçmiş tüm alt listelerdeki elemanları alır ve bunları tek bir düz listede birleştirir. Özyinelemeli (recursive) bir yaklaşımla her katmanı işler.

Giriş Örneği

Python

[[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

Çıkış Örneği

Python

[1, 'a', 'cat', 2, 3, 'dog', 4, 5]

Nasıl Çalışır?

Fonksiyon, listenin her bir elemanını kontrol eder. Eğer eleman bir listeyse, kendini tekrar çağırarak (özyineleme) o alt listeyi düzleştirir. Eğer eleman bir liste değilse (yani bir sayı, dize vb. ise), doğrudan düzleştirilmiş listeye ekler.

Görev 2: İç İçe Geçmiş Listeleri Tersine Çevirme

Amaç

Verilen bir listenin içindeki elemanları tersine çeviren ve eğer listenin içindeki elemanlar da başka listeler içeriyorsa, onların da elemanlarını tersine çeviren bir fonksiyon yazmaktır.

Fonksiyon: reverse_nested_list(nested_list)

Bu fonksiyon, hem ana listeyi hem de içerdiği tüm alt listeleri özyinelemeli olarak tersine çevirir.

Giriş Örneği

Python

[[1, 2], [3, 4], [5, 6, 7]]

Çıkış Örneği

Python

[[[7, 6, 5], [4, 3], [2, 1]]]

Nasıl Çalışır?

Fonksiyon ilk olarak ana listeyi tersine çevirir. Ardından, tersine çevrilmiş ana listedeki her bir elemanı kontrol eder. Eğer eleman bir listeyse, reverse_nested_list fonksiyonunu o alt liste üzerinde tekrar çağırarak (özyineleme) onun da elemanlarını tersine çevirir. Bu süreç, en içteki listelere ulaşana kadar devam eder.

Kullanım

Her iki fonksiyon da Python'da doğrudan çağrılarak kullanılabilir. Fonksiyonların tanımlandığı .py dosyasını içe aktararak veya doğrudan kopyalayıp yapıştırarak test edebilirsiniz.

Geliştirici:
Metehan Günen
