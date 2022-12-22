import customtkinter as ct 
import tkinter 
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import os
import shutil
from PIL import Image, ImageTk


def browse_folder():
    count = 0
    directory_path = askdirectory()
    #print(directory_path)
    file_list = os.listdir(directory_path)
    os.chdir(directory_path)
    no_of_files = len(file_list)
    if no_of_files == 0 :
        #print('Empty Folder')
        messagebox.showerror('Error','Empty Folder Please Select Another Folder')
    for file in file_list :
        for item in os.scandir():
            if item.is_dir():
                continue
        if file.endswith((".jpg",".jpeg",".png",'.ico','.psd','.gif','.ps','.ai')):
            dir_name = "IMAGES"
            new_path = os.path.join(directory_path,dir_name)
            file_list = os.listdir()
            if dir_name not in file_list:
                os.mkdir(new_path)
            shutil.move(file,new_path)
        if file.endswith(('.avi','.mp4','.mpeg','.3g','.mkv','.flv','.wmv','.rmvb')):
            dir_name = "VIDEOS"
            new_path = os.path.join(directory_path,dir_name)
            file_list = os.listdir()
            if dir_name not in file_list:
                os.mkdir(new_path)
            shutil.move(file,new_path)
        elif file.endswith('.pdf'):
            dir_name = "PDFFiles"
            new_path = os.path.join(directory_path,dir_name)
            file_list = os.listdir()
            #print(file_list)
            if dir_name not in file_list:
                os.mkdir(new_path)
            shutil.move(file,new_path)
        elif file.endswith((".m4a",".m4b",".mp3")):
            dir_name = 'AUDIO'
            new_path = os.path.join(directory_path,dir_name)
            file_list = os.listdir()
            if dir_name not in file_list :
                os.mkdir(new_path)
            shutil.move(file,new_path)
        elif file.endswith(('.xls','.xlsx','.xlsm')):
            dir_name = 'EXCELFILES'
            new_path = os.path.join(directory_path,dir_name)
            file_list = os.listdir()
            if dir_name not in file_list:
                os.mkdir(new_path)
            shutil.move(file,new_path)
        elif file.endswith(('.txt','.docx','.doc','.rtf')):
            dir_name = "WORDFILES"
            new_path = os.path.join(directory_path,dir_name)
            file_list = os.listdir()
            if dir_name not in file_list:
                os.mkdir(new_path)
            shutil.move(file,new_path)
        
        elif file.endswith(('.rar','.zip','.pkg','.7z')):
            dir_name = "Compressed FILES"
            new_path = os.path.join(directory_path,dir_name)
            file_list = os.listdir()
            if dir_name not in file_list:
                os.mkdir(new_path)
            shutil.move(file,new_path)
        elif file.endswith(('.apk','.exe')):
            dir_name = 'Executable Files'
            new_path = os.path.join(directory_path,dir_name)
            file_list = os.listdir()
            if dir_name not in file_list :
                os.mkdir(new_path)
            shutil.move(file,new_path)

                
        count = count+1
    messagebox.showinfo('Done','All Files Are Organized')




ct.set_appearance_mode("Dark") 
app = ct.CTk()
app.geometry("400x400")
app.resizable(False,False)
app.title("File Organizer")

app.iconbitmap('organize_icon.ico')
frame_1 = ct.CTkFrame(master=app,fg_color='black')
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


choose_destination_label = ct.CTkLabel(frame_1,text="Choose The Destination \n You Want To Organize",font=('calbri',10,'bold'),fg_color='white')
choose_destination_label.pack(pady=30,padx=20)

browse_image = ct.CTkImage(light_image=Image.open('images//browse.png'),
                                  size=(30, 30))

browse_btn = ct.CTkButton(frame_1,text="Browse",command=browse_folder,image=browse_image,width=200,height=20,
        border_width=2,
        corner_radius=20,
        bg_color="white",
        fg_color= "white",
        hover_color= "green"
)
browse_btn.pack(pady=30,padx=20)



app.mainloop()
