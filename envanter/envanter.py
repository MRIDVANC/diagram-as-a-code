# import pandas as pd
#
# # Excel dosyasının adı
# excel_file = "envanter.xlsx"
#
# # Excel dosyasını oku
# df = pd.read_excel(excel_file)
#
# # Her satırı temsil edecek bir sınıf tanımlayalım
# class Switch:
#     def __init__(self, switch_name, port, connected_server):
#         self.switch_name = switch_name
#         self.port = port
#         self.connected_server = connected_server
#
# # Sınıf nesnelerini oluşturup bir listeye ekleyelim
# switch_objects = []
# for index, row in df.iterrows():
#     switch_name = row["Switch isimleri"]
#     port = row["1. Port"]
#     connected_server = row["Takılı olduğu sunucu"]
#     switch = Switch(switch_name, port, connected_server)
#     switch_objects.append(switch)
#
# # Sınıf nesnelerini kullanabilirsiniz
# for switch in switch_objects:
#     print("Switch Name:", switch.switch_name)
#     print("Port:", switch.port)
#     print("Connected Server:", switch.connected_server)
#     print("=" * 40)  # Her sınıf sonrası çıktıyı ayırmak için
