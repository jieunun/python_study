# 윈도우 레지스트리 관련 API 모듈(내장모듈)
from winreg import *


# 1. 레지스트리 연결 및 키 열기
screensaver_path = r"Control Panel\Desktop"
reg_handle = ConnectRegistry(None,HKEY_CURRENT_USER)
key = OpenKey(reg_handle,screensaver_path,0,access=KEY_WRITE)



# 2. 레지스트리 키 삭제
value = r"SCRNSAVE.EXE"

try:
    # key = 열린 키 or 사전 정의된 HKEY_* 상수
    # value = 제거할 값을 식별하는 문자열
    DeleteValue(key, value)
    print("삭제했음")

except EnvironmentError:
    print("Encountered problems deleting into the Registry")



# 3. 레지스트리 닫기

# 오픈했던 키 닫기
CloseKey(key)