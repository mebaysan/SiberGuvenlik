# İçindekiler
- [İçindekiler](#%c4%b0%c3%a7indekiler)
- [Giriş](#giri%c5%9f)
- [Ağlara Giriş](#a%c4%9flara-giri%c5%9f)
  - [İletişim Nedir?](#%c4%b0leti%c5%9fim-nedir)
  - [Ağ Nedir?](#a%c4%9f-nedir)
  - [İnternet Nedir?](#%c4%b0nternet-nedir)
  - [Önemli Ağ Terimleri](#%c3%96nemli-a%c4%9f-terimleri)
    - [Sunucu](#sunucu)
    - [Hyperconverged Cihazlar](#hyperconverged-cihazlar)
    - [Uç Sistemler - Uç Birimler](#u%c3%a7-sistemler---u%c3%a7-birimler)
    - [Paketler](#paketler)
    - [Veri İletişimi (Data Transmission)](#veri-%c4%b0leti%c5%9fimi-data-transmission)
    - [Ağ Protokolü Nedir?](#a%c4%9f-protokol%c3%bc-nedir)
    - [MAC Adresi](#mac-adresi)
    - [ISP](#isp)
    - [IP](#ip)
    - [DNS (Domain Name Server)](#dns-domain-name-server)
    - [Arp (Address Resolution Protocol)](#arp-address-resolution-protocol)
    - [VPN (Virtual Private Network)](#vpn-virtual-private-network)
  - [Cihazların İletişime Başlaması](#cihazlar%c4%b1n-%c4%b0leti%c5%9fime-ba%c5%9flamas%c4%b1)
    - [Handshake (3-Way Handshake)](#handshake-3-way-handshake)
    - [Syn Paketi](#syn-paketi)
    - [ACK Paketi](#ack-paketi)
  - [VPN Kullanımı](#vpn-kullan%c4%b1m%c4%b1)
  - [DNS Değiştirmek](#dns-de%c4%9fi%c5%9ftirmek)
- [Dark Web](#dark-web)
  - [Tor Browser Yüklemek](#tor-browser-y%c3%bcklemek)
- [Ufak Bir Terminal Trick'i](#ufak-bir-terminal-tricki)
- [Ağlara Saldırmak](#a%c4%9flara-sald%c4%b1rmak)
  - [Saldırı Öncesi Ayarlar](#sald%c4%b1r%c4%b1-%c3%96ncesi-ayarlar)
    - [MAC Adresi Değiştirmek](#mac-adresi-de%c4%9fi%c5%9ftirmek)
    - [Monitor ve Managed Mod](#monitor-ve-managed-mod)
        - [Mod Değiştirmek İçin 1. Yöntem (airmon-ng)](#mod-de%c4%9fi%c5%9ftirmek-%c4%b0%c3%a7in-1-y%c3%b6ntem-airmon-ng)
        - [Mod Değiştirmek İçin 2. Yöntem (iwconfig)](#mod-de%c4%9fi%c5%9ftirmek-%c4%b0%c3%a7in-2-y%c3%b6ntem-iwconfig)
  - [Ağlarla İlgili Bilgi Toplamak](#a%c4%9flarla-%c4%b0lgili-bilgi-toplamak)
    - [Ağları İncelemek (Sniffing)](#a%c4%9flar%c4%b1-%c4%b0ncelemek-sniffing)
    - [Belirli Bir Ağa Özel Bilgi Edinmek](#belirli-bir-a%c4%9fa-%c3%96zel-bilgi-edinmek)
    - [Deauth Saldırısı](#deauth-sald%c4%b1r%c4%b1s%c4%b1)

# Giriş
Bu döküman **Linux** işletim sisteminin **Kali Linux** dağıtımı üzerinde hazırlanmıştır. İlgili sistem bilgileri aşağıda bulunmaktadır.<br>
```
# lsb_release -a
>>> No LSB modules are available.
Distributor ID: Kali
Description:    Kali GNU/Linux Rolling
Release:        2020.2
Codename:       kali-rolling

# cal
>>>   May 2020        
Su Mo Tu We Th Fr Sa  
                1  2  
 3  4  5  6  7  8  9  
10 11 12 13 14 15 16  
17 18 19 20 21 [22] 23  
24 25 26 27 28 29 30  
31   
```
# Ağlara Giriş
## İletişim Nedir?
**İsim olarak**; duygu, düşünce veya bilgilerin akla gelebilecek her türlü yolla başkalarına aktarılması, bildirişim, haberleşme, komünikasyon. (TDK, 2020) <br>
**Teknik olarak**; Telefon, telgraf, televizyon, radyo vb. araçlardan yararlanarak yürütülen bilgi alışverişi, bildirişim, haberleşme, muhabere, komünikasyon. (TDK, 2020)
## Ağ Nedir?
Kendisini oluşturan yapıda çalışan, en az iki birimin ortak bir amaç için daha önce belirledikleri protokollerle bir iletişim hattını kullanarak yaptıkları haberleşme ya da **iletişim sisteminin** genel adıdır.
## İnternet Nedir?
İrili ufaklı bir çok ağın birleşerek oluşturdukları, dünyada sayısı yüz milyonları bulan cihazları birbirlerine bağlayıp işlem yapmasını sağlayan bir **ağdır**.
## Önemli Ağ Terimleri
### Sunucu
Kısaca sunucu; bulundukları ağlarda diğer ağ bileşenlerinin kendilerine erişip işlem yapmalarını sağlayan, genellikle ortak bir amaç için çalışan, kendi kaynaklarını erişime açmış cihazlardır. Genellikle **client (istemci)** cihazlardan güçlüdürler.
### Hyperconverged Cihazlar
Sanal platformlar için geliştirilmiş özel ürünlerdir. Kısaca; Data Center'larda bulunan donanımları (Storage, SAN Switch vd.) birleştirerek tek bir mimari çatı altında toplayan, yönetimi, ekonomiyi ve performansı birleştiren ürünlerdir.
### Uç Sistemler - Uç Birimler
Uç sistemler terimi tek bir cihazı temsil etmemektedir. Hostlardan (sunucu) hizmet alan ya da tek başına çalıştığında da işlem gücüne sahip olan cihazların (laptop, masaüstü, akıllı telefon, TV vd.) tümüne **Uç Sistemler** denmektedir.
### Paketler
Demiştik ki İnternet; cihazların birbirleriyle iletişime geçip işlem yapmasını sağlayan bir **ağdır**. Bu cihazlar birbirleriyle iletişime geçerken **paket**lerden yararlanırlar. Yani bir cihazın başka bir cihaz ile  ileteceği veriye, ilgili başlıkları (**header**, web geliştirme ile ilgilenenler bilirler -> text/html vb.) ekleyip, tek seferde ağa bırakılacak maksimum veri miktarına göre **(MTU)** küçük parçalara bölme işlemi sonucunda elde edilen **veri parçacıkları**dır.
### Veri İletişimi (Data Transmission)
Bir ağı oluşturan hostların (sunucu) ve uç sistemlerin aralarında yapmış oldukları veri alış-verişine verilen isimdir. Veri iletiminde beş bileşen vardır. Bu beş bileşenin yegane amacı **veriyi istenilen zamanda, doğru hedefe, veri kaybı olmadan iletmektir**. Veri İletişimi'nin beş bileşeni:
- **Sender (Gönderen)**
  - Ağ ortamında mesajı oluşturan ve oluşturduğu mesajı ortama bırakan cihazlardır. Genellikle host (sunucu)'lardır.
- **Receiver (Alıcı)**
  - Ağ ortamında kendisi için sender tarafından gönderilen mesajı alan cihazlardır. Genellikle uç sistemlerdir. Aynı zamanda alıcılar **hedef** olarak da adlandırılabilirler.
- **Message (Mesaj)**
  - Sender'dan receiver'a gönderilmesi için ağ ortamına bırakılan veriye mesaj denir.
- **Medium (Ortam)**
  - Sender'dan receiver'a mesajın ulaşması için kullanılan yola medium (ortam) denir. Bilgisayar ağında bu yol; fiber optik kablolar, bakır kablolar ve kablosuz ortamlardır.
- **Protocol (Protokol)**
  - Sender'dan receiver'a bir medium kullanılarak gidecek mesajın, eksiksiz ve zamanında iletilmesinin sağlanması için önceden tanımlanmış kurallar bütünüdür. 

![1-data-transmission](./assets/1-data-transmission.jpg)
### Ağ Protokolü Nedir?
Farklı ağ ortamları arasında iletişimin sağlanmasında, adreslemenin yapılmasında, hata kontrolünün yapılmasında ve olası hata durumunda paketlerin yeniden gönderilmesinde sorumlu olan protokollerin tamamıdır.
### MAC Adresi
Aslında bir Ağ protokolü **değildir**. Network'de (ağ) bulunan her cihazın sahip olduğu, başka ağlara dahil olduğunda bile değişmeyen bir adresi vardır. Bu adres **48 bitlik MAC** adresidir. Fakat **istenirse bu adres manuel olarak değiştirilebilir!** <br>
Ağda bulunan her bir cihaza ait ağ kartı (NIC) tek bir MAC adresine sahiptir (örnek: 281,321,675,498,362). 
### ISP 
İnternet Servis Sağlayıcı demektir. İnternet'i belirli ücretler veya yasalar, sözleşmeler vb. karşılığında bize ulaştıran şirket veya kuruluşlardır (Türk Telekom vb.).
### IP
Fiziksel ya da sanal olarak bir ağa katılan her bir cihazın(birimin) sahip olduğu (olması gereken) ve dahil olduğu ağda sadece o cihaz için tahsis edilmiş, çeşitli kurallara göre tasarlanmış sayısal kimliktir. Günümüzde iki sürümü bulunmaktatır. Versiyon 4 (IP/v4) ve Versiyon 6 (IP/v6). <br>
Local IP adreslerimiz ile Public IP adreslerimiz farklı kavramlardır. <br>
Local IP; kullandığımız cihaza, interneti aldığı cihaz (modem vb.) tarafından atanan IP adresidir. `ifconfig` komutu ile Local IP adresimizi öğrenebiliriz.
```
# ifconfig
>>> eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.87  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::76e6:e2ff:fe28:35bc  prefixlen 64  scopeid 0x20<link>
        ether 74:e6:e2:28:35:bc  txqueuelen 1000  (Ethernet)
        RX packets 148083  bytes 182884871 (174.4 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 67865  bytes 10050056 (9.5 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
<br>
Public IP; bize ISP(İnternet Servis Sağlayıcı Türk Telekom vb.) tarafından verilir. İnternet'e bu IP adresi ile çıkarız.

### DNS (Domain Name Server)
İnternet ağ yapısında her cihaz bir IP adresine sahiptir. Kısaca DNS'ler IP adreslerinin domain'lere (alan adı) aktarılmasını sağlar. <br>
Aslında `www.domainim.com` 'a gittiğimizde `domain.com`'a değil, bu domainin host edildiği sunucunun (host) IP adresine istek atarız. Bu IP adresini çözümleyen sistem DNS'dir. Ufak bir örnek yaparak daha iyi pekişmesini sağlayalım.
```
# ping google.com
>>> PING google.com (216.58.206.174) 56(84) bytes of data.
64 bytes from sof02s27-in-f14.1e100.net (216.58.206.174): icmp_seq=1 ttl=53 time=40.5 ms
```
Gördüğümüz gibi `google.com`'a gitmek istediğimizde, o domainin IP adresini (216.58.206.174) çözümleyen sistemdir.
### Arp (Address Resolution Protocol)
OSI Layer 3'de verilen IP adreslerinin, Layer 2'deki MAC adreslerine çözümlenmesini sağlayan bir protokoldür. **STD 37** kodlu bir İnternet standardıdır.
### VPN (Virtual Private Network)
Sanal Özel Ağ demektir. **Uzaktan** erişim yoluyla **farklı ağlara** bağlanabilmeyi sağlayan teknolojidir. VPN sanal bir ağ uzantısı oluşturduğundan, VPN kullanarak bir ağa sanal olarak bağlandığımız cihaz, sanki **fiziksel olarak bağlıymış gibi** veri alış-verişi yapabilir. 

## Cihazların İletişime Başlaması
Cihazlar iletişime başlamadan önce kendi aralarında bir iletişim şekli belirlerler. Aynı zamanda veri iletiminin doğru ve düzenli olması açısından bir de protokol belirlenir.
### Handshake (3-Way Handshake)
El sıkışma anlamına gelir. İletişime başlayacak iki cihazın da karşılıklı anlaşmasına **handshake** denir. TCP protokolüne göre iki taraf iletişime el sıkışarak başlar.
### Syn Paketi
Senkronizasyon paketi anlamına gelir. İletişim başlatmak isteyen cihaz, iletişime geçmek istediği cihaza **ilk önce** Syn paketi gönderir.
### ACK Paketi
Kabul paketi anlamına gelir. İletişime geçilmek istenen cihaz kendisine Syn paketi gelmesi durumunda sender'a **Syn + ACK** paketi gönderir ve sinyali alıp cevap verebilir durumda olduğunu işaret eder.

![2three-way-handshake.png](./assets/2three-way-handshake.png)

## VPN Kullanımı
Dilersek işlemlerimize başlamadan önce www.whatismyip.com üzerinden Public IP adresimizi görüntüleyebiliriz. <br>
VPN kullanmak için `VPN Book` denilen aracı kullanmaktayız. <br>
Öncelikle bir adet VPN Book'a ihtiyacımız vardır. Bunu internette arama yaparak rahat bir şekilde temin edebiliriz (www.vpnbook.com vb.). OpenVPN türünde bir VPN Book indirmemiz gerekmektedir. <br>
İndirdiğimiz VPN Book'ları `openvpn` komutu ile çalıştırarak VPN'i aktif edebiliriz. Username ve Password genelde VPN Book'u indirdiğimiz sitede bulunmaktadır. En son satırdaki output'u alırsak VPN'i başarılı bir şekilde aktif etmişiz demektir. `ctrl + c` kombinasyonu ile işlemi bitirebiliriz.
```
# openvpn vpnbook-fr8-tcp80.ovpn 
>>> Fri May 22 00:48:21 2020 Initialization Sequence Completed
```
## DNS Değiştirmek
`/etc/dhcp/dhclient.conf` dosyasını herhangi bir text editör ile açıyoruz. <br>
`#prepend domain-name-servers` satırını bulup başındaki `#` işaretini kaldırıyoruz. Comment Line olarak düşünebiliriz. <br>
`cat /etc/resolv.conf` komutu ile DNS'lerimizin değişip değişmediğini görebiliriz. Eğer burada eklediğimiz DNS'leri göremediysek direkt bu dosyayı değiştirebiliriz (nameserver satırı). <br>
Unutmamalıyız ki bu işlemi bilgisayarımızı her açıp kapattığımızda **tekrarlamalıyız!** 
```
# nano /etc/dhcp/dhclient.conf
# cat /etc/resolv.conf
>>> # Generated by NetworkManager
search home
nameserver 192.168.1.1

# nano /etc/resolv.conf
```

# Dark Web
Öncelikle bu bölüme **Dark Web != Deep Web** diyerek başlamakta fayda var :stuck_out_tongue_winking_eye: <br>
İnsanların erişiminin olmadığı, arama motorlarının indexlemediği herhangi bir içerik **Deep Web** içerisinde yer almaktadır/ **Deep Web** olarak adlandırılmaktadır. Bunlara örnek olarak Cloud'a atılan fakat sadece bizim erişimimiz olan dosyalar vs. verilebilir. <br>
**Dark Web** ise; insanların erişimlerinin kısıtlandığı, özel VPN'ler ile ([Tor Browser](www.torproject.org)) girilebilen **web siteleri topluluğu**dur. <br>
Kısaca Tor Browser ise; kullandığımız süre boyunca VPN'imizi sürekli değiştirmemizi sağlar ve IP adresimizi sürekli olarak değiştirir. Bu sayede IP adresimizin izinin sürülmesi zorlaşır. **VPN içinde VPN içinde VPN** şeklinde düşünebiliriz.

![Tor Browser](./assets/3-tor-browser.png)

## Tor Browser Yüklemek
Kurulum için VPN'i aktif etmemiz kurulum adına faydalı olacaktır (bir çok ülkede yasaklı olmasından dolayı). <br>
Öncelikle `apt-get install tor` komutu ile Tor Browser için gerekli olan paketleri yükleyelim.
```
# apt-get install tor
```
- [Tor Browser indirme sayfası](https://www.torproject.org/download/)'na giderek işletim sistemimize uygun olan kurulum paketini indirebiliriz. 
- `cd` komutu sayesinde kurulum paketini indirdiğimiz dizine gidebiliriz. Ardından `tar -xvf` komutu ile indirdiğimiz arşiv dosyasını dizine çıkartabiliriz. 
- Çıkarttığımız dizine giderek `./start-tor-browser.desktop` komutu ile tor browser'ı çalıştırabiliriz.
```
# cd Downloads
# tar -xvf tor-browser
# ./start-tor-browser.desktop
```
- `root` kullanıcısı ile oturum açtıysak bize hata verecektir (root kullanıcısı ile tor browser açılamaz vb.).
- Tor Browser dosyalarını çıkarttığımız dizin içerisinde `Browser` adındaki dizine gidelim.

![Browser Dizin](./assets/4-tor-conf.png)

- `nano start-tor-browser` komutu ile tor browser SHELL Script konfigürasyon dosyasını açalım<br>
if [ "id -u" -eq 0 ]; then <br>
        complain "The Tor Browser Bundle should not be run as root.  Exiting." <br>
        exit 1 <br>
fi
- satırLARINI bulup her satır başına `#` koyalım ve yorum satırı haline getirelim ve dosyayı **kaydedip çıkalım**. 
- tekrar `./start-tor-browser.desktop` komutu ile Tor Browser'ı çalıştırabiliriz. Her adımı doğru uyguladıysak başarılı bir şekilde tarayıcımız açılacaktır.
```
# cd Browser/
# nano start-tor-browser
# ./start-tor-browser
```
- Eğer yine hata alırsak veya browser açılması takılırsa, açılış ekranından **Configure** seçeneğini seçerek **Bridge (Köprü)** üzerinden bağlanmayı deneyebiliriz. Fakat unutmamalıyız ki **ilk başta açılış biraz uzun sürmektedir**.

![Tor Browser Success](./assets/5-tor-success.png)

- `hidden wiki` araması yaparak Dark Web uzantısına sahip `.onion` uzantılı linkleri bulabiliriz.

![Hidden Wiki](./assets/6-hidden-wiki.png)

# Ufak Bir Terminal Trick'i
Dökümantasyonun kalan kısmında bolca kod/komut örnekleri göreceğiz. Linux dağıtımlarında; <br>
**Normal yetkilere sahip kullanıcılar** tarafından çalıştırılan komutlar `$` ile başlarken.
```
$ ifconfig
>>> eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.87  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::76e6:e2ff:fe28:35bc  prefixlen 64  scopeid 0x20<link>
        ether 74:e6:e2:28:35:bc  txqueuelen 1000  (Ethernet)
        RX packets 148698  bytes 183420481 (174.9 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 68290  bytes 10119801 (9.6 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
.
.
.

```
**Üst düzey yetkili root kullanıcılar** tarafından çalıştırılan komutlar `#` ile başlar.
```
# ifconfig
>>> eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.87  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::76e6:e2ff:fe28:35bc  prefixlen 64  scopeid 0x20<link>
        ether 74:e6:e2:28:35:bc  txqueuelen 1000  (Ethernet)
        RX packets 148715  bytes 183426397 (174.9 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 68308  bytes 10123370 (9.6 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
.
.
.
```

# Ağlara Saldırmak
Dökümanımızın bu bölümünde bolca `wlan0` argümanını göreceğiz. Ağ arayüzümüzü temsil eder. Benim cihazımda `wlan0` olarak gözüktüğü için argüman olarak `wlan0` gönderiyorum. **Döküman boyunca `wlan0` gördüğümüz yerlerin argüman olduğunu ve kendinize ait işlem yapmak istediğiniz ağ arayüzünüzü kullanmanız gerektiğini lütfen unutmayın.** :innocent:
- Ağ arayüzlerimizi listelemek ve öğrenmek için `ifconfig` komutunu kullanabiliriz.
- Sadece wireless arayüzlerimizi listelemek için ise `iwconfig wlan0` komutunu kullanabiliriz. Yine kendinize ait ağ arayüzünü argüman olarak göndermeniz gerektiğini lütfen unutmayınız. :innocent:
## Saldırı Öncesi Ayarlar
### MAC Adresi Değiştirmek
Cihazlar birbirleriyle iletişim kurarken MAC adresleri üzerinden iletişim kurarlar. Fakat bunu sistemsel olarak değiştirebiliriz.
- `ifconfig wlan0 down` ağ arayüzümüzü düşürüyoruz, servis dışı bırakıyoruz.
- `macchanger wlan0 --random` komutu ile ilgili ağ arayüzümüzün MAC adresini değiştiriyoruz. Çıktıdan da görüleceği üzere MAC adresi başarılı bir şekilde değişmiş oldu.
- `ifconfig wlan0 up` komutu ile tekrar ağ arayüzümüzü aktif hale getiriyoruz.
```
# ifconfig wlan0 down
# macchanger wlan0 --random
>>> Current MAC:   2a:f9:66:3e:94:53 (unknown)
Permanent MAC: 4c:bb:58:42:c3:89 (unknown)
New MAC:       82:b3:a4:1e:dd:08 (unknown)

# ifconfig wlan0 up

# ifconfig
>>> wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.105  netmask 255.255.255.0  broadcast 192.168.1.255
        ether 82:b3:a4:1e:dd:08  txqueuelen 1000  (Ethernet)
        RX packets 11961  bytes 1369251 (1.3 MiB)
        RX errors 0  dropped 2  overruns 0  frame 0
        TX packets 1262  bytes 228105 (222.7 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
### Monitor ve Managed Mod
**Ufak bir not: `wlan0` ve `wlan0mon` argümanlarının cihazdan cihaza değişebileceğini lütfen unutmayın :innocent: Kendi ağ arayüzlerinizi listelemek için `ifconfig` kullanabilirsiniz** :innocent: <br>
**Monitor Mode:** herhangi bir ağa bağlanmadan pasif olarak ilgili ağdaki tüm trafiği izlememize olanak sağlayan mod. <br>
**Managed Mode:** istemcimizin bir ağa bağlanarak hizmet aldığı mod. <br>
##### Mod Değiştirmek İçin 1. Yöntem (airmon-ng)
- `airmon-ng start wlan0` ile monitör mod'a geçebiliriz.
- `ifconfig` ile veya `iwconfig wlan0mon` ile monitör mod'a geçip geçmediğimize bakabiliriz.
- `airmon-ng stop wlan0mon` ile geri managed mod'a geçebiliriz.
```
# airmon-ng start wlan0
>>> Found 2 processes that could cause trouble.
Kill them using 'airmon-ng check kill' before putting
the card in monitor mode, they will interfere by changing channels
and sometimes putting the interface back in managed mode

    PID Name
    909 wpa_supplicant
  16148 NetworkManager

PHY     Interface       Driver          Chipset

phy0    wlan0           ath9k           Qualcomm Atheros QCA9565 / AR9565 Wireless Network Adapter (rev 01)

                (mac80211 monitor mode vif enabled for [phy0]wlan0 on [phy0]wlan0mon)
                (mac80211 station mode vif disabled for [phy0]wlan0)


# iwconfig wlan0mon
>>> wlan0mon  IEEE 802.11  Mode:Monitor  Frequency:2.462 GHz  Tx-Power=16 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:off


# airmon-ng stop wlan0mon
>>> PHY     Interface       Driver          Chipset

phy0    wlan0mon        ath9k           Qualcomm Atheros QCA9565 / AR9565 Wireless Network Adapter (rev 01)

                (mac80211 station mode vif enabled on [phy0]wlan0)

                (mac80211 monitor mode vif disabled for [phy0]wlan0mon)
```
##### Mod Değiştirmek İçin 2. Yöntem (iwconfig)
- `ifconfig wlan0 down` komutu ile ilgili ağ arayüzümüzü servis dışı bırakırız
- `iwconfig wlan0 mode monitor` ilgili ağ arayüzümüzü **monitor** moda geçiririz
- `ifconfig wlan0 up` ilgili ağ arayüzümüzü tekrar devreye sokarız
- `iwconfig wlan0` ile ilgili ağ arayüzümüzün modunu kontrol edebiliriz
```
# ifconfig wlan0 down
# iwconfig wlan0 mode monitor
# ifconfig wlan0 up
# iwconfig wlan0
>>> wlan0     IEEE 802.11  Mode:Monitor  Frequency:2.462 GHz  Tx-Power=16 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:off

```
- Geri çevirmek istersek ise aynı komutları **managed mode** için yapıyoruz.
-  `ifconfig wlan0 down` komutu ile ilgili ağ arayüzümüzü servis dışı bırakırız
- `iwconfig wlan0 mode managed` ilgili ağ arayüzümüzü **managed** moda geçiririz
- `ifconfig wlan0 up` ilgili ağ arayüzümüzü tekrar devreye sokarız
- `iwconfig wlan0` ile ilgili ağ arayüzümüzün modunu kontrol edebiliriz
```
# ifconfig wlan0 down
# iwconfig wlan0 mode managed
# ifconfig wlan0 up
# iwconfig wlan0
>>> wlan0     IEEE 802.11  ESSID:"SUPERONLINE_WiFi_9547"  
          Mode:Managed  Frequency:2.462 GHz  Access Point: 64:6D:6C:65:03:82   
          Bit Rate=39 Mb/s   Tx-Power=16 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Encryption key:off
          Power Management:off
          Link Quality=24/70  Signal level=-86 dBm  
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:1  Invalid misc:2   Missed beacon:0
```
## Ağlarla İlgili Bilgi Toplamak
### Ağları İncelemek (Sniffing)
Networkler üzerindeki trafikleri izlemeye verilen isim **sniffing**'dir.
- Öncelikle eğer monitör modda değilsek `airmon-ng start wlan0` ile monitör moda geçebiliriz.
- Teyit etmek için bir üst başlıktan bildiğimiz `iwconfig wlan0mon` komutunu kullanabiliriz.
- **Sniffing** yapmak için `airodump-ng wlan0mon` komutunu kullanabiliriz. Bu sayede etrafımızdaki ağları ve onlarla ilgili bilgileri görebiliriz. `ctrl + c` kombinasyonu ile çıkış yapabiliriz.
```
# airmon-ng start wlan0
# airodump-ng wlan0mon
```
![airodump-ng wlan0mon](./assets/7-airodump-ng.png)
**airodump-ng** sonucu gelen veriler ne anlama gelmektedir?
- **BSSID** -> MAC Adresi 
- **PWR** -> Power, ağların bize uzaklığıdır. Absolute olarak küçüldükçe bize yaklaşmaktadır. Yani -84 olarak gözüken ilk ağ -85 olana göre daha yakındadır
- **Beacons** -> Sinyaller
- **#Data** -> Elimizde olan, kullanabileceğimiz datalar
- **CH** -> Channel, veri alış-verişi hangi kanaldan yapılıyor onu göstermektedir
- **ENC** -> Encryption, ağın nasıl şifrelendiğini göstermektedir. WPA2 diğerlerine göre daha güvenlidir
- **CIPHER** -> Decrypt modeli
- **ESSID** -> Ağın adıdır
### Belirli Bir Ağa Özel Bilgi Edinmek
Temel olarak yapı şu şekildedir: `airodump-ng --channel <channel> --bssid <bssid> --write <file-name> <interface>`
- `# airodump-ng --channel 11 --bssid 64:6D:6C:65:03:82 --write deneme.txt wlan0mon` komutu ile tek bir bssid'e ait trafiği izlemeye başladık. Ve bize bu ağa bağlı cihazların MAC adresleri (**STATION**) vb. kritik bilgileri verecektir. `--write` argümanını geçersek aldığı bilgileri bir dosyaya yazacaktır.
```
# airodump-ng --channel 11 --bssid 64:6D:6C:65:03:82 --write deneme.txt wlan0mon   
```
![airodump-ng ağa özel](./assets/8-aga-ozel-airodump-ng.png)

Ağa özel bilgi edindikten sonra gelen veriler bir önceki başlığa ek olarak;
- **Frames** -> Paket alış-verişindeki paketlerin sayısını verir.
- Bu ekrandaki çıktıdan daha detaylı olan bilgi `--write` argümanı ile yazılan `.cap` uzantılı dosya içerisinde bulunur.
### Deauth Saldırısı
Deauth saldırısı kısaca hedef cihaz ile host arasındaki iletişimi keserek (**deauthentication paketleri** göndererek) hedefi ağdan düşürme saldırısıdır. Bunu da `aireplay` aracını kullanarak yapacağız. <br>
**Deauth Paketi Nedir?** <br>
Bir client (istemci/biz) bağlı olduğu kablosuz ağ ile olan bağlantısını koparmak istediğinde aslında istemci, kablosuz ağa bir deauthentication paketi gönderir ve bağlantıyı sonlandırır. Biz de bu saldırıda başkalarının (hedef) adına modemlere (kaynak) deauthentication paketleri göndereceğiz ve hedefleri ağdan düşüreceğiz.<br>
Temel komut dizimi şu şekildedir: `aireplay-ng --deauth <packets> -a <kaynak_mac> -c <hedef_mac> <interface>` <br>
Bu saldırıda mantık şu şekilde işlemektedir; **kaynak, düşürmeye çalıştığımız hedefe: 'ben senden ayrılacağım' diyor, hedef de kaynağa diyor ki: 'ben senden ayrılacağım'**. Aslında ikisi de birbirlerine bir şey demiyor. Biz kendilerinin yerlerine geçip yine kendilerine bir şeyler söylüyoruz gibi düşünebiliriz.
- `aireplay-ng --deauth 10000 -a 64:6D:6C:65:03:82 -c 0E:80:62:12:28:0D wlan0mon` komutu ile kaynak MAC ve hedef MAC'e deauth paketleri (10000 adet) yolluyoruz.
- Eğer kısa süreli ağdan düşsün ve geri bağlansın istersek 5 10 adet paket yollayabiliriz.

![aireplay-ng deauth](./assets/9-deauth.png)