from datetime import date
from datetime import datetime 
import random
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
        elif me == "không":
            speak("Bạn muốn làm gì tiếp?")
            break
        else:
            speak("Hãy nhập với mệnh lệnh được cho sẵn là [có] hoặc [không]")
def detailsmod():
            while True:
                muc = "Xin hãy nhập đúng kí hiệu (số) đã cho"
                thit = "Đây là thư viện đã cho, hãy nhập kí hiệu [số] để kích hoạt: "
                nec = "đang mở"
                speak("Chế độ từ khóa thông minh được [thiết lập]")
                print("="*50)
                speak("Hãy chọn chế độ với từ khóa được viết sẵn:")
                print("[1]_Youtube details mode Interactive")
                print("[2]_Web-scraping details mode Interactive")
                print("[3]_Open-app details mode Interactive")
                print("[4]_Exit mode")
                me = int(input("You: "))
                if me == 4:
                    speak("Bạn muốn làm gì tiếp?")
                    break
                elif me == 1:
                    speak(f"{thit}")
                    print("Trực Tiếp Game(1)                Vandiril(9)       Danh sách phim[98]")
                    print("Muse Việt Nam(2)                 GEARVN(10)        Về mục lựa chọn[99]")
                    print("Pewdiepie(3)                     Lemuria TFT(11)   .........")
                    print("AMTECH Studio(4)                 meGAME(12)        .........")
                    print("League of Legends(5)             AnhEm TV(13)      .........")
                    print("Kurzgesagt – In a Nutshell(6)    MixiGaming(14)    .........")
                    print("Shawn TFT(7)                     Phân Tích Game(15)")
                    print("TNC Channel(8)                   UnusualVideos(16) ")
                    while True:
                        fcg = "Kênh channel"
                        ytc = int(input("You: "))
                        if ytc == 99:
                            break
                        elif ytc == 98:
                            speak(f"{thit}")
                            print("One punch man(1)       Tensei shitara slime datta ken(2)  >NGUỒN: Muse Việt Nam")
                            print("You laugh you lose(3)  meme review(4)                     >NGUỒN: Pewdiepie")
                            print("thoát danh sách phát[99]")
                            while True:
                                choice = int(input("You: "))
                                if choice == 99:
                                    break
                                elif choice == 1:
                                    speak(f"Danh sách phim one punch man {nec}")
                                    webbrowser.open("https://www.youtube.com/playlist?list=PLdM751AKK4aNByWA9qP5XI2haBXOo9tAt")
                                elif choice == 2:
                                    speak(f"Danh sách phim Tensei shitara slime datta ken {nec}")
                                    webbrowser.open("https://www.youtube.com/playlist?list=PLdM751AKK4aNYfKgHcH0AV42Per56uAXH")
                                elif choice == 3:
                                    speak(f"Danh sách phát You laugh you lose {nec}")
                                    webbrowser.open("https://www.youtube.com/playlist?list=PLYH8WvNV1YEm6ETE_AS0nV2sKIsU2cUPW")
                                elif choice == 4:
                                    speak(f"Danh sách phát meme review {nec}")
                                    webbrowser.open("https://www.youtube.com/playlist?list=PLYH8WvNV1YEn_iiBMZiZ2aWugQfN1qVfM")
                                else:
                                    speak(f"{muc}")
                        elif ytc == 16:
                            speak(f"{fcg} UnusualVideos {nec}")
                            webbrowser.open("https://www.youtube.com/channel/UCpnkp_D4FLPCiXOmDhoAeYA")
                        elif ytc == 15:
                            speak(f"{fcg} Phân Tích Game {nec}")
                            webbrowser.open("https://www.youtube.com/channel/UCAmiHmhyH7irW2Yr_RoI0uA")
                        elif ytc == 14:
                            speak(f"{fcg} MixiGaming {nec}")
                            webbrowser.open("https://www.youtube.com/channel/UCA_23dkEYToAc37hjSsCnXA")
                        elif ytc == 13:
                            speak(f"{fcg} AnhEm TV {nec}")
                            webbrowser.open("https://www.youtube.com/channel/UCDri2yZO_tqdD70bK-D7iQg")
                        elif ytc == 12:
                            speak(f"{fcg} meGAME {nec}")
                            webbrowser.open("https://www.youtube.com/channel/UCT9aAKhmaMLO8QxmHrAzSXA")
                        elif ytc == 11:
                            speak(f"{fcg} Lemuria TFT {nec}")
                            webbrowser.open("https://www.youtube.com/channel/UCi0fnpTfSmdH76N6MNgPdEQ")
                        elif ytc == 10:
                            speak(f"{fcg} GEARVN {nec}")
                            webbrowser.open("https://www.youtube.com/channel/UCdxRpD_T4-HzPsely-Fcezw")
                        elif ytc == 9:
                            speak(f"{fcg} Vandiril {nec}")
                            webbrowser.open("https://www.youtube.com/channel/UCZ-oWkpMnHjTJpeOOlD80OA")
                        elif ytc == 8:
                            speak(f"{fcg} TNC Channel {nec}")
                            webbrowser.open("https://www.youtube.com/channel/UCvLGkK-wBBaoXwV71Tgx08Q")
                        elif ytc == 7:
                            speak(f"{fcg} Shawn TFT {nec}")
                            webbrowser.open("https://www.youtube.com/channel/UC4_xpnCfHTwDJ49WXHQquug")
                        elif ytc == 6:
                            speak(f"{fcg} Kurzgesagt – In a Nutshell {nec}")
                            webbrowser.open("https://www.youtube.com/channel/UCsXVk37bltHxD1rDPwtNM8Q")
                        elif ytc == 5:
                            speak(f"{fcg} League of Legends {nec}")
                            webbrowser.open("https://www.youtube.com/channel/UC2t5bjwHdUX4vM2g8TRDq5g")
                        elif ytc == 4:
                            speak(f"{fcg} AMTECH Studio {nec}")
                            webbrowser.open("https://www.youtube.com/channel/UCJ9nxbwgqwwjWuGTQPekeTQ")
                        elif ytc == 3:
                            speak(f"{fcg} Pewdiepie {nec}")
                            webbrowser.open("https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw")
                        elif ytc == 2:
                            speak(f"{fcg} Muse Việt Nam {nec}")
                            webbrowser.open("https://www.youtube.com/channel/UCott96qGP5ADmsB_yNQMvDA")
                        elif ytc == 1:   
                            speak(f"{fcg} Trực Tiếp Game {nec}")
                            webbrowser.open("https://www.youtube.com/channel/UCc_gMV4N9vJtpy7GcMUHaVw")                 
                        else:
                            speak(f"{muc}")
                elif me == 2:
                    speak(f"{thit}")
                    print("Wikipedia(1)    Phim Hàn(5)      Nonolive(9)")
                    print("Facebook(2)     Gmail(6)         Du lịch online(10)")
                    print("Animehay.tv(3)  Google Earth(7)  Zalo(11)")
                    print("Động Phim(4)    Shopee(8)        Python class(12)")
                    print("...........     ............     Về mục lựa chọn[99]")
                    while True:
                        short = int(input("You: "))
                        if short == 99:
                            break
                        elif short == 1:
                            speak("Bạn muốn tìm kiếm nội dung gì ở wikipedia?")
                            while True:
                                noidung = input("You: ").lower()
                                if "ngừng wiki" in noidung:
                                    break
                                else:
                                    timkiem = wiki.page(f'{noidung}')
                                    speak(timkiem.summary)
                                    speak("[ngừng wiki] nếu bạn muốn thoát")
                        elif short == 2:
                            speak(f"Facebook {nec}")
                            webbrowser.open("https://www.facebook.com/")
                        elif short == 3:
                            speak(f"Anime hay {nec}")
                            webbrowser.open("https://animehay.tv/")
                        elif short == 4:
                            speak(f"Động Phim {nec}")
                            webbrowser.open("https://dongphym.com/")
                        elif short ==5:
                            speak(f"Phim Hàn {nec}")
                            webbrowser.open("http://www.phymhan.com/")
                        elif short == 6:
                            speak(f"Gmail {nec}")
                            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                        elif short == 7:
                            speak(f"Google Earth {nec}")
                            webbrowser.open("https://earth.google.com/web/@12.37269667,109.44710412,-4095.49886217a,8155037.67908692d,35y,3.73110197h,0t,0r")
                        elif short == 8:
                            speak(f"Shopee {nec}")
                            webbrowser.open("https://shopee.vn/?utm_source=an_17209090000&utm_medium=affiliates&utm_campaign=4jcz9mgzpk8w-&utm_content=c7cd9271b3af48eba1c1d89f0bf322a7-34745-101654&af_siteid=an_17209090000&pid=affiliates&c=4jcz9mgzpk8w-&af_click_lookback=7d&af_viewthrough_lookback=1d&is_retargeting=true&af_reengagement_window=7d&af_sub_siteid=c7cd9271b3af48eba1c1d89f0bf322a7-34745-101654")
                        elif short == 9:
                            speak(f"Nonolive {nec}")
                            webbrowser.open("https://www.nonolive.com/69696969?fbclid=IwAR0b5nheeYMGnSHWbHZWpr9UKqn8eGt4G438R9vEuqt3m5i0gWYk4vGmcOQ")
                        elif short == 10:
                            speak(f"Du lịch online {nec}")
                            webbrowser.open("https://lifeat.io")
                        elif short == 11:
                            speak(f"Zalo {nec}")
                            webbrowser.open("https://chat.zalo.me/")
                        elif short == 12:
                            speak(f"Chương trình dạy học Python {nec}")
                            webbrowser.open("https://www.howkteam.vn/course/lap-trinh-python-co-ban-37") 
                        else:
                            speak(f"{muc}")
                elif me == 3:
                    speak(f"{thit}")
                    print("Google Chorme(1)       Garena(4)                       Zoom(7)")
                    print("Microsoft Egde(2)      League of Legends PBE(5)        ........")
                    print("Albion Online(3)       Discord(6)                      Về mục lựa chọn[99]")
                    while True:
                        choice = int(input("You: "))
                        if choice == 99:
                            break
                        elif choice == 1:
                            speak(f"Trình duyệt Google Chrome {nec}")
                            cmd = "C:/Program Files/Google/Chrome/Application/chrome.exe"
                            result = subprocess.run(cmd, shell=True)
                        elif choice == 2:
                            speak(f"Trình duyệt Microsoft Egde {nec}")
                            cmd = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
                            result = subprocess.run(cmd, shell=True)
                        elif choice == 3:
                            speak(f"Albion Online {nec}")
                            cmd = "D:/LITTE GAME/launcher/AlbionLauncher.exe"
                            result = subprocess.run(cmd, shell=True)
                        elif choice == 4:
                            speak(f"Garena {nec}")
                            cmd = "C:/Program Files (x86)/Garena/Garena/Garena.exe"
                            result = subprocess.run(cmd, shell=True)
                        elif choice == 5:
                            speak(f"Liên Minh Huyền Thoại P.B.E {nec}")
                            cmd = "D:/Riot Games/Riot Client/RiotClientServices.exe"
                            result = subprocess.run(cmd, shell=True)
                        elif choice == 6:
                            speak(f"Discord {nec}")
                            cmd = "C:/Users/this pc/AppData/Local/Discord/app-1.0.9002/Discord.exe"
                            result = subprocess.run(cmd, shell=True)
                        elif choice == 7:
                            speak(f"Zoom {nec}")
                            cmd = "C:/Users/this pc/AppData/Roaming/Zoom/bin/Zoom.exe"
                            result = subprocess.run(cmd, shell=True)
                        else:
                            speak(f"{muc}")
                elif me == 5:
                    while True:
                        necc = "Đang mở"
                        speak("Mở kép giữa hai kiểu dữ liệu được mở ở mục ẩn")
                        speak(f"{thit}")
                        print("Học online(1)       Cờ giải trí[LMHT_VN]_(3)      ......")
                        print("Viết học code(2)    Cờ giải trí[LMHT_PBE]_(4)     ......")
                        print("........            .......                       Về mục lựa chọn[99]")
                        coder = int(input("You: "))
                        if coder == 99:
                            break
                        elif coder == 1:
                            speak(necc)
                            webbrowser.open("https://chat.zalo.me/")
                            cmd = "C:/Users/this pc/AppData/Roaming/Zoom/bin/Zoom.exe"
                            result = subprocess.run(cmd, shell=True)
                            speak("Hãy nhập môn học bằng kí hiệu [số] để kích hoạt: ")
                            print("Đại số(1)       Ngữ văn[tập 1]_(5)      .....")
                            print("Hình học(2)     Ngữ văn[tập_2]_(6)      .....")
                            print("Vật lí(3)       Lịch sử(7)              Về mục lựa chọn[99]")
                            print("Hóa học(4)      Địa lí(8)")
                            print("Sinh học(9)     Giáo dục công dân(10)")
                            while True:
                                study = int(input("You: "))
                                if study == 99:
                                    break
                                elif study == 1:
                                    speak(f"Đại số {nec}")
                                    cmd = "D:/SGK 11/đại.pdf"
                                    result = subprocess.run(cmd, shell=True)
                                elif study == 2:
                                    speak(f"Hình học {nec}")
                                    cmd = "D:/SGK 11/hình.pdf"
                                    result = subprocess.run(cmd, shell=True)
                                elif study == 3:
                                    speak(f"Vật lí {nec}")
                                    cmd = "D:/SGK 11/lý.pdf"
                                    result = subprocess.run(cmd, shell=True)
                                elif study == 4:
                                    speak(f"Hóa học {nec}")
                                    cmd = "D:/SGK 11/hóa.pdf"
                                    result = subprocess.run(cmd, shell=True)
                                elif study == 5:
                                    speak(f"Ngữ văn tập 1 {nec}")
                                    cmd = "D:/SGK 11/văn1.pdf"
                                    result = subprocess.run(cmd, shell=True)
                                elif study == 6:
                                    speak(f"Ngữ văn tập 2 {nec}")
                                    cmd = "D:/SGK 11/văn2.pdf"
                                    result = subprocess.run(cmd, shell=True)
                                elif study == 7:
                                    speak(f"Lịch sử {nec}")
                                    cmd = "D:/SGK 11/sử.pdf"
                                    result = subprocess.run(cmd, shell=True)
                                elif study == 8:
                                    speak(f"Địa lí {nec}")
                                    cmd = "D:/SGK 11/địa.pdf"
                                    result = subprocess.run(cmd, shell=True)
                                elif study == 9:
                                    speak(f"Sinh học {nec}")
                                    cmd = "D:/SGK 11/sinh.pdf"
                                    result = subprocess.run(cmd, shell=True)
                                elif study == 10:
                                    speak(f"Giáo dục công dân {nec}")
                                    cmd = "D:/SGK 11/gdcd.pdf"
                                    result = subprocess.run(cmd, shell=True)
                                else:
                                    speak(f"{muc}")
                        elif coder == 2:
                                speak(necc)
                                cmd = "C:/Users/this pc/AppData/Local/Programs/Microsoft VS Code/Code.exe"
                                result = subprocess.run(cmd, shell=True)
                                webbrowser.open("https://www.howkteam.vn/course/lap-trinh-python-co-ban-37")
                                webbrowser.open("https://github.com/")
                                cmd = "C:/Program Files/Google/Chrome/Application/chrome.exe"
                                result = subprocess.run(cmd, shell=True)
                        elif coder == 3:
                            speak(necc)
                            cmd = "C:/Program Files (x86)/Garena/Garena/Garena.exe"
                            result = subprocess.run(cmd, shell=True)
                            webbrowser.open("https://www.facebook.com/")
                            webbrowser.open("https://www.youtube.com/")
                        elif coder == 4:
                            speak(necc)
                            cmd = "D:/Riot Games/Riot Client/RiotClientServices.exe"
                            result = subprocess.run(cmd, shell=True)
                            webbrowser.open("https://www.facebook.com/")
                            webbrowser.open("https://www.youtube.com/")
                        else:
                            speak(f"{muc}")
                else:
                    speak(f"{muc}")
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
def get_choices(choice):
    if choice == "B":
        return "Búa"
    elif choice == "G":
        return "Giấy"
    elif choice == "K":
        return "Kéo"
    else:
        return speak("Không đúng với từ khóa đã cho!")
def game():
    speak("Chào mừng đến với trò búa giấy kéo!")
    speak("[B] là búa, [G] là giấy, [K] là kéo và [Q] là thoát trò chơi")

    choices = ["B", "G", "K"]
    counter = 1
    game_on = True

    while game_on:
        speak(f"Trận {counter}. Xin bạn hãy nhập lựa chọn: ")
        người_chơi = input("You: ")
        người_chơi = người_chơi.upper()

        if người_chơi == "Q":
            speak("Cảm ơn vì đã tham gia trò chơi!")
            game_on = False 
        else:
            random_index = random.randint(0,2)
            máy_chơi = choices[random_index]

            speak(f"Bạn chọn {get_choices(người_chơi)} và máy chọn {get_choices(máy_chơi)}")

            if người_chơi == "B" and máy_chơi == "K":
                speak("Chúc mừng, bạn Thắng. Búa đập Kéo")
            elif người_chơi == "K" and máy_chơi == "G":
                speak("Chúc mừng, bạn Thắng. Kéo cắt Giấy")
            elif người_chơi == "G" and máy_chơi == "B":
                speak("Chúc mừng, bạn Thắng. Giấy bọc Búa")
            elif người_chơi == "B" and máy_chơi == "G":
                speak("Rất tiếc, máy Thắng. Giấy bọc Búa")
            elif người_chơi == "K" and máy_chơi == "B":
                speak("Rất tiếc, máy Thắng. Búa đập Kéo")
            elif người_chơi == "G" and máy_chơi == "K":
                speak("Rất tiếc, máy Thắng. Kéo cắt Giấy")
            elif người_chơi == máy_chơi:
                speak(f"Oh! Bạn với máy Hòa. với lựa chọn trùng là {get_choices(người_chơi)}")
            else:
                speak("Hãy nhập từ khóa đã cho là [B], [G], [K] và [Q]")

            counter+=1
        print("-"*45)
def bye():
    hour = datetime.now().hour
    if hour >=6 and hour<12:
        speak("Chúc bạn buổi sáng tốt lành")
    elif hour >=12 and hour<14:
        speak("Chúc bạn buổi trưa tốt lành")
    elif hour >=14 and hour<18:
        speak("Chúc bạn buổi chiều tốt lành")
    elif hour >=18 and hour<24:
        speak("Chúc bạn buổi tối tốt lành")
def wellcome():
    hour = datetime.now().hour
    if hour >=6 and hour<12:
        speak("Chào buổi sáng")
    elif hour >=12 and hour<14:
        speak("Chào buổi trưa")
    elif hour >=14 and hour<18:
        speak("Chào buổi chiều")
    elif hour >=18 and hour<24:
        speak("Chào buổi tối")
    speak('Tôi là trợ lí ảo Asis, tôi có thể làm gì cho bạn?')

if __name__ =="__main__":
    wellcome()
    while True:
        you = input("You: ").lower()
        if "bye" in you:
            bye()
            break
        elif "ngày" in you:
            ngày()
        elif "trò chơi" in you:
            game()
            speak("Bạn muốn làm gì tiếp?")
        elif "giờ" in you:
            thời_gian()
        elif "thời gian" in you:
            thời_gian()
        elif "google" in you:
            google()
        elif "youtube" in you:
            youtube()
        elif "mode" in you:
            detailsmod()
        elif "tắt laptop" in you:
            shutdownprograms()
        else:
            speak(f"Từ khóa {you} này không nằm trong khả năng của tôi")
            speak("Bạn muốn làm gì tiếp?")
        
        
