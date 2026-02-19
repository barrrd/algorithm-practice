while True:
    try:
        line = input()
        print(line)
    except EOFError:
        # 입력의 끝(EOF)에 도달하면 반복문 종료
        break