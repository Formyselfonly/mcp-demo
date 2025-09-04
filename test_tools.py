#!/usr/bin/env python3
"""
测试脚本 - 验证所有MCP工具的功能
"""

import json
import host_info_tools
import web_search_tools
import weather_tools

def test_host_info():
    """测试系统信息工具"""
    print("=" * 60)
    print("测试系统信息工具")
    print("=" * 60)
    result = host_info_tools.get_host_info()
    data = json.loads(result)
    print(f"系统: {data['system']} {data['release']}")
    print(f"处理器: {data['cpu_model']}")
    print(f"内存: {data['memory_gb']} GB")
    print(f"CPU核心数: {data['cpu_count']}")
    print("✅ 系统信息工具测试通过\n")

def test_web_search():
    """测试网络搜索工具"""
    print("=" * 60)
    print("测试网络搜索工具")
    print("=" * 60)
    
    # 测试网络搜索
    result = web_search_tools.web_search("Python编程", 3)
    data = json.loads(result)
    print(f"搜索查询: {data['query']}")
    if data.get('instant_answer'):
        print(f"即时答案: {data['instant_answer']['title']}")
    print(f"相关主题数量: {len(data.get('related_topics', []))}")
    print("✅ 网络搜索工具测试通过\n")
    
    # 测试新闻搜索
    result = web_search_tools.get_news("人工智能", 3)
    data = json.loads(result)
    print(f"新闻查询: {data['query']}")
    print(f"文章数量: {len(data.get('articles', []))}")
    print("✅ 新闻搜索工具测试通过\n")

def test_weather():
    """测试天气查询工具"""
    print("=" * 60)
    print("测试天气查询工具")
    print("=" * 60)
    
    # 测试当前天气
    result = weather_tools.get_weather("北京")
    data = json.loads(result)
    print(f"城市: {data['location']['city']}")
    print(f"温度: {data['current_weather']['temperature']}°C")
    print(f"天气: {data['current_weather']['description']}")
    print("✅ 当前天气工具测试通过\n")
    
    # 测试天气预报
    result = weather_tools.get_weather_forecast("上海", 3)
    data = json.loads(result)
    print(f"城市: {data['location']['city']}")
    print(f"预报天数: {data['forecast_days']}")
    print(f"预报数据: {len(data.get('forecast', []))} 天")
    print("✅ 天气预报工具测试通过\n")

def main():
    """运行所有测试"""
    print("🚀 开始测试所有MCP工具...\n")
    
    try:
        test_host_info()
        test_web_search()
        test_weather()
        
        print("=" * 60)
        print("🎉 所有工具测试完成！")
        print("=" * 60)
        print("现在你可以运行 'python demo_main.py' 启动MCP服务器")
        print("然后在Cursor中使用这些工具了！")
        
    except Exception as e:
        print(f"❌ 测试过程中出现错误: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
