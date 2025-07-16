import streamlit as st

# Dictionary for UI translations
translations = {
    "english": {
        "title": "AI Prompt Generator",
        "subtitle": "Configure your AI prompt by selecting the options below:",
        "task_input": "Enter your task for the AI:",
        "options_header": "Prompt Options",
        "generate_button": "Generate Prompt",
        "copy_button": "Copy Prompt to Clipboard",
        "copied_message": "Prompt copied to clipboard!",
        "prompt_header": "Generated Prompt",
        "prompt_label": "Your AI prompt:",
        "lang_comm": "Language & Communication",
        "file_ops": "File Operations",
        "code_quality": "Code Quality & Style",
        "perf_security": "Performance & Security",
        "testing_exec": "Testing & Execution",
        "project_specs": "Project Specifics",
        "response_lang": "Response Language",
        "explanation_detail": "Explanation Detail",
        "edit_files": "Allow AI to edit files",
        "generate_files": "Allow AI to generate files",
        "ban_requests": "Ban external requests",
        "code_style": "Code Style",
        "error_handling": "Include error handling",
        "doc_level": "Documentation Level",
        "optimize_perf": "Optimize for performance",
        "preferred_framework": "Preferred Framework",
        "security_check": "Include security considerations",
        "compatibility": "Compatibility Requirements",
        "create_tests": "Create unit tests",
        "executable": "Run tests without modifying existing ones",
        "dir_check": "Directory to check (optional)",
        "not_specified": "Not specified",
        "ui_language": "UI Language"
    },
    "chinese": {
        "title": "AI 提示生成器",
        "subtitle": "通过选择以下选项配置您的 AI 提示：",
        "task_input": "输入您给 AI 的任务：",
        "options_header": "提示选项",
        "generate_button": "生成提示",
        "copy_button": "复制提示到剪贴板",
        "copied_message": "提示已复制到剪贴板！",
        "prompt_header": "生成的提示",
        "prompt_label": "您的 AI 提示：",
        "lang_comm": "语言和沟通",
        "file_ops": "文件操作",
        "code_quality": "代码质量和风格",
        "perf_security": "性能和安全",
        "testing_exec": "测试和执行",
        "project_specs": "项目细节",
        "response_lang": "响应语言",
        "explanation_detail": "解释详细程度",
        "edit_files": "允许 AI 编辑文件",
        "generate_files": "允许 AI 生成文件",
        "ban_requests": "禁止外部请求",
        "code_style": "代码风格",
        "error_handling": "包含错误处理",
        "doc_level": "文档级别",
        "optimize_perf": "优化性能",
        "preferred_framework": "首选框架",
        "security_check": "包含安全考虑",
        "compatibility": "兼容性要求",
        "create_tests": "创建单元测试",
        "executable": "运行测试但不修改现有测试",
        "dir_check": "要检查的目录（可选）",
        "not_specified": "未指定",
        "ui_language": "界面语言",
        "minimal": "最小",
        "low": "低",
        "medium": "中等",
        "high": "高",
        "comprehensive": "全面"
    }
}

def generate_prompt(task="", language="english", edit_file=False, generate_file=False, 
                   ban_request=False, unittest=False, run=False, dir=None,
                   code_style=None, documentation_level=None, error_handling=False,
                   performance_optimization=False, security_check=False, 
                   framework=None, compatibility=None, explanation_detail="medium"):
    """
    Generate an AI prompt based on the selected options.

    Parameters:
    - task: The specific task for the AI
    - language: Language for the response (english, chinese, spanish, french)
    - edit_file: Whether to allow AI to edit files
    - generate_file: Whether to allow AI to generate files
    - ban_request: Whether to ban certain requests
    - unittest: Whether to create a unittest
    - run: Whether to run tests after generation without modifying existing tests
    - dir: Directory to be checked
    - code_style: Preferred code style (PEP8, Google, etc.)
    - documentation_level: Level of documentation required
    - error_handling: Whether to include error handling
    - performance_optimization: Whether to optimize for performance
    - security_check: Whether to include security considerations
    - framework: Preferred framework to use
    - compatibility: Compatibility requirements
    - explanation_detail: Level of detail in explanations

    Returns:
    - A formatted prompt string
    """
    prompt = ""

    # Add the task if provided
    if task:
        prompt += f"Task: {task}\n\n"

    # Language & Communication settings
    if language != "english":
        if language == "chinese":
            prompt += "请使用中文回答。\n\n"
        elif language == "spanish":
            prompt += "Por favor, responde en español.\n\n"
        elif language == "french":
            prompt += "Veuillez répondre en français.\n\n"

    # Explanation detail
    if explanation_detail != "medium":
        prompt += f"Please provide {explanation_detail} level of detail in your explanations.\n"

    # File operations permissions section
    has_file_ops = edit_file or (not generate_file) or ban_request
    if has_file_ops:
        prompt += "## File Operations\n"
        if edit_file:
            prompt += "You are allowed to edit existing files.\n"

        if not generate_file:  # Default is True, so only include if False
            prompt += "You are NOT allowed to generate new files.\n"

        if ban_request:
            prompt += "Please do not make any external API calls or access external resources.\n"

    # Code Quality & Style section
    has_code_quality = code_style or documentation_level or error_handling
    if has_code_quality:
        prompt += "\n## Code Quality & Style\n"
        if code_style:
            prompt += f"Please follow {code_style} style guidelines.\n"

        if documentation_level:
            prompt += f"Include {documentation_level} level of documentation in the code.\n"

        if error_handling:
            prompt += "Implement proper error handling and validation.\n"

    # Performance & Security section
    if performance_optimization or security_check:
        prompt += "\n## Performance & Security\n"
        if performance_optimization:
            prompt += "Optimize the code for performance.\n"
        if security_check:
            prompt += "Include security best practices and considerations.\n"

    # Framework & Compatibility section
    if framework or compatibility:
        prompt += "\n## Framework & Compatibility\n"
        if framework:
            prompt += f"Use {framework} framework.\n"
        if compatibility:
            prompt += f"Ensure compatibility with {compatibility}.\n"

    # Testing & Execution section
    has_testing = unittest or run
    if has_testing:
        prompt += "\n## Testing & Execution\n"
        if unittest:
            prompt += "Please create unit tests for the code.\n"
        if run:
            prompt += "Please run the tests after generation without modifying existing tests.\n"

    # Project Specifics section
    if dir:
        prompt += f"\n## Project Specifics\nPlease check the following directory: {dir}\n"

    return prompt

def main():
    # Apply custom CSS to make the UI more compact
    st.markdown("""
    <style>
        /* Reduce overall padding and margins */
        .stApp {
            padding-top: 0.5rem;
            padding-bottom: 0.5rem;
        }
        /* Make the header smaller */
        .stApp header {
            height: auto !important;
            padding-top: 0.5rem !important;
            padding-bottom: 0.5rem !important;
        }
        /* Reduce padding in containers */
        .stMarkdown, .stButton, .stTextArea, div.stSelectbox, div.stRadio, div.stCheckbox {
            padding-top: 0.25rem !important;
            padding-bottom: 0.25rem !important;
            margin-bottom: 0.25rem !important;
        }
        /* Make text areas more compact */
        .stTextArea textarea {
            min-height: 5rem !important;
        }
        /* Make expanders more compact */
        .streamlit-expanderHeader {
            padding-top: 0.25rem !important;
            padding-bottom: 0.25rem !important;
        }
        .streamlit-expanderContent {
            padding-top: 0.25rem !important;
            padding-bottom: 0.25rem !important;
        }
        /* Make buttons smaller */
        .stButton button {
            padding: 0.25rem 1rem !important;
            font-size: 0.8rem !important;
        }
        /* Make select boxes smaller */
        div.stSelectbox > div {
            padding-top: 0.25rem !important;
            padding-bottom: 0.25rem !important;
        }
        /* Make radio buttons more compact */
        div.stRadio > div {
            padding-top: 0.25rem !important;
            padding-bottom: 0.25rem !important;
        }
        /* Make checkboxes more compact */
        div.stCheckbox > div {
            padding-top: 0.25rem !important;
            padding-bottom: 0.25rem !important;
        }
        /* Make headers smaller */
        h1 {
            font-size: 1.5rem !important;
            margin-bottom: 0.5rem !important;
        }
        h2 {
            font-size: 1.2rem !important;
            margin-bottom: 0.5rem !important;
        }
        h3 {
            font-size: 1rem !important;
            margin-bottom: 0.5rem !important;
        }
        /* Make code blocks more compact */
        pre {
            padding: 0.5rem !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Initialize session state for storing the generated prompt and UI language
    if "prompt" not in st.session_state:
        st.session_state.prompt = ""
        st.session_state.prompt_generated = False

    if "ui_language" not in st.session_state:
        st.session_state.ui_language = "english"

    # Get translations for the current UI language
    t = translations[st.session_state.ui_language]

    # UI Language selector in a small container at the top right
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"<h1>{t['title']}</h1>", unsafe_allow_html=True)
        with col2:
            ui_lang = st.selectbox(
                t["ui_language"],
                options=["english", "chinese"],
                index=0 if st.session_state.ui_language == "english" else 1,
                key="ui_lang_selector",
                label_visibility="collapsed"
            )
            # Update UI language if changed
            if ui_lang != st.session_state.ui_language:
                st.session_state.ui_language = ui_lang
                st.rerun()

    # Compact layout with task input and options side by side
    col_task, col_options = st.columns([1, 1])

    with col_task:
        # Task input in the left column
        task = st.text_area(t["task_input"], height=80)

        # Generate button below task input
        generate_button = st.button(t["generate_button"], use_container_width=True)

        # Display the generated prompt if available
        if st.session_state.prompt_generated:
            st.subheader(t["prompt_header"])
            st.code(st.session_state.prompt, language="markdown")

    with col_options:
        # Options in the right column
        st.markdown(f"<h3>{t['options_header']}</h3>", unsafe_allow_html=True)

        # Tabs for different option categories to save space
        tabs = st.tabs([t["lang_comm"], t["file_ops"], t["code_quality"], t["testing_exec"]])

        # Tab 1: Language & Communication
        with tabs[0]:
            language = st.radio(
                t["response_lang"],
                options=["english", "chinese", "spanish", "french"],
                index=0,
                horizontal=True
            )

            explanation_options = ["minimal", "low", "medium", "high", "comprehensive"]
            explanation_detail = st.select_slider(
                t["explanation_detail"],
                options=explanation_options,
                value="medium",
                format_func=lambda x: t.get(x, x)
            )

        # Tab 2: File Operations
        with tabs[1]:
            edit_file = st.checkbox(t["edit_files"], value=False)
            generate_file = st.checkbox(t["generate_files"], value=True)
            ban_request = st.checkbox(t["ban_requests"], value=True)

            # Framework & Compatibility in the same tab to save space
            framework = st.selectbox(
                t["preferred_framework"],
                options=[None, "Django", "Flask", "FastAPI", "React", "Vue", "Angular", "TensorFlow", "PyTorch", "Other"],
                format_func=lambda x: t["not_specified"] if x is None else x
            )

            compatibility = st.selectbox(
                t["compatibility"],
                options=[None, "Python 3.6+", "Python 3.8+", "Python 3.10+", "Cross-browser", "Mobile-friendly", "Other"],
                format_func=lambda x: t["not_specified"] if x is None else x
            )

        # Tab 3: Code Quality
        with tabs[2]:
            code_style = st.selectbox(
                t["code_style"],
                options=[None, "PEP8", "Google", "NumPy", "Microsoft", "Custom"],
                format_func=lambda x: t["not_specified"] if x is None else x
            )

            documentation_level = st.select_slider(
                t["doc_level"],
                options=[None, "minimal", "standard", "detailed", "comprehensive"],
                value=None,
                format_func=lambda x: t["not_specified"] if x is None else x
            )

            error_handling = st.checkbox(t["error_handling"], value=False)
            performance_optimization = st.checkbox(t["optimize_perf"], value=False)
            security_check = st.checkbox(t["security_check"], value=False)

        # Tab 4: Testing & Execution
        with tabs[3]:
            unittest = st.checkbox(t["create_tests"], value=False)
            run = st.checkbox(t["executable"], value=True)

            dir = st.text_input(t["dir_check"])
            if dir == "":
                dir = None

    # Generate prompt when button is clicked
    if generate_button:
        # Generate the prompt and store it in session state
        st.session_state.prompt = generate_prompt(
            task=task,
            language=language,
            edit_file=edit_file,
            generate_file=generate_file,
            ban_request=ban_request,
            unittest=unittest,
            run=run,
            dir=dir,
            code_style=code_style,
            documentation_level=documentation_level,
            error_handling=error_handling,
            performance_optimization=performance_optimization,
            security_check=security_check,
            framework=framework,
            compatibility=compatibility,
            explanation_detail=explanation_detail
        )
        st.session_state.prompt_generated = True
        st.rerun()  # Rerun to update the UI

    # The prompt is already displayed in the task column when generated

if __name__ == '__main__':
    main()
