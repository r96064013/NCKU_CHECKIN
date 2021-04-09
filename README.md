# NCKU_CHECKIN

## 帳號密碼設定流程(一次性設定)：
1.	開啟”請設定帳號密碼.csv”
![](https://i.imgur.com/PZG2DQT.png)
2.	分別輸入帳號、密碼與今日上班地點
![](https://i.imgur.com/tVS0rfS.png)
3.	開啟程式 testX_windows_final.exe
![](https://i.imgur.com/EBFZomj.png)
---
## LINE通知設定流程(一次性設定)：
1. 請點連結並登入 https://notify-bot.line.me/my/

![](https://i.imgur.com/ymRRAhN.png)

2. 點選發行權杖

![](https://i.imgur.com/PqhnKd2.png)

3. 請填寫權杖名稱"簽到提醒"，並點選"透過1對1聊天接收LINE Notify的通知"，最後點選發行
![](https://i.imgur.com/TcHOw1v.png)
4. 點選複製權杖

![](https://i.imgur.com/rbnYiYB.png)

6. 打開資料夾裡的請設定帳號密碼.csv
![](https://i.imgur.com/AKWVveL.png)
7. 把權杖貼到 LINE後面的格子並存檔(檔案名稱不可變動，副檔名必須是CSV)
![](https://i.imgur.com/wR8JG0i.png)
8. 之後自動打卡都會透過LINE通知您，如果程式掛掉就不會通知(這時候你就要快去打卡)
![](https://i.imgur.com/jZT23gz.png)

==註記：設定成功，系統開啟時LINE會推播"系統啟動...."==

## 打卡時間設定：
1.	開啟”請設定帳號密碼.csv”
![](https://i.imgur.com/PZG2DQT.png)
2. 請填入打卡的開始時間與結束時間(切記不可相反)
![](https://i.imgur.com/kTE5onv.png)

---
## Chrome瀏覽器無法開啟
ChromeDriver不支援Chrome網頁瀏覽器的版本時，會引起Chrome閃退。
使用ChromeDriver開發Chrome自動控制時，需要注意以下幾點：
1.	確認Chrome 瀏覽器版本
    * Step 1:開啟Chrome選單->點選設定
    * ![](https://i.imgur.com/xfL2eNE.png)
    * Step 2:選擇 關於Chrome
    * ![](https://i.imgur.com/qf4ThYD.png)
    * Step 3:確認Chrome版本
    * ![](https://i.imgur.com/4F3zUOU.png)
2.	下載可支援此Chrome版本的ChromeDriver
    * Step 1:下載位載:https://sites.google.com/a/chromium.org/chromedriver/downloads
    * ![](https://i.imgur.com/Aenmppk.png)
    * Step 2:下載後，解壓縮chromedriver_win，並執行ChromeDriver，確認版本
    * ![](https://i.imgur.com/Eueqcw1.png)
3.	將ChromeDriver移至專案目錄下，避免程式找不到ChromeDriver
	![](https://i.imgur.com/bKBEh2J.png)

