import scapy.all as scapy  # bu paketi (scapy) indrmeliyzi pip ile
from scapy_http import http  # bu paketi (scapy_http) indrmeliyzi pip ile
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Enter a interface")
user_input = parser.parse_args()[0]
interface = user_input.interface


def listen_packet(interface):
    scapy.sniff(iface=interface, store=False,
                prn=analyze_packets)  # store = False -> aldığın verileri hafızaya kaydetme, prn -> paket geldikçe nereye yollayayım


def analyze_packets(packet):  # listen_packet'in gönderdiği paketi parametre olarak alıyor
    # packet.show() # paketi gösterir
    if packet.haslayer(http.HTTPRequest):  # http httprequest layer'i var mı
        if packet.haslayer(scapy.Raw):  # yukardaki katman varsa Raw katmanı var mı ona bak
            packet[scapy.Raw].load  # yukardaki katman varsa load katmanını getir


# https://github.com/singe/dns2proxy -> gerekli tool

listen_packet(interface)
