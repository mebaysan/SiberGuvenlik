# --------------------- ARP (Ey Ar Pi) ---------------------#
# https://scapy.net/

import scapy.all as scapy
import optparse


def get_user_input():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ipaddress", dest='ip_address', help="Enter IP address")
    (user_input, arguments) = parser.parse_args()
    if not user_input.ip_address:
        print("Enter IP address")
    return user_input


def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)  # arp paketimizi oluşturuyoruz
    # scapy.ls(scapy.ARP()) # -> scapy içindeki method. içine verdiğimiz instance için parametreleri gösterir

    broadcast_packet = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')  # broadcast paketi oluşturduk

    combined_packet = broadcast_packet / arp_request_packet  # 2 paketi tek paket haline getir dedik

    (answered_list, unanswered_list) = scapy.srp(combined_packet,
                                                 timeout=1)  # paketi yolluyoruz. timeout -> 1 sn bekle cevap gelmezse bekleme devam et dedik

    answered_list.summary()  # scapy içindeki method özet halinde bize dönen değerleri gösterir


user_ip_address = get_user_input()
scan_my_network(user_ip_address.ip_address)
