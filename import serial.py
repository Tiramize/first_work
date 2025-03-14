import serial  # Импорт модуля для работы с последовательными портами.
import time    # Импорт модуля для работы с временем (например, для задержек).
import serial.tools.list_ports  # Импорт утилит для получения списка доступных COM-портов.
speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200']# Список возможных скоростей передачи данных для последовательного порта.
ports = [p.device for p in serial.tools.list_ports.comports()]# Получение списка доступных COM-портов на устройстве.
port_name = ports[0]    # Выбор первого доступного порта из списка.
port_speed = int(speeds[-1])    # Выбор последней (самой высокой) скорости из списка и преобразование её в целое число.
port_timeout = 10   # Установка таймаута для чтения из порта (в секундах).
ard = serial.Serial(port_name, port_speed, timeout=port_timeout)    # Открытие последовательного порта с заданными параметрами.
time.sleep(1)   # Ожидание 1 секунды для стабилизации соединения.
ard.flushInput()    # Очистка входного буфера порта для удаления старых данных.
try:
     # Чтение всех доступных байтов из входного буфера и накопление их.
    msg_bin = ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    msg_str_ = msg_bin.decode() # Декодирование полученных байтов в строку.
    print(len(msg_bin)) # Вывод длины полученного бинарного сообщения.

except Exception as e:
      print('Error!')  # Обработка исключений и вывод сообщения об ошибке.
ard.close() # Закрытие последовательного порта.
time.sleep(1)  # Ожидание 1 секунды перед окончанием программы.
print(msg_str_) # Вывод полученного сообщения.