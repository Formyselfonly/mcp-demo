#!/usr/bin/env python3
"""
演示脚本 - 展示增强的个人资料MCP工具功能
"""

import json
import get_name_profile

def demo_user_profile():
    """演示用户档案功能"""
    print("=" * 60)
    print("🎯 演示用户档案功能")
    print("=" * 60)
    
    # 获取完整用户档案
    profile = get_name_profile.get_user_profile()
    print("📋 完整用户档案:")
    print(f"姓名: {profile['basic_info']['name']}")
    print(f"职位: {profile['basic_info']['title']}")
    print(f"位置: {profile['basic_info']['location']}")
    print(f"GitHub: {profile['basic_info']['github']}")
    print()

def demo_resume_summary():
    """演示简历摘要功能"""
    print("=" * 60)
    print("📄 演示简历摘要功能")
    print("=" * 60)
    
    summary = get_name_profile.get_resume_summary()
    print(f"摘要: {summary['summary']}")
    print("主要成就:")
    for achievement in summary['key_achievements']:
        print(f"  ✅ {achievement}")
    print(f"简历链接: {summary['github_link']}")
    print()

def demo_skills_by_category():
    """演示按类别获取技能功能"""
    print("=" * 60)
    print("🛠️ 演示按类别获取技能功能")
    print("=" * 60)
    
    categories = ["frameworks", "ai_platforms", "core_tech", "research"]
    
    for category in categories:
        skills_info = get_name_profile.get_skills_by_category(category)
        print(f"📚 {category.upper()} 技能 ({skills_info['count']} 项):")
        for skill in skills_info['skills']:
            print(f"  🔧 {skill}")
        print()

def demo_project_details():
    """演示项目详情功能"""
    print("=" * 60)
    print("🚀 演示项目详情功能")
    print("=" * 60)
    
    projects = ["ECommerceGPT", "minimax_audiomixing_streamlit", "PromptCompletionsForDifyAI", "PromptEval"]
    
    for project in projects:
        details = get_name_profile.get_project_details(project)
        print(f"📁 项目: {project}")
        print(f"   描述: {details['description']}")
        print(f"   技术: {details['technology']}")
        print(f"   目的: {details['purpose']}")
        print(f"   GitHub: {details['github']}")
        print()

def demo_interactive_features():
    """演示交互功能"""
    print("=" * 60)
    print("🔄 演示交互功能")
    print("=" * 60)
    
    # 更新兴趣
    result = get_name_profile.update_user_interest("AI研究")
    print(f"更新兴趣: {result}")
    
    # 测试不存在的类别
    invalid_category = get_name_profile.get_skills_by_category("invalid_category")
    print(f"无效类别测试: {invalid_category}")
    
    # 测试不存在的项目
    invalid_project = get_name_profile.get_project_details("InvalidProject")
    print(f"无效项目测试: {invalid_project}")
    print()

def main():
    """运行所有演示"""
    print("🚀 开始演示增强的个人资料MCP工具...\n")
    
    try:
        demo_user_profile()
        demo_resume_summary()
        demo_skills_by_category()
        demo_project_details()
        demo_interactive_features()
        
        print("=" * 60)
        print("🎉 所有演示完成！")
        print("=" * 60)
        print("现在你可以在Cursor中使用这些MCP工具了！")
        print("试试询问:")
        print("  - '我的完整档案是什么？'")
        print("  - '我的简历摘要'")
        print("  - '我的框架技能有哪些？'")
        print("  - 'ECommerceGPT项目的详细信息'")
        print("  - '添加新兴趣：机器学习'")
        
    except Exception as e:
        print(f"❌ 演示过程中出现错误: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
