# Kerry MCP Tools Collection

这是一个为Cursor设计的MCP (Model Context Protocol) 工具集合，提供多种实用功能，包括系统信息查询、个人档案管理、网络搜索和天气查询等。

## 🚀 功能特性

### 🔧 系统信息工具 (Host Info)
- 获取系统信息（操作系统、版本、架构）
- 获取CPU信息（处理器型号、核心数）
- 获取内存信息（总内存、已用内存、使用率）
- 获取磁盘信息（总容量、已用空间、使用率）

### 👤 个人档案工具 (Profile)
- 获取完整用户档案信息
- 简历摘要和专业成就
- 按类别查询技能列表
- 项目详细信息查询
- 动态更新用户兴趣

### 🌐 网络搜索工具 (Web Search)
- 实时网络搜索功能
- 新闻文章搜索
- 基于DuckDuckGo API
- 支持多语言搜索

### 🌤️ 天气查询工具 (Weather)
- 实时天气信息查询
- 多天天气预报
- 支持全球城市查询
- 基于OpenWeatherMap API

## 系统要求

- Python 3.8+
- Windows 10/11 (已测试)
- macOS (理论上支持)
- Linux (理论上支持)

## 📦 安装步骤

### 1. 克隆或下载项目
```bash
git clone https://github.com/Formyselfonly/mcp-demo.git
cd mcp-demo
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

或者手动安装：
```bash
pip install mcp psutil requests
```

### 3. 测试MCP工具
```bash
# 测试所有工具
python test_tools.py

# 测试个人档案工具
python demo_profile.py

# 测试系统信息工具
python host_info_tools.py
```

应该看到类似这样的输出：
```json
🚀 开始测试所有MCP工具...

============================================================
🎯 演示用户档案功能
============================================================
📋 完整用户档案:
姓名: KerryZheng
职位: AI Engineer, LLM Engineer, AI Agent Engineer
位置: 深圳
GitHub: https://github.com/Formyselfonly/resume

============================================================
📄 演示简历摘要功能
============================================================
摘要: AI研究生，专注于大模型和人工智能体研究
主要成就:
  ✅ 发表SCI论文：MemoryRepository for AI NPC
  ✅ 2年实习经验，多个个人项目展示
  ✅ AI中台开发经验丰富
  ✅ Prompt工程专家，多领域应用
```

## 🎯 在Cursor中使用

### 方法1：通过Cursor设置界面（推荐）

1. 打开Cursor
2. 按 `Ctrl+,` 打开设置
3. 搜索 "MCP" 或 "Model Context Protocol"
4. 添加新的MCP server，配置如下：
   - **名称**: `kerry-mcp-tools`
   - **命令**: `python`
   - **参数**: `["demo_main.py"]`
   - **工作目录**: `D:\githubproject\mcp-demo` (或你的实际路径)
   - **环境变量**: 
     - `PYTHONPATH`: `D:\githubproject\mcp-demo`

### 方法2：通过配置文件

在Cursor的设置中添加以下配置：
```json
{
  "mcpServers": {
    "kerry-mcp-tools": {
      "command": "python",
      "args": ["demo_main.py"],
      "cwd": "D:\\githubproject\\mcp-demo",
      "env": {
        "PYTHONPATH": "D:\\githubproject\\mcp-demo"
      }
    }
  }
}
```

## 🚀 启动MCP Server

### 方法1：直接运行（推荐）
```bash
python demo_main.py
```

### 方法2：测试工具
```bash
# 测试所有工具
python test_tools.py

# 测试个人档案
python demo_profile.py
```

## 💡 使用方法

### 启动MCP服务器
1. 运行 `python demo_main.py` 启动MCP服务器
2. 在Cursor中，MCP服务器应该自动连接
3. 现在你可以在对话中使用各种工具

### 可用工具列表

#### 🔧 系统信息工具
- `get_host_info` - 获取系统硬件和性能信息

#### 👤 个人档案工具
- `get_user_profile` - 获取完整用户档案
- `get_resume_summary` - 获取简历摘要
- `get_skills_by_category` - 按类别查询技能
- `get_project_details` - 获取项目详情
- `update_user_interest` - 更新用户兴趣

#### 🌐 网络搜索工具
- `web_search` - 执行网络搜索
- `get_news` - 获取新闻文章

#### 🌤️ 天气查询工具
- `get_weather` - 查询当前天气
- `get_weather_forecast` - 获取天气预报

### 使用示例
在Cursor中询问：
- "我的个人档案是什么？"
- "我的技能有哪些？"
- "搜索Python编程教程"
- "北京今天天气怎么样？"
- "我的系统信息"

## 故障排除

### 常见问题

1. **MCP server无法启动**
   - 检查Python是否正确安装
   - 检查依赖包是否安装：`pip list | findstr mcp`

2. **Cursor无法连接MCP server**
   - 确保MCP server正在运行
   - 检查工作目录路径是否正确
   - 检查环境变量设置

3. **权限问题**
   - 在Windows上，可能需要以管理员身份运行PowerShell
   - 检查文件路径权限

### 日志信息

MCP server会输出详细的日志信息，包括：
- 工具注册状态
- 服务器启动状态
- 连接信息

## 🔧 扩展功能

要添加新的工具，只需：

1. 在相应的工具文件中定义新函数（如 `get_name_profile.py`）
2. 在 `demo_main.py` 中使用 `mcp.add_tool()` 注册工具
3. 重启MCP服务器

### 项目结构
```
mcp-demo/
├── demo_main.py              # MCP服务器主程序
├── host_info_tools.py        # 系统信息工具
├── get_name_profile.py       # 个人档案工具
├── web_search_tools.py       # 网络搜索工具
├── weather_tools.py          # 天气查询工具
├── config.py                 # 配置文件
├── test_tools.py             # 测试脚本
├── demo_profile.py           # 个人档案演示
├── requirements.txt          # 依赖包
└── README.md                 # 说明文档
```

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 🌟 关于作者

**KerryZheng** - AI Engineer, LLM Engineer, AI Agent Engineer

- **GitHub**: [Formyselfonly](https://github.com/Formyselfonly)
- **简历**: [AI Engineer Resume](https://github.com/Formyselfonly/resume)
- **专业领域**: 大模型研究、Prompt工程、AI平台开发

## 📚 相关链接

- [MCP协议文档](https://modelcontextprotocol.io/)
- [Cursor编辑器](https://cursor.sh/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [DuckDuckGo API](https://duckduckgo.com/api)
