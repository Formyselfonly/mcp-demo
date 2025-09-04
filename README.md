# MCP Server for Cursor

这是一个为Cursor设计的MCP (Model Context Protocol) server，提供系统信息查询功能。

## 功能特性

- 获取系统信息（操作系统、版本、架构）
- 获取CPU信息（处理器型号、核心数）
- 获取内存信息（总内存、已用内存、使用率）
- 获取磁盘信息（总容量、已用空间、使用率）

## 系统要求

- Python 3.8+
- Windows 10/11 (已测试)
- macOS (理论上支持)
- Linux (理论上支持)

## 安装步骤

### 1. 克隆或下载项目
```bash
git clone <your-repo-url>
cd mcp-demo
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

或者手动安装：
```bash
pip install mcp psutil
```

### 3. 测试MCP server
```bash
python demo_tools.py
```

应该看到类似这样的输出：
```json
{
  "system": "Windows",
  "release": "11",
  "machine": "AMD64",
  "processor": "Intel64 Family 6...",
  "memory_gb": 31.63,
  "cpu_count": 20,
  "cpu_model": "Intel64 Family 6...",
  "memory_used_gb": 25.97,
  "memory_percent": 82.1,
  "disk_total_gb": 624.68,
  "disk_used_gb": 5.4,
  "disk_percent": 0.86
}
```

## 在Cursor中使用

### 方法1：通过Cursor设置界面（推荐）

1. 打开Cursor
2. 按 `Ctrl+,` 打开设置
3. 搜索 "MCP" 或 "Model Context Protocol"
4. 添加新的MCP server，配置如下：
   - **名称**: `host-info-server`
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
    "host-info-server": {
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

## 启动MCP Server

### 方法1：使用PowerShell脚本（推荐）
```powershell
.\start_mcp_server.ps1
```

### 方法2：直接运行
```bash
python demo_main.py
```

### 方法3：使用批处理文件
```cmd
start_mcp_server.bat
```

## 使用方法

1. 启动MCP server
2. 在Cursor中，MCP server应该自动连接
3. 现在你可以在对话中使用 `get_host_info` 工具来获取系统信息

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

## 扩展功能

要添加新的工具，只需：

1. 在 `demo_tools.py` 中定义新函数
2. 在 `demo_main.py` 中使用 `mcp.add_tool()` 注册工具
3. 重启MCP server

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！
