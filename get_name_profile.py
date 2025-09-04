# user_profile.py
def get_user_profile():
    """获取用户完整档案 - 基于GitHub简历数据"""
    return {
        "basic_info": {
            "name": "KerryZheng",
            "title": "AI Engineer, LLM Engineer, AI Agent Engineer",
            "location": "深圳",
            "linkedin": "Available on GitHub resume",
            "github": "https://github.com/Formyselfonly/resume"
        },
        "education": {
            "degree": "AI Graduate Student",
            "focus": "LLM Research, AI Entities and NPCs",
            "research": "MemoryRepository for AI NPC (SCI paper published April 2024)"
        },
        "experience": {
            "internship": "2 years of internship experience",
            "specialization": "AI Platform Development, NLP, LLMs, AIGC"
        },
        "technical_skills": {
            "frameworks": [
                "Dify", "Coze", "RAGFlow",
                "LangChain", "LangGraph", "LangSmith",
                "FastAPI", "Flask"
            ],
            "ai_platforms": [
                "ECommerceGPT - Cross-border eCommerce GPT Efficiency Tool",
                "minimax_audiomixing_streamlit - Speech & Mixing Interface",
                "StableDiffusion", "ComfyUI"
            ],
            "core_technologies": [
                "Large Language Models (LLMs)",
                "Prompt Engineering",
                "Retrieval-Augmented Generation (RAG)",
                "AI Agent Development",
                "Game NPCs",
                "Chatbots",
                "Data Processing & Fine-tuning"
            ]
        },
        "projects": {
            "ai_tools": [
                "ECommerceGPT - Text-based large model for eCommerce operations",
                "minimax_audiomixing_streamlit - Audio-to-image tool",
                "PromptCompletionsForDifyAI - Automated prompt testing",
                "PromptEval - Prompt evaluation system"
            ],
            "research": [
                "MemoryRepository for AI NPC - Enables long-term, human-like dialogues",
                "AI entities with emotional and partial consciousness systems"
            ]
        },
        "achievements": {
            "publications": "SCI paper published in April 2024",
            "expertise": "Expert in prompt engineering across multiple domains",
            "innovation": "Developed solutions for prompt testing time and cost issues"
        }
    }

def update_user_interest(new_interest):
    """更新用户兴趣"""
    # 模拟更新逻辑
    return f"已添加新兴趣: {new_interest}"

def get_resume_summary():
    """获取简历摘要"""
    return {
        "summary": "AI研究生，专注于大模型和人工智能体研究",
        "key_achievements": [
            "发表SCI论文：MemoryRepository for AI NPC",
            "2年实习经验，多个个人项目展示",
            "AI中台开发经验丰富",
            "Prompt工程专家，多领域应用"
        ],
        "github_link": "https://github.com/Formyselfonly/resume"
    }

def get_skills_by_category(category):
    """根据类别获取技能"""
    skills_map = {
        "frameworks": ["Dify", "Coze", "RAGFlow", "LangChain", "LangGraph", "LangSmith", "FastAPI", "Flask"],
        "ai_platforms": ["ECommerceGPT", "minimax_audiomixing_streamlit", "StableDiffusion", "ComfyUI"],
        "core_tech": ["LLMs", "Context Engineering","Prompt Engineering", "RAG", "AI Agent Development", "Game NPCs", "Chatbots"],
        "research": ["MemoryRepository for AI NPC", "Multi Agent"]
    }
    
    if category in skills_map:
        return {
            "category": category,
            "skills": skills_map[category],
            "count": len(skills_map[category])
        }
    return f"类别 '{category}' 不存在，可用类别: {list(skills_map.keys())}"

def get_project_details(project_name):
    """获取项目详细信息"""
    projects = {
        "ECommerceGPT": {
            "description": "跨境电商GPT效率工具",
            "technology": "文本大模型",
            "purpose": "提升电商运营效率",
            "github": "https://github.com/Formyselfonly/ECommerceGPT"
        },
        "minimax_audiomixing_streamlit": {
            "description": "语音&混音接口",
            "technology": "文生图工具",
            "purpose": "音频到图像转换",
            "github": "https://github.com/Formyselfonly/minimax_audiomixing_streamlit"
        },
        "PromptCompletionsForDifyAI": {
            "description": "Prompt自动化测试",
            "technology": "自动化测试框架",
            "purpose": "解决Prompt测试的时间和成本问题",
            "github": "https://github.com/Formyselfonly/PromptCompletionsForDifyAI"
        },
        "PromptEval": {
            "description": "Prompt评估系统",
            "technology": "主观和客观评估",
            "purpose": "Prompt质量评估",
            "github": "https://github.com/Formyselfonly/PromptEval"
        }
    }
    
    if project_name in projects:
        return projects[project_name]
    return f"项目 '{project_name}' 不存在，可用项目: {list(projects.keys())}"