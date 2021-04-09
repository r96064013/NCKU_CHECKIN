
# Fill in today's health information
from selenium import webdriver
import random
import time
from time import sleep
import getpass
import csv
from datetime import datetime
import requests

holiday = ["2021-02-10", "2021-02-11", "2021-02-12", "2021-02-13", "2021-02-14", \
               "2021-02-15","2021-02-16","2021-02-28","2021-03-01","2021-04-02","2021-04-05", \
               "2021-06-14", "2021-09-18","2021-09-19","2021-10-11","2021-12-31"]
Compensatory_leave =  "2021-02-20"
    
#headers = {"Authorization": "Bearer " + "DFFr19CQ6rd4UY9jjemSxyBtqoWtIDn8TNlWDPlpBjn","Content-Type": "application/x-www-form-urlencoded"}
#headers = {"Authorization": "Bearer " + "7LwRSUF2SQfjwrK8xKILCzYrSYZ8QHwItcG3ryyE9kN","Content-Type": "application/x-www-form-urlencoded"}
#headers = {"Authorization": "Bearer " + "BdInGBrHRU11O61IQtNmxbUE0VFbT7WqMkuTYorObPA","Content-Type": "application/x-www-form-urlencoded"} #wu
check_in_botton = '//button[normalize-space()="上班簽到"]'
check_out_botton = '//button[normalize-space()="下班簽退"]'
view_list_botton = '//button[normalize-space()="查看本日刷卡紀錄"]'
sign_out_botton = '//button[normalize-space()="重新輸入"]'

def job(set_time_minute):
    
  time_set = float(set_time_minute) * 60
  SYSJ = None 
  start_time = time.time()
  while True:
    t1 = time.time() - start_time  
    SYSJ = time_set - t1  
    m, s = divmod(SYSJ, 60)  
    h, m = divmod(m, 60)  
    if SYSJ > 0:
        # print("%02d:%02d:%02d" % (h, m, s))  
        print("\r目前剩餘: %02d:%02d:%02d 分鐘可簽退.." % (h, m, s),end="")  
    else:
        #print("\n倒數")
        #playsound('clock_bell.mp3', block=True)
        break
    
def read_setup_file():
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
                elif(count == 3):
                    LINE = row[1]
                elif(count == 4):
                    NAME = row[1]
                elif(count == 5):
                    set_hours_st = row[1]
                elif(count == 6):
                    set_minutes_st = row[1]
                elif(count == 7):
                    set_hours_end = row[1]
                elif(count == 8):
                    set_minutes_end = row[1]
                count = count +1
        return usrid, password, location, LINE, NAME, set_hours_st, set_minutes_st, set_hours_end, set_minutes_end
        open('請設定帳號密碼.csv', newline='').close()
    except:
        print("沒有設定檔，採手動輸入帳號密碼...")    
        usrid =""
        password=""   
        location="NCKU"
        LINE = ""
        NAME = ""
        set_hours_st = "8"
        set_hours_end = "8"
        set_minutes_st = 0
        set_minutes_end = 17
        return usrid, password, location, LINE, NAME, set_hours_st, set_minutes_st, set_hours_end, set_minutes_end
        
def survey_account_password_input(driver, usrid, password):
    user_id = driver.find_element_by_xpath("//*[@id='user_id']")
    user_id.send_keys(str(usrid))
    user_id = driver.find_element_by_xpath("//*[@id='passwd']")
    user_id.send_keys(str(password))
    
def checkin_account_password_input(driver, usrid, password):
    user_id = driver.find_element_by_xpath("//*[@id='psnCode']")
    user_id.send_keys(str(usrid))
    user_id = driver.find_element_by_xpath("//*[@id='password']")
    user_id.send_keys(str(password))

def check_work_list(driver):
    sleep(2)
    #print("..............")    
    #table = driver.find_element_by_id('checkinList')
    trlist = driver.find_elements_by_tag_name('tr')
    print("簽到次數: ",len(trlist)-4)
    #text = str("簽到次數: "+ str(len(trlist)-4))
    #params = {"message": text}
    #requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)
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
            
    return check_list_arry

def open_browser():
    #print("----runing----")              
    driver = webdriver.Chrome()
    #driver.maximize_window()
    # 改變視窗大小為最小化 (因為沒有可見視窗，所以長寬為關閉前大小)
    driver.minimize_window()
    #print ("最小化：(" + str(driver.get_window_size().get("width")) + "," + str(driver.get_window_size().get("height")) + ")")
    #driver.implicitly_wait(1)
    driver.get('https://eadm.ncku.edu.tw/welldoc/ncku/iftwd/signIn.php')
    return driver
    sleep(1)

def line_broadcast(text, LINE):
    headers = {"Authorization": "Bearer " + LINE ,"Content-Type": "application/x-www-form-urlencoded"}
    params = {"message": text}
    requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)
     
def check_in_procedure(usrid, password, LINE, NAME):
  
    #usrid ="10908103"
    #password="14840430"
    
    #print(datetime.now().strftime('%H:%M:%S'),"----1----") 
    
    driver = open_browser()
    checkin_account_password_input(driver, usrid, password) 
    sleep(1)
    
    now_handle = driver.current_window_handle #主視窗編號
    print("簽到視窗編號 : " , now_handle)
    #text = "主視窗編號:" + now_handle
    #line_broadcast(text, LINE)
    
    try:
        submit_botton = driver.find_element_by_xpath(check_in_botton)
        submit_botton.click()
    except Exception as e:
        text = "簽到失敗"
        line_broadcast(text, LINE)
        print(e," line:281")
    
    sleep(2)    
    try:
        alert = driver.switch_to.alert #切換到alert
        if(alert.text == "遲到!您最晚的上班的時間為 08:30"):
            print('alert text : ' + alert.text) #列印alert的文字
            alert.accept() #點選alert的【確認】按鈕  
    except:                    
        pass
    sleep(0.5)
    try:
        alert = driver.switch_to.alert #切換到alert
        if(alert.text == "【提醒您】自即日起，每日須至本校新型冠狀病毒(COVID-19)資訊平台專區登錄健康資訊，或掃描足跡 QR Code 亦可登錄相關資訊。"):
            print('alert text : ' + alert.text) #列印alert的文字
            #text = str('alert text : ' + alert.text)
            #line_broadcast(text, LINE)
            alert.accept() #點選alert的【確認】按鈕  
    except:                    
        pass
    sleep(0.5)
    try:
        alert = driver.switch_to.alert #切換到alert
        if(alert.text == "遲到!您最晚的上班的時間為 08:30"):
            #print('alert text : ' + alert.text) #列印alert的文字
            alert.accept() #點選alert的【確認】按鈕  
    except:                    
        pass
    sleep(2)
    #driver1.get('https://app.pers.ncku.edu.tw/ncov/index.php?auth')
    all_handles = driver.window_handles #全部視窗控制權
    #driver.switch_to_window(now_handle)
    for handle in all_handles:  
        if handle != now_handle:     
            #輸出待選擇的視窗控制代碼  
            print("今日健康資訊視窗編號 : ",handle) #  
            #text = "今日健康資訊視窗編號:" + handle
            #line_broadcast(text, LINE)
            driver.switch_to_window(handle)  
            time.sleep(1)  
            
            try:
                print("登入今日健康資訊視窗編號.... ") 
                survey_account_password_input(driver, usrid, password)
            except Exception as e:
                pass
                
            try:
                submit_botton = driver.find_element_by_xpath("//*[@id='submit_by_acpw']")
                submit_botton.click()
            except Exception as e:
                line_broadcast("新型冠狀病毒（COVID-19）資訊平台專區登入button有誤", LINE)
    
            sleep(2)
            b = driver.find_elements_by_xpath("//*[contains(text(), '回報今日健康資訊')]")
            if len(b) > 0:
                print("正在填寫健康聲明書.........")
                #text = "正在填寫健康聲明書"
                #line_broadcast(text, LINE)
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
                    submit_botton = driver.find_element_by_xpath("//*[@id='arch_grid']/div[3]/form/div/div/div[3]/button[1]")
                    submit_botton.click()
                    text = "健康聲明填寫完畢"
                    line_broadcast(text, LINE)
                    print("健康聲明填寫完畢")
                  
                except:
                    text = "健康聲明填寫異常"
                    line_broadcast(text, LINE)
                try:
                    time.sleep(1)
                    submit_botton = driver.find_element_by_xpath("//*[@id='msg']/div[2]/div/div[3]/button")
                    submit_botton.click()
                except:
                    text = "存檔成功沒按掉"
                    line_broadcast(text, LINE)    
                try:
                    driver.switch_to_window(now_handle)  
                    #print("切回簽到視窗提供觀看..")
                except:
                    text = "視窗沒切回簽到"
                    line_broadcast(text, LINE)                                                 
        
    sleep(1)
    try:
        submit_botton = driver.find_element_by_xpath(view_list_botton)
        submit_botton.click()
    except Exception as e:
        print(e," line:287")
    sleep(1) 
    check_list_arry = check_work_list(driver)   
    for x in range(len(check_list_arry)):
        if(check_list_arry[x][2]=='上班'):
            text = str(NAME) + str("您好！幫妳簽到了喔 :D，本日簽到資訊為:"+str(check_list_arry[x]))
            line_broadcast(text, LINE)
           
            print()
            print("本日簽到資訊為:",str(check_list_arry[x]))
            print()
            driver.quit()
            return check_list_arry
             
def check_out_procedure(check_list_arry, check_out_number, usrid, password, LINE, NAME):
     
    check_in_time = check_list_arry[check_out_number][3].split(":")     
    #print("check_in_time: ",check_in_time)
    check_in_time = int(check_in_time[0])*60 + int(check_in_time[1])
    check_out_time = datetime.now().strftime('%H:%M').split(":")
    #print("check_out_time: ",check_out_time)
    check_out_time = int(check_out_time[0])*60 + int(check_out_time[1])
    if(check_out_time - check_in_time >= 540):
        sleep_time = (random.randint(10,150))/10
        print("隨機等待: ", sleep_time, "分鐘，以防止被系統抓到自動打卡")
        job(sleep_time)
        driver = open_browser()
        checkin_account_password_input(driver, usrid, password)      
        try:
            submit_botton = driver.find_element_by_xpath(check_out_botton)
            submit_botton.click()
        except:
            pass
    else:
        print("簽退時間未到！！ 等待時間到自動簽退下班............")
        change_time = datetime.now().strftime('%H:%M:%S')
        while True:
            check_out_time = datetime.now().strftime('%H:%M').split(":")
            check_out_time = int(check_out_time[0])*60 + int(check_out_time[1])
            if(check_out_time - check_in_time >= 540):
                sleep_time = (random.randint(10,150))/10
                print("隨機等待: ", sleep_time, "分鐘，以防止被系統抓到自動打卡")
                job(sleep_time)
                driver = open_browser()
                checkin_account_password_input(driver, usrid, password)  
                submit_botton = driver.find_element_by_xpath(check_out_botton)
                submit_botton.click()
                break
            elif(datetime.now().strftime('%H:%M:%S') != change_time):
                job(abs(check_out_time - (check_in_time + 540)))
                '''
                if(datetime.now().strftime('%S') == '03' and datetime.now().strftime('%H') == '17'):
                    print("目前時間: ",datetime.now().strftime('%H:%M')," 目前剩餘 : ", abs(check_out_time - (check_in_time + 540)), " 分鐘可簽退..")
                    change_time = datetime.now().strftime('%H:%M:%S')
                '''   
    d = driver.find_elements_by_xpath("//*[contains(text(), '簽退不符合規定訊息')]")  
    if len(d) > 0:
        time.sleep(2)
        try:
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
            submit_botton = driver.find_element_by_xpath("/html/body/div[1]/div[3]/span/button[1]")
            submit_botton.click()
        except:
            pass
    
    sleep(2)
    try:
        submit_botton = driver.find_element_by_xpath(view_list_botton)
        submit_botton.click()
    except Exception as e:
        print(e)
    
    sleep(1) 
    check_list_arry = check_work_list(driver)   
    for x in range(len(check_list_arry)):
        if(check_list_arry[len(check_list_arry)-x-1][2]=='下班'):
            #print(check_list_arry[len(check_list_arry)-x-1])
            text = str(NAME) + str("您好！幫妳簽退了喔 >///<，本日簽退資訊為:"+str(check_list_arry[len(check_list_arry)-x-1]))
            line_broadcast(text, LINE)
           
            print()
            print("本日簽退資訊為:",str(check_list_arry[len(check_list_arry)-x-1]))
            print()
            check_out_information = str(check_list_arry[len(check_list_arry)-x-1])
            break
    try:
        time.sleep(4)
        #print("登出中.....")  
        submit_botton = driver.find_element_by_xpath(sign_out_botton)
        submit_botton.click()
    except:
       pass
    #print("關閉視窗.....")  
    driver.quit()
    print("等待上班時間....") 
    return check_out_information
             
if __name__ == '__main__':
    read_setup_list = read_setup_file()
    usrid = read_setup_list[0]
    password = read_setup_list[1]
    location = read_setup_list[2]
    LINE = read_setup_list[3]
    NAME = read_setup_list[4]
    set_hours_st = read_setup_list[5]
    set_minutes_st = read_setup_list[6]
    set_hours_end = read_setup_list[7]
    set_minutes_end = read_setup_list[8]
    #print(read_setup_list)
    #print("usrid,password,location",usrid,password,location)
    if(password == "" or usrid == ""):
        while True:
            #usrid= input("請輸入帳號: ")
            usrid= getpass.getpass("請輸入帳號: ")
            password= getpass.getpass("請輸入密碼: ")
            if password=="":
                pass
            else:
                break
    print("網頁與帳號密碼測試中....")
    line_broadcast("系統啟動....",LINE)
    driver = open_browser()
    checkin_account_password_input(driver, usrid, password)
    try:
        submit_botton = driver.find_element_by_xpath(view_list_botton)
        submit_botton.click()
    except Exception as e:
        print(e)      
    check_list_arry = check_work_list(driver)
    sleep(1)
    driver.quit()
    
    today_buffer_flag = 0
    today_buffer = "0"
    while True:
        sleep(0.1)
        today=str(time.strftime("%w"))
        date_YMD = datetime.now().strftime('%Y-%m-%d')
        for i in range(len(holiday)):
            if(date_YMD == holiday[i]):
                if(today_buffer != today):
                    print("放假日: ",holiday[i])
                    text = "放假日: " + holiday[i]
                    line_broadcast(text,LINE)
                today_buffer = today
        
        if(today != today_buffer_flag):
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')," 星期", today)   
            today_buffer_flag = today
            
        if(today_buffer != today and today != '6' and today != '7' and today != '0' or date_YMD == Compensatory_leave):  
            #print(today)  
            today_buffer = today
            
            driver = open_browser()
            checkin_account_password_input(driver, usrid, password)
            try:
                submit_botton = driver.find_element_by_xpath(view_list_botton)
                submit_botton.click()
            except Exception as e:
                print(e)      
            check_list_arry = check_work_list(driver)
            print("check_list_arry:",check_list_arry,"check_list_arry len:", len(check_list_arry),datetime.now().strftime('%Y-%m-%d %H:%M:%S')," 星期", today)
            sleep(1)
            driver.quit()
            
            
            #print("phase0")
            if(int(set_hours_st) == int(set_hours_end)):               
                minute = str(random.randint(int(set_minutes_st),int(set_minutes_end)))
                minute = minute.zfill(2)
                set_hours = set_hours_st
                #print("phase1",set_hours,minute)
            elif(int(set_hours_st) < int(set_hours_end)):
                set_hours = random.randint(int(set_hours_st),int(set_hours_end))
                if(int(set_hours) == int(set_hours_st)):
                    minute = str(random.randint(int(set_minutes_st),59))
                    minute = minute.zfill(2)
                    set_hours = set_hours_st
                    #print("phase2",set_hours,minute)
                elif(int(set_hours) == int(set_hours_end)):
                    minute = str(random.randint(0,int(set_minutes_end)))
                    minute = minute.zfill(2)
                    set_hours = set_hours_end
                    #print("phase3",set_hours,minute)
            else:
                print("時間參數設定錯誤，預設打卡時間為8:00~8:17")
                set_hours = 8
                minute = str(random.randint(0,17))
                minute = minute.zfill(2)
                print("phase4",set_hours,minute)
                
            second = str(random.randint(0,59))
            second = second.zfill(2)
            
            set_hours = int(set_hours)
            set_hours = "%02d" % set_hours
            check_in_time1 = set_hours +":" + minute +":"+ second
            '''
            if((int(datetime.now().strftime("%S")) + 15) > 59):
                check_in_time1 = datetime.now().strftime("%H") + ":" + str(int(datetime.now().strftime("%M")) + 1) + ":15" 
            else:
                check_in_time1 = datetime.now().strftime("%H:%M") + ":" + str(int(datetime.now().strftime("%S")) + 15)
            '''     
            
            #print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')," 星期", today)
            #text = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" 星期"+ today)
            #params = {"message": text}
            #requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)
            print() 
            print("--------------------------下次簽到時間(尚未簽到):", check_in_time1,"--------------------------")
            #text = str("預計下次簽到時間為: "+ check_in_time1 + "  目前尚未簽到哦！！！！！")
            #line_broadcast(text,LINE)
            print()
            check_out_again_flag = -1  
            checkin_flag = 0
            while True:
                date_HMS = datetime.now().strftime("%H:%M:%S")
                if(date_HMS == check_in_time1 and len(check_list_arry)== 0):#沒上班
                    check_list_arry = check_in_procedure(usrid, password, LINE, NAME)
                    checkin_flag = 1
                elif(len(check_list_arry) >= 1 and check_out_again_flag == -1 or checkin_flag == 1):#有上班
                    check_out_number = -1
                    checkin_flag = 0
                    for i in range(len(check_list_arry)):
                        if(check_list_arry[i][2]=='上班'):#找上班第一筆
                            check_out_number = i 
                            break  
                    for i in range(len(check_list_arry)):
                        if(check_list_arry[len(check_list_arry)-i-1][2]=='下班'): #有上班+有下班
                            check_out_again_flag = i
                            print("今日已經打過卡，打卡資訊為：")
                            print(check_list_arry[check_out_number])
                            print(check_list_arry[len(check_list_arry)-i-1])      
                            text = str(NAME) + "您好！今日您的打卡的資訊為："
                            line_broadcast(text, LINE)
                            line_broadcast(  str(check_list_arry[check_out_number]),LINE)
                            line_broadcast(  str(check_list_arry[len(check_list_arry)-i-1]),LINE)
                            #check_list_arry=''
                            today_buffer_flag = 0
                            #print()
                            #print("--------------------------下次簽到時間(尚未簽到):", check_in_time1,"--------------------------")
                            #text = str("預計下次簽到時間為: "+ check_in_time1 + "  目前尚未簽到哦！！！！！")
                            #line_broadcast(text,LINE)
                            #print()
                            break
                    if(today_buffer_flag == 0):
                        break
                    
                    if(check_out_number != -1 and check_out_again_flag == -1): #有上班沒下班的情況
                        check_out_information = check_out_procedure(check_list_arry, check_out_number, usrid, password, LINE, NAME)
                        #check_list_arry=''
                        today_buffer_flag = 0
                        #line_broadcast(  str(check_list_arry[check_out_number]),LINE)
                        #line_broadcast(  str(check_out_information),LINE)
                        break

                        
























