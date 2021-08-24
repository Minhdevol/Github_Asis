from datetime import date
from datetime import datetime 
from random import randint
import webbrowser
import subprocess
import os
import pyttsx3
import wikipediaapi
import sys

asis = pyttsx3.init()
voices = asis.getProperty("voices")
asis.setProperty("voice",voices[1].id)

wikipediaapi.log.setLevel(level=wikipediaapi.logging.DEBUG)
out_hdlr = wikipediaapi.logging.StreamHandler(sys.stderr)
out_hdlr.setFormatter(wikipediaapi.logging.Formatter('%(asctime)s %(message)s'))
out_hdlr.setLevel(wikipediaapi.logging.DEBUG)
wikipediaapi.log.addHandler(out_hdlr)
wiki = wikipediaapi.Wikipedia(language='vi')

def speak(audio):
    print('Asis: ' + audio)
    asis.say(audio)
    asis.runAndWait()
def thời_gian():
    giờ = datetime.now().strftime("%I")
    phút = datetime.now().strftime("%M")
    speak(F"Bây giờ là {giờ} giờ {phút} phút")
def ngày():
    days = datetime.now().strftime("%d/%m/%Y")
    speak(f"Hôm nay là ngày {days}")  
def shutdownprograms():
    while True:
        speak("Bạn có muốn tắt máy tính không? [có] hoặc [không]")
        me = input("You: ").lower()
        if me == "có":
            os.system("shutdown /s /t 30")
            speak("HÃY TẮT TẤT CẢ ỨNG DỤNG CÒN ĐANG CHẠY, CHƯƠNG TRÌNH SẼ TẮT TRONG 30 GIÂY")
            break
        if me == "không":
            speak("Bạn muốn làm gì tiếp?")
            break
        else:
            speak("Hãy nhập với mệnh lệnh được cho sẵn là [có] hoặc [không]")
def detailsmod():
    while True:
        speak("Bạn có muốn lựa chọn chế độ từ khóa thông minh:")
        speak("[có] hoặc [không]")
        u = input("You: ").lower()
        if "có" in u:
            while True:
                speak("Chế độ từ khóa thông minh được [thiết lập]")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                speak("Hãy chọn chế độ với từ khóa được viết sẵn:")
                print("Asis_youtube details mode Interactive:      1")
                print("Asis_web-scraping details mode Interactive: 2")
                print("Asis_open-app details mode Interactive:     3")
                print("Asis: exit smart mode-[4]")
                me = int(input("You: "))
                if me == 1:
                    speak("Hãy nhập kênh channel youtube, bằng kí hiệu (số)")
                    print("Asis: Thư viện Asis_youtube: Youtube Channel: ")
                    print("Trực Tiếp Game(1)                Vandiril(9)       Danh sách phim[98]")
                    print("Muse Việt Nam(2)                 GEARVN(10)        Về mục lựa chọn mode[99]")
                    print("Pewdiepie(3)                     Lemuria TFT(11)   .........")
                    print("AMTECH Studio(4)                 meGAME(12)        .........")
                    print("League of Legends(5)             AnhEm TV(13)      .........")
                    print("Kurzgesagt – In a Nutshell(6)    MixiGaming(14)    .........")
                    print("Shawn TFT(7)                     Phân Tích Game(15)")
                    print("TNC Channel(8)                   UnusualVideos(16) ")
                    while True:
                        ytc = int(input("You: "))
                        if ytc == 99:
                            break
                        if ytc == 98:
                            speak("Hãy nhập danh sách phim trên youtube, bằng kí hiệu (số)")
                            print("Asis: Thư viện danh sách từ các kênh channel Youtube:")
                            print("One punch man(1)       Tensei shitara slime datta ken(2)  >NGUỒN: Muse Việt Nam")
                            print("You laugh you lose(3)  meme review(4)                     >NGUỒN: Pewdiepie")
                            print("thoát danh sách phát[99]")
                            while True:
                                choice = int(input("You: "))
                                if choice == 1:
                                    speak("Danh sách phim one punch man đang mở")
                                    webbrowser.open("https://www.youtube.com/playlist?list=PLdM751AKK4aNByWA9qP5XI2haBXOo9tAt")
                                if choice == 2:
                                    speak("Danh sách phim Tensei shitara slime datta ken đang mở")
                                    webbrowser.open("https://www.youtube.com/playlist?list=PLdM751AKK4aNYfKgHcH0AV42Per56uAXH")
                                if choice == 3:
                                    speak("Danh sách phát You laugh you lose đang mở")
                                    webbrowser.open("https://www.youtube.com/playlist?list=PLYH8WvNV1YEm6ETE_AS0nV2sKIsU2cUPW")
                                if choice == 4:
                                    speak("Danh sách phát meme review đang mở")
                                    webbrowser.open("https://www.youtube.com/playlist?list=PLYH8WvNV1YEn_iiBMZiZ2aWugQfN1qVfM")
                                if choice == 99:
                                    break
                        if ytc == 16:
                            speak("Kênh channel UnusualVideos đang mở")
                            webbrowser.open("https://www.youtube.com/channel/UCpnkp_D4FLPCiXOmDhoAeYA")
                        if ytc == 15:
                            speak("Kênh channel Phân Tích Game đang mở")
                            webbrowser.open("https://www.youtube.com/channel/UCAmiHmhyH7irW2Yr_RoI0uA")
                        if ytc == 14:
                            speak("Kênh channel MixiGaming đang mở")
                            webbrowser.open("https://www.youtube.com/channel/UCA_23dkEYToAc37hjSsCnXA")
                        if ytc == 13:
                            speak("Kênh channel AnhEm TV đang mở")
                            webbrowser.open("https://www.youtube.com/channel/UCDri2yZO_tqdD70bK-D7iQg")
                        if ytc == 12:
                            speak("Kênh channel meGAME đang mở")
                            webbrowser.open("https://www.youtube.com/channel/UCT9aAKhmaMLO8QxmHrAzSXA")
                        if ytc == 11:
                            speak("Kênh channel Lemuria TFT đang mở")
                            webbrowser.open("https://www.youtube.com/channel/UCi0fnpTfSmdH76N6MNgPdEQ")
                        if ytc == 10:
                            speak("Kênh channel GEARVN đang mở")
                            webbrowser.open("https://www.youtube.com/channel/UCdxRpD_T4-HzPsely-Fcezw")
                        if ytc == 9:
                            speak("Kênh channel Vandiril đang mở")
                            webbrowser.open("https://www.youtube.com/channel/UCZ-oWkpMnHjTJpeOOlD80OA")
                        if ytc == 8:
                            speak("Kênh channel TNC Channel đang mở")
                            webbrowser.open("https://www.youtube.com/channel/UCvLGkK-wBBaoXwV71Tgx08Q")
                        if ytc == 7:
                            speak("Kênh channel Shawn TFT đang mở")
                            webbrowser.open("https://www.youtube.com/channel/UC4_xpnCfHTwDJ49WXHQquug")
                        if ytc == 6:
                            speak("Kênh channel Kurzgesagt – In a Nutshell đang mở")
                            webbrowser.open("https://www.youtube.com/channel/UCsXVk37bltHxD1rDPwtNM8Q")
                        if ytc == 5:
                            speak("Kênh channel League of Legends đang mở")
                            webbrowser.open("https://www.youtube.com/channel/UC2t5bjwHdUX4vM2g8TRDq5g")
                        if ytc == 4:
                            speak("Kênh channel AMTECH Studio đang mở")
                            webbrowser.open("https://www.youtube.com/channel/UCJ9nxbwgqwwjWuGTQPekeTQ")
                        if ytc == 3:
                            speak("kênh channel Pewdiepie đang mở")
                            webbrowser.open("https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw")
                        if ytc == 2:
                            speak("Kênh channel Muse Việt Nam đang mở")
                            webbrowser.open("https://www.youtube.com/channel/UCott96qGP5ADmsB_yNQMvDA")
                        if ytc == 1:   
                            speak("Kênh channel Trực Tiếp Game đang mở")
                            webbrowser.open("https://www.youtube.com/channel/UCc_gMV4N9vJtpy7GcMUHaVw")                 
                        else:
                            speak("Xin hãy nhập đúng kí hiệu (số) đã cho")
                if me == 2:
                    speak("Hãy nhập qua kí hiệu (số), từ các danh mục tiện lợi dược viết sẵn:")
                    print("Wikipedia(1)    Phim Hàn(5)      Nonolive(9)")
                    print("Facebook(2)     Gmail(6)         .....")
                    print("Animehay.tv(3)  Google Earth(7)  .....")
                    print("Động Phim(4)    Shopee(8)        Về mục lựa chọn[99]")
                    while True:
                        short = int(input("You: "))
                        if short == 1:
                            speak("Bạn muốn tìm kiếm nội dung gì ở wikipedia?")
                            while True:
                                noidung = input("You: ").lower()
                                if "ngừng wiki" in noidung:
                                    break
                                else:
                                    timkiem = wiki.page(f'{noidung}')
                                    speak(timkiem.summary)
                                    speak("[ngừng wiki] nếu bạn muốn thoát và ngừng dùng wikipedia")
                        if short == 2:
                            speak("Facebook đang mở")
                            webbrowser.open("https://www.facebook.com/")
                        if short == 3:
                            speak("Anime hay đang mở")
                            webbrowser.open("https://animehay.tv/")
                        if short == 4:
                            speak("Động Phim đang mở")
                            webbrowser.open("https://dongphym.com/")
                        if short ==5:
                            speak("Phim Hàn đang mở")
                            webbrowser.open("http://www.phymhan.com/")
                        if short == 6:
                            speak("Gmail đang mở")
                            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                        if short == 7:
                            speak("Google Earth đang mở")
                            webbrowser.open("https://earth.google.com/web/@12.37269667,109.44710412,-4095.49886217a,8155037.67908692d,35y,3.73110197h,0t,0r")
                        if short == 8:
                            speak("Shopee đang mở")
                            webbrowser.open("https://shopee.vn/?utm_source=an_17209090000&utm_medium=affiliates&utm_campaign=4jcz9mgzpk8w-&utm_content=c7cd9271b3af48eba1c1d89f0bf322a7-34745-101654&af_siteid=an_17209090000&pid=affiliates&c=4jcz9mgzpk8w-&af_click_lookback=7d&af_viewthrough_lookback=1d&is_retargeting=true&af_reengagement_window=7d&af_sub_siteid=c7cd9271b3af48eba1c1d89f0bf322a7-34745-101654")
                        if short == 9:
                            speak("Nonolive đang mở")
                            webbrowser.open("https://www.nonolive.com/69696969?fbclid=IwAR0b5nheeYMGnSHWbHZWpr9UKqn8eGt4G438R9vEuqt3m5i0gWYk4vGmcOQ")
                        if short == 99:
                            break
                        else:
                            speak("Xin hãy nhập đúng kí hiệu (số) đã cho")
                if me == 3:
                    speak("Hãy nhập kí hiệu (số), với từ khóa được viết sẵn")
                    print("Google Chorme(1)       Garena(4)                       ...........")
                    print("Microsoft Egde(2)      League of Legends PBE(5)        Về lựa chọn mode[99]")
                    print("Albion Online(3)       Discord(6)")
                    while True:
                        choice = int(input("You: "))
                        if choice == 1:
                            speak("Trình duyệt Google Chrome đang mở")
                            cmd = "C:/Program Files/Google/Chrome/Application/chrome.exe"
                            result = subprocess.run(cmd, shell=True)
                        if choice == 2:
                            speak("Trình duyệt Microsoft Egde đang mở")
                            cmd = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
                            result = subprocess.run(cmd, shell=True)
                        if choice == 3:
                            speak("Albion Online đang mở")
                            cmd = "D:/LITTE GAME/launcher/AlbionLauncher.exe"
                            result = subprocess.run(cmd, shell=True)
                        if choice == 4:
                            speak("Garena đang mở")
                            cmd = "C:/Program Files (x86)/Garena/Garena/Garena.exe"
                            result = subprocess.run(cmd, shell=True)
                        if choice == 5:
                            speak("Liên Minh Huyền Thoại P.B.E đang mở")
                            cmd = "D:/Riot Games/Riot Client/RiotClientServices.exe"
                            result = subprocess.run(cmd, shell=True)
                        if choice == 6:
                            speak("Discord đang mở")
                            cmd = "C:/Users/this pc/AppData/Local/Discord/app-1.0.9002/Discord.exe"
                            result = subprocess.run(cmd, shell=True)
                        if choice == 99:
                            break
                        elif choice == "":
                            speak("Xin hãy nhập đúng kí hiệu (số) đã cho")
                if me == 4:
                    break
        if "không" in u:
            speak("Bạn muốn làm gì tiếp?")
            break
        else:
            speak("Xin hãy nhập đúng kí hiệu (số) đã cho")
def google():
    speak("Bạn muốn tìm kiếm gì ở google?")
    while True:
       search = input("You: ")
       if "hủy tìm kiếm" in search:
           speak("Bạn muốn làm gì tiếp?")
           break
       url=f"https://www.google.com/search?q={search}"
       webbrowser.get().open(url)
       speak(f"Đây là kết quả mà tôi tìm kiếm được, với từ khóa {search}")
       speak("[hủy tìm kiếm] nếu bạn không muốn tiếp tục tìm kiếm qua google")
def youtube():
    speak("Bạn muốn tìm kiếm gì ở youtube?")
    while True:
        search = input("You: ")
        if "hủy tìm kiếm" in search:
            speak("Bạn muốn làm gì tiếp?")
            break
        url=f"https://www.youtube.com/search?q={search}"
        webbrowser.get().open(url)
        speak(f"Đây là kết quả mà tôi tìm kiếm được, với từ khóa {search}")
        speak("[hủy tìm kiếm] nếu bạn không muốn tiếp tục tìm kiếm qua youtube")
def game():
    speak("Tôi có trò búa kéo bao, bạn có muốn chơi")
    speak("[có] hoặc [không]")
    player = input("You: ").lower()
    if "có" in player:
        while True:
            speak("Bạn chọn búa kéo hay bao?")
            player = input("You: ").lower()
            computer = randint(0,2)
            if computer == 0:
                computer = "búa"
            if computer == 1:
                computer = "kéo"
            if computer == 2:
                computer = "bao"
            if "hủy trò chơi" in player:
                speak("Bạn muốn làm gì tiếp?")
                break
            
            print("////////////////")
            print("Bạn chọn :" + player + "///")
            print("Asis chọn:" + computer +"///")
            print("////////////////")
            speak(f"Bạn chọn {player} Asis chọn {computer}")
            
            if player == computer:
                reslut = "kết quả bạn HÒA"
                speak(reslut)
                speak("[hủy trò chơi] nếu bạn không chơi tiếp")
            else:
                if player == "búa":
                    if computer == "kéo":
                        reslut = "kết quả bạn THẮNG"
                        speak(reslut)
                        speak("[hủy trò chơi] nếu bạn không chơi tiếp")
                    else:
                        reslut = "kết quả bạn THUA"
                        speak(reslut)
                        speak("[hủy trò chơi] nếu bạn không chơi tiếp")
                elif player == "kéo":
                    if computer == "búa":
                        reslut = "kết quả bạn THUA"
                        speak(reslut)
                        speak("[hủy trò chơi] nếu bạn không chơi tiếp")
                    else:
                        reslut = "kết quả bạn THẮNG"
                        speak(reslut)
                        speak("[hủy trò chơi] nếu bạn không chơi tiếp")
                elif player == "bao":
                    if computer == "búa":
                        reslut = "kết quả bạn THẮNG"
                        speak(reslut)
                        speak("[hủy trò chơi] nếu bạn không chơi tiếp")
                    else:
                        reslut = "kết quả bạn THUA"
                        speak(reslut)
                        speak("[hủy trò chơi] nếu bạn không chơi tiếp")
def bye():
    hour = datetime.now().hour
    if hour >=6 and hour<12:
        speak("Chúc bạn buổi sáng tốt lành")
    elif hour >=12 and hour<14:
        speak("Chúc bạn buổi trưa tốt lành")
    if hour >=14 and hour<18:
        speak("Chúc bạn buổi chiều tốt lành")
    if hour >=18 and hour<24:
        speak("Chúc bạn buổi tối tốt lành")
def wellcome():
    hour = datetime.now().hour
    if hour >=6 and hour<12:
        speak("Chào buổi sáng")
    elif hour >=12 and hour<14:
        speak("Chào buổi trưa")
    if hour >=14 and hour<18:
        speak("Chào buổi chiều")
    if hour >=18 and hour<24:
        speak("Chào buổi tối")
    speak('Tôi là trợ lí ảo Asis, tôi có thể làm gì cho bạn?')

if __name__ =="__main__":
    wellcome()
    while True:
        you = input("You: ").lower()
        if "bye" in you:
            bye()
            break
        if "ngày" in you:
            ngày()
        if "trò chơi" in you:
            game()
        if "giờ" in you:
            thời_gian()
        if "thời gian" in you:
            thời_gian()
        if "google" in you:
            google()
        if "youtube" in you:
            youtube()
        if "mode" in you:
            detailsmod()
        if "tắt laptop" in you:
            shutdownprograms()
        
        
