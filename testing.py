import tkinter as tk
from tkinter import filedialog
import subprocess
import os


#Set up the main application window
root = tk.Tk()
root.title("統合generatorGUI 詳細設定画面")

#row0
title1_box = tk.Label(root,text="テストファイル関連", height=1, width=82, font=("Helvetica",14), bg="#86B6F6", anchor="w", relief=tk.SOLID, bd=1)
title1_box.place(x=5, y=50)

#row1
text_box_1_0 = tk.Label(root,text="検査種別の選択", height=1, width=29, font=("Helvetica",12), bg="#B0DAFF", anchor="center", relief=tk.SOLID, bd=1)
text_box_1_0.place(x=5, y=77)

text_box_1_1 = tk.Label(root,text="テストパターンファイル名設定", height=1, width=36, font=("Helvetica",12), bg="#C4E1F6", anchor="center", relief=tk.SOLID, bd=1)
text_box_1_1.place(x=272, y=77)

text_box_1_2 = tk.Label(root,text="テストスクリプトファイル名設定", height=1, width=34, font=("Helvetica",12), bg="#C4E1F6", anchor="center", relief=tk.SOLID, bd=1)
text_box_1_2.place(x=602, y=77)

#row2
text_box_2_0 = tk.Label(root,text="DID自動検査", height=2, width=29, font=("Helvetica",12), bg="#B0DAFF", anchor="center", relief=tk.SOLID, bd=1)
text_box_2_0.place(x=5, y=100)

def open_file(event):
    filename = filedialog.askopenfilename()
    if filename:
        filename = os.path.basename(filename)

        label_2_1.config(text=filename)

label_2_1 = tk.Label(root, height=2, width=36, font=("Helvetica",12), bg="#FFFFFF", cursor="hand2", relief=tk.SOLID, bd=1, wraplength=330, justify="left")
label_2_1.place(x=272, y=100)

label_2_1.bind("<Button-1>", open_file)

#create editable textbox 
textbox_2_2 = tk.Text(root, height=2, width=34, font=("Helvetica",12), relief=tk.SOLID, bd=1)
textbox_2_2.place(x=602, y=100)


#row3
text_box_3_0 = tk.Label(root,text="ダイアグ通信自動検査", height=2, width=29, font=("Helvetica",12), bg="#B0DAFF", anchor="center", relief=tk.SOLID, bd=1)
text_box_3_0.place(x=5, y=141)

def open_file(event):
    filename = filedialog.askopenfilename()
    if filename:
        filename = os.path.basename(filename)

        label_3_1.config(text=filename)

label_3_1 = tk.Label(root, height=2, width=36, font=("Helvetica",12), bg="#FFFFFF", cursor="hand2", relief=tk.SOLID, bd=1, wraplength=330, justify="left")
label_3_1.place(x=272, y=141)

label_3_1.bind("<Button-1>", open_file)

#create editable textbox 
textbox_3_2 = tk.Text(root, height=2, width=34, font=("Helvetica",12), relief=tk.SOLID, bd=1)
textbox_3_2.place(x=602, y=141)

#row4
text_box_4_0 = tk.Label(root,text="故障検知自動検査", height=2, width=29, font=("Helvetica",12), bg="#B0DAFF", anchor="center", relief=tk.SOLID, bd=1)
text_box_4_0.place(x=5, y=182)

def open_file(event):
    filename = filedialog.askopenfilename()
    if filename:
        filename = os.path.basename(filename)

        label_4_1.config(text=filename)

label_4_1 = tk.Label(root, height=2, width=36, font=("Helvetica",12), bg="#FFFFFF", cursor="hand2", relief=tk.SOLID, bd=1, wraplength=330, justify="left")
label_4_1.place(x=272, y=182)

label_4_1.bind("<Button-1>", open_file)

#create editable textbox 
textbox_4_2 = tk.Text(root, height=2, width=34, font=("Helvetica",12), relief=tk.SOLID, bd=1)
textbox_4_2.place(x=602, y=182)



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#create second Table

#row0
title1_box = tk.Label(root,text="generator関連", height=1, width=114, font=("Helvetica",14), bg="#ACD793", anchor="w", relief=tk.SOLID, bd=1)
title1_box.place(x=5, y=255)

#row1
text_box_1_0 = tk.Label(root,text="検査種別の選択", height=2, width=19, font=("Helvetica",11), bg="#C8E4B2", anchor="center", relief=tk.SOLID, bd=1)
text_box_1_0.place(x=5, y=282)

text_box_1_1 = tk.Label(root,text="generatorファイル名設定", height=2, width=24, font=("Helvetica",11), bg="#D7E5CA", anchor="center", relief=tk.SOLID, bd=1)
text_box_1_1.place(x=171, y=282)

text_box_1_2 = tk.Label(root,text="テストパターン\n生成設設定", height=2, width=22, font=("Helvetica",11), bg="#D7E5CA", anchor="center", relief=tk.SOLID, bd=1)
text_box_1_2.place(x=383, y=282)

text_box_1_3 = tk.Label(root,text="テストパターン生成\nシート設定", height=2, width=19, font=("Helvetica",11), bg="#D7E5CA", anchor="center", relief=tk.SOLID, bd=1)
text_box_1_3.place(x=580, y=282)

text_box_1_4 = tk.Label(root,text="テストパターン生成結果\nセル(Range)設定", height=2, width=23, font=("Helvetica",11), bg="#D7E5CA", anchor="center", relief=tk.SOLID, bd=1)
text_box_1_4.place(x=753, y=282)

text_box_1_5 = tk.Label(root,text="スクリプト生成\nシート設定", height=2, width=16, font=("Helvetica",11), bg="#D7E5CA", anchor="center", relief=tk.SOLID, bd=1)
text_box_1_5.place(x=957, y=282)

text_box_1_6 = tk.Label(root,text="スクリプト生成結果\nセル(Range)設定", height=2, width=18, font=("Helvetica",11), bg="#D7E5CA", anchor="center", relief=tk.SOLID, bd=1)
text_box_1_6.place(x=1098, y=282)

#row2
text_box_2_0 = tk.Label(root,text="DID自動検査", height=2, width=18, font=("Helvetica",11), bg="#C8E4B2", anchor="center", relief=tk.SOLID, bd=1)
text_box_2_0.place(x=5, y=321)

def open_file_tb2(event):
    filename_tb_2 = filedialog.askopenfilename()
    if filename_tb_2:
        filename_tb_2 = os.path.basename(filename_tb_2)

        text_box_2_1.config(text=filename_tb_2)

text_box_2_1 = tk.Label(root, height=2, width=23, font=("Helvetica",11), background="#FFFFFF", cursor="hand2", relief=tk.SOLID, bd=1, wraplength=210, justify="left")
text_box_2_1.place(x=172, y=321)

text_box_2_1.bind("<Button-1>", open_file_tb2)

#create editable textbox 
textbox_2_2 = tk.Text(root, height=2, width=24, font=("Helvetica",11), relief=tk.SOLID, bd=1)
textbox_2_2.place(x=384, y=321)

textbox_2_3 = tk.Text(root, height=2, width=21, font=("Helvetica",11), relief=tk.SOLID, bd=1)
textbox_2_3.place(x=581, y=321)

textbox_2_4 = tk.Text(root, height=2, width=25, font=("Helvetica",11), relief=tk.SOLID, bd=1)
textbox_2_4.place(x=754, y=321)

textbox_2_5 = tk.Text(root, height=2, width=17, font=("Helvetica",11), relief=tk.SOLID, bd=1)
textbox_2_5.place(x=959, y=321)

textbox_2_6 = tk.Text(root, height=2, width=20, font=("Helvetica",11), relief=tk.SOLID, bd=1)
textbox_2_6.place(x=1100, y=321)


#row3
text_box_3_0 = tk.Label(root,text="ダイアグ通信自動検査", height=2, width=18, font=("Helvetica",11), bg="#C8E4B2", anchor="w", relief=tk.SOLID, bd=1)
text_box_3_0.place(x=5, y=360)

def open_file_tb2(event):
    filename_tb_3 = filedialog.askopenfilename()
    if filename_tb_3:
        filename_tb_3 = os.path.basename(filename_tb_3)

        text_box_3_1.config(text=filename_tb_3)

text_box_3_1 = tk.Label(root, height=2, width=23, font=("Helvetica",11), background="#FFFFFF", cursor="hand2", relief=tk.SOLID, bd=1, wraplength=210, justify="left")
text_box_3_1.place(x=172, y=360)

text_box_3_1.bind("<Button-1>", open_file_tb2)

#create editable textbox 
textbox_3_2 = tk.Text(root, height=2, width=24, font=("Helvetica",11), relief=tk.SOLID, bd=1)
textbox_3_2.place(x=384, y=360)

textbox_3_3 = tk.Text(root, height=2, width=21, font=("Helvetica",11), relief=tk.SOLID, bd=1)
textbox_3_3.place(x=581, y=360)

textbox_3_4 = tk.Text(root, height=2, width=25, font=("Helvetica",11), relief=tk.SOLID, bd=1)
textbox_3_4.place(x=754, y=360)

textbox_3_5 = tk.Text(root, height=2, width=17, font=("Helvetica",11), relief=tk.SOLID, bd=1)
textbox_3_5.place(x=959, y=360)

textbox_3_6 = tk.Text(root, height=2, width=20, font=("Helvetica",11), relief=tk.SOLID, bd=1)
textbox_3_6.place(x=1100, y=360)


#row4
text_box_4_0 = tk.Label(root,text="故障検知自動検査", height=2, width=18, font=("Helvetica",11), bg="#C8E4B2", anchor="center", relief=tk.SOLID, bd=1)
text_box_4_0.place(x=5, y=399)

def open_file_tb2(event):
    filename_tb_4 = filedialog.askopenfilename()
    if filename_tb_4:
        filename_tb_4 = os.path.basename(filename_tb_4)

        text_box_4_1.config(text=filename_tb_4)

text_box_4_1 = tk.Label(root, height=2, width=23, font=("Helvetica",11), background="#FFFFFF", cursor="hand2", relief=tk.SOLID, bd=1, wraplength=210, justify="left")
text_box_4_1.place(x=172, y=399)

text_box_4_1.bind("<Button-1>", open_file_tb2)

#create editable textbox 
textbox_4_2 = tk.Text(root, height=2, width=24, font=("Helvetica",11), relief=tk.SOLID, bd=1)
textbox_4_2.place(x=384, y=399)

textbox_4_3 = tk.Text(root, height=2, width=21, font=("Helvetica",11), relief=tk.SOLID, bd=1)
textbox_4_3.place(x=581, y=399)

textbox_4_4 = tk.Text(root, height=2, width=25, font=("Helvetica",11), relief=tk.SOLID, bd=1)
textbox_4_4.place(x=754, y=399)

textbox_4_5 = tk.Text(root, height=2, width=17, font=("Helvetica",11), relief=tk.SOLID, bd=1)
textbox_4_5.place(x=959, y=399)

textbox_4_6 = tk.Text(root, height=2, width=20, font=("Helvetica",11), relief=tk.SOLID, bd=1)
textbox_4_6.place(x=1100, y=399)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#create bottom button

def on_close():
    root.destroy()

restore_previous_btn = tk.Button(root, text="前回値復元", width=10, font=("Helvetica",11), background="#FEEE91", cursor="hand2", relief=tk.RAISED)
restore_previous_btn.place(x=900, y=457)

update_btn = tk.Button(root, text="更新", width=10, font=("Helvetica",11), background="#D7E5CA", cursor="hand2", relief=tk.RAISED)
update_btn.place(x=1027, y=457)

update_btn = tk.Button(root, text="戻る", width=10, font=("Helvetica",11), background="#B4B4B8", cursor="hand2", relief=tk.RAISED, command=on_close)
update_btn.place(x=1150, y=457)



#create title
main_label = tk.Label(root, text="統合generatorGUI 詳細設定", font=("Arial", 20), fg="black", anchor=tk.W, width=50)
main_label.place(x=20, y=5)

def return_setting():
    subprocess.run(['python', 'main.py'])

setting_btn = tk.Button(root, text="設定", width=10, font=("Helvetica",11), background="#86B6F6", cursor="hand2", relief=tk.RAISED, command=return_setting)
setting_btn.place(x=668, y=11)

root.geometry('1270x500')
root.mainloop()