import re

def is_valid_email(email):
    # 이메일 주소가 맞는지 확인하는 아주 똑똑한 규칙(정규표현식)
    # 아래 규칙을 쉽게 설명하면:
    # 1. 이메일의 앞부분에는 영어, 숫자, 점(.), 밑줄(_), 퍼센트(%), 더하기(+), 빼기(-)가 올 수 있어요.
    # 2. 그 다음에는 꼭 @가 있어야 해요. (이메일의 가운데에 꼭 들어가요)
    # 3. @ 뒤에는 영어, 숫자, 점(.), 빼기(-)가 올 수 있어요. (이게 이메일 회사 이름이에요)
    # 4. 그 다음에는 꼭 점(.)이 있어야 해요. (이메일 회사 이름과 마지막 부분을 나눠줘요)
    # 5. 마지막에는 영어가 두 글자 이상 있어야 해요. (com, net, kr 같은 것)
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # 위 규칙에 맞으면 True, 아니면 False를 돌려줘요
    return re.match(pattern, email) is not None

# 이메일 주소가 맞는지 확인해볼 10개를 준비했어요
emails = [
    "test@example.com",         # 맞는 이메일
    "user.name@domain.co.kr",   # 맞는 이메일
    "invalid-email@",           # 틀린 이메일 (@ 뒤가 없음)
    "another.user@domain.com",  # 맞는 이메일
    "user@domain",              # 틀린 이메일 (마지막 점(.)과 글자가 없음)
    "user@domain.c",            # 틀린 이메일 (마지막 글자가 1개임)
    "user@domain.company",      # 맞는 이메일
    "user@domain..com",         # 틀린 이메일 (점이 두 번 연속 나옴)
    "user@.com",                # 틀린 이메일 (@ 뒤에 회사 이름이 없음)
    "user@domain.com"           # 맞는 이메일
]

# 이메일 주소마다 맞는지 확인해서 결과를 보여줘요
for email in emails:
    result = "유효함" if is_valid_email(email) else "유효하지 않음"
    print(f"{email}: {result}")