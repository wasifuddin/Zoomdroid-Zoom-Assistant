import pyautogui
import pandas as pd
import tkinter as tk
from datetime import datetime
import os
import time
import email
import imaplib
import smtplib
import dropbox
df_status = pd.read_csv('bot_status.csv')
df_status.iloc[0, df_status.columns.get_loc('idle')] = 1
df_status.iloc[0, df_status.columns.get_loc('upload')] = 0
df_status.iloc[0, df_status.columns.get_loc('in_meet')] = 0
df_status.iloc[0, df_status.columns.get_loc('sav_rec')] = 0
df_status.to_csv('bot_status.csv', index=False)

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)


# def main():
access_token = 'BQov8ICOlMAAAAAAAAAAAZ0YmVdI80uwwEuiB3VYKUxjkIT3sGOBMZ3b7JMo0GiK'
transferData = TransferData(access_token)
#------------------------------------------------------------------------------------------------------------------------------------------------------



mail = imaplib.IMAP4_SSL('imap.gmail.com')
# (retcode, capabilities) = mail.login("zoombot6767@gmail.com","#ZOOM123bot")
(retcode, capabilities) = mail.login("zoombot6767@gmail.com","iuwkezkvzlxjxjop")
c = 10
k = 0
global keyin

filename = 'meet_details.csv'
bot_status_file = 'bot_status.csv'
def start_rec():
    os.startfile(r"C:\Program Files (x86)\Free Cam 8\freecam.exe")
    time.sleep(5)
    print(1)
    pyautogui.hotkey('ctrl','n')
    time.sleep(3)
    print(1)
    pyautogui.click(544, 922)
    print(1)
    time.sleep(1)
    pyautogui.click(537, 1013)
    print(4)
    time.sleep(1)
    pyautogui.click(35, 1041)


def sign_in(meetingid,pswd):
    #Opens up the Zoom app
    os.startfile(r'C:\Users\asus\AppData\Roaming\Zoom\bin\Zoom.exe')
    time.sleep(15)
    # Clicking Join button
    pyautogui.click(776,436)
    time.sleep(3)
    # Entering the Meeting ID
    pyautogui.write(meetingid)
    pyautogui.press('enter')
    time.sleep(20)
    # Entering the Password
    pyautogui.write(pswd)
    pyautogui.press('enter')
    return 1

def sendEmail(content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('zoombot6767@gmail.com', 'iuwkezkvzlxjxjop')

    server.sendmail('wasifuddin544@gmail.com',"wasifuddin544@gmail.com", content)
    server.close()












#Reading the CSV file
df_status = pd.read_csv(bot_status_file)
# print(df_zoom)
while True:
    try:
        df_zoom = pd.read_csv(filename)
        # print(df_zoom)
        mail.list()
        mail.select('inbox')
        df = pd.read_csv(filename)

        n = 0
        (retcode, messages) = mail.search(None, '(UNSEEN)')
        if retcode == 'OK':

           for num in messages[0].split() :
              print ('Processing ')
              n=n+1
              typ, data = mail.fetch(num,'(RFC822)')
              for response_part in data:
                 if isinstance(response_part, tuple):
                     original = email.message_from_bytes(response_part[1])
                    # print (original['From'])
                    # print (original['Subject'])adsds
                     raw_email = data[0][1]
                     raw_email_string = raw_email.decode('utf-8')
                     email_message = email.message_from_string(raw_email_string)
                     for part in email_message.walk():
                            if (part.get_content_type() == "text/plain"): # ignore attachments/html
                                  body = part.get_payload(decode=True)
                                  save_string = str(r"E:\Wasifpyprojects\Tkinter Apps\storing_email\saving"+str(k)+ ".txt" )
                                  k +=1
                                  myfile = open(save_string, 'a')
                                  # myfile.write(original['From']+'\n')
                                  # myfile.write(original['Subject']+'\n')
                                  myfile.write(body.decode('utf-8'))
                                  print(body.decode('utf-8'))
                                  line = body.decode('utf-8')
                                  print(line)
                                  if 'Change' in line:
                                      df = pd.read_csv('meet_details.csv')
                                      dict_data = {}
                                      #line = '#Change Meeting Topic=Neuron to Time=04:35, Day=Mon ,Attend by=Bot'
                                      line = line.replace('Change Meeting ', '')
                                      line = line.replace('to', ',')
                                      listdata = line.split(',')
                                      for i in listdata:
                                          i = i.strip()
                                          i = i.split('=')
                                          dict_data[i[0]] = i[1]
                                      print(dict_data)
                                      c = 0
                                      for i in df['Meet_Topic']:
                                          if i == dict_data['Topic']:
                                              df.at[c, 'Timing'] = dict_data['Time']
                                              df.at[c, 'Meet_day'] = dict_data['Day']
                                              df.at[c, 'Meet_attend'] = dict_data['Attend by']
                                              # df.iloc[c, df.columns.get_loc('Timing')] = dict_data['Time']
                                              # df.iloc[c, df.columns.get_loc('Meet_day')] = dict_data['Day']
                                              # df.iloc[c, df.columns.get_loc('Meet_attend')] = dict_data['Attend by']
                                              df.to_csv('meet_details.csv', index=False)
                                              break
                                          c += 1
                                      print(df)
                                  #myfile.write('**********\n')
                                  myfile.close()
                            else:
                                  continue
                     typ, data = mail.store(num,'+FLAGS','\\Seen')

        print (n)
    except:
        pass
    #############################  ZOOM CODE ###########################################################

    #Determining the current time
    current_time_zoom = datetime.now().strftime('%H:%M')
    # Checking if the current time exists in our file
    print(current_time_zoom)
    if current_time_zoom in str(df_zoom['Timing']):
        row_zoom = df_zoom.loc[df_zoom['Timing'] == current_time_zoom]
        m_id_zoom = str(row_zoom.iloc[0,3])
        m_pswd_zoom = str(row_zoom.iloc[0,4])
        meet_title = str(row_zoom.iloc[0,5])
        meet_topic_st = meet_title
        meet_title = meet_title.strip()  + ('.wmv')
        print(m_id_zoom,m_pswd_zoom)
        df_status.iloc[0, df_status.columns.get_loc('idle')] = 0
        df_status.iloc[0, df_status.columns.get_loc('in_meet')] = 1
        df_status.to_csv(bot_status_file, index=False)
        start_rec()
        keyin = sign_in(m_id_zoom,m_pswd_zoom)
        #sign_in('4638796187','AM3SU7')
        time.sleep(60)
        content = 'I have joined the meeting on ' + meet_topic_st + ' on your behalf sir! I will send you the meeting recording as soon as the meeting is finished'
        try:
            sendEmail(content)
        except:
            sendEmail(content)
        if keyin == 1:
            while True:
                end_zoom = pyautogui.locateCenterOnScreen('join_btn_zoombot.PNG', confidence=0.9)
                print(end_zoom)
                if end_zoom is not None:
                    pyautogui.press('esc')
                    os.system("TASKKILL /F /IM Zoom.exe")
                    df_status.iloc[0, df_status.columns.get_loc('in_meet')] = 0
                    df_status.iloc[0, df_status.columns.get_loc('sav_rec')] = 1
                    df_status.to_csv(bot_status_file, index=False)
                new_zoom = pyautogui.locateCenterOnScreen('recend.PNG', grayscale=True, confidence=0.7)
                print(new_zoom)
                if new_zoom is not None:
                    # os.system("TASKKILL /F /IM Zoom.exe")
                    time.sleep(3)
                    pyautogui.click(125, 400)
                    time.sleep(1)
                    pyautogui.hotkey('ctrl', 'd')
                    time.sleep(1)

                    pyautogui.typewrite(meet_title)
                    time.sleep(1)
                    pyautogui.press('enter')
                    keyin = 0
                    time.sleep(60)
                    pyautogui.hotkey('alt', 'f4')
                    os.system("TASKKILL /F /IM freecam.exe")
                    file_from = 'D:/' + meet_title  # This is name of the file to be uploaded
                    file_to = '/zoomdroid uploads/' + meet_title  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

                    # API v2
                    print('Uploading..............')

                    df_status.iloc[0, df_status.columns.get_loc('sav_rec')] = 0
                    df_status.iloc[0, df_status.columns.get_loc('upload')] =1
                    df_status.to_csv(bot_status_file, index=False)
                    try:
                        transferData.upload_file(file_from, file_to)
                    except:
                        time.sleep(10)
                        transferData.upload_file(file_from, file_to)
                    time.sleep(60)
                    print(60)
                    df_status.iloc[0, df_status.columns.get_loc('idle')] = 1
                    df_status.iloc[0, df_status.columns.get_loc('upload')] = 0
                    df_status.to_csv(bot_status_file, index=False)
                    content = 'I have sent you the meeting recording on ' + meet_topic_st + ' in Dropbox Sir'

                    try:
                        sendEmail(content)
                    except:
                        time.sleep(10)
                        sendEmail(content)
                    break




