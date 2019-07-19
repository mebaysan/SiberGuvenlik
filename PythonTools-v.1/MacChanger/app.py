import subprocess  # bilgisayarın kendi sistemine ulaşıyoruz
import optparse  # terminalde parse işlemi yapmamıza yarar

parse_object = optparse.OptionParser()  # bir obje oluşturuyoruz

parse_object.add_option("-i", "--interface", dest="interface",
                        # kullanıcıdan aldığımız input'u nereye kaydedeceğimizi söyledik(interface değişkeni)
                        help="interface to change")  # terminalde input almamızı sağlar
# help= -> --help yazınca terminalde ne yazsın dedik
parse_object.add_option("-m", "--mac_address", dest="mac_address", help="new mac address")
(user_inputs, arguments) = parse_object.parse_args()  # parse objesinin argümanlarını döner(dest) bir tuple içinde
print(user_inputs.interface)  # kullanıcının girdiği değişkeni(dest=interface) aldık
print(user_inputs.mac_address)
print("mac changer çalıştı")

subprocess.call(["ifconfig", user_inputs.interface,
                 "down"])  # sırasıyla içeri verilen kodlar terminalde(linuxta ise kendi terminalinda, windowsta ise kendi terminalinde) çalışır -> 'ifconfig eth0 down' demiş olduk
subprocess.call(["ifconfig", user_inputs.interface, "hw", "ether", user_inputs.mac_address])
subprocess.call(["ifconfig", user_inputs.interface, "up"])
print("mac changer çalışmayı durdurdu")
