print(str(all([1, 2, abs(-3)-3])))
#abs: 절댓값을 구하는 함수 -> abs(-3) == 3
#all: 중간에 0이나 빈 문자열이 있으면 False, 아니면 True를 반환 -> all([1, 2, 0]) == False

print(chr(ord('a'))=='a')
#ord: 문자를 유니코드 정수로 변환 -> ord('a') == 97
#chr: 정수를 유니코드 문자로 변환 -> chr(97) == 'a'
#ord <-> chr
#결과는 참이므로 True