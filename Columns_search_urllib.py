# url : XML이 있는 OpenAPI주소
# extract_range : Columns추출을 위한 시작과 끝(보통 item)
def columns(url, extract_range):
    # urllib을 활용한 Columns searching

    import requests
    import re

    # Column은 보통 <...>형태를 띄고 있다.
    c = re.compile(r'[<](.+?)[>]')
    # 전체 Columns의 끝점을 찾기 위한 regex
    c2 = re.compile(r'([/].+)')
    # 내용이 없는 경우 XML에서 <.../>로 한번에 표현하기도 함
    c3 = re.compile(r'(.+[/])')

    # HTML 추출
    res = requests.get(url).text

    # Column후보 추출
    Col_candidate = c.findall(res)


    Columns = []
    # Column이 모여있는 범위 지정 및 추출
    for i in Col_candidate[Col_candidate.index(extract_range)+1:Col_candidate.index('/'+extract_range)]:
        # 특수한 경우가 있어 포함
        if '!' in i:
            continue
        elif c3.findall(i) != []:
            Columns.append(c3.findall(i)[0])
        elif c2.findall(i) == []:
            Columns.append(i)
        else:
            continue

    return Columns  # DataFrame을 만들기 위한 Columns 추출 완료