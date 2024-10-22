def main():
    # 입력을 받고 정수로 변환
    a, b = map(int, input("시, 분 입력하기 : ").split())

    # 입력 값의 범위 검사
    if not (0 <= a <= 23 and 0 <= b <= 59):
        print("잘못된 입력입니다.")
        return 0

    print("입력 시간은", a, "시", b, "분 입니다.")

    print("45분 일찍으로 변경하면")
    # 분이 45 이상인 경우
    if b >= 45:
        d = b - 45
        c = a
    else:
        # 분이 45보다 작은 경우
        d = 60 + b - 45
        c = a - 1
        if c < 0:
            c = 23

    print("알람이 울릴 시간은", c, "시", d, "분 입니다.")

    return 0
    
if __name__ == "__main__":
    main()