# JadenCase 문자열 만들기

# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 
# 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

def solution(s):
    answer = ''
    
    string_list = s.split()
    
    for string in string_list:         
        if (string[0].isalpha()):
            # if len(string)==1:
            #     answer += string[0].upper()
            # else:
            #     answer += (string[0].upper()+string[1:].lower())
            answer += (string[0].upper()+string[1:].lower())

        else:
            answer += (string[0]+string[1].lower())
            
            
            # if len(string) == 1:
            #     answer += string[0]
            # else:
            #     answer += (string[0]+string[1:].lower())   
        answer +=' '
    return answer[:-1]


