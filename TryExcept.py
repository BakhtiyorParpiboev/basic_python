digit = input('enter your age:')
try:
    digit = int(digit)
except:
    print('please enter number!')
else:
    print(f" wow you are {2024-digit}. Thank you")



try:
    with open('myfile.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except IOError:
    print("파일을 읽는 중에 오류가 발생했습니다.")
else:
    print("파일 읽기 성공!")
finally:
    print("파일 처리 완료.")


try:
    f = open('nonfile.txt','r')
except FileNotFoundError:
    pass