from vehicle import Quadcopter, FixedWingDrone
from controller import Controller
import time

def main():
    # Kontrol merkezi oluştur
    controller = Controller()  # Kontrol merkezi nesnesi yaratılıyor

    # Araçları oluştur
    vehicles = [
        Quadcopter(1),  # İlk quadcopter aracı oluşturuluyor
        FixedWingDrone(2),  # İlk sabit kanatlı drone aracı oluşturuluyor
        Quadcopter(3)  # İkinci quadcopter aracı oluşturuluyor
    ]

    # Araçları kaydet ve başlat
    for vehicle in vehicles:
        controller.register_vehicle(vehicle)  # Araç kontrol merkezine kaydediliyor
        vehicle.start()  # Araçlar başlatılıyor

    try:
        # Ana program çalışırken beklensin
        while True:
            time.sleep(1)  # Ana döngü çalışıyor, program bekliyor
    except KeyboardInterrupt:
        
        print("\nProgram sonlandırılıyor...")  # Sonlandırma mesajı
        for vehicle in vehicles:
            vehicle.stop()  # Araçlar durduruluyor
        controller.stop()  # Kontrol merkezi durduruluyor

if __name__ == "__main__":
    main()  # Ana fonksiyon çalıştırılıyor
