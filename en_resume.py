import webbrowser
import pandas as pd
import streamlit as st
import resume_text as rs
from PIL import Image


def company_worked(name, duty):
    with st.expander(name):
        st.markdown(f"""
        {duty}
        """, unsafe_allow_html=True)


def profile_page(info, work):
    st.markdown('''---''')
    img = Image.open(rs.img)
    with st.container():
        col1, col2 = st.columns([1.2, 1.8])

        with col1:
            st.image(img, width=150, caption=f"{info['personal_info'][1]}")
            st.markdown(f'''**{info['personal_info'][0]}:**''')
            st.markdown(f'''
            {info['personal_info'][2]}<br>
            {info['personal_info'][3]}<br>
            ''', unsafe_allow_html=True)
            # education
            st.markdown(f'''**{info['education'][0]}:**''')
            st.success(f'''
                   - {info['education'][1]}
                   - {info['education'][2]}
                    ''')
            # certificates
            st.markdown(f'''**{info['certification'][0]}:**''')
            google_certificate = st.button(info['certification'][1])
            if google_certificate:
                webbrowser.open_new(info['certification'][2])
            tesol_certificate = st.button(info['certification'][3])
            if tesol_certificate:
                webbrowser.open_new(info['certification'][4])

            # technic skills
            st.markdown(f'''**{info['tech_skills'][0]}:**''')
            st.info(info['tech_skills'][1])
            # language skills
            st.markdown(f'''**{info['language_skills'][0]}:**''')
            st.error(info['language_skills'][1])

        with col2:
            # 年度调整

            year = st.slider(
                f'''{info['experience'][0]}:''', min_value=2006, max_value=2022, value=2022, step=1)
            st.markdown(f'''**{info['experience'][1]}:**''')
            # 工作经验
            exp_list = list(work.columns)
            if year < 2009:
                company_worked(work[f'{exp_list[0]}'][0], work[f'{exp_list[0]}'][1])
            elif year < 2012:
                for i in range(len(exp_list) - 5):
                    m = len(exp_list) - i - 6
                    company_worked(work[f'{exp_list[m]}'][0], work[f'{exp_list[m]}'][1])
            elif year < 2015:
                for i in range(len(exp_list) - 4):
                    m = len(exp_list) - i - 5
                    company_worked(work[f'{exp_list[m]}'][0], work[f'{exp_list[m]}'][1])
            elif year < 2016:
                for i in range(len(exp_list) - 3):
                    m = len(exp_list) - i - 4
                    company_worked(work[f'{exp_list[m]}'][0], work[f'{exp_list[m]}'][1])
            elif year < 2017:
                for i in range(len(exp_list) - 2):
                    m = len(exp_list) - i - 3
                    company_worked(work[f'{exp_list[m]}'][0], work[f'{exp_list[m]}'][1])
            elif year < 2019:
                for i in range(len(exp_list) - 1):
                    m = len(exp_list) - i - 2
                    company_worked(work[f'{exp_list[m]}'][0], work[f'{exp_list[m]}'][1])
            elif year <= 2022:
                for i in range(len(exp_list)):
                    m = len(exp_list) - i - 1
                    company_worked(work[f'{exp_list[m]}'][0], work[f'{exp_list[m]}'][1])
    st.markdown('''---''')


def app():
    # load data
    info = pd.DataFrame(rs.info_dic_en)
    experience = pd.DataFrame(rs.work_experiences_en)
    app_title = rs.title_en
    st.markdown(app_title)

    # page style
    st.markdown(rs.css_style, unsafe_allow_html=True)
    profile_page(info, experience)
