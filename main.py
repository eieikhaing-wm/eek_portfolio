import tkinter as tk
from tkinter import filedialog
import os
from tkinter import font
import subprocess
import openpyxl
from openpyxl import load_workbook

# Set up the main application window
root = tk.Tk()
root.title("統合generatorGUI　生成画面")

#Row0
title_box = tk.Label(root,text="検査種別の選択", height=2, width=31, font=("Helvetica",13), bg="#ACD793", anchor="center", relief=tk.SOLID, bd=1)
title_box.place(x=24, y=50)

title_box = tk.Label(root,text="パラメータ仕様書各設定", height=2, width=40, font=("Helvetica",13), bg="#ACD793", anchor="center", relief=tk.SOLID, bd=1)
title_box.place(x=308, y=50)

title_box = tk.Label(root,text="パターン／スクリプト\n生成成否", height=2, width=20, font=("Helvetica",13), bg="#ACD793", anchor="center", relief=tk.SOLID, bd=1)
title_box.place(x=673, y=50)

title_box = tk.Label(root,text="前回生成日時", height=2, width=14, font=("Helvetica",13), bg="#ACD793", anchor="center", relief=tk.SOLID, bd=1)
title_box.place(x=858, y=50)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Row1
text_box_1 = tk.Label(root,text="DID自動検査", height=1, width=28, font=("Helvetica",13), bg="#FFFFFF", anchor="w", relief=tk.SOLID, bd=1)
text_box_1.place(x=51, y=93)

#creat checkbutton
var_1 = tk.IntVar()
chk_btn_1 = tk.Checkbutton(root, text="", variable=var_1, bg="#FFFFFF", font=("Helvetica",8), relief=tk.RAISED)
chk_btn_1.place(x=23, y=92)


def open_file_dialog(event):
    file_name = filedialog.askopenfilename()
    if file_name:
        file_name = os.path.basename(file_name)
        
        label_1_1.config(text=file_name)

# ラベルを作成
label_1_1 = tk.Label(root,text=" ", height=1, width=40, font=("Helvetica",13), bg="#FFFFFF", cursor="hand2", anchor="w", relief=tk.SOLID, bd=1, wraplength=400)
label_1_1.place(x=308, y=93)

# ラベルにクリックイベントをバインド
label_1_1.bind("<Button-1>", open_file_dialog)

#--------------------------------------------------------------------------------------------------------------------------
label_1_3 = tk.Label(root,text="〇 ", height=1, width=10, font=("Helvetica",13), bg="#FFFFFF", anchor="center", relief=tk.SOLID, bd=1)
label_1_3.place(x=673, y=93)

label_1_4 = tk.Label(root,text="〇 ", height=1, width=10, font=("Helvetica",13), bg="#FFFFFF", anchor="center", relief=tk.SOLID, bd=1)
label_1_4.place(x=765, y=93)

label_1_5 = tk.Label(root,text="2024/01/01", height=1, width=14, font=("Helvetica",13), bg="#FFFFFF", anchor="center", relief=tk.SOLID, bd=1)
label_1_5.place(x=858, y=93)

#------------------------------------------------------------------------------------------------------------------------------------------
#Row2
text_box_2 = tk.Label(root,text="ダイアグ通信自動検査", height=1, width=28, font=("Helvetica",13), bg="#FFFFFF", anchor="w", relief=tk.SOLID, bd=1)
text_box_2.place(x=51, y=117)


#creat checkbutton
var_2 = tk.IntVar()
chk_btn_2 = tk.Checkbutton(root, text="", variable=var_2, bg="#FFFFFF", font=("Helvetica",8), relief=tk.RAISED)
chk_btn_2.place(x=23, y=116)



def open_file_dialog(event):
    file_name = filedialog.askopenfilename()
    if file_name:
        file_name = os.path.basename(file_name)
        label_2_1.config(text=file_name)

# ラベルを作成
label_2_1 = tk.Label(root,text=" ", height=1, width=40, font=("Helvetica",13), bg="#FFFFFF", cursor="hand2", anchor="w", relief=tk.SOLID, bd=1)
label_2_1.place(x=308, y=117)

# ラベルにクリックイベントをバインド
label_2_1.bind("<Button-1>", open_file_dialog)

label_2_3 = tk.Label(root,text="〇 ", height=1, width=10, font=("Helvetica",13), bg="#FFFFFF", anchor="center", relief=tk.SOLID, bd=1)
label_2_3.place(x=673, y=117)

label_2_4 = tk.Label(root,text="〇 ", height=1, width=10, font=("Helvetica",13), bg="#FFFFFF", anchor="center", relief=tk.SOLID, bd=1)
label_2_4.place(x=765, y=117)

label_2_5 = tk.Label(root,text="2024/01/01", height=1, width=14, font=("Helvetica",13), bg="#FFFFFF", anchor="center", relief=tk.SOLID, bd=1)
label_2_5.place(x=858, y=117)
#---------------------------------------------------------------------------------------------------------------------------------------
#Row3
text_box_3 = tk.Label(root,text="故障検知自動検査", height=1, width=28, font=("Helvetica",13), bg="#FFFFFF", anchor="w", relief=tk.SOLID, bd=1)
text_box_3.place(x=51, y=141)

#creat checkbutton
var_3 = tk.IntVar()
chk_btn_3 = tk.Checkbutton(root, text="", variable=var_3, bg="#FFFFFF", font=("Helvetica",8), relief=tk.RAISED)
chk_btn_3.place(x=23, y=140)


def open_file_dialog(event):
    file_name = filedialog.askopenfilename()
    if file_name:
        file_name = os.path.basename(file_name)
        label_3_1.config(text=file_name)

# ラベルを作成
label_3_1 = tk.Label(root,text=" ", height=1, width=40, font=("Helvetica",13), bg="#FFFFFF", cursor="hand2", anchor="w", relief=tk.SOLID, bd=1)
label_3_1.place(x=308, y=141)

# ラベルにクリックイベントをバインド
label_3_1.bind("<Button-1>", open_file_dialog)

label_3_2 = tk.Label(root,text="〇 ", height=1, width=10, font=("Helvetica",13), bg="#FFFFFF", anchor="center", relief=tk.SOLID, bd=1)
label_3_2.place(x=673, y=141)

label_3_3 = tk.Label(root,text="〇 ", height=1, width=10, font=("Helvetica",13), bg="#FFFFFF", anchor="center", relief=tk.SOLID, bd=1)
label_3_3.place(x=765, y=141)

label_3_4 = tk.Label(root,text="2024/01/01", height=1, width=14, font=("Helvetica",13), bg="#FFFFFF", anchor="center", relief=tk.SOLID, bd=1)
label_3_4.place(x=858, y=141)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Row4

#label
label_4 = tk.Label(root,text="パラメータ仕様書　格納フォルダ", height=1, width=31, font=("Helvetica",13), bg="#EEEEEE", anchor="w")
label_4.place(x=30, y=207)

normal_font = font.Font(family="Helvetica", size=16, weight="normal")

def select_folder():
    folder_path = filedialog.askdirectory()  # open filedialog
    if folder_path:  # if select folder
        entry.delete(0, tk.END)  # clear textbox
        entry.insert(0, folder_path)  # display textbox of selected folder name

# create select button
button = tk.Button(root, text="指定", width=9, font=("Helvetica",10), command=select_folder, background="#B7B7B7")
button.place(x=30, y=230)

# テキストボックスの作成
entry = tk.Entry(root, width=72, font=normal_font, bg="#FFFFFF", relief=tk.SOLID, bd=1)
entry.place(x=112, y=230)

#------------------------------------------------------------------------------------------------------------------
#Row5

#label
label_5 = tk.Label(root,text="テストパターン.テストスクリプトファイル　出力フォルダ", height=1, width=60, font=("Helvetica",13), bg="#EEEEEE", anchor="w")
label_5.place(x=30, y=278)

normal_font = font.Font(family="Helvetica", size=16, weight="normal")

def select_folder():
    folder_path = filedialog.askdirectory()  # open filedialog
    if folder_path:  # if select folder
        entry_1.delete(0, tk.END)  # clear textbox
        entry_1.insert(0, folder_path)  # display textbox of selected folder name

# create select button
button_1 = tk.Button(root, text="指定", width=9, font=("Helvetica",10), command=select_folder, background="#B7B7B7")
button_1.place(x=30, y=300)

# テキストボックスの作成
entry_1 = tk.Entry(root, width=72, font=normal_font, bg="#FFFFFF", relief=tk.SOLID, bd=1)
entry_1.place(x=112, y=300)

#---------------------------------------------------------------------------------------------------------------------------
#Row6

#label
label_6 = tk.Label(root,text="自動検査環境用iniファイル　出力フォルダ", height=1, width=60, font=("Helvetica",13), bg="#EEEEEE", anchor="w")
label_6.place(x=30, y=348)

normal_font = font.Font(family="Helvetica", size=16, weight="normal")

def select_folder():
    folder_path = filedialog.askdirectory()  # open filedialog
    if folder_path:  # if select folder
        entry_2.delete(0, tk.END)  # clear textbox
        entry_2.insert(0, folder_path)  # display textbox of selected folder name

# create select button
button_2 = tk.Button(root, text="指定", width=9, font=("Helvetica",10), command=select_folder, background="#B7B7B7")
button_2.place(x=30, y=370)

# テキストボックスの作成
entry_2 = tk.Entry(root, width=72, font=normal_font, bg="#FFFFFF", relief=tk.SOLID, bd=1)
entry_2.place(x=112, y=370)

#------------------------------------------------------------------------------------------------------------------------------------------------
#create generate button

def on_close():
    root.destroy()

button_3 = tk.Button(root, text="生成", width=10, font=("Helvetica",10), background="#C1E2A4", cursor="hand2", relief=tk.RAISED)
button_3.place(x=785, y=440)

#create close button
button_3 = tk.Button(root, text="閉じる", width=10, font=("Helvetica",10), background="#B4B4B8", cursor="hand2", relief=tk.RAISED, command=on_close)
button_3.place(x=880, y=440)


#---------------------------------------------------------------------------------------------------------------------------------------------
#create title
main_label = tk.Label(root, text="統合generatorGUI", font=("Arial", 20), fg="black", anchor=tk.W, width=50)
main_label.place(x=20, y=5)

def call_detail_setting():
    subprocess.run(['python', 'testing.py'])

detail_setting_btn = tk.Button(root, text="詳細設定", width=10, font=("Helvetica",10), background="#9AC5F4", cursor="hand2", relief=tk.RAISED, command=call_detail_setting)
detail_setting_btn.place(x=790, y=15)

root.geometry('1000x500')
# Run the application
root.mainloop()