#1. 화면보호기 사용 여부
#2. 화면보호기 대기시간
#3. 화면보호기 해제 시 암호 사용 여부

from tkinter import *
import tkinter as tk
from winreg import *

#루트화면 (root window) 생성
window = Tk()
#화면 크기 및 위치(너비x높이+x좌표+y좌표)
window.geometry('400x200+800+100') 

#타이틀 표시
window.title('MPI Screen Saver')

path = r"Control Panel\Desktop"
exe = r"SCRNSAVE.EXE"

def isUse_add():
    #레지스트리 연결 및 키 열기
    reg_handle = ConnectRegistry(None, HKEY_CURRENT_USER)
    key = OpenKey(reg_handle, path, 0, access=KEY_WRITE)

    #레지스트리 키 값 등록
    try:
        SetValueEx(key, exe, 0, REG_SZ, r"C:\Windows\system32\scrnsave.scr")
        print("created")

    except EnvironmentError:
        print("Encountered problems writing into the Registry")
    
    #키 닫기
    CloseKey(key)

def isUse_del():
    reg_handle = ConnectRegistry(None, HKEY_CURRENT_USER)
    key = OpenKey(reg_handle, path, 0, access=KEY_WRITE)
    
    #레지스트리 키 삭제
    try:
        DeleteValue(key, exe)
        print("deleted")

    except EnvironmentError:
        print("Encountered problems deleting into the Registry")

    CloseKey(key)

def timeout_alt():
    reg_handle = ConnectRegistry(None, HKEY_CURRENT_USER)
    key = OpenKey(reg_handle, path, 0, access=KEY_WRITE)

    try:
        SetValueEx(key, r"ScreenSaveTimeOut", 0, REG_SZ, entry.get())
        print("alternated")

    except EnvironmentError:
        print("Encountered problems changing into the Registry")

    CloseKey(key)

def isSecure_t():
    reg_handle = ConnectRegistry(None, HKEY_CURRENT_USER)
    key = OpenKey(reg_handle, path, 0, access=KEY_WRITE)

    try:
        SetValueEx(key, r"ScreenSaverIsSecure", 0, REG_SZ, "1")
        print("safe")

    except EnvironmentError:
        print("Encountered problems changing into the Registry")

    CloseKey(key)

def isSecure_f():
    reg_handle = ConnectRegistry(None, HKEY_CURRENT_USER)
    key = OpenKey(reg_handle, path, 0, access=KEY_WRITE)

    try:
        SetValueEx(key, r"ScreenSaverIsSecure", 0, REG_SZ, "0")
        print("unsafe")

    except EnvironmentError:
        print("Encountered problems changing into the Registry")

    CloseKey(key)

if __name__=="__main__":
    label1 = Label(window, text='1. 화면보호기 사용 여부') 
    label1.grid(row=0, column=0)

    btn1_1 = Button(window, text='사용', command=isUse_add, width=10)
    btn1_1.grid(row=0, column=1)
    
    btn1_2 = Button(window, text='미사용', command=isUse_del, width=10)
    btn1_2.grid(row=0, column=2)

    label2 = Label(window, text='2. 화면보호기 대기시간') 
    label2.grid(row=1, column=0)

    entry = tk.Entry(fg='gray19', bg='snow', width=20)
    entry.grid(row=1, column=1)

    btn2 = Button(window, text='변경', command=timeout_alt, width=10)
    btn2.grid(row=1, column=2)

    label3 = Label(window, text='3. 화면보호기 암호 여부') 
    label3.grid(row=2, column=0)

    btn3_1 = Button(window, text='사용', command=isSecure_t, width=10)
    btn3_1.grid(row=2, column=1)

    btn3_2 = Button(window, text='미사용', command=isSecure_f, width=10)
    btn3_2.grid(row=2, column=2)

#메인루프 실행
window.mainloop()