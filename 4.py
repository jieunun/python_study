print(list(filter(lambda n : True if n>0 else False, [1,-2,3,-5,8,-3])))
#lambda n : True if n>0 else False는
#if: n>0 return True / else: return False와 같음
#filter(True/False, []) -> 요소 중 True인 값만 반환
#list -> 리스트로 변환