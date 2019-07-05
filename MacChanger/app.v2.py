import subprocess
import optparse
import re # regex kütüphanesini dahil ettik


def get_user_input():
    parse_object = optparse.OptionParser()

    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change")

    parse_object.add_option("-m", "--mac_address", dest="mac_address", help="new mac address")
    return parse_object.parse_args()


def change_mac_address(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface,
                     "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])
    print("mac changer çalışmayı durdurdu")


def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface]) # burdan gelen (subprocess) değeri ifconfig değişkenimize eşitler
    new_mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',str(ifconfig)) # regex kontrolü yapıyoruz. başına r konulması bunun regex formatında olduğunu beliritir. ilk parametre regex formatı, ikinci parametre ise hangi string içinde kontrol edileceği
            # re.search bize string döndürmez
    if new_mac:
        return new_mac.group(0) # string dönmediği için dönen değerden stringi yakalıyoruz
    else:
        return None

print("Mac changer started!")
(user_input, arguments) = get_user_input()
change_mac_address(user_input.interface, user_input.mac_address)
final_mac = control_new_mac(str(user_input.interface))
if final_mac == user_input.mac_address:
    print("Success!, Mac address has changed!")
else:
    print("Error! Mac address not changed!")