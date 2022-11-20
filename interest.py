import requests
import os
import pandas as pd
from bs4 import BeautifulSoup

def base_interest():
    """
    기준금리를 크롤링하는 함수입니다.
    """

    url = 'http://www.bok.or.kr/portal/singl/baseRate/list.do?dataSeCd=01&menuNo=200643'

    response = requests.get(url)
    response.status_code

    soup = BeautifulSoup(response.text, 'html.parser')

    # results = soup.select('.fixed tbody td')

    fixed_table = soup.select_one('.fixed')
    tr_tags = fixed_table.select('tr')[1:]

    interest_results = []


    for tr_tag in tr_tags:
        year = tr_tag.select('td')[0].text.strip()
        date = tr_tag.select('td')[1].text.strip()
        interest = float(tr_tag.select('td')[2].text.strip())
        
               


        temp={
            '연도': year,
            '날짜': date,
            '기준금리': interest,
        }
        
        interest_results.append(temp)

        
    


    # 데이터프레임 생성
    interest_df = pd.DataFrame(interest_results)
    interest_df


    # 파일 생성
    file_name = 'interest.csv'

    


    interest_df.to_csv(file_name, encoding='utf-8-sig', index=False)
    print("기준금리 파일이 생성되었습니다.")


    return interest_results