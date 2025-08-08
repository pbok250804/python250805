import re

def is_valid_email(email):
    # 이메일이 맞는지 확인하는 규칙(정규표현식)입니다.
    # 아래는 아주 쉽게 설명한 내용입니다.
    # ^ : 맨 처음부터 시작해요
    # [a-zA-Z0-9._%+-]+ : 영어, 숫자, 점(.), 밑줄(_), 퍼센트(%), 더하기(+), 빼기(-)가 한 번 이상 나와요 (이게 이메일의 앞부분이에요)
    # @ : 꼭 @가 들어가야 해요 (이게 이메일의 가운데에 있어요)
    # [a-zA-Z0-9.-]+ : 영어, 숫자, 점(.), 빼기(-)가 한 번 이상 나와요 (이게 이메일의 뒷부분이에요)
    # \. : 점(.)이 꼭 한 번 나와야 해요 (이게 이메일의 마지막 부분 앞에 있어요)
    # [a-zA-Z]{2,} : 영어가 두 글자 이상 나와요 (이게 .com, .net 같은 부분이에요)
    # $ : 맨 끝이에요
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# 테스트할 이메일 주소 10개
emails = [
    "test@example.com",         # 올바른 이메일
    "user.name@domain.co.kr",   # 올바른 이메일
    "user_name@domain.com",     # 올바른 이메일
    "username@domain",          # .com 같은 끝부분이 없어서 틀림
    "username@.com",            # @ 뒤에 글자가 없어서 틀림
    "user@domain.c",            # 마지막 부분이 한 글자라서 틀림
    "user@domain.company",      # 올바른 이메일
    "user@domain..com",         # 점이 두 번 연속 나와서 틀림
    "user@domain.com.",         # 마지막에 점이 있어서 틀림
    "user@domain-com"           # .com 같은 점이 없어서 틀림
]

for email in emails:
    # 이메일이 맞으면 "유효함", 아니면 "유효하지 않음"이라고 출력해요
    result = "유효함" if is_valid_email(email) else "유효하지 않음"
    print(f"{email}: {result}")