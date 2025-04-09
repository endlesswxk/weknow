# 导入必要的库
import requests
import time
import json

# 和风天气 API 信息
from weknowConfig import API_KEY, API_HOST
API_HOST = 'mr63yv4ye6.re.qweatherapi.com'
LOCATION = '101190101'
API_URL = f'https://{API_HOST}/v7/weather/7d?location={LOCATION}'

# 保存数据的函数
def save_weather_data(data, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f'{file_name} 数据保存成功')
        # 替换字段为中文说明，并添加字段说明
        translated_data = {
            '日期': data.get('daily', [{}])[0].get('fxDate', ''),  # 天气对应的日期
            '最高温度': data.get('daily', [{}])[0].get('tempMax', ''),  # 当天的最高温度
            '最低温度': data.get('daily', [{}])[0].get('tempMin', ''),  # 当天的最低温度
            '白天天气状况': data.get('daily', [{}])[0].get('textDay', ''),  # 白天的天气状况描述
            '夜间天气状况': data.get('daily', [{}])[0].get('textNight', '')  # 夜间的天气状况描述
        }
        # 保存为新的 JSON 文件
        try:
            with open('weather_data_cn.json', 'w', encoding='utf-8') as file:
                json.dump(translated_data, file, ensure_ascii=False, indent=4)
            print('中文数据保存成功')
        except Exception as e:
            print(f'中文数据保存失败: {e}')
    except Exception as e:
        print(f'{file_name} 数据保存失败: {e}')
# 获取天气数据的函数
def get_weather_data():
    try:
        headers = {'X-QW-Api-Key': f'{API_KEY}'}
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()
        data = response.json()
        save_weather_data(data, 'weather_data.json')
    except requests.RequestException as e:
        print(f'请求失败: {e}')
    except ValueError as e:
        print(f'数据解析失败: {e}')

# 主函数，设置定时任务
def main():
    # while True:
        get_weather_data()
        # time.sleep(900)  # 每隔 15 分钟更新一次数据

if __name__ == '__main__':
    main()