# 导入必要的库
import requests
import pandas as pd

# 和风天气 API 信息
from weknowConfig import API_KEY, API_HOST
API_URL = f'https://{API_HOST}/geo/v2/city/lookup?location=nanj&number=20'

# 获取所有城市数据的函数
def get_all_cities_data():
    try:
        headers = {'X-QW-Api-Key': f'{API_KEY}'}
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f'请求失败: {e}')
    except ValueError as e:
        print(f'数据解析失败: {e}')

# 保存数据到 Excel 的函数
def save_to_excel(data):
    try:
        df = pd.DataFrame(data['location'])
        df.to_excel('all_cities_data.xlsx', index=False)
        print('数据保存到 Excel 成功')
    except Exception as e:
        print(f'数据保存到 Excel 失败: {e}')

# 主函数
if __name__ == '__main__':
    cities_data = get_all_cities_data()
    if cities_data:
        save_to_excel(cities_data)