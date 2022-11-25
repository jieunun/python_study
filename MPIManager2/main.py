import tkinter as tk
from winreg import *

#루트화면 (root window) 생성
scrsvr = tk() 

#타이틀 표시
scrsvr.title('MPI Screen Saver')

#텍스트 표시
label = tk.Label(scrsvr, text='화면보호기 점검 항목') 

#레이블 배치 실행
label.pack()

screensaver_path = r"Control Panel\Desktop"
scrnsave = r"SCRNSAVE.EXE"

def scrnsave_add():
    #레지스트리 연결 및 키 열기
    reg_handle = ConnectRegistry(None, HKEY_CURRENT_USER)
    key = OpenKey(reg_handle, screensaver_path, 0, access=KEY_WRITE)

    #레지스트리 키 값 등록
    try:
        SetValueEx(key, scrnsave, 0, REG_SZ, r"C:\Windows\system32\scrnsave.scr")
        print("created")

    except EnvironmentError:
        print("Encountered problems writing into the Registry")
    
    #키 닫기
    CloseKey(key)

def scrnsave_del():
    reg_handle = ConnectRegistry(None, HKEY_CURRENT_USER)
    key = OpenKey(reg_handle, screensaver_path, 0, access=KEY_WRITE)
    
    #레지스트리 키 삭제
    try:
        DeleteValue(key, scrnsave)
        print("deleted")

    except EnvironmentError:
        print("Encountered problems deleting into the Registry")

    CloseKey(key)

def ScreenSaveTimeOut_alt():
    reg_handle = ConnectRegistry(None, HKEY_CURRENT_USER)
    key = OpenKey(reg_handle, screensaver_path, 0, access=KEY_WRITE)

    try:
        SetValueEx(key, r"ScreenSaveTimeOut", 0, REG_SZ, ScreenSaveTimeOut.get())
        print("alternated")

    except EnvironmentError:
        print("Encountered problems changing into the Registry")

    CloseKey(key)

if __name__=="__main__":
    button_create = Button(scrsvr, text='레지스트리 추가', command=scrnsave_add)
    button_create.pack(padx=10, pady=10) #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 

    button_delete = Button(scrsvr, text='레지스트리 삭제', command=scrnsave_del)
    button_delete.pack(padx=10, pady=10)

    ScreenSaveTimeOut = tk.Entry(fg='gray19', bg='snow', width=20)
    ScreenSaveTimeOut.pack(padx=10, pady=10)

    button_alter = Button(scrsvr, text='대기 시간 변경', command=ScreenSaveTimeOut_alt)
    button_alter.pack(padx=10, pady=10)


#메인루프 실행
scrsvr.mainloop()