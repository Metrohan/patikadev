# Python Projeleri

Bu depo, iki farklı Python görevi için geliştirilmiş çözümleri içermektedir:

- Listeyi düzleştirme (Flattening)
- İç içe geçmiş listeleri tersine çevirme (Nested Reverse)

---

## 🧩 Görev 1: Listeyi Düzleştirme (Flatten)

### 🎯 Amaç

Verilen çok katmanlı bir listeyi düzleştirerek **tek boyutlu bir liste** haline getiren bir fonksiyon geliştirmek.

### 📌 Fonksiyon: `flatten_list(nested_list)`

Bu fonksiyon, iç içe geçmiş tüm alt listeleri özyinelemeli olarak işler ve elemanlarını tek bir düz listede birleştirir.

### 🧪 Giriş Örneği

```python
nested = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
flatten_list(nested)
```

### ✅ Çıkış Örneği

```python
[1, 'a', 'cat', 2, 3, 'dog', 4, 5]
```

### ⚙️ Nasıl Çalışır?

Fonksiyon, her bir elemanı kontrol eder:
- Eğer eleman bir **liste** ise, fonksiyon kendini o alt liste üzerinde **tekrar çağırır** (özyineleme).
- Eğer eleman bir **liste değilse**, doğrudan düzleştirilmiş son listeye eklenir.

---

## 🔁 Görev 2: İç İçe Geçmiş Listeleri Tersine Çevirme

### 🎯 Amaç

Verilen bir listenin içindeki elemanları tersine çevirmek ve eğer iç elemanlar da listeler içeriyorsa, **onların da elemanlarını tersine çevirmek**.

### 📌 Fonksiyon: `reverse_nested_list(nested_list)`

Bu fonksiyon, hem ana listeyi hem de içerdiği tüm alt listeleri **özyinelemeli olarak** tersine çevirir.

### 🧪 Giriş Örneği

```python
nested = [[1, 2], [3, 4], [5, 6, 7]]
reverse_nested_list(nested)
```

### ✅ Çıkış Örneği

```python
[[[7, 6, 5], [4, 3], [2, 1]]]
```

### ⚙️ Nasıl Çalışır?

1. İlk olarak **ana liste ters çevrilir**.
2. Daha sonra her bir alt eleman:
   - Liste ise: fonksiyon kendisini tekrar çağırarak içeriği de ters çevirir.
   - Liste değilse: olduğu gibi bırakılır.

---

## ⚙️ Kullanım

Fonksiyonları çalıştırmak için doğrudan çağırabilir veya `.py` dosyasını projenize dahil edebilirsiniz.

```python
from your_module import flatten_list, reverse_nested_list

flat = flatten_list(your_nested_list)
reversed_nested = reverse_nested_list(your_nested_list)
```

---

## 👨‍💻 Geliştirici

**Metehan Günen**

---
