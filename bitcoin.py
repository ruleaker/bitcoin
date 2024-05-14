import okx.MarketData as MarketData
import os
import time


flag = "0"  # 实盘:0 , 模拟盘：1

marketDataAPI =  MarketData.MarketAPI(flag=flag)

def enter(x,cnt = 0):
    while(cnt <= x):
        cnt+=1
        print("")


while True:
    data = marketDataAPI.get_tickers(
    instType="SWAP",
    uly="BTC-USDT"
    )
    for item in data['data']:
        os.system('cls')
        print("""
░░▄▄█▀▀▀▀▀█▄▄░░
▄█▀░░▄░▄░░░░▀█▄
█░░░▀█▀▀▀▀▄░░░█
█░░░░█▄▄▄▄▀░░░█
█░░░░█░░░░█░░░█
▀█▄░▀▀█▀█▀░░▄█▀
░░▀▀█▄▄▄▄▄█▀▀░░


██████╗ ██╗████████╗ ██████╗ ██████╗ ██╗███╗   ██╗
██╔══██╗██║╚══██╔══╝██╔════╝██╔═══██╗██║████╗  ██║
██████╔╝██║   ██║   ██║     ██║   ██║██║██╔██╗ ██║
██╔══██╗██║   ██║   ██║     ██║   ██║██║██║╚██╗██║
██████╔╝██║   ██║   ╚██████╗╚██████╔╝██║██║ ╚████║
╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝
""")
        print(f"[B] Bitcoin Price:     >>>>||【 {item['last']} 】||<<<<      ")
        print(f"[B] Bitcoin Price:     >>>>||【 {item['last']} 】||<<<<      ")
        print(f"[B] Bitcoin Price:     >>>>||【 {item['last']} 】||<<<<      ")
        print(f"[B] Bitcoin Price:     >>>>||【 {item['last']} 】||<<<<      ")
        print(f"[B] Bitcoin Price:     >>>>||【 {item['last']} 】||<<<<      ")
        enter(3)

        time.sleep(0.1)
