import threading
import time
import random
import math

# Vehicle sınıfı
class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, altitude):
        self.id = vehicle_id
        self.type = vehicle_type
        self.x = random.uniform(-10, 10)  # x başlangıç koordinatı
        self.y = random.uniform(-10, 10)  # y başlangıç koordinatı
        self.speed = random.uniform(0.5, 5)  # Rastgele hızın değeri
        self.heading = random.uniform(0, 360)  # Rastgele yönün açısı
        self.altitude = altitude  # İrtifa değeri
        self.is_active = True  # Araç durumu
        self.update_thread = threading.Thread(target=self._update_loop)  # Güncelleme thread'i
        self.controller = None  # Kontrol merkezi

    def start(self):
        self.update_thread.start()  # Thread başlatılıyor

    def stop(self):
        self.is_active = False  # Aktif durumu false yapılıyor
        self.update_thread.join()  # Thread'in tamamlanması bekleniyor

    def _update_loop(self):
        while self.is_active:
            # Konum güncellemesi
            self.x += self.speed * math.cos(math.radians(self.heading))
            self.y += self.speed * math.sin(math.radians(self.heading))

            # Sınır kontrolü ve dönüş
            if abs(self.x) > 10 or abs(self.y) > 10:
                self.heading = (self.heading + 180) % 360  # Yön değiştir

            # Veri kontrol merkezine gönderiliyor
            if self.controller:
                data = {
                    'id': self.id,
                    'type': self.type,
                    'x': round(self.x, 2),
                    'y': round(self.y, 2),
                    'speed': round(self.speed, 2),
                    'heading': round(self.heading, 2),
                    'altitude': self.altitude  # İrtifa verisi
                }
                self.controller.receive_vehicle_data(data)  # Veri gönderimi

            time.sleep(1)  # 1 Hertz ile Güncelleme sıklığı yapılıyor

# Alt sınıf olan Quadcopter
class Quadcopter(Vehicle):
    def __init__(self, vehicle_id):
        super().__init__(vehicle_id, "quadcopter", 100)  # İrtifa 100m

# Alt sınıf olan FixedWingDrone
class FixedWingDrone(Vehicle):
    def __init__(self, vehicle_id):
        super().__init__(vehicle_id, "fixed_wing", 200)  # İrtifa 200m
