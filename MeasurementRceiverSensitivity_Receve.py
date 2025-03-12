import serial
import serial.tools.list_ports
import time

datalist = []
flag = 0
counter = 0
try:
    Serial_Port = serial.Serial(port='COM10', baudrate=19200, parity='N')
    print("COM10 connect success")
except:
    print("COM10 connect failed")

while True:
    if Serial_Port.in_waiting > 0:
        # 受信 (rx)
        data = Serial_Port.read(1)
        hexdata = data.hex().upper()  
        print(hexdata)

        if hexdata == 'C0' and flag == 0:
            flag = 1
            datalist.append(hexdata)
        elif hexdata == 'C0' and flag == 1:
            datalist.append(hexdata)
            print("データ受信完了:", " ".join(datalist))
            # 処理後リセット
            datalist = []
            flag = 0
            counter += 1
            print("送信パケット番号",counter)
        else:
            datalist.append(hexdata)
    else:
        print("waiting")
        time.sleep(0.180)
