
# Fill in today's health information
from selenium import webdriver
import random
import time
from time import sleep
import getpass
import csv
from datetime import datetime
import requests

   

    
#headers = {"Authorization": "Bearer " + "m5Uja5HHKHXbG7yKdCacXgbLHcBAQ5SJ6KyTQv5A1YC","Content-Type": "application/x-www-form-urlencoded"}

#check_in_bottom = "//*[@id='sitemain']/div[2]/div[3]/div[1]/div[3]/div[4]/div/button[1]"

#check_out_bottom = "//*[@id='sitemain']/div[2]/div[3]/div[1]/div[3]/div[4]/div/button[2]"

#view_list_bottom = "//*[@id='sitemain']/div[2]/div[3]/div[1]/div[3]/div[5]/div/button[1]"

#sign_out_bottom = "//*[@id='sitemain']/div[2]/div[3]/div[1]/div[3]/div[5]/div/button[2]"

check_in_bottom = '//button[normalize-space()="上班簽到"]'

check_out_bottom = '//button[normalize-space()="下班簽退"]'

view_list_bottom = '//button[normalize-space()="查看本日刷卡紀錄"]'

sign_out_bottom = '//button[normalize-space()="重新輸入"]'

    
def main():
    try:
        with open('請設定帳號密碼.csv', newline='') as csvfile:
            rows = csv.reader(csvfile)
            count=0
            for row in rows:
                #print(row[1])
                #print(count)
                if(count == 0):
                    usrid = row[1]
                elif(count == 1):
                    password = row[1]
                elif(count == 2):
                    location = row[1]
                count = count +1
                open('請設定帳號密碼.csv', newline='').close()
    except:
        print("沒有設定檔，採手動輸入帳號密碼...")    
        usrid =""
        password=""   
    

    #usrid ="10908103"
    #password="14840430"

    today_buffer = "0"
    if(password == "" or usrid == ""):
        while True:
            usrid= input("請輸入帳號: ")
            password= getpass.getpass("請輸入密碼: ")
            if password=="":
                pass
            else:
                break
    print("系統啟動中...")
    
    
    today=str(time.strftime("%w"))    
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')," 星期", today)

    #print("----runing----")              
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 改變視窗大小為最小化 (因為沒有可見視窗，所以長寬為關閉前大小)
    #driver.minimize_window()
    #print ("最小化：(" + str(driver.get_window_size().get("width")) + "," + str(driver.get_window_size().get("height")) + ")")
    #driver.implicitly_wait(1)
    driver.get('https://eadm.ncku.edu.tw/welldoc/ncku/iftwd/signIn.php')
    user_id = driver.find_element_by_xpath("//*[@id='psnCode']")
    user_id.send_keys(str(usrid))
    user_id = driver.find_element_by_xpath("//*[@id='password']")
    user_id.send_keys(str(password))
    sleep(1)
    
    try:
        submit_bottom = driver.find_element_by_xpath(view_list_bottom)
        submit_bottom.click()
    except Exception as e:
        pass

    sleep(2)
    #print("..............")    
    #table = driver.find_element_by_id('checkinList')
    trlist = driver.find_elements_by_tag_name('tr')
    print("簽到次數: ",len(trlist)-4)    
    if((len(trlist)-4) == 0):                
        try:
            submit_bottom = driver.find_element_by_xpath(check_in_bottom )
            submit_bottom.click()            
            #params = {"message": "簽到成功"}
            #requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)
            sleep(2)
            try:
                alert = driver.switch_to.alert #切換到alert
                if(alert.text == "遲到!您最晚的上班的時間為 08:30"):
                    #print('alert text : ' + alert.text) #列印alert的文字
                    alert.accept() #點選alert的【確認】按鈕  
            except:                    
                pass
            try:
                alert = driver.switch_to.alert #切換到alert
                if(alert.text == "【提醒您】自即日起，每日須至本校新型冠狀病毒(COVID-19)資訊平台專區登錄健康資訊，或掃描足跡 QR Code 亦可登錄相關資訊。"):
                    #print('alert text : ' + alert.text) #列印alert的文字
                    alert.accept() #點選alert的【確認】按鈕  
            except:                    
                pass
            
            try:
                alert = driver.switch_to.alert #切換到alert
                if(alert.text == "遲到!您最晚的上班的時間為 08:30"):
                    #print('alert text : ' + alert.text) #列印alert的文字
                    alert.accept() #點選alert的【確認】按鈕  
            except:                    
                pass
            
            now_handle = driver.current_window_handle #主視窗編號
            #print("簽到視窗編號 : " , now_handle)
            sleep(2)
            #driver1.get('https://app.pers.ncku.edu.tw/ncov/index.php?auth')
            all_handles = driver.window_handles #全部視窗控制權
            #driver.switch_to_window(now_handle)
            for handle in all_handles:  
                if handle != now_handle:     
                    #輸出待選擇的視窗控制代碼  
                    #print("今日健康資訊視窗編號 : ",handle) #  
                    driver.switch_to_window(handle)  
                    time.sleep(1)  
                    
                    #print("登入今日健康資訊視窗編號.... ") 
                    user_id = driver.find_element_by_xpath("//*[@id='user_id']")
                    user_id.send_keys(str(usrid))
                    user_id = driver.find_element_by_xpath("//*[@id='passwd']")
                    user_id.send_keys(str(password))
                    
                    try:
                        submit_bottom = driver.find_element_by_xpath("//*[@id='submit_by_acpw']")
                        submit_bottom.click()
                    except Exception as e:
                        pass
            
                    sleep(2)
                    b = driver.find_elements_by_xpath("//*[contains(text(), '回報今日健康資訊')]")
                    if len(b) > 0:
                        print("正在填寫健康聲明書.........")
                        #params = {"message": "正在填寫健康聲明書"}
                        #requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)
                        answers = driver.find_elements_by_css_selector("div[class='form-control2 input-group']")
                        for answer in answers:
                            try:
                                #print(answer)
                                ans = answer.find_elements_by_css_selector('label')
                                #li = random.choice(ans)
                              
                                if(len(ans)>10):
                                    li = ans[15]
                                    li.click()
                                    time.sleep(0.1)
                                else:
                                    li = ans[0]
                                    li.click()
                                    time.sleep(0.1)
                                #eee = eee + 300
                                #$driver.execute_script(c+str(eee)+d)
                            except Exception as e:
                                #print("click error: " ,e)
                                pass
                            try:
                                text = answer.find_element_by_css_selector("input[name='stay_1_other'][type='text']")
                                text.send_keys(location)
                            except Exception as c:
                                #print("send_keys error: ",c)
                                pass
                        try:
                            submit_bottom = driver.find_element_by_xpath("//*[@id='arch_grid']/div[3]/form/div/div/div[3]/button[1]")
                            submit_bottom.click()
                            time.sleep(1)
                            submit_bottom = driver.find_element_by_xpath("//*[@id='msg']/div[2]/div/div[3]/button")
                            submit_bottom.click()
                        except:
                            pass
                        #print("健康聲明填寫完畢 !")  
                        try:
                            driver.switch_to_window(now_handle)  
                            #print("切回簽到視窗提供觀看..")
                        except:
                            pass                               
        except Exception as e:
            pass
        
   
    elif((len(trlist)-4) > 0):
        
        check_list = []
        check_list_arry = []
        count_1 = 1
        count_0 = 1
        for row in trlist:#遍歷行物件，獲取每一個行中所有的列物件
            tdlist = row.find_elements_by_tag_name('td')
            #print("count_0: ", count_0)
            count_0 = count_0 + 1
            #print("check_list_arry: ",check_list_arry)
            #time.sleep(4)
            for col in tdlist:
                #print("count_1: ", count_1)
                #print(col.text + '\t',end='')
                if(len(tdlist)==5):
                    #print(col.text)
                    check_list.append(col.text)                
                    if(count_1 % 5 == 0):
                        #print("check_list----------: ",check_list)
                        check_list_arry.append(check_list)
                        #print("check_list_arry-----: ",check_list_arry)
                        #check_list.clear()     
                        check_list = []
                    count_1 = count_1 + 1
                                           
        if(check_list_arry[0][2] == '上班'):
            #print("第一筆打卡紀錄是上班") 
            check_in_time = check_list_arry[0][3].split(":")  
            print()
            print("--------------------------本日簽到上班時間為:", datetime.now().strftime('%Y-%m-%d'), check_list_arry[0][3]+datetime.now().strftime(':%S'),"--------------------------")
            #text = str("本日簽到時間為:"+ datetime.now().strftime('%Y-%m-%d ')+ check_list_arry[0][3]+datetime.now().strftime(':%S'))
            #params = {"message": text}
            #requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)
            print()
            #print("check_in_time: ",check_in_time)
            check_in_time = int(check_in_time[0])*60 + int(check_in_time[1])
            #print("check_in_time: ",check_in_time)
            
            #datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            check_out_time = datetime.now().strftime('%H:%M').split(":")
            #print("check_out_time: ",check_out_time)
            check_out_time = int(check_out_time[0])*60 + int(check_out_time[1])
            #print("check_out_time: ",check_out_time)
            
            if(check_out_time - check_in_time >= 540):
                try:
                    sleep_time = (random.randint(0,59))
                    print("sleep_time: ",sleep_time)
                    time.sleep(int(sleep_time))
                    submit_bottom = driver.find_element_by_xpath(check_out_bottom)
                    submit_bottom.click()
                    print()
                    print("--------------------------本日簽退時間為:",datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%H:%M:%S'),"--------------------------")    
                    text = str("本日簽退時間為:"+datetime.now().strftime('%Y-%m-%d ')+ datetime.now().strftime('%H:%M:%S'))
                    #params = {"message": text}
                    #requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)
                    print()
                except Exception as e:
                    print(e)
            else:
                print("簽退時間未到！！ 等待時間到自動簽退下班............")
                change_time = datetime.now().strftime('%H:%M:%S')
                while True:
                    check_out_time = datetime.now().strftime('%H:%M').split(":")
                    check_out_time = int(check_out_time[0])*60 + int(check_out_time[1])
                    if(check_out_time - check_in_time >= 540):
                        sleep_time = (random.randint(0,59))
                        print("sleep_time: ",sleep_time)
                        time.sleep(int(sleep_time))
                        submit_bottom = driver.find_element_by_xpath(check_out_bottom)
                        submit_bottom.click()
                        print()
                        print("--------------------------本日簽退時間為:",datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%H:%M:%S'),"--------------------------") 
                        text = str("本日簽退時間為:"+datetime.now().strftime('%Y-%m-%d ')+ datetime.now().strftime('%H:%M:%S'))
                        #params = {"message": text}
                        #requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)
                        print()
                        break
                    elif(datetime.now().strftime('%H:%M:%S') != change_time):
                        if(datetime.now().strftime('%S') == '03'):
                            print("目前時間: ",datetime.now().strftime('%H:%M')," 目前剩餘 : ", abs(check_out_time - (check_in_time + 540)), " 分鐘可簽退..")
                            text = str("目前時間: "+datetime.now().strftime('%H:%M')+" 目前剩餘 : "+ str(abs(check_out_time - (check_in_time + 540)))+ " 分鐘可簽退..")
                            #params = {"message": text}
                            #requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)
                            change_time = datetime.now().strftime('%H:%M:%S')
                            
     
            d = driver.find_elements_by_xpath("//*[contains(text(), '簽退不符合規定訊息')]")  
            if len(d) > 0:
                #print("正在填寫簽退不符合規定訊息.........公務於可下班時間(或加班結束時間)即結束，惟未立即簽退離開")
                #submit_bottom = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/input")
                time.sleep(2)
                try:
                    #print(len(driver.find_elements_by_css_selector("div[class='ng-scope ng-binding']")))
                    sss = driver.find_elements_by_css_selector("div[class='ng-scope ng-binding']")
                    #print(sss,len(sss),"*111111111111111")
                    a = sss[0].find_elements_by_css_selector('input')
                    #print(a,len(a),"************")
                    a[0].click()
                    #time.sleep(1)
                    #for answer in sss:
                            #print(answer)
                            #anss = answer.find_elements_by_css_selector('input')
                            #print(anss,"---------------",len(anss))
                            #anss[0].click()
                            
                    submit_bottom = driver.find_element_by_xpath("/html/body/div[1]/div[3]/span/button[1]")
                    submit_bottom.click()
                    print("下班打卡完畢 !") 
                    text = "簽退成功 !"
                    #params = {"message": text}
                    #requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)
                except:
                    pass
    
    try:
        time.sleep(4)
        #print("登出中.....")  
        submit_bottom = driver.find_element_by_xpath(sign_out_bottom )
        submit_bottom.click()
    except:
       pass
    #print("關閉視窗.....")  
    driver.quit()

                

 

if __name__ == '__main__':
   main()
   

    

























