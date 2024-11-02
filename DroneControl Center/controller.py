import threading
from queue import Queue
import time

class Controller:
    def __init__(self):
        self.vehicles = {}  # Araçların kaydedileceği bir sözlük oluşturuluyor
        self.data_queue = Queue()  # Araç verileri için bir kuyruk oluşturuluyor
        self.is_active = True  # Kontrol merkezinin aktif durumunu tutan bir değişken
        self.process_thread = threading.Thread(target=self._process_data)  # Verileri işlemek için bir iş parçacığı
        self.process_thread.start()  # İş parçacığı başlatılıyor

    def register_vehicle(self, vehicle):
        vehicle.controller = self  # Araç kontrol merkezine atanıyor
        self.vehicles[vehicle.id] = vehicle  # Araçlar sözlüğe kaydediliyor

    def receive_vehicle_data(self, data):
        self.data_queue.put(data)  # Araç verileri kuyruğa ekleniyor

    def _process_data(self):
        while self.is_active:
            while not self.data_queue.empty():  # Kuyrukta veri varsa
                data = self.data_queue.get()  # Veriyi kuyruğun başından al
                # Veriyi istenen formatta yazdır
                print(f"[Araç {data['id']}] Konum: ({data['x']}, {data['y']}), "
                      f"Hız: {data['speed']}, Yön: {data['heading']}°, "
                      f"İrtifa: {data['altitude']}m")  # Araç verileri yazdırılıyor
            time.sleep(0.1)  # İşleme sıklığı

    def stop(self):
        self.is_active = False  # Kontrol merkezi durduruluyor
        self.process_thread.join()  # İş parçacığı bitene kadar bekleniyor
