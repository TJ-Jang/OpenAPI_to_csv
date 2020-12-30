def create(url, extract_range)
    # BeautifulSoup을 활용하여 내용을 추출하고, DataFrame을 만듦
    import requests
    from bs4 import BeautifulSoup
    import requests
    import pandas as pandas
    import numpy as np
    import Columns_search_urllib  # Columns를 찾기 위해 만든 Python file

    Columns = Columns_search_urllib.columns(url, extract_range)

    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    del(res)
    
    # 빈 데이터프레임 생성
    data = pd.DataFrame()
    
    # BeautifulSoup을 활용하여 범위 내 자료 추출
    datar = soup.find_all(extract_range)

    # data 추출 및 dataframe 생성
    for col in Columns:
        c = []
        for item in datar:
            try:
                stri = item.find(col.lower()).get_text()
                stri = stri.replace('\t', '')
                stri = stri.replace('\n', '')
                stri = stri.replace('\r', '')
                c.append(stri)
            except:
                # 내용이 없을 경우 공란을 추가
                c.append('')
        data[col] = c
    return data
