import random #random 모듈 호줄

random_number = random.randint(1, 100) #random_number : 1~100 사이 랜덤 정수

#print(random_number)

game_count = 1 #game_count : 1로 초기화

while True: 
    try: #함수 시작
        my_number = int(input("1~100 사이의 숫자를 입력하세요:")) #my_number : 정수형 input값
        
        if my_number > random_number: #만약 my_number가 random_number보다 크면
            print("다운")
        elif my_number < random_number: #만약 my_number가 random_number보다 작으면
            print("업")
        elif my_number == random_number: #만약 my_number와 random_number가 같으면
            print(f"축하합니다.{game_count}회 만에 맞췄습니다") #game_count 값을 출력하려면 ""앞에 f를 써야 함
            break #함수 종료
        
        game_count = game_count + 1 #flag 값
    except: #예외처리
        print("에러가 발생하였습니다. 숫자를 입력하세요")