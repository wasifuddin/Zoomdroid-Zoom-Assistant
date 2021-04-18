import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
import pandas as pd
import store_data
import os
import pyttsx3
import speech_recognition
import datetime
import threading
import time

win = tk.Tk()
win.geometry('500x650+550+100')
win.rowconfigure(0, weight=1)
win.columnconfigure(0, weight=1)
win.configure(bg='black')
win.title('Zoomdroid')
logo_icon = tk.PhotoImage(file='Images/logo6.png')
win.iconphoto(False, logo_icon)

info_dict = {}












###############################    FUNCTION FUNCTION FUNCTION ##########################################################


# [----------------------------- FUNCTION User Sign Up ------------------------------------------------]
# User Sign Up frame : fr1 Frame Name [----- sign_up_fr ------]


def fname(event):
    global f_name
    f_name.delete(0, 'end')


def lname(event):
    global l_name
    l_name.delete(0, 'end')


def u_name(event):
    global user_name
    user_name.delete(0, 'end')


def u_email(event):
    global user_email
    user_email.delete(0, 'end')


def b_name(event):
    global bot_name
    bot_name.delete(0, 'end')


def b_email(event):
    global bot_email
    bot_email.delete(0, 'end')


def pasword(event):
    global passwd
    passwd.delete(0, 'end')


def cpasword(event):
    global com_passwd
    com_passwd.delete(0, 'end')


def get_info():
    global f_name
    global l_name
    global user_name
    global user_email
    global bot_name
    global bot_email
    global passwd
    global com_passwd
    global info_dict
    info_dict['fullname'] = f_name.get().strip()
    info_dict['lastname'] = l_name.get().strip()
    info_dict['username'] = user_name.get().strip()
    info_dict['user_email'] = user_email.get().strip()
    info_dict['botname'] = bot_name.get().strip()
    info_dict['bot_email'] = bot_email.get().strip()
    info_dict['password'] = passwd.get().strip()
    info_dict['c_password'] = com_passwd.get().strip()
    store_data.signup_entry(info_dict)
    msg_note_lb.config(text='Account Created Succesfully', width=28, height=2)
    show_frame(fr4)
    print(info_dict)


# ----------------------------------FUNCTION User Sign In Data----------------------------------------------
# Sign In Frame : fr4 Frame Name [----- sgn_fr_holder ------]


signin_dict = {}


def user_id_clear(event):
    global user_id
    user_id.delete(0, 'end')


def pass_id_clear(event):
    global pass_id
    pass_id.delete(0, 'end')


def get_signin_info():
    global user_id
    global pass_id
    global signin_dict
    global msg_note_lb
    global user_id
    global pass_id
    # signin_dict['user_id'] = user_id.get().strip()
    # signin_dict['pass_id'] = pass_id.get().strip()
    # store_data.signin_entry(signin_dict)
    # print(signin_dict)
    df_profile1 = pd.read_csv('user_data.csv')
    xusername = user_id.get().strip()
    xpass = pass_id.get().strip()
    if df_profile1['username'][0] == xusername and df_profile1['password'][0] == xpass:
        msg_note_lb.config(text='', width=0, height=0)
        user_id.delete(0, tk.END)
        pass_id.delete(0, tk.END)
        user_id.insert(0, '    User Name : ')
        pass_id.insert(0, '    Password : ')
        show_frame(fr5)
    else:
        #
        msg_note_lb.config(text='Wrong Sign In Info', width=28, height=2)
        user_id.delete(0, tk.END)
        pass_id.delete(0, tk.END)
        user_id.insert(0, '    User Name : ')
        pass_id.insert(0, '    Password : ')

        show_frame(fr3)
        show_frame(fr4)


# ----------------------------------FUNCTION Meeting Data Entry----------------------------------------------
# Meeting Entry : Frame Name [----- meet_entry ------]


def callpsd(event):
    global psd
    psd.delete(0, 'end')


def callmid(event):
    global meet_id
    meet_id.delete(0, 'end')


def callmtm(event):
    global meet_tm
    meet_tm.delete(0, 'end')


def callmtp(event):
    global meet_tp
    meet_tp.delete(0, 'end')


dict_meetinfo = {}


def get_meetinfo():
    global dict_meetinfo
    global meet_id
    global meet_tp
    global meet_tm
    global psd
    global meet_attend_value
    global meet_day_value
    global meet_info
    dict_meetinfo['Timing'] = meet_tm.get().strip()
    dict_meetinfo['Meet_day'] = meet_day_value.get().strip()
    meetby_desicion = str(meet_attend_value.get()).strip()
    if meetby_desicion  == '0':
        dict_meetinfo['Meet_attend'] = 'me'
    elif  meetby_desicion  == '1':
        dict_meetinfo['Meet_attend'] = 'bot'
    dict_meetinfo['MeetingID'] = meet_id.get().strip()
    dict_meetinfo['Password'] = psd.get().strip()
    dict_meetinfo['Meet_Topic'] = meet_tp.get().strip()
    list_meetinfo = [dict_meetinfo['Timing'],dict_meetinfo['Meet_day'],dict_meetinfo['Meet_attend'],dict_meetinfo['MeetingID'],dict_meetinfo['Password'],dict_meetinfo['Meet_Topic']]
    store_data.add_meeting(list_meetinfo)
    # store_data.add_meeting(dict_meetinfo)
    print(list_meetinfo)
    meet_id.delete(0, tk.END)
    meet_tp.delete(0, tk.END)
    meet_tm.delete(0, tk.END)
    psd.delete(0, tk.END)
    meet_tp.insert(0, '    Meeting Topic')
    meet_id.insert(0, '    Enter Meeting ID')
    psd.insert(0, '    Enter Password')
    meet_tm.insert(0, '    Meeting Timing')
    meet_day_value.set("Sun")


global change_value
change_value = 0
meet_day_store = 'Sun'
global stopage_value

def restor_frame():
    global meet_day_value
    global dict_meetinfo
    global meet_id
    global meet_tp
    global meet_tm
    global psd
    global meet_attend_value
    global meet_day_value
    global meet_info
    global change_value
    global meet_day_store
    global meet_day_option
    global meet_attend
    global stopage_value
    stopage_value = win.after(70, restor_frame)
    #print('the value is', meet_day_value.get())
    if meet_day_value.get() != meet_day_store:
        a1 = meet_tm.get().strip()
        a2 = meet_day_value.get().strip()
        a3 = meet_id.get().strip()
        a4 = psd.get().strip()
        a5 = str(meet_attend_value.get()).strip()
        a6 = meet_tp.get().strip()
        a7 = meet_attend_value.get()
        print(a7, a6)
        print(a1, a2, a3, a4, a5, a6)
        meet_day_store = a2
        meet_id.destroy()
        meet_tp.destroy()
        meet_tm.destroy()
        psd.destroy()
        meet_attend.destroy()
        meet_day_option.destroy()

        logo_spacing_mentry = tk.Label(meet_entry, text='', fg='white', height=4, bg='black')
        logo_spacing_mentry.grid(row=0, columnspan=5, sticky='w')
        logo_spacing1_mentry = tk.Label(meet_entry, text='', fg='white', height=4, bg='black')
        logo_spacing1_mentry.grid(row=1, column=0, sticky='w')
        logo_spacing2_mentry = tk.Label(meet_entry, text='', fg='white', height=4, bg='black')
        logo_spacing2_mentry.grid(row=2, column=0, sticky='w', ipady=0)

        meet_tp = tk.Entry(meet_entry, font=font_signup, width=48, bg=wid_color_bg, fg=wid_color_fg)
        meet_tp.insert(0, a6)
        meet_tp.grid(row=3, column=0, ipadx=60, ipady=10, pady=10, padx=20, columnspan=5, sticky='w')
        meet_tp.bind("<FocusIn>", callmtp)

        meet_id = tk.Entry(meet_entry, font=font_signup, width=13, bg=wid_color_bg, fg=wid_color_fg)
        meet_id.insert(0, a3)
        meet_id.grid(row=4, column=0, ipadx=60, ipady=10, pady=15, padx=20, sticky='w')
        meet_id.bind("<FocusIn>", callmid)

        psd = tk.Entry(meet_entry, font=font_signup, width=13, bg=wid_color_bg, fg=wid_color_fg)
        psd.insert(0, a4)
        psd.grid(row=4, column=1, ipadx=60, ipady=10, pady=10, sticky='w', columnspan=3)
        psd.bind("<FocusIn>", callpsd)

        # meet_attend_value = tk.IntVar()
        meet_attend = tk.Label(meet_entry, font=font_signup, text='    Meeting will be attended by', width=13,
                               bg=wid_color_bg, fg=wid_color_fg, anchor='w')
        meet_attend.grid(row=5, column=0, ipadx=130, ipady=10, pady=15, padx=20, sticky='w', columnspan=5)

        me_rdbtn = tk.Radiobutton(meet_entry, font=font_signup, text="  Me", variable=meet_attend_value, value=0,
                                  cursor='dot', bg=wid_color_bg, width=10, fg=wid_color_fg,
                                  selectcolor='dark slate gray')
        me_rdbtn.grid(row=5, column=1, ipady=8, pady=10, sticky='w')

        bot_rdbtn = tk.Radiobutton(meet_entry, font=font_signup, text="  Bot", variable=meet_attend_value, value=1,
                                   cursor='dot', bg=wid_color_bg, width=10, fg=wid_color_fg,
                                   selectcolor='dark slate gray', )
        bot_rdbtn.grid(row=5, column=2, ipadx=10, ipady=8, pady=10, sticky='w')

        meet_tm = tk.Entry(meet_entry, font=font_signup, width=13, bg=wid_color_bg, fg=wid_color_fg)
        meet_tm.insert(0, a1)
        meet_tm.grid(row=6, column=0, ipadx=60, ipady=10, pady=15, padx=20, sticky='w')
        meet_tm.bind("<FocusIn>", callmtm)

        meet_day = tk.Label(meet_entry, font=font_signup, text='    Meeting day : ', width=13, bg=wid_color_bg,
                            fg=wid_color_fg, anchor='w')
        meet_day.grid(row=6, column=1, ipadx=20, ipady=10, pady=10, sticky='w', columnspan=3)

        meet_day_value = tk.StringVar(meet_entry)
        meet_day_value.set(a2)
        meet_day_option = tk.OptionMenu(meet_entry, meet_day_value, 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', "Sat")
        meet_day_option.config(font=('Helvetica', (10)), bg=wid_color_bg, fg=wid_color_fg, activeforeground='black',
                               activebackground=wid_color_fg)
        meet_day_option['menu'].config(font=('Helvetica', (10)), bg=wid_color_bg, fg=wid_color_fg, bd=3,
                                       activeforeground='black', activebackground=wid_color_fg)
        meet_day_option.grid(row=6, column=2, ipadx=27, ipady=5, sticky='w', columnspan=3)
        # meet_day_option.bind("<FocusIn>", restor_frame())
        # restor_frame()

        reg_btn = tk.Button(meet_entry, font=font_signup, text='Register Meeting', bg=wid_color_bg, fg=wid_color_fg,
                            command=get_meetinfo)
        reg_btn.grid(row=7, column=2, ipadx=9, ipady=5, pady=90, sticky='e')

        goto_metsche_btn = tk.Button(meet_entry, font=font_signup, text='Schedule', bg=wid_color_bg, fg=wid_color_fg,
                                     command=lambda: change_meet_to_sch())
        goto_metsche_btn.grid(row=7, column=1, ipadx=9, ipady=5, pady=90, sticky='e')

        # backicon1= ImageTk.PhotoImage(Image.open("backiconblue.png"))
        back_btn_meet = tk.Button(meet_entry, image=backicon, width=18, height=18, border=0,
                                  command=lambda: config_chg_bt_sch_normal())
        back_btn_meet.place(relx=0.01, rely=0.01)
        # change_value = 1
        # win.after_cancel(stopage_value)
def change_meet_to_sch():
    show_frame(fr3)
    global back_btn_meetsch
    back_btn_meetsch.config(command = lambda : show_frame(fr2))
    global stopage_value
    win.after_cancel(stopage_value)
def config_chg_bt_sch_normal():
    global  back_btn_meetsch
    back_btn_meetsch.config(command = lambda :show_frame(fr5))
    show_frame(fr5)
    global stopage_value
    win.after_cancel(stopage_value)
# ----------------------------------FUNCTION Meeting Schedule----------------------------------------------
# Meeting Schedule Show : fr3 Frame Name [----- met_sch_fr ------]


del_row_no = []


def select_record():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry5.delete(0, tk.END)
    entry6.delete(0, tk.END)
    selected = tree.focus()
    values = tree.item(selected, 'values')
    entry1.insert(0, values[5])
    entry2.insert(0, values[3])
    entry3.insert(0, values[4])
    entry4.insert(0, values[0])
    entry5.insert(0, values[1])
    entry6.insert(0, values[2])


def clicker(e):
    select_record()


def update_record():
    selected = tree.focus()
    tree.item(selected, text="",
              values=(entry4.get(), entry5.get(), entry6.get(), entry2.get(), entry3.get(), entry1.get()))
    data[int(selected)] = [entry4.get(), entry5.get(), entry6.get(), entry2.get(), entry3.get(), entry1.get()]
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry5.delete(0, tk.END)
    entry6.delete(0, tk.END)


def delete_row():
    row_delete = tree.selection()[0]
    del_row_no.append(int(row_delete))
    del_row_no.sort(reverse=True)
    tree.delete(row_delete)
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry5.delete(0, tk.END)
    entry6.delete(0, tk.END)


def delete_all():
    global data

    for record in tree.get_children():
        tree.delete(record)
    data = []


def save_changes():
    global del_row_no
    global data
    if data is not None and del_row_no is not None:
        for i in del_row_no:
            del (data[i])
    del_row_no = []
    df1 = pd.DataFrame(data, columns=['Timing', 'Meet_day','Meet_attend', 'MeetingID', 'Password' , 'Meet_Topic'])
    df1.to_csv(filename, index=False)

    for record in tree.get_children():
        tree.delete(record)
    if data is not None:
        j = 0
        for rec1 in data:
            tree.insert(parent='', index='end', iid=j, text='',
                        values=(rec1[0], rec1[1], rec1[2], rec1[3], rec1[4], rec1[5]))
            j += 1


def continuous_update():
    global data
    df2 = pd.read_csv(filename)
    data = df2.to_numpy().tolist()
    for record1 in tree.get_children():
        tree.delete(record1)
    id_no_var_c1 = 0
    for rec2 in data:
        tree.insert(parent='', index='end', iid=id_no_var_c1, text='',
                    values=(rec2[0], rec2[1], rec2[2], rec2[3], rec2[4], rec2[5]))
        id_no_var_c1 += 1


# ----------------------------------FUNCTION CHAT BOT----------------------------------------------
# Chat Bot : fr5 Frame Name [----- chatbot_fr ------]

# ENGINE SETUP

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    win.after(1000)
    engine.runAndWait()


def del_entry_box(event):
    global user_msg_entry
    user_msg_entry.delete(0, 'end')


def meet_details_show_lbl(meet_topic_bot, meet_time_bot, meet_no, day_query):
    if meet_no != 0:
        reply = 'Sir ' + day_query + ' you have meetings on.........'
        speak_reply = 'Sir ' + day_query + ' you have meetings on.........'
        l = tk.Label(bot_msg_fr, text=reply, font=font_type_bottext, anchor='w', fg=wid_fg, bg=wid_bg)
        l.pack(anchor='w', pady=5)

        for i in range(meet_no):
            reply = str(i + 1) + ') Meeeting on ' + meet_topic_bot[i] + ' at ' + meet_time_bot[i] + '\n'
            speak_reply += 'Meeeting on ' + meet_topic_bot[i] + ' at ' + meet_time_bot[i] + '\n'
            l = tk.Label(bot_msg_fr, text=reply, font=font_type_bottext, anchor='w', fg=wid_fg, bg=wid_bg)
            l.pack(anchor='w', pady=5)
            #
            # speak(reply)
        threading.Thread(target=lambda: speak(speak_reply)).start()
    else:
        if day_query == 'today':
            reply = 'Today'
        elif day_query == 'tomorrow':
            reply = "Tomorrow"
        reply += " you have no meeting Sir"
        l = tk.Label(bot_msg_fr, text=reply, font=font_type_bottext, anchor='w', fg=wid_fg, bg=wid_bg)
        l.pack(anchor='w', pady=5)
        threading.Thread(target=lambda: speak(reply)).start()


def meet_details_extract(day_of_meet):
    meet_no = 0
    index = 0
    meet_time_bot = []
    meet_topic_bot = []
    df_meetdata_bot = pd.read_csv('meet_details.csv')
    for i in df_meetdata_bot['Meet_day']:
        if i == day_of_meet:
            time_store = str(df_meetdata_bot.iloc[index, 0])
            topic_store = str(df_meetdata_bot.iloc[index, 5])
            meet_time_bot.append(time_store)
            meet_topic_bot.append(topic_store)
            meet_no += 1
        index += 1
    return meet_topic_bot, meet_time_bot, meet_no


def response():
    clear_lb()
    global user_msg_entry
    global user_msg
    global bot_msg
    global l
    statement = user_msg_entry.get()

    user_msg = tk.Label(user_msg_fr, font=font_type_bottext, text=statement, fg=wid_fg, bg=wid_bg)
    user_msg.pack(anchor='e', pady=5)

    # threading.Thread(target = lambda :speak(statement)).start()
    statement = statement.lower()
    user_msg_entry.delete(0, 'end')

    print(statement)
    if 'hi' in statement:
        df_bot = pd.read_csv('user_data.csv')
        greet_reply = ['Hello Sir! I\'m '+ df_bot['botname'][0] +' your Virtual Zoom Assistant.',
                       'It seems that you have not registered any meetings yet!',
                       'Kindly register your meetings so that I can assist you'

                       ]
        # 'I can assist you by attending, managing and keeping \ntrack of your zoom meetings as per your need',
        hi_reply = 'Hello Sir! I\'m '+ df_bot['botname'][0] +' your Virtual Zoom Assistant. \nIt seems that you have not registered any meetings yet! \n Kindly register your meetings so that I can assist you'

        threading.Thread(target=lambda: speak(hi_reply)).start()

        for i in greet_reply:
            l1 = tk.Label(bot_msg_fr, text=i, font=font_type_bottext, anchor='w', fg=wid_fg, bg=wid_bg)
            # l1.grid(row=0, sticky='w', rowspan=5)
            l1.pack(anchor='w', pady=5)
    if 'how many' in statement:
        dt = datetime.datetime.today()
        if 'today' in statement:
            day_of_meet = datetime.date(dt.year, dt.month, dt.day).strftime('%a')
            meet_details_extract(day_of_meet)
            m_topic, m_time, m_no = meet_details_extract(day_of_meet)
            l = tk.Label(bot_msg_fr, text='Today you have ' + str(m_no) + ' meetings sir', fg=wid_fg,
                         font=font_type_bottext, anchor='w', bg=wid_bg)
            l.pack(anchor='w', pady=5)
            threading.Thread(target=lambda: speak('Today you have ' + str(m_no) + ' meetings sir')).start()

        if 'tomorrow' in statement:
            dt_day = dt.day + 1
            day_of_meet = datetime.date(dt.year, dt.month, dt_day).strftime('%a')
            m_topic, m_time, m_no = meet_details_extract(day_of_meet)
            l = tk.Label(bot_msg_fr, text='Tomorrow you have ' + str(m_no) + ' meetings sir', fg=wid_fg,
                         font=font_type_bottext, anchor='w', bg=wid_bg)
            l.pack(anchor='w', pady=5)
            threading.Thread(target=lambda: speak('Tomorrow you have ' + str(m_no) + ' meetings sir')).start()

    if 'next meeting' in statement:
        dt = datetime.datetime.today()
        day_of_meet = datetime.date(dt.year, dt.month, dt.day).strftime('%a')
        if day_of_meet in str(df_meetdata_bot['Meet_day']):
            row_next = df_meetdata_bot.loc[df_meetdata_bot['Meet_day'] == day_of_meet]
            next_meet_time = str(row_next.iloc[0, 0])
            next_meet_topic = str(row_next.iloc[0, 5])
            l = tk.Label(bot_msg_fr,
                         text='Your next meeting is on ' + next_meet_topic + ' at ' + next_meet_time + ' sir',
                         fg=wid_fg, font=font_type_bottext, anchor='w', bg=wid_bg)
            l.pack(anchor='w', pady=5)
            threading.Thread(target=lambda: speak(
                'Your next meeting is on ' + next_meet_topic + ' at ' + next_meet_time + ' sir')).start()
    if 'what' in statement:
        dt = datetime.datetime.today()
        if 'today' in statement:
            day_of_meet = datetime.date(dt.year, dt.month, dt.day).strftime('%a')
            m_topic, m_time, m_no = meet_details_extract(day_of_meet)
            day_query = 'today'
            meet_details_show_lbl(m_topic, m_time, m_no, day_query)

        if 'tomorrow' in statement:
            dt_day = dt.day + 1
            day_of_meet = datetime.date(dt.year, dt.month, dt_day).strftime('%a')
            m_topic, m_time, m_no = meet_details_extract(day_of_meet)
            day_query = 'tomorrow'
            meet_details_show_lbl(m_topic, m_time, m_no, day_query)


def clear_lb():
    global frtext
    global user_msg_fr
    global bot_msg_fr

    frtext.destroy()
    user_msg_fr.destroy()
    bot_msg_fr.destroy()
    frtext_cover = tk.Label(chatbot_fr, image=bot_img2, width=490, height=470)
    frtext_cover.grid(row=0, column=0, pady=50, sticky='w', rowspan=2)

    frtext = tk.Label(chatbot_fr, image=bot_img1, width=490, height=475)
    frtext.place(relx=0.0, rely=0.068)

    user_msg_fr = tk.Frame(chatbot_fr, bg='black')
    user_msg_fr.grid(row=0, sticky='e')

    bot_msg_fr = tk.Frame(chatbot_fr, bg='black')
    bot_msg_fr.grid(row=0, sticky='w', rowspan=10)

    frtext_lb_chat = tk.Label(frtext, text="Chat Screen", fg=wid_fg, bg=wid_bg, font=("Helvetica", 14, "bold"),
                              width=20)
    frtext_lb_chat.place(relx=0.23, rely=0.05)

    menu_tittlelb = tk.Label(chatbot_fr, text='', bg='black', width=70, height=2)
    menu_tittlelb.place(relx=0.0, rely=0.0)

    new_meet_bot_head = tk.Button(menu_tittlelb, width=15, text='Profile', font=font_type_head_bot, bg='black',
                                  fg=wid_fg,command=lambda: show_frame(fr6))
    new_meet_bot_head.place(relx=0.06, rely=0.03)

    new_meet_bot_head1 = tk.Button(menu_tittlelb, width=17, text='ADD Meeting', font=font_type_head_bot, bg='black',
                                   fg=wid_fg, command=lambda: show_frame(fr2))
    new_meet_bot_head1.place(relx=0.341, rely=0.03)

    new_meet_bot_head2 = tk.Button(menu_tittlelb, width=20, text='Meeting Schedule', font=font_type_head_bot,
                                   bg='black', fg=wid_fg, command=lambda: show_frame(fr3))
    new_meet_bot_head2.place(relx=0.65, rely=0.03)

    borderlb = tk.Label(frtext, text="", bg='cyan', width=80)
    borderlb.place(relx=0.0, rely=0.01, relheight=0.01)

    borderlb1 = tk.Label(frtext, text="", bg='cyan', width=80)
    borderlb1.place(relx=0.0, rely=0.8, relheight=0.01)

    set_logolb = tk.Label(chatbot_fr, image=settingicon, bg='black')
    set_logolb.place(relx=0.001, rely=0.005)

    send_user_entry_bt = tk.Button(chatbot_fr, font=font_type_bot, text='Send', bg='cyan', command=lambda: response())
    send_user_entry_bt.place(relx=0.8, rely=0.781)


# ----------------------------------FUNCTION PROFILE STATUS----------------------------------------------
# PROFILE STATUS : fr6 Frame Name [----- profile_fr ------]


def status_update():
    global status_lb_pf1
    global status_lb_pf2
    global status_lb_pf3
    global status_lb_pf4
    bot_df = pd.read_csv('bot_status.csv')
    if int(bot_df['idle'][0]) == 1:
        status_lb_pf1.config(bg=wid_fg, fg=wid_color_bg)
    else:
        status_lb_pf1.config(bg=wid_bg, fg=wid_color_fg)

    if int(bot_df['in_meet'][0]) == 1:
        status_lb_pf2.config(bg=wid_fg, fg=wid_color_bg)
    else:
        status_lb_pf2.config(bg=wid_bg, fg=wid_color_fg)

    if int(bot_df['sav_rec'][0]) == 1:
        status_lb_pf3.config(bg=wid_fg, fg=wid_color_bg)
    else:
        status_lb_pf3.config(bg=wid_bg, fg=wid_color_fg)

    if int(bot_df['upload'][0]) == 1:
        status_lb_pf4.config(bg=wid_fg, fg=wid_color_bg)
    else:
        status_lb_pf4.config(bg=wid_bg, fg=wid_color_fg)

    win.after(100, status_update)


def load_data():
    global f_name_pf
    global l_name_pf
    global user_name_pf
    global pass_pf
    global user_email_pf
    global bot_email_pf
    df_profile = pd.read_csv('user_data.csv')
    f_name_pf.delete(0, tk.END)
    l_name_pf.delete(0, tk.END)
    user_name_pf.delete(0, tk.END)
    pass_pf.delete(0, tk.END)
    user_email_pf.delete(0, tk.END)
    bot_email_pf.delete(0, tk.END)

    f_name_pf.insert(0, df_profile['fullname'][0])
    l_name_pf.insert(0, df_profile['lastname'][0])
    user_name_pf.insert(0, df_profile['username'][0])
    pass_pf.insert(0, df_profile['password'][0])
    user_email_pf.insert(0, df_profile['user_email'][0])
    bot_email_pf.insert(0, df_profile['bot_email'][0])


def save_changes_pf():
    global f_name_pf
    global l_name_pf
    global user_name_pf
    global pass_pf
    global user_email_pf
    global bot_email_pf

    df_profile.iloc[0, df_profile.columns.get_loc('fullname')] = f_name_pf.get()
    df_profile.iloc[0, df_profile.columns.get_loc('lastname')] = l_name_pf.get()
    df_profile.iloc[0, df_profile.columns.get_loc('username')] = user_name_pf.get()
    df_profile.iloc[0, df_profile.columns.get_loc('password')] = pass_pf.get()
    df_profile.iloc[0, df_profile.columns.get_loc('user_email')] = user_email_pf.get()
    df_profile.iloc[0, df_profile.columns.get_loc('bot_email')] = bot_email_pf.get()
    df_profile.to_csv('user_data.csv', index=False)


def signout_profile():
    global msg_note_lb

    show_frame(fr5)
    show_frame(fr4)


# ----------------------------------FUNCTION LOADING----------------------------------------------
# LOADING : fr7 Frame Name [----- app_bg_fr ------]
def change_load_others():
    win.after(5000, show_frame(fr4))


#############################################################################################


def show_frame(frame):
    if frame == fr3:
        continuous_update()
    if frame == fr6:
        load_data()
    if frame == fr2:
        global meet_id
        global meet_tp
        global meet_tm
        global psd
        global meet_attend_value
        global meet_day_value
        global meet_info
        global change_value
        global meet_attend
        global storage_value
        meet_id.delete(0, tk.END)
        meet_tp.delete(0, tk.END)
        meet_tm.delete(0, tk.END)
        psd.delete(0, tk.END)
        meet_tp.insert(0, '    Meeting Topic')
        meet_id.insert(0, '    Enter Meeting ID')
        psd.insert(0, '    Enter Password')
        meet_tm.insert(0, '    Meeting Timing')
        meet_day_value.set("Sun")
        threading.Thread(target=lambda: restor_frame()).start()

    if frame != fr2:
        try:
            win.after_cancel(storage_value)
        except:
            pass
    if frame == fr5:
        clear_lb()
    frame.tkraise()


##########################################################################################################################################

# -------------------------- Frame Gathering ----------------------------------------------


# User Sign Up frame : fr1 Frame Name [----- sign_up_fr ------]

fr1 = tk.Frame(win, bg='black', width=400, height=500)

# Meeting Entry : fr2 Frame Name [----- meet_entry ------]

fr2 = tk.Frame(win, bg='black', width=400, height=500)

# Meeting Schedule Show : fr3 Frame Name [----- met_sch_fr ------]

fr3 = tk.Frame(win, bg='black', width=400, height=500)

# Sign In Frame : fr4 Frame Name [----- sgn_fr_holder ------]

fr4 = tk.Frame(win, bg='black', width=400, height=500)

# Chat Bot Frame : fr5 Frame Name [----- sgn_fr_holder ------]

fr5 = tk.Frame(win, bg='black', width=400, height=500)

# Profile Frame : fr6 Frame Name [----- profile_fr ------]

fr6 = tk.Frame(win, bg='black', width=400, height=500)
# Loading Frame : f7 Frame Name [----- app_bg_fr ------]

fr7 = tk.Frame(win, bg='black', width=400, height=500)


for frame in (fr1, fr2, fr3, fr4, fr5, fr6, fr7):
    frame.grid(row=0, column=0, sticky='nsew')

######################################################################################################################################################

# BAKCGROUND COLOR OF WIDGET
wid_color_bg = 'black'
# FOREGROUND COLOR OF WIDGET

wid_color_fg = 'cyan'
# FOR CHAT BOT
wid_fg = 'cyan'
wid_bg = 'black'
# FONTS OF FRAMES

font_signup = ("Helvetica", 9, "bold")
font_signin = ("Helvetica", 9, "bold")
font_type = ("Helvetica", 9, "bold")
font_type_bot = ("Helvetica", 11, "bold")
font_type_bottext = ("Helvetica", 12, "bold")
font_type_head_bot = ("Helvetica", 10, "bold")
# DATABASE FILE

filename = 'meet_details.csv'
df_bot = pd.read_csv('user_data.csv')
df_meetdata_bot = pd.read_csv(filename)

# IMAGE OF BACKGROUND



backgrdx = ImageTk.PhotoImage(Image.open("Images/m_bg.jpg"))
backgrdy = ImageTk.PhotoImage(Image.open("Images/m_12.jpg"))
settingicon = ImageTk.PhotoImage(Image.open("Images/set_final.jpg"))
backicon = ImageTk.PhotoImage(Image.open("Images/blueb_iconfinal.jpg"))

# LOGO OF FRAMES


#################################################################################


####################################################################################################################

# ----------------------------------- MEET ENTRY [ meet_entry ] START ----------------------------------------------


# FRAME HOLDER


meet_entry = tk.Label(fr2, width=500, height=700, image=backgrdy, anchor='center')
meet_entry.grid(row=0, column=0, ipady=90, rowspan=40)
# LOGO BENEATH SPACE

logo_spacing_mentry = tk.Label(meet_entry, text='', fg='white', height=4, bg='black')
logo_spacing_mentry.grid(row=0, columnspan=5, sticky='w')
logo_spacing1_mentry = tk.Label(meet_entry, text='', fg='white', height=4, bg='black')
logo_spacing1_mentry.grid(row=1, column=0, sticky='w')
logo_spacing2_mentry = tk.Label(meet_entry, text='', fg='white', height=4, bg='black')
logo_spacing2_mentry.grid(row=2, column=0, sticky='w', ipady=0)

meet_tp = tk.Entry(meet_entry, font=font_signup, width=48, bg=wid_color_bg, fg=wid_color_fg)
meet_tp.insert(0, '    Meeting Topic')
meet_tp.grid(row=3, column=0, ipadx=60, ipady=10, pady=10, padx=20, columnspan=5, sticky='w')
meet_tp.bind("<FocusIn>", callmtp)

meet_id = tk.Entry(meet_entry, font=font_signup, width=13, bg=wid_color_bg, fg=wid_color_fg)
meet_id.insert(0, '    Enter Meeting ID')
meet_id.grid(row=4, column=0, ipadx=60, ipady=10, pady=15, padx=20, sticky='w')
meet_id.bind("<FocusIn>", callmid)

psd = tk.Entry(meet_entry, font=font_signup, width=13, bg=wid_color_bg, fg=wid_color_fg)
psd.insert(0, '    Enter Password')
psd.grid(row=4, column=1, ipadx=60, ipady=10, pady=10, sticky='w', columnspan=3)
psd.bind("<FocusIn>", callpsd)

meet_attend_value = tk.IntVar()
meet_attend = tk.Label(meet_entry, font=font_signup, text='    Meeting will be attended by', width=13, bg=wid_color_bg,
                       fg=wid_color_fg, anchor='w')
meet_attend.grid(row=5, column=0, ipadx=130, ipady=10, pady=15, padx=20, sticky='w', columnspan=5)

me_rdbtn = tk.Radiobutton(meet_entry, font=font_signup, text="  Me", variable=meet_attend_value, value=0,
                          cursor='dot', bg=wid_color_bg, width=10, fg=wid_color_fg, selectcolor='dark slate gray')
me_rdbtn.grid(row=5, column=1, ipady=8, pady=10, sticky='w')

bot_rdbtn = tk.Radiobutton(meet_entry, font=font_signup, text="  Bot", variable=meet_attend_value, value=1,
                           cursor='dot', bg=wid_color_bg, width=10, fg=wid_color_fg, selectcolor='dark slate gray', )
bot_rdbtn.grid(row=5, column=2, ipadx=10, ipady=8, pady=10, sticky='w')

meet_tm = tk.Entry(meet_entry, font=font_signup, width=13, bg=wid_color_bg, fg=wid_color_fg)
meet_tm.insert(0, '    Meeting Timing')
meet_tm.grid(row=6, column=0, ipadx=60, ipady=10, pady=15, padx=20, sticky='w')
meet_tm.bind("<FocusIn>", callmtm)

meet_day = tk.Label(meet_entry, font=font_signup, text='    Meeting day : ', width=13, bg=wid_color_bg, fg=wid_color_fg,
                    anchor='w')
meet_day.grid(row=6, column=1, ipadx=20, ipady=10, pady=10, sticky='w', columnspan=3)

meet_day_value = tk.StringVar(meet_entry)
meet_day_value.set('Sun')
meet_day_option = tk.OptionMenu(meet_entry, meet_day_value, 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', "Sat")
meet_day_option.config(font=('Helvetica', (10)), bg=wid_color_bg, fg=wid_color_fg, activeforeground='black',
                       activebackground=wid_color_fg)
meet_day_option['menu'].config(font=('Helvetica', (10)), bg=wid_color_bg, fg=wid_color_fg, bd=3,
                               activeforeground='black', activebackground=wid_color_fg)
meet_day_option.grid(row=6, column=2, ipadx=27, ipady=5, sticky='w', columnspan=3)


reg_btn = tk.Button(meet_entry, font=font_signup, text='Register Meeting', bg=wid_color_bg, fg=wid_color_fg,
                    command=get_meetinfo)
reg_btn.grid(row=7, column=2, ipadx=9, ipady=5, pady=90, sticky='e')

goto_metsche_btn = tk.Button(meet_entry, font=font_signup, text='Schedule', bg=wid_color_bg, fg=wid_color_fg,
                             command=lambda: change_meet_to_sch())
goto_metsche_btn.grid(row=7, column=1, ipadx=9, ipady=5, pady=90, sticky='e')

# backicon1= ImageTk.PhotoImage(Image.open("backiconblue.png"))
back_btn_meet = tk.Button(meet_entry, image=backicon, width=18, height=18, border=0, command=lambda: config_chg_bt_sch_normal())
back_btn_meet.place(relx=0.01, rely=0.01)

# ----------------------------------- MEET ENTRY [ meet_entry ] START ----------------------------------------------

####################################################################################################################


####################################################################################################################

# ----------------------------------- SIGN UP [ sign_up_fr ] START -------------------------------------------------

# Holding Frame


sign_up_fr = tk.Label(fr1, width=500, height=700, image=backgrdx, anchor='center')
sign_up_fr.grid(row=0, column=0, ipady=60, ipadx=6)
# Frame logo

logo_spacing = tk.Label(sign_up_fr, text='', fg='white', height=4, bg='black')
logo_spacing.grid(row=0, columnspan=5, sticky='w')
logo_spacing1 = tk.Label(sign_up_fr, text='', fg='white', height=4, bg='black')
logo_spacing1.grid(row=1, column=0, sticky='w')
logo_spacing2 = tk.Label(sign_up_fr, text='', fg='white', height=4, bg='black')
logo_spacing2.grid(row=2, column=0, sticky='w')

f_name = tk.Entry(sign_up_fr, font=font_signup, width=13, bg=wid_color_bg, fg=wid_color_fg)
f_name.insert(0, '    First Name :')
f_name.grid(row=3, column=0, ipadx=60, ipady=10, pady=15, padx=20, sticky='w')
f_name.bind("<FocusIn>", fname)

l_name = tk.Entry(sign_up_fr, font=font_signup, width=13, bg=wid_color_bg, fg=wid_color_fg)
l_name.insert(0, '    Last Name :')
l_name.grid(row=3, column=1, ipadx=60, ipady=10, pady=10, sticky='w', columnspan=3)
l_name.bind("<FocusIn>", lname)

user_name = tk.Entry(sign_up_fr, font=font_signup, width=13, bg=wid_color_bg, fg=wid_color_fg)
user_name.insert(0, '    User Name : ')
user_name.grid(row=4, column=0, ipadx=60, ipady=10, pady=15, padx=20, sticky='w')
user_name.bind("<FocusIn>", u_name)

user_email = tk.Entry(sign_up_fr, font=font_signup, width=13, bg=wid_color_bg, fg=wid_color_fg)
user_email.insert(0, '    User Email : ')
user_email.grid(row=4, column=1, ipadx=60, ipady=10, pady=10, sticky='w', columnspan=3)
user_email.bind("<FocusIn>", u_email)

bot_name = tk.Entry(sign_up_fr, font=font_signup, width=13, bg=wid_color_bg, fg=wid_color_fg)
bot_name.insert(0, '    Bot Name : ')
bot_name.grid(row=5, column=0, ipadx=60, ipady=10, pady=15, padx=20, sticky='w')
bot_name.bind("<FocusIn>", b_name)

bot_email = tk.Entry(sign_up_fr, font=font_signup, width=13, bg=wid_color_bg, fg=wid_color_fg)
bot_email.insert(0, '    Bot Email : ')
bot_email.grid(row=5, column=1, ipadx=60, ipady=10, pady=10, sticky='w', columnspan=3)
bot_email.bind("<FocusIn>", b_email)

passwd = tk.Entry(sign_up_fr, font=font_signup, width=13, bg=wid_color_bg, fg=wid_color_fg)
passwd.insert(0, '    Password : ')
passwd.grid(row=6, column=0, ipadx=60, ipady=10, pady=15, padx=20, sticky='w')
passwd.bind("<FocusIn>", pasword)

com_passwd = tk.Entry(sign_up_fr, font=font_signup, width=13, bg=wid_color_bg, fg=wid_color_fg)
com_passwd.insert(0, '    Confirm Password : ')
com_passwd.grid(row=6, column=1, ipadx=60, ipady=10, pady=10, sticky='w', columnspan=3)
com_passwd.bind("<FocusIn>", cpasword)

crt_accnt_btn = tk.Button(sign_up_fr, font=font_signup, text="Create Account", bg=wid_color_bg, fg=wid_color_fg,
                          width=15, command=get_info)
crt_accnt_btn.grid(row=7, column=0, padx=140, ipadx=40, ipady=10, pady=10, sticky='we', columnspan=2)

back_btn_signup = tk.Button(sign_up_fr, image=backicon, width=18, height=18, border=0, command=lambda: show_frame(fr4))
back_btn_signup.place(relx=0.01, rely=0.01)

# ----------------------------------- SIGN UP [ sign_up_fr ] END ---------------------------------------------------

####################################################################################################################


####################################################################################################################

# ----------------------------------- SIGN IN [ sgn_fr_holder ] START ----------------------------------------------

# Frame Holder

sgn_fr_holder = tk.Label(fr4, width=500, height=700, image=backgrdx, anchor='center')
sgn_fr_holder.grid(row=0, column=0, ipady=70, ipadx=8)

logo_spacing_signin = tk.Label(sgn_fr_holder, text='', fg='white', height=4, bg='black')
logo_spacing_signin.grid(row=0, columnspan=5, sticky='w')
logo_spacing1_signin = tk.Label(sgn_fr_holder, text='', fg='white', height=4, bg='black')
logo_spacing1_signin.grid(row=1, column=0, sticky='w')
logo_spacing2_signin = tk.Label(sgn_fr_holder, text='', fg='white', height=4, bg='black')
logo_spacing2_signin.grid(row=2, column=0, sticky='w')

user_id = tk.Entry(sgn_fr_holder, font=font_signin, width=15, bg=wid_color_bg, fg=wid_color_fg)
user_id.insert(0, '    User Name : ')
user_id.grid(row=5, column=0, columnspan=3, ipadx=60, ipady=10, pady=15, padx=70, sticky='we')
user_id.bind("<FocusIn>", user_id_clear)

pass_id = tk.Entry(sgn_fr_holder, font=font_signin, width=15, bg=wid_color_bg, fg=wid_color_fg)
pass_id.insert(0, '    Password : ')
pass_id.grid(row=6, column=0, columnspan=3, ipadx=60, ipady=10, pady=15, padx=70, sticky='we')
pass_id.bind("<FocusIn>", pass_id_clear)

keep_signin_lbl = tk.Label(sgn_fr_holder, font=font_signin, text='  Keep me sign in', width=16, fg=wid_color_fg,
                           bg=wid_color_bg, anchor='w')
keep_signin_lbl.grid(row=7, column=0, padx=165, ipadx=10, ipady=8, pady=10, sticky='w', columnspan=3)

value_signin_box = tk.IntVar()
keep_signin_box = tk.Checkbutton(sgn_fr_holder, variable=value_signin_box,
                                 onvalue=1, offvalue=0,
                                 width=1, bg=wid_color_bg)
keep_signin_box.grid(row=7, column=1, padx=30, pady=10, sticky='w', columnspan=2)

sign_in_btn = tk.Button(sgn_fr_holder, font=font_signin, text="Sign In", bg=wid_color_bg, fg=wid_color_fg, width=15,
                        command=get_signin_info)
sign_in_btn.grid(row=8, column=0, padx=140, ipadx=40, ipady=8, pady=10, sticky='we', columnspan=2)

sign_up_btn = tk.Button(sgn_fr_holder, font=font_signin, text="Sign Up", bg=wid_color_bg, fg=wid_color_fg, width=15,
                        command=lambda: show_frame(fr1))
sign_up_btn.grid(row=9, column=0, padx=140, ipadx=40, ipady=8, pady=10, sticky='we', columnspan=2)

msg_note_lb = tk.Label(sgn_fr_holder, text='', width=0, height=0, font=('Helvetica', 12, 'bold'), bg=wid_color_bg,
                       fg=wid_color_fg)
msg_note_lb.place(relx=0.2, rely=0.85)
# ----------------------------------- SIGN IN [ sgn_fr_holder ] END ------------------------------------------------

####################################################################################################################


####################################################################################################################

# ----------------------------------- Meeting Schedule [ met_sch_fr ] START ----------------------------------------


# Frame Holder


img1 = ImageTk.PhotoImage(Image.open("Images/m_10.jpg"))

met_sch_fr = tk.Label(fr3, width=500, height=700, image=img1, anchor='center')
met_sch_fr.grid(row=0, column=0, ipady=60)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11, 'bold'))  # Modify the font of the body
style.configure("Treeview.Heading", font=('Calibri', 11, 'bold'))  # Modify the font of the headings

style.configure("Treeview.Heading",
                background="black",
                foreground="cyan",
                rowheight=25,
                fieldbackground="black"
                )

style.configure("Treeview",
                background="black",
                foreground="cyan",
                rowheight=25,
                fieldbackground="black"
                )

style.map('Treeview',
          background=[('selected', 'DeepSkyBlue4')], foreground=[('selected', 'cyan')])

tree = ttk.Treeview(met_sch_fr, style='Treeview')

df = pd.read_csv(filename)

data = df.to_numpy().tolist()

tree['columns'] = ('time', 'day', 'attendby', 'id', "pass", 'topic')

tree.column('#0', width=0, stretch='no')
tree.column('time', anchor='center', width=40)
tree.column('day', anchor='center', width=40)
tree.column('attendby', anchor='center', width=75)
tree.column('id', anchor='center', width=110)
tree.column('pass', anchor='center', width=70)
tree.column('topic', anchor='w', width=130)

tree.heading('#0', anchor='w', text='')
tree.heading('time', anchor='center', text='Time')
tree.heading('day', anchor='center', text='Day')
tree.heading('attendby', anchor='center', text='Attend By')
tree.heading('id', anchor='center', text='ID')
tree.heading('pass', anchor='center', text='Pass')
tree.heading('topic', anchor='center', text='Topic')

id_no_var_c = 0
for rec in data:
    tree.insert(parent='', index='end', iid=id_no_var_c, text='',
                values=(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5]))
    id_no_var_c += 1

tree.grid(row=1, column=0, columnspan=3, padx=17)

entry1 = tk.Entry(met_sch_fr, font=font_type, width=5, bg=wid_color_bg, fg=wid_color_fg)
entry1.grid(row=4, column=0, ipadx=60, ipady=10, sticky='w')

entry2 = tk.Entry(met_sch_fr, font=font_type, width=5, bg=wid_color_bg, fg=wid_color_fg)
entry2.grid(row=4, column=1, ipadx=60, ipady=10, sticky='w')

entry3 = tk.Entry(met_sch_fr, font=font_type, width=5, bg=wid_color_bg, fg=wid_color_fg)
entry3.grid(row=4, column=2, ipadx=60, ipady=10, sticky='w')

entry4 = tk.Entry(met_sch_fr, font=font_type, width=5, bg=wid_color_bg, fg=wid_color_fg)
entry4.grid(row=6, column=0, ipadx=60, ipady=10, sticky='w')

entry5 = tk.Entry(met_sch_fr, font=font_type, width=5, bg=wid_color_bg, fg=wid_color_fg)
entry5.grid(row=6, column=1, ipadx=60, ipady=10, sticky='w')

entry6 = tk.Entry(met_sch_fr, font=font_type, width=5, bg=wid_color_bg, fg=wid_color_fg)
entry6.grid(row=6, column=2, ipadx=60, ipady=10, sticky='w')

lab1 = tk.Label(met_sch_fr, anchor='w', font=font_type, text='Topic  :', width=5, bg=wid_color_bg, fg=wid_color_fg)
lab1.grid(row=3, column=0, ipadx=60, ipady=10, sticky='w')

lab2 = tk.Label(met_sch_fr, anchor='w', font=font_type, text='ID  :', width=5, bg=wid_color_bg, fg=wid_color_fg)
lab2.grid(row=3, column=1, ipadx=60, ipady=10, sticky='w')

lab3 = tk.Label(met_sch_fr, anchor='w', font=font_type, text='Pass  :', width=5, bg=wid_color_bg, fg=wid_color_fg)
lab3.grid(row=3, column=2, ipadx=60, ipady=10, sticky='w')

lab4 = tk.Label(met_sch_fr, anchor='w', font=font_type, text='Time  :', width=5, bg=wid_color_bg, fg=wid_color_fg)
lab4.grid(row=5, column=0, ipadx=60, ipady=10, sticky='w')

lab5 = tk.Label(met_sch_fr, anchor='w', font=font_type, text='Day  :', width=5, bg=wid_color_bg, fg=wid_color_fg)
lab5.grid(row=5, column=1, ipadx=60, ipady=10, sticky='w')

lab6 = tk.Label(met_sch_fr, anchor='w', font=font_type, text='Attend By  :', width=5, bg=wid_color_bg, fg=wid_color_fg)
lab6.grid(row=5, column=2, ipadx=60, ipady=10, sticky='w')

main_label = tk.Label(met_sch_fr, anchor='center', font=('Helvetica', 13, 'bold'), text='Meeting Schedule', width=25,
                      bg=wid_color_bg, fg=wid_color_fg)
main_label.grid(row=0, column=0, ipadx=60, ipady=10, sticky='w', padx=60, columnspan=3)

del_row_btn = tk.Button(met_sch_fr, anchor='center', font=font_type, text='Delete Row', width=5, bg=wid_color_bg,
                        fg=wid_color_fg, command=delete_row)
del_row_btn.grid(row=7, column=0, ipadx=30, ipady=6, sticky='w', pady=40, padx=30)

del_all_btn = tk.Button(met_sch_fr, anchor='center', font=font_type, text='Delete All', width=5, bg=wid_color_bg,
                        fg=wid_color_fg, command=delete_all)
del_all_btn.grid(row=7, column=1, ipadx=30, ipady=6, sticky='w', pady=40, padx=30)

up_row_btn = tk.Button(met_sch_fr, anchor='center', font=font_type, text='Update Row', width=5, bg=wid_color_bg,
                       fg=wid_color_fg, command=update_record)
up_row_btn.grid(row=7, column=2, ipadx=30, ipady=6, sticky='w', pady=40, padx=30)

savechange_btn = tk.Button(met_sch_fr, anchor='center', font=font_type, text='Save Changes', width=5, bg=wid_color_bg,
                           fg=wid_color_fg, command=save_changes)
savechange_btn.grid(row=8, column=2, ipadx=30, ipady=6, sticky='w', padx=30)

back_btn_meetsch = tk.Button(met_sch_fr, image=backicon, width=18, height=18, border=0, command=lambda: show_frame(fr5))
back_btn_meetsch.place(relx=0.01, rely=0.01)

tree.bind("<ButtonRelease-1>", clicker)

# ----------------------------------- Meeting Schedule [ met_sch_fr ] END ------------------------------------------

####################################################################################################################


####################################################################################################################

# -------------------------------------- CHATBOT [ chatbot_fr ] START ----------------------------------------------

bot_img1 = ImageTk.PhotoImage(Image.open("Images/m_13.jpg"))
chatbot_fr = tk.Label(fr5, width=500, height=700, image=bot_img1, anchor='center')
chatbot_fr.grid(row=0, column=0, ipady=60)

frtext = tk.Frame(chatbot_fr, bg='black', width=500, height=470)
frtext.grid(row=0, column=0, pady=50, sticky='ne', rowspan=2)

bot_img2 = ImageTk.PhotoImage(Image.open("Images/w13.jpg"))
frtext_cover = tk.Label(chatbot_fr, image=bot_img2, width=490, height=470)

frtext_cover.grid(row=0, column=0, pady=50, sticky='w', rowspan=2)

frtext = tk.Label(chatbot_fr, image=img1, width=490, height=475)
frtext.place(relx=0.0, rely=0.068)

frtext_lb_chat = tk.Label(frtext, text="Chat Screen", fg='cyan', bg="black", font=("Helvetica", 14, "bold"), width=20)
frtext_lb_chat.place(relx=0.23, rely=0.038)

user_msg_fr = tk.Frame(chatbot_fr, bg='black')
user_msg_fr.grid(row=0, sticky='e')

bot_msg_fr = tk.Frame(chatbot_fr, bg='black')
bot_msg_fr.grid(row=0, sticky='w', rowspan=10)

menu_tittlelb = tk.Label(chatbot_fr, text='', bg='black', width=70, height=2)
menu_tittlelb.place(relx=0.0, rely=0.0)
new_meet_bot_head = tk.Button(menu_tittlelb, width=15, text='Profile', font=font_type_head_bot, bg='black', fg=wid_fg,
                              command=lambda: show_frame(fr6))
new_meet_bot_head.place(relx=0.06, rely=0.03)

new_meet_bot_head1 = tk.Button(menu_tittlelb, width=17, text='ADD Meeting', font=font_type_head_bot, bg='black',
                               fg=wid_fg, command=lambda: show_frame(fr2))
new_meet_bot_head1.place(relx=0.341, rely=0.03)

new_meet_bot_head2 = tk.Button(menu_tittlelb, width=20, text='Meeting Schedule', font=font_type_head_bot, bg='black',
                               fg=wid_fg, command=lambda: show_frame(fr3))
new_meet_bot_head2.place(relx=0.65, rely=0.03)

user_msg_entry = tk.Entry(chatbot_fr, font=font_type_bot, width=40, bg='cyan')
user_msg_entry.place(relx=0.06, rely=0.78, relheight=0.05)
user_msg_entry.insert(0, ' Enter your message here:')
user_msg_entry.bind("<FocusIn>", del_entry_box)

send_user_entry_bt = tk.Button(chatbot_fr, font=font_type_bot, text='Send', bg='cyan', command=lambda: response())
send_user_entry_bt.place(relx=0.8, rely=0.781)

borderlb = tk.Label(frtext, text="", bg='cyan', width=80)
borderlb.place(relx=0.0, rely=0.01, relheight=0.01)

borderlb1 = tk.Label(frtext, text="", bg='cyan', width=80)
borderlb1.place(relx=0.0, rely=0.8, relheight=0.01)

set_logolb = tk.Label(chatbot_fr, image=settingicon, bg='black')
set_logolb.place(relx=0.001, rely=0.005)

# --------------------------------------- CHATBOT [ chatbot_fr ] END -----------------------------------------------

####################################################################################################################


####################################################################################################################

# ----------------------------------- PROFILE [ profile_fr ] START -------------------------------------------------

# Holding Frame


profile_fr = tk.Label(fr6, width=500, height=700, image=bot_img1, anchor='center')
profile_fr.grid(row=0, column=0, ipady=60, ipadx=6)
# Frame logo
prof_title1 = tk.Label(profile_fr, text='User Profile', width=20, height=2, font=("Helvetica", 14, "bold"),
                       bg=wid_color_bg, fg=wid_color_fg)
prof_title1.place(relx=0.2, rely=0.00)

df_profile = pd.read_csv('user_data.csv')

font_pf = ("Helvetica", 10, "bold")

line_lb1 = tk.Label(profile_fr, text='', width=80, bg=wid_color_fg)
line_lb1.place(relx=0.0, rely=0.05, relheight=0.005)




head_pf_lbwrt1 = tk.Label(profile_fr, text='First Name:', width=26, font=font_pf, bg=wid_bg, fg=wid_fg, anchor='w')
head_pf_lbwrt1.place(relx=0.043, rely=0.09, relheight=0.04)
head_pf_lbwrt2 = tk.Label(profile_fr, text='Last Name:', width=26, font=font_pf, bg=wid_bg, fg=wid_fg, anchor='w')
head_pf_lbwrt2.place(relx=0.507, rely=0.09, relheight=0.04)

f_name_pf = tk.Entry(profile_fr, font=font_pf, width=30, bg=wid_bg, fg=wid_color_fg)

f_name_pf.place(relx=0.043, rely=0.13, relheight=0.05)

l_name_pf = tk.Entry(profile_fr, font=font_pf, width=30, bg=wid_bg, fg=wid_color_fg)

l_name_pf.place(relx=0.507, rely=0.13, relheight=0.05)



head_pf_lbwrt3 = tk.Label(profile_fr, text='User Name :', width=26, font=font_pf, bg=wid_bg, fg=wid_fg, anchor='w')
head_pf_lbwrt3.place(relx=0.043, rely=0.2, relheight=0.04)
head_pf_lbwrt4 = tk.Label(profile_fr, text='Password :', width=26, font=font_pf, bg=wid_bg, fg=wid_fg, anchor='w')
head_pf_lbwrt4.place(relx=0.507, rely=0.2, relheight=0.04)

user_name_pf = tk.Entry(profile_fr, font=font_pf, width=30, bg=wid_bg, fg=wid_color_fg)

user_name_pf.place(relx=0.043, rely=0.24, relheight=0.05)

pass_pf = tk.Entry(profile_fr, font=font_pf, width=30, bg=wid_bg, fg=wid_color_fg)

pass_pf.place(relx=0.507, rely=0.24, relheight=0.05)




head_pf_lbwrt5 = tk.Label(profile_fr, text='User Email :', width=26, font=font_pf, bg=wid_bg, fg=wid_fg, anchor='w')
head_pf_lbwrt5.place(relx=0.043, rely=0.315, relheight=0.04)
head_pf_lbwrt6 = tk.Label(profile_fr, text='Bot Email:', width=26, font=font_pf, bg=wid_bg, fg=wid_fg, anchor='w')
head_pf_lbwrt6.place(relx=0.507, rely=0.315, relheight=0.04)

user_email_pf = tk.Entry(profile_fr, font=font_pf, width=30, bg=wid_bg, fg=wid_color_fg)

user_email_pf.place(relx=0.043, rely=0.355, relheight=0.05)

bot_email_pf = tk.Entry(profile_fr, font=font_pf, width=30, bg=wid_bg, fg=wid_color_fg)

bot_email_pf.place(relx=0.507, rely=0.355, relheight=0.05)

logout_bt_pf = tk.Button(profile_fr, font=("Helvetica", 10, "bold"), text='Sign Out', width=11, height=2, bg=wid_bg,
                         fg=wid_fg, command=lambda: signout_profile())
logout_bt_pf.place(relx=0.043, rely=0.43, relheight=0.045)

save_bt_pf = tk.Button(profile_fr, font=("Helvetica", 10, "bold"), text='Save Changes', width=11, height=2, bg=wid_bg,
                       fg=wid_fg, command=lambda: save_changes_pf())
save_bt_pf.place(relx=0.73, rely=0.43, relheight=0.045)

line_lb2 = tk.Label(profile_fr, text='', width=80, bg=wid_color_fg)
line_lb2.place(relx=0.0, rely=0.5, relheight=0.005)

prof_title1 = tk.Label(profile_fr, text='Zoomdroid Status', width=20, height=2, font=("Helvetica", 14, "bold"),
                       bg=wid_color_bg, fg=wid_color_fg)
prof_title1.place(relx=0.2, rely=0.51)

font_status = ("Helvetica", 12, "bold")

status_lb_pf1 = tk.Label(profile_fr, text="Idle", font=font_status, width=10, bg=wid_bg, fg=wid_fg)
status_lb_pf1.place(relx=0.03, rely=0.7)

status_lb_pf2 = tk.Label(profile_fr, text="In Meet", font=font_status, width=10, bg=wid_bg, fg=wid_fg)
status_lb_pf2.place(relx=0.26, rely=0.7)

status_lb_pf3 = tk.Label(profile_fr, text="Saving Rec", font=font_status, width=10, bg=wid_bg, fg=wid_fg)
status_lb_pf3.place(relx=0.49, rely=0.7)

status_lb_pf4 = tk.Label(profile_fr, text="Uploading Rec", font=font_status, width=11, bg=wid_bg, fg=wid_fg)
status_lb_pf4.place(relx=0.72, rely=0.7)

back_btn_signup = tk.Button(profile_fr, image=backicon, width=18, height=18, border=0, command=lambda: show_frame(fr5))
back_btn_signup.place(relx=0.01, rely=0.01)

# threading.Thread(target=lambda: status_update()).start()
status_update()
# ----------------------------------- PROFILE [ profile_fr ] END ---------------------------------------------------

####################################################################################################################




####################################################################################################################

# ----------------------------------- LOADING [ app_bg_fr ] START ---------------------------------------------------


bg_load = ImageTk.PhotoImage(Image.open('Images/f8_bg.jpg'))
load_icon_img = ImageTk.PhotoImage(Image.open("Images/load_icon2.jpg"))

app_bg_fr = tk.Label(fr7, width=492, height=650, image = bg_load, anchor='center')
app_bg_fr.grid(row=0, column=0,padx =2 )


app_tittle = tk.Label(fr7, text = 'ZOOMDROID',width = 10,font = ("Helvetica", 22, "bold"), height = 2, bg = 'black', fg = 'cyan2')
app_tittle.place(relx = 0.3 , rely = 0.1, relheight = 0.08)
app_loading = tk.Label(fr7, text = 'Loading.....',width = 10,font = ("Helvetica", 18, "bold"), height = 2, bg = 'black', fg = 'cyan2')
app_loading.place(relx = 0.4 , rely = 0.6, relheight = 0.065)
load_icon_view =tk.Label(fr7, image = load_icon_img,width = 35, height = 2, bg ='black')
load_icon_view.place(relx = 0.33 , rely = 0.6, relheight = 0.07)
dev_name = tk.Label(fr7, text = 'Developed      By',width = 20,font = ("Helvetica", 13, "bold"), height = 2, bg = 'black', fg = 'cyan2')
dev_name.place(relx = 0.3 , rely = 0.86, relheight = 0.05)
dev_name = tk.Label(fr7, text = '  Wasif   Uddin  ',width = 14,font = ("Helvetica", 13, "bold"), height = 2, bg = 'black', fg = 'cyan2')
dev_name.place(relx = 0.37 , rely = 0.9, relheight = 0.05)


threading.Thread(target = lambda :change_load_others()).start()


# ----------------------------------- LOADING [ app_bg_fr ] ENDT ---------------------------------------------------


####################################################################################################################

show_frame(fr7)
win.mainloop()