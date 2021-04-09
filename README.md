# NCKU_CHECKIN

[TOC]

###### tags: `自動簽到程式` `成功大學` `打卡`
---

## 注意事項：
* ==本程式為學術交流用途，程式相關問題而導致沒簽到請自行負責==
* 下載後請將檔案解壓縮，並且先開啟"請設定帳號密碼.csv"進行設定(設定流程在後面)
* 系統執行檔案為"test11_windows_final.exe"，本程式限用window系統
* 系統啟動後不要關閉Dos(黑色)視窗，縮小即可
* 系統開啟後如果發現瀏覽無法正常開啟，請依照"Chrome瀏覽器無法開啟"章節解決問題
* 本程式簽到時間可手動設定，請見"打卡時間設定"章節
* 本程式簽退時間為簽到時間 + 1~15分鐘(隨機)，以防止自動打卡被抓
* 簽到瀏覽器頁面請勿手動關閉，當簽到或簽退完成後程式將自動關閉頁面
* 系統遇到周六與周日會自動停止打卡，無須關閉程式
* 如遇到六日補假時，請自行手動打卡
* 遇到國定假日或是連假時請下班後關閉程式，以免誤打卡
---

## 帳號密碼設定流程(一次性設定)：
1.	開啟”請設定帳號密碼.csv”
![](https://i.imgur.com/PZG2DQT.png)
2.	分別輸入帳號、密碼與今日上班地點
![](https://i.imgur.com/tVS0rfS.png)
3.	開啟程式 testX_windows_final.exe
![](https://i.imgur.com/EBFZomj.png)
4. 系統執行畫面
![](https://i.imgur.com/VhG4Rgr.png)
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

---
## 簽到時間設定：
1.	開啟”請設定帳號密碼.csv”
![](https://i.imgur.com/PZG2DQT.png)
2. 請填入打卡的開始時間與結束時間(切記不可相反)
![](https://i.imgur.com/kTE5onv.png)

---

## 捷徑設定：
1. 對執行檔點右鍵，點選"釘選到開始畫面"
![](https://i.imgur.com/7OQoMLw.png)
2. 未來如果要開啟程式，按開始就可以看到(沒有的話請滑動滑鼠滾輪)
![](https://i.imgur.com/WhiG6mS.png)

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

---

## 誌謝
* 謝謝阿蓉提供帳號密碼讓我測試，在這過程中好幾次因為程式BUG而沒有打到卡，在這邊要跟你說聲抱歉QAQ
* 我原本要做MAC版本的，但是跟學妹吵架(後來學妹不借我MAC了)所以沒有完成編譯成MAC的執行檔，不過還是謝謝學妹

