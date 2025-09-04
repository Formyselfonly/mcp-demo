# MCP工具使用说明

本项目提供了多个MCP (Model Context Protocol) 工具，包括系统信息查询、网络搜索和天气查询功能。

## 已实现的工具

### 1. 系统信息工具 (host_info_tools.py)
- **功能**: 获取电脑硬件和系统信息
- **工具**: `get_host_info()`
- **返回信息**: 操作系统、CPU型号、内存、磁盘使用情况等

### 2. 网络搜索工具 (web_search_tools.py)
- **功能**: 实时网络搜索和新闻查询
- **工具**: 
  - `web_search(query, num_results=5)`: 网络搜索
  - `get_news(query="technology", num_articles=5)`: 新闻搜索
- **数据源**: DuckDuckGo API (免费)

### 3. 天气查询工具 (weather_tools.py)
- **功能**: 实时天气查询和天气预报
- **工具**:
  - `get_weather(city, country_code="", api_key="")`: 当前天气
  - `get_weather_forecast(city, days=5, api_key="")`: 天气预报
- **数据源**: OpenWeatherMap API (需要免费注册)

## 配置说明

### 天气API配置
1. 访问 [OpenWeatherMap](https://openweathermap.org/api_keys) 注册免费账号
2. 获取API密钥
3. 在 `config.py` 文件中设置：
   ```python
   OPENWEATHER_API_KEY = "your_api_key_here"
   USE_DEMO_MODE = False
   ```

### 演示模式
如果不配置API密钥，工具会使用演示数据，让你了解功能效果。

## 使用方法

### 启动MCP服务器
```bash
python demo_main.py
```

### 在Cursor中使用
1. 确保MCP服务器正在运行
2. 在Cursor中，这些工具会自动可用
3. 你可以直接询问：
   - "我电脑什么型号？" - 获取系统信息
   - "搜索Python编程教程" - 进行网络搜索
   - "北京今天天气怎么样？" - 查询天气

## 工具详细说明

### 系统信息查询
```python
# 获取完整系统信息
get_host_info()
```
返回信息包括：
- 操作系统版本
- CPU型号和核心数
- 内存大小和使用情况
- 磁盘空间使用情况

### 网络搜索
```python
# 搜索特定内容
web_search("Python编程教程", num_results=5)

# 获取最新新闻
get_news("人工智能", num_articles=5)
```

### 天气查询
```python
# 查询当前天气
get_weather("北京", "CN")

# 查询天气预报
get_weather_forecast("上海", days=3)
```

## 文件结构
```
mcp-demo/
├── demo_main.py          # MCP服务器主程序
├── host_info_tools.py    # 系统信息工具
├── web_search_tools.py   # 网络搜索工具
├── weather_tools.py      # 天气查询工具
├── config.py             # 配置文件
├── requirements.txt      # 依赖包
└── USAGE.md             # 使用说明
```

## 依赖包
- `mcp`: MCP协议支持
- `psutil`: 系统信息获取
- `requests`: HTTP请求处理

## 注意事项
1. 网络搜索功能使用DuckDuckGo API，无需API密钥
2. 天气查询需要OpenWeatherMap API密钥才能获取实时数据
3. 所有工具都有错误处理机制，网络异常时会返回友好的错误信息
4. 演示模式下的数据仅供测试，不代表真实情况

## 扩展功能
你可以根据需要添加更多工具：
- 股票查询
- 翻译服务
- 文件操作
- 数据库查询
- 等等...

只需要按照现有工具的格式创建新的工具文件，并在 `demo_main.py` 中注册即可。
