# NCKU_CHECKIN

設定流程(一次性設定)：
1.	開啟”請設定帳號密碼.csv”
![](https://i.imgur.com/PZG2DQT.png)
2.	分別輸入帳號、密碼與今日上班地點
![](https://i.imgur.com/tVS0rfS.png)
3.	開啟程式 testX_windows_final.exe
![](https://i.imgur.com/EBFZomj.png)

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

