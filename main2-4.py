import socket #socket 모듈 호출
import requests #socket 모듈 호출
import re #re 모듈 호출

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #INET, STREAMing socket 생성
in_addr.connect(("www.google.co.kr", 443)) #연결(도메인(ip), server_addr 크기)
print("내부IP: ",in_addr.getsockname()[0]) #socket으로 외부 페이지 접근, ip 알아오기

req = requests.get("http://ipconfig.kr") #외부 ip 확인
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1] #해당하는 문자열 확인(re.match와 달리 모두 일치하지 않아도 됨)
print("외부IP: ",out_addr) #출력