# 我自己的办法
考虑到原理其实就是运行一个服务,然后返回结果,我测了下
其实没这么麻烦,我感觉如果打包到uv里面,然后一个mcp.json就搞定啦
(因为uv的话可以安装并且运行)
或者说打包为python package,在pypi里面上传,然后别人pip install
只会配置mcp.json即可
0904新发现:发现market里面确实是这么做的
"""
{
  "mcpServers": {
    "time": {
      "command": "uvx",
      "args": [
        "mcp-server-time",
        "--local-timezone=America/New_York"
      ]
    }
  }
}
"""
# 在 demo_main.py 中添加
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["stdio", "http"], default="stdio")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    
    mcp = FastMCP("kerry-mcp-server")
    # ... 添加工具
    
    if args.mode == "http":
        print(f"Starting HTTP server on {args.host}:{args.port}")
        uvicorn.run(http_server(mcp), host=args.host, port=args.port)
    else:
        print("Starting stdio server for Cursor")
        mcp.run("stdio")


# 在云服务器上
git clone https://github.com/your-username/mcp-demo.git
cd mcp-demo
pip install -r requirements.txt
python demo_main.py --mode http --host 0.0.0.0 --port 8000


# 其他用户的 .cursor/mcp.json
{
    "mcpServers": {
      "kerry-ai-tools": {
        "url": "http://your-server-ip:8000",
        "headers": {}
      }
    }
}