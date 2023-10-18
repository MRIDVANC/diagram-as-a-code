import pandas as pd

# Excel dosyasının adı
excel_file = "envanter.xlsx"

# Excel dosyasını oku
df = pd.read_excel(excel_file)

# "Switch isimleri" sütununu bir dizi olarak alın

# Sütunları ayrı ayrı alın
first = df.iloc[:, 0]  # İlk sütun
second = df.iloc[:, 1]  # İkinci sütun
third = df.iloc[:, 2]  # Üçüncü sütun


# Değerleri ayrı ayrı yazdırın
print("First Column:")
print(first)

print("Second Column:")
print(second)

print("Third Column:")
print(third)
