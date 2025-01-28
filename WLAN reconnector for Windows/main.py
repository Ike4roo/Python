import os
import time
import locale
import ctypes
import tkinter
import subprocess
from tkinter import messagebox as mb

#put below a full path where this script will be always located:
path = 'C:\\scripts\\AutoWLAN'
#encoding of .txt export file, normally utf-8
encode = 'utf-8'

#change name of your connection on line below:
interface_name = 'WLAN'
ssid_name = 'WiFi_SSID'
#PS: to check it, go to Network Connections list and copy name of connection you want
#PPS: Before put SSID, your machine should be already authorized in the network with this SSID

#----//----//----//----//----//----//----//----//----
#----//----//----//----//----//----//----//----//----
#----//----//----//----//----//----//----//----//----

#Don't make any changes below if you don't know what for!

#What lang
def lang(os_lang):
    if 'en_EN' in os_lang:
        iface_stat_name = 'Connected'
        lang = 'En'
    elif 'ru_RU' in os_lang:
        iface_stat_name = 'Подключен'
        lang = 'Ru'
    elif 'es_ES' in os_lang:
        iface_stat_name = 'Conectado'
        lang = 'Es'
    else:
        iface_stat_name = 'Locale is not defined'
    #print(status)
    return iface_stat_name


#Message txt_msg with type msg_type
def msg(txt_msg, msg_type):
    if msg_type == 'warning':
        mb.showwarning('Warning',txt_msg)
    elif msg_type == 'info':
        mb.showinfo('All is ok',txt_msg)
    elif msg_type == 'error':
        mb.showerror('Error',txt_msg)
    else:
        print('error occured transferring type of message!')
    return 0

#admin rights
def admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0



#Interface status
def check_iface_stat():
    if iface_stat_name in interface:
        iface_stat = 'Up'
        write_file()
    else:
        iface_stat = 'Down'
        write_file()
        connect()
    return iface_stat

#func file write
def write_file():
    with open('history.txt', 'a', encoding = encode) as file:
        file.write('At: ' + now + ' ' + interface_name + ' was ' + iface_stat + '\n')
        #file.write(locale check-word is ' + iface_stat_name + ')
    file.close

#interface up func
def connect():
    os.system('netsh wlan connect name=' + ssid_name + ' ssid=' + ssid_name + ' interface=' + interface_name)




#----//----//----//----//----//----//----//----//-----

#Time on a machine
now = time.ctime()

#Locale
os_lang = locale.getdefaultlocale()

#Connection status
netsh_interface = subprocess.check_output('netsh interface show interface ' + interface_name, shell=True)
interface = netsh_interface.decode('cp866')
#Language <-> what func
iface_stat_name = lang(os_lang)
iface_stat = check_iface_stat()







    

    

    
# else:
#     txt_msg = 'Something awful. I cannot start!'
#     msg_type = 'error'
#     msg(txt_msg, msg_type)

    





#----//----//----//----//----//----//----//----//-----













# def wlancon(status):
#     global interface
#     #os.system('netsh interface show interface WLAN')
#     if status in os.system('netsh interface show interface {interface_name}'):
#         interface = 'On'
#     else:
#         interface = 'Down'





#основное тело программы
# if admin() == True:
#     txt_wr_1 = lang(os_lang)





#print(lang(os_lang))
#print(wlancon(status))



#print(lang(os_lang))

# if status != 'null':
#     print('OS is defined')
# else:
#     print(status)

#mb.showinfo('Not defined locale!', 'Your locale is not supported! Modify script and add yours.')







# def wlancon(status):
#     con_res = os.system('netsh interface show interface WLAN')
#     if status in con_res:
#         status = 'on'
#         return status
#     else:
#         status = 'off'
#         return status 



    # doc = open(script_path + '\\laststat.txt','r')
    # timenow = time.ctime()
    # doc.write('Try to connect to WLAN at ' + timenow + '\n')

#wlancon()




#def wfile():






# def search_str(path_to_scr + '\\laststat.txt', word_stat_en, word_stat_ru):
#     with open(path_to_scr + '\\laststat.txt', 'r') as file:
#         # читаем файл
#         content = file.read()
#         # смотрим строку
#         if word_stat_en or word_stat_ru in content:
#             doc = open(path_to_scr + '\\sessions.txt','a')  # открытие в режиме append
#             timenow = time.ctime()
#             doc.write('Already connected. Checked at ' + timenow + '\n')  # запись
#         else:
#             print('string does not exist in a file')

# search_str(r'E:\demos\files_demos\account\sales.txt', 'laptop')

# def is_admin():
#     try:
#         return os.getuid() == 0
#     except AttributeError:
#         return ctypes.windll.shell32.IsUserAnAdmin() != 0

# if is_admin() == True:
#     #запуск скрипта
#     #root = tkinter.Tk()
#     #root.withdraw()
#     #mb.showinfo('Good','Adm is on')



#     plscommand = 'netsh interface show interface WLAN > laststat.txt'
#     os.system(plscommand)
#     doc = open(path_to_scr + '\\laststat.txt','r')


#     plsconnect = 'netsh wlan connect name="IR-WFv" ssid="IR-WFv" interface="WLAN"'
#     os.system(plsconnect)
#     #mb.showinfo(f"Connected to WLAN!")

#     doc = open(path_to_scr + '\\sessions.txt','a')  # открытие в режиме append
#     timenow = time.ctime()
#     doc.write('Try to connect to WLAN at ' + timenow + '\n')  # запись
    
#     doc.close()  # закрытие файла
    
# else:
#     root = tkinter.Tk()
#     root.withdraw()
#     mb.showerror('WLAN RECONNECTOR ERROR!','Use adm rights to use this script!')
