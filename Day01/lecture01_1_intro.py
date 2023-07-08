# 0.개요 : 파이썬의 주요 특징


# 1.파이썬은 인간다운 언어 (아래 로직에 대해 아직 알 필요 없음.)
if 4 in [1, 2, 3, 4]: print("4가 있습니다.")


# 2.파이썬은 인터프리터 언어.
# 컴퓨터의 두뇌는 CPU인데, CPU가 이해할수 있는 언어는 0101 등으로 이루어진 기계어 뿐.
# 위와 같은 인간다운 언어는 CPU가 이해할 수 없으므로, CPU가 이해할수 있도록 해주는 번역(interpreting)작업이 필요.
# 한꺼번에 모든 소스를 번역해주는 언어를 컴파일언어, 한줄한줄 번역해주는 언어를 인터프리터 언어라고 한다.
# 파이썬은 한줄한줄. 그래서 실행시 다소 느림.
# 파이썬을 설치하면 파이썬의 인터프리터가 내장되어 설치된다. 즉, 파이썬을 설치한다는 의미는 인터프리터를 설치한다는것과 같은 의미.


# 3.파이썬은 실행이 되게 하려면 줄을 맞춰야 한다.(pythonic 하다) (아래 로직에 대해 아직 알 필요 없음.)
languages = ['python', 'perl', 'c', 'java']
for lang in languages:
    if lang in ['c', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")