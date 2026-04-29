import streamlit as st
import requests

# 页面配置
st.set_page_config(page_title="MathMentor-MiMo", layout="wide")
st.title("🍎 MathMentor 数学辅导助手")

# 侧边栏配置
with st.sidebar:
    st.header("配置中心")
    api_key = st.text_input("请输入 MiMo API Key", type="password")
    st.info("本项目基于小米 MiMo-V2.5 系列模型开发，用于个性化数学辅导。")

# 主界面
tab1, tab2, tab3 = st.tabs(["错题分析", "教案生成", "多模态批改"])

with tab1:
    st.subheader("📊 学生错题库长文本分析")
    st.write("上传学生近期的错题记录，MiMo 将利用 1M Token 的能力为您分析知识盲点。")
    uploaded_file = st.file_uploader("上传文件 (PDF/TXT)", type=['txt', 'pdf'])
    if st.button("开始深度分析"):
        st.warning("请先在左侧输入 API Key")

with tab2:
    st.subheader("📝 针对性题目生成")
    topic = st.text_input("请输入本节课重点知识点（如：因数和倍数）")
    difficulty = st.select_slider("选择难度", options=["基础", "进阶", "竞赛"])
    if st.button("生成测试题"):
        st.info(f"正在根据 {topic} 生成 {difficulty} 难度的题目...")

with tab3:
    st.subheader("📸 多模态作业批改")
    st.write("上传作业照片，由 MiMo-V2.5 原生多模态模型进行自动批改。")
    st.file_uploader("上传作业照片", type=['png', 'jpg', 'jpeg'])
