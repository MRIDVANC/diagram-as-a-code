import pandas as pd


class Switch:
    def __init__(self, switch_name, switch_port, port_speed, port, connected_server):
        self.port_speed = port_speed
        self.switch_name = switch_name
        self.switch_port = switch_port
        self.port = port
        self.connected_server = connected_server


# Excel dosyasını okuyup sunucu adına göre switchleri arayan fonksiyon
def read_excel_and_search_server(envanter_file, search_server):
    try:
        # Excel dosyasını okumaya çalış
        df = pd.read_excel(envanter_file)
    except FileNotFoundError:
        # Excel dosyası bulunamazsa hata mesajı gönder
        print(f"Excel dosyası bulunamadı: {envanter_file}")
        return

    # Switch nesnelerini içerecek bir liste oluştur
    switch_objects = []

    # Excel dosyasındaki her satırı işleyerek Switch nesnelerini oluştur
    for index, row in df.iterrows():
        switch_name = row["Switch isimleri"]
        switch_port = row["Switch Port"]
        port_speed = row["Port Speed"]
        port = row["Server Port"]
        connected_server = row["Takılı olduğu sunucu"]
        switch = Switch(switch_name, switch_port, port_speed, port, connected_server)
        switch_objects.append(switch)

    # Bulunan switchleri saklamak için bir liste oluştur
    found_switches = []

    # Kullanıcının girdiği sunucu adına göre switchleri ara
    for switch in switch_objects:
        if switch.connected_server == search_server:
            found_switches.append(switch)

    if not found_switches:
        # Eğer hiç switch bulunamazsa kullanıcıya bilgi ver ve çıkmak için 'q' girmesini iste
        print(f"'{search_server}' sunucusuna bağlı bir switch bulunamadı. (Çıkmak için 'q' girin): ")
    else:
        # Bulunan switchleri ekrana yazdır
        for found_switch in found_switches:
            print("Switch Name:", found_switch.switch_name)
            print("Switch Port:", found_switch.switch_port)
            print("Port Speed:", found_switch.port_speed)
            print("Port:", found_switch.port)
            print("Connected Server:", found_switch.connected_server)
            print("=" * 40)


if __name__ == "__main__":
    excel_file = "envanter.xlsx"  # Excel dosyasının yolu ve adı
    while True:
        # Kullanıcıdan sunucu adı girmesini iste, çıkmak için 'q' girilebilir
        search_server_name = input("Aramak istediğiniz sunucu ismini girin (Çıkmak için 'q' girin): ")
        if search_server_name.lower() == 'q':
            break
        # Excel dosyasını oku ve sonuçları göster
        read_excel_and_search_server(excel_file, search_server_name)
