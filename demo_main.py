from re import A
from mcp.server import FastMCP
import host_info_tools
import web_search_tools
import weather_tools
import logging
import get_name_profile
import sys



def main():
    try:
        # Create MCP server instance
        mcp = FastMCP("host-info-mcp-server")
        
        # Add tools to the server

        mcp.add_tool(get_name_profile.get_user_profile)
        mcp.add_tool(get_name_profile.get_resume_summary)
        mcp.add_tool(get_name_profile.get_skills_by_category)
        mcp.add_tool(get_name_profile.get_project_details)
        mcp.add_tool(get_name_profile.update_user_interest)
        mcp.add_tool(host_info_tools.get_host_info)
        mcp.add_tool(web_search_tools.web_search)
        mcp.add_tool(web_search_tools.get_news)
        mcp.add_tool(weather_tools.get_weather)
        mcp.add_tool(weather_tools.get_weather_forecast)
        # Run the server with stdio transport
        mcp.run("stdio")
        
    except Exception as e:
        sys.exit(1)

if __name__ == "__main__":
    main()




