#1. 화면보호기 사용 여부
#2. 화면보호기 대기시간
#3. 화면보호기 해제 시 암호 사용 여부

from ast import In
from faulthandler import disable
from pydoc import visiblename
from sre_parse import State
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from turtle import left
from winreg import *

#루트화면 (root window) 생성
window = Tk()
#화면 크기 및 위치(너비x높이+x좌표+y좌표)
window.geometry('300x250+100+100') 

#타이틀 표시
window.title('화면보호기')

path = r"Control Panel\Desktop"
exe = r"SCRNSAVE.EXE"

global isSafe
isSafe = IntVar()

global entryValue
entry = IntVar()

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

def waitTime_alt():
    reg_handle = ConnectRegistry(None, HKEY_CURRENT_USER)
    key = OpenKey(reg_handle, path, 0, access=KEY_WRITE)

    try:
        if (safe_entry == 300):
           SetValueEx(key, r"ScreenSaveTimeOut", 0, REG_SZ, str(safe_entry))
        else:
            SetValueEx(key, r"ScreenSaveTimeOut", 0, REG_SZ, str(entry.get()))
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

def checkDisabled():
    if detail1.get() == 1:
        waitTime.configure(state=DISABLED)
        unsecured.configure(state=DISABLED)
    else:
        waitTime.configure(state=ACTIVE)
        unsecured.configure(state=ACTIVE)

def checkUnsafe():
    if isSafe.get() == 1:
        unused.configure(state=DISABLED)
        waitTime.configure(state=DISABLED)
        unsecured.configure(state=DISABLED)
    else:
        unused.configure(state=ACTIVE)
        waitTime.configure(state=ACTIVE)
        unsecured.configure(state=ACTIVE)

    global flag_isSafe
    flag_isSafe = isSafe.get()
    print ("checkUnfafe : flag is "+str(flag_isSafe))

def save():
    entryValue = entry.get()
    if flag_isSafe == 1:
        save_safe()
        print("save_safe")
    if flag_isSafe == 2:
        save_unsafe()
        print("save_unsafe")

def save_safe():
    isUse_add()
    global safe_entry
    safe_entry = 300
    print("save_safe : " + str(safe_entry))
    waitTime_alt()
    safe_entry = 0
    isSecure_t()

def save_unsafe():
    print(str(detail1.get())+" "+str(detail2.get())+ " "+str(detail3.get()))
    #1.체크
    if detail1.get() == 1:
        isUse_del()
    #1.언체크
    else:
        #2.체크
        if detail2.get() == 1:
            waitTime_alt()
            #3.체크
            if detail3.get() == 1:
                isSecure_f()
            #3.언체크
            else:
                isSecure_t()
        #2.언체크
        else:
            #3.체크
            if detail3.get() == 1:
                isSecure_f()
            #체크된 항목 없음
            else:
                tk.messagebox.showwarning("warning", "취약 세부사항은 1개 이상 선택되어야 합니다.")
    

if __name__=="__main__":
    frame_isSafe = tk.Frame(window, width=300, height=100)
    frame_detail = tk.LabelFrame(window, text="세부사항", width=300, height=100)
    frame_bnt = tk.Frame(window, width=300, height=100)

    global flag_isSafe
    flag_isSafe = IntVar()
    bnt_safe = tk.Radiobutton(frame_isSafe, text="안전", value=1, variable=isSafe, command=checkUnsafe)
    bnt_unsafe = tk.Radiobutton(frame_isSafe, text="취약", value=2, variable=isSafe, command=checkUnsafe)
    bnt_unsafe.select()

    global detail1, detail2, detail3
    detail1 = IntVar()
    detail2 = IntVar()
    detail3 = IntVar()

    unused = Checkbutton(frame_detail, text="화면보호기 미사용", variable=detail1, command=checkDisabled)
    waitTime = Checkbutton(frame_detail, text="대기시간", variable=detail2)
    entry = tk.Entry(frame_detail, fg='gray19', bg='snow', width=10)
    entry.insert(0,"0")
    ms = tk.Label(frame_detail, text='ms')
    unsecured = Checkbutton(frame_detail, text="암호 미사용", variable=detail3)

    print("main : isSafe is " + str(isSafe))
    bnt_save = tk.Button(frame_bnt, text="적용", width=10, command=save)
    
    frame_isSafe.grid(column=1, row=1, padx=30, pady=10, sticky="w")
    bnt_safe.pack()
    bnt_unsafe.pack()
    
    frame_detail.grid(column=1, row=2, padx=50, sticky="w")
    unused.grid(column=0, row=0, columnspan=3, sticky="w")
    waitTime.grid(column=0, row=1, sticky="w")
    entry.grid(column=1, row=1, sticky="w")
    ms.grid(column=2, row=1, sticky="w")
    unsecured.grid(column=0, row=2, columnspan=3, sticky="w")

    frame_bnt.grid(column=1, row=3, padx=30, sticky="s")

    bnt_save.pack(side="left", padx=10, pady=30)

#메인루프 실행
window.mainloop()