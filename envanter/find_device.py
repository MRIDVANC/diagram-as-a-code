import pandas as pd


class Switch:
    def __init__(self, switch_name, switch_port, port_speed, port, connected_server, mac_adres):
        self.port_speed = port_speed
        self.switch_name = switch_name
        self.switch_port = switch_port
        self.port = port
        self.connected_server = connected_server
        self.mac_address = mac_adres


# Excel dosyasını okuyup sunucu adına göre switchleri arayan fonksiyon
def read_excel_and_search_server(envanter_file, search_server, mac_adres=None):
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
        mac_adres = row["MAC Adres"]
        connected_server = row["Takılı olduğu sunucu"]
        switch = Switch(switch_name, switch_port, port_speed, port, connected_server, mac_adres)
        switch_objects.append(switch)

    # Bulunan switch isimlerini saklamak için bir küme oluştur
    unique_servers = set()

    # Bulunan switchleri saklamak için bir liste oluştur
    found_switches = []

    # Kullanıcının girdiği sunucu adına göre switchleri ara
    search_server_lower = search_server.lower()  # Küçük harfe çevir
    for switch in switch_objects:
        if search_server_lower in switch.connected_server.lower() and len(search_server) >= 3:
            unique_servers.add(switch.connected_server)
            found_switches.append(switch)

    if not found_switches:
        # Eğer hiç switch bulunamazsa kullanıcıya bilgi ver ve çıkmak için 'q' girilmesini iste
        print(f"'{search_server}' sunucusuna bağlı en az 3 karakter içeren bir switch bulunamadı.")
        print("Bunlardan hangisini seçmek istediğinizi belirtin:")
        for i, switch in enumerate(switch_objects, start=1):
            print(f"{i}. Switch Name: {switch.switch_name}, Connected Server: {switch.connected_server}")

        # Kullanıcının seçim yapmasını iste
        while True:
            user_input = input("Hangi Sunucuyu arıyorsunuz? (Çıkmak için 'q' girin): ")
            if user_input.lower() == 'q':
                break
            try:
                selected_index = int(user_input)
                selected_switch = switch_objects[selected_index - 1]

                # Seçilen Switch'in detaylarını ekrana yazdır
                print(f"\nSeçilen Switch:")
                print("Switch Name:", selected_switch.switch_name)
                print("Switch Port:", selected_switch.switch_port)
                print("Port Speed:", selected_switch.port_speed)
                print("Port:", selected_switch.port)
                print("Connected Server:", selected_switch.connected_server)
                print("Mac Adres:", selected_switch.mac_address)
                print("=" * 40)
            except (ValueError, IndexError):
                print("Geçersiz giriş. Lütfen geçerli bir sayı girin.")
    else:
        # Kullanıcıya sadece benzersiz Sunucuları göster
        print("Bulunan Sunucular:")
        for i, server in enumerate(unique_servers, start=1):
            print(f"{i}. Sunucu: {server}")

        # Kullanıcının seçim yapmasını iste
        while True:
            user_input = input("Hangi Sunucuyu seçmek istersiniz? (Çıkmak için 'q' girin): ")
            if user_input.lower() == 'q':
                break
            try:
                selected_index = int(user_input)
                selected_server = list(unique_servers)[selected_index - 1]

                # Seçilen Sunucu'ya sahip switch'leri ekrana yazdır
                print(f"\nSwitch'ler için Sunucu {selected_server} seçildi:")
                for found_switch in found_switches:
                    if found_switch.connected_server == selected_server:
                        print("Switch Name:", found_switch.switch_name)
                        print("Switch Port:", found_switch.switch_port)
                        print("Port Speed:", found_switch.port_speed)
                        print("Port:", found_switch.port)
                        print("Connected Server:", found_switch.connected_server)
                        print("Mac Adres:", found_switch.mac_address)
                        print("=" * 40)
            except (ValueError, IndexError):
                print("Geçersiz giriş. Lütfen geçerli bir sayı girin.")


if __name__ == "__main__":
    excel_file = "envanter.xlsx"  # Excel dosyasının yolu ve adı
    while True:
        # Kullanıcıdan sunucu adı girmesini iste, çıkmak için 'q' girilebilir
        search_server_name = input("Aramak istediğiniz sunucu ismini girin (Çıkmak için 'q' girin): ")
        if search_server_name.lower() == 'q':
            break
        # Excel dosyasını oku ve sonuçları göster
        read_excel_and_search_server(excel_file, search_server_name)
