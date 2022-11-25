# 윈도우 레지스트리 관련 API 모듈(내장모듈)
from winreg import *



# 화면보호기 점검항목 조치 원리
# = 화면 보호기 미사용 중일 경우 -> 사용으로 변경
# = HKEY_CURRENT_USER\Control Panel\Desktop 하위에 SCRNSAVE.EXE 가 없을 경우 -> 추가
# = 종류 REG_SZ \ 값 C:\Windows\system32\scrnsave.scr



# 1. 레지스트리 키 생성

# 키를 생성할 경로
# r: Raw String으로, Escape에 영향없이 문자열을 그대로 표시함
test_key = r"Control Panel\Desktop\Test_key"

# 키 생성
CreateKey(HKEY_CURRENT_USER,test_key)



# 2. 레지스트리 연결 및 키 열기

# 화면보호기 경로
screensaver_path = r"Control Panel\Desktop"

# 읽어오기만 할 경우엔 access=KEY_READ 사용
reg_handle = ConnectRegistry(None,HKEY_CURRENT_USER)

 # 읽어오기만 할 경우엔 access=KEY_READ 사용
 # 0은 reserved인데 딱히 건들 일 없을 듯..
key = OpenKey(reg_handle,screensaver_path,0,access=KEY_WRITE)



# 3. 레지스트리 키 값 등록

try:
    #SetValue는 Str 값만 넣을 수 있기 때문에 SetValueEx 사용
    SetValueEx(key,r"SCRNSAVE.EXE",0,REG_SZ,r"C:\Windows\system32\scrnsave.scr")
    print("생성했음")

except EnvironmentError:
    print("Encountered problems writing into the Registry")



# 4. 레지스트리 닫기

# 오픈했던 키 닫기
CloseKey(key)
