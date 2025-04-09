# 天气数据获取与保存项目

## 项目概述
本项目包含两个 Python 脚本，分别用于获取城市数据和天气数据，并将其保存到本地文件中。

## 功能介绍
1. **getCities.py**：通过和风天气 API 获取包含 'nanj' 的城市数据，并将数据保存到 `all_cities_data.xlsx` 文件中。
2. **weather_app.py**：通过和风天气 API 获取指定地点的 7 天天气数据，将原始数据保存到 `weather_data.json` 文件中，并将部分关键信息翻译成中文后保存到 `weather_data_cn.json` 文件中。

## API 调用方式
### 和风天气 API 信息
- `API_KEY` 和 `API_HOST` 从 `weknowConfig` 模块中导入。
- 城市数据 API URL：`https://{API_HOST}/geo/v2/city/lookup?location=nanj&number=20`
- 天气数据 API URL：`https://{API_HOST}/v7/weather/7d?location={LOCATION}`，其中 `LOCATION` 为地点代码。

### 请求头
请求时需要在请求头中添加 `X-QW-Api-Key` 字段，值为 `API_KEY`。

## 配置说明
- 在 `weknowConfig.py` 文件中配置 `API_KEY` 和 `API_HOST`。
- 在 `weather_app.py` 文件中可以修改 `LOCATION` 变量来指定获取天气数据的地点。

## 运行步骤
1. 确保已经安装所需的库：`requests` 和 `pandas`。
2. 配置 `weknowConfig.py` 文件中的 `API_KEY` 和 `API_HOST`。
3. 运行 `getCities.py` 脚本获取城市数据。
4. 运行 `weather_app.py` 脚本获取天气数据。

## 注意事项
- 请确保你的 `API_KEY` 是有效的，否则 API 请求将失败。
- 由于天气数据可能会发生变化，建议定期运行 `weather_app.py` 脚本来更新数据。