title_cn = '''### 个人简历'''
title_en = '''# Résumé'''
img = "info_file/m_im.jpg"
css_style = """
    <style>
    div.stButton > button:first-child {
        height: 100%;
        width: 100%; 
    }
    .main {
        background-color:#f7f5f2;
        background-size:cover;
        
    }
    img {
        border-radius:50%;
    }
    </style>"""
info_dic_cn = {
    'tech_skills': ['专业技能', 'Python, R, SQL, Linear Regression, PowerBI, Tableau, Streamlit ,MS Office', '', '', ''],
    'language_skills': ['精通语言', '中文, 英文, 韩文', '', '', ''],
    'personal_info': ['联系方式', '安龙', '电话：+86 15900742695', '邮箱：anlong1013@163.com', ''],
    'certification': ['证书', 'Google 数据分析专业证书',
                      'https://www.coursera.org/account/accomplishments/specialization/certificate/K2K7XG8WHQTM',
                      'TESOL 国际英语教师资格证',
                      'https://login.teflserver.net/dpdf/10-334185/43173/ITTT00318024'],
    'education': ['教育背景', '天津商学院宝德职业技术学院： 国际贸易专业', '燕山大学: 英语专业', '', ''],
    'experience': ['工作年限', '工作经验', '', '', '']
}

info_dic_en = {
    'tech_skills': ['Tech Skills', 'Python, R, SQL, Linear Regression, PowerBI, Tableau, Streamlit, MS Office', '', '', ''],
    'language_skills': ['Languages', 'Mandarin, English, Korean', '', '', ''],
    'personal_info': ['Contact', 'Long An / Michael ', 'Cell：+86 15900742695', 'E-mail：anlong1013@163.com', ''],
    'certification': ['Certifications', 'Google Data Analytics Professional Certificate',
                      'https://www.coursera.org/account/accomplishments/specialization/certificate/K2K7XG8WHQTM',
                      'Certificate in Teaching English to Speakers of Other Languages',
                      'https://login.teflserver.net/dpdf/10-334185/43173/ITTT00318024'],
    'education': ['Education', 'Tianjin University of Commerce： International Trade', 'Yanshan University: English', '',
                  ''],
    'experience': ['Years of Working', 'Experience', '', '', '']
}

work_experiences_cn = {
    'first_exp': ['大宇制纸 (2006.6-2008.6) 中国天津',
                  ':man_in_business_suit_levitating: *财务会计* <br>'
                  ':black_small_square: 制作会计凭证 <br>'
                  ':black_small_square: 核对采购单，销售单，运输费等较大金额收入支出单据 <br>'
                  ':black_small_square: 制作中韩文会计报表，如资产负载表，损溢表，现金流量表等'],
    'second_exp': ['阿斯达 (2009.6-2011.2) 中国延吉',
                   ':man_in_business_suit_levitating: *Flash 设计师* <br>'
                   ':black_small_square: 使用公司内部资源，将Flash所需网页图片用Photoshop进行切割并输出 <br>'
                   ':black_small_square: 根客户需求设计和维护网页 <br>'
                   ':black_small_square: 制Flash产品，如主页，导航，网页其他组件 <br>'
                   ':black_small_square: 制作E-learning教学课件，曾带领5人团队根据客户需求制作教学课件并为公司盈利超过$20000'],
    'third_exp': ['盖茨诺联合律师事务所 (2012.2-2014.2) 美国纽约',
                  ':man_in_business_suit_levitating: *律师助理* <br>'
                  ':black_small_square: 执行多项行政工作，例如接电话,接待客户，预约，编制案件文档等等 <br>'
                  ':black_small_square: 参与30起以上不同类型的案件，包括移民，民事，刑事，交通等，涉及案件的申请和文件的管理流程 <br>'
                  ':black_small_square: 按照当地法律流程准备去往各个法院的文件 <br>'
                  ':black_small_square: 协调客户和律师寻找案件最佳可执行方案 <br> '
                  ':black_small_square: 陪同客户去往法院，并为其口译'],
    'fourth_exp': ['弗吉亚（中国） (2014.7-2015.7) 中国上海',
                   ':man_in_business_suit_levitating: *亚洲区 Helpdesk 工程师* <br>'
                   ':black_small_square: 属于IT技术支持链中 level 1 的范畴, 为韩国,日本,泰国,印度,马来西亚,中国的用户提供技术支持 <br>'
                   ':black_small_square: 通过电话,邮件, Stratos系统帮用户解决日常遇到的电脑,软件,账户,应用权限问题 <br>'
                   ':black_small_square: 管理用户帐号,为已授权的用户在系统内分配相应权限,如SAP, IAM等等 <br>'
                   ':black_small_square: 在其他IT部门和用户之间进行协调工作 <br>'
                   ':black_small_square: 编写报告, 优化方案, 技术文档'],
    'fifth_exp': ['融义财富 (2015.9-2016.3) 中国上海',
                  ':man_in_business_suit_levitating: *私募基金销售* <br>'
                  ':black_small_square: 电话或拜访，面谈客户，获取需求 <br>'
                  ':black_small_square: 筛选优质客户，推荐适合的私募产品 <br>'
                  ':black_small_square: 获取了基金从业资格证'],
    'sixth_exp': ['语风文化 (2016.5-2018.4) 中国无锡',
                  ':man_in_business_suit_levitating: *讲师（对外汉语，英语，韩语）* <br>'
                  ':black_small_square: 根据学生的水平进行语言教学 <br>'
                  ':black_small_square: 管理学生档案 <br>'
                  ':black_small_square: 对学生的学习进度和课程进行反馈'],
    'seventh_exp': ['岱恩教育 (2018.6-至今) 中国上海',
                    ':man_in_business_suit_levitating: *教学主管 / 授课讲师 / 课程设计与运营 / 工具类产品设计 / 数据分析* <br>'
                    ':black_small_square: 根据市场需求，与教学团队一同设计并制作了一套330课时的体系英语课程，包括固选，自选，小班等多种在线授课模式 <br>'
                    ':black_small_square: 带领兼职老师团队，制作了一系列行业课程，包括汽车，医疗，机械，市场营销等，约328节课时 <br>'
                    ':black_small_square: 基于公司课程，累计在线授课 300 余节 <br>'
                    ':black_small_square: 负责管理，运营微信小程序岱恩英语天天练，涉及制作学习内容，每日一句，各种专题，分类设计，学习逻辑等。基于数据，提出优化方案。目前已有3万7'
                    '千多的学员，每周以平均200人的数量持续增长 <br> '
                    ':black_small_square: 管理教学团队，培训教研老师的课件设计思路，teaching flow等 <br>'
                    ':black_small_square: 搭建公司兼职平台，设计雇佣逻辑，制定performance metrics，制作需求表格，项目进行流程，报价表，兼职人员名单等 <br>'
                    ':black_small_square: 每周进行数据统计，比如各个课程的上课情况，学员的主题偏好，小程序中学员对专题的完成度等等, 制作可视化图表，制作分析报告 <br>'
                    ':black_small_square: 与开发和产品团队沟通，优化并设计公司学习工具类产品，例如学员学习路径设计，交互设计，原型图设计，产品逻辑设计 <br>'
                    ':black_small_square: 根据销售反馈的需求，制作新的产品方案 <br>'
                    ':black_small_square: 利用自己的碎片时间和休息时间，完成课程并获得 Google 数据分析师证和TESOL国际教师资格证 '],
}

work_experiences_en = {
    'first_exp': ['DAEWOO (06/2006-06/2008) Tianjin,CN',
                  ':man_in_business_suit_levitating: *Accounting* <br>'
                  ':black_small_square: Checked material purchase lists. <br>'
                  ':black_small_square: Checked effective bills and sale detailed lists. <br>'
                  ':black_small_square: Filled out accounting documents, balance sheet statements, income statements,'
                  'statements of cash flow. etc, both in Chinese and Korean.'],
    'second_exp': ['ASADAL Technology (06/2009-02/2011) Yanji,CN',
                   ':man_in_business_suit_levitating: *Flash Designer* <br>'
                   ':black_small_square: Cut image sources and export by Photoshop. <br>'
                   ':black_small_square: Designed and maintained webpages according to the demand of clients. <br>'
                   ':black_small_square: Developed Flash products such as Navigation, Element, Main Visual, etc. <br>'
                   ':black_small_square: Led a team of 5 people to complete an E-learning project according to the '
                   'customer needs, and made profits of more than $20,000 for the company.'],
    'third_exp': [' Law Office of Giacchino J.Russo & Associates (02/2012-02/2014) NYC,US',
                  ':man_in_business_suit_levitating: *Paralegal* <br>'
                  ':black_small_square: Managed numerous tasks, included answer telephones, compute. <br>'
                  ':black_small_square: Handled various cases and applications, and managed filing procedures. <br>'
                  ':black_small_square: Prepared documents to each court in accordance with local legal procedures.<br>'
                  ':black_small_square: Coordinated with client and lawyer to find the best executable plan for the '
                  'case. <br> '
                  ':black_small_square: Accompanied clients to court and interpreted for them.'],
    'fourth_exp': ['Faurecia (China) (07/2014-07/2015) Shanghai,CN',
                   ':man_in_business_suit_levitating: *Asia Helpdesk Engineer* <br>'
                   ':black_small_square: Belongs to the category of Level 1 in IT technical support chain, provided '
                   'technical support for users in South Korea, Japan, Thailand, India, Malaysia and China. <br> '
                   ':black_small_square: Helped users solve their daily computer, software, account, and application '
                   'permissions problems through phone, email, and Stratos. <br> '
                   ':black_small_square: Managed user accounts and assign permissions to authorized users in the '
                   'system, such as SAP, IAM, etc. <br> '
                   ':black_small_square: Coordinated work between other IT departments and users. <br>'
                   ':black_small_square: Wrote reports, optimization solutions and technical documents.'],
    'fifth_exp': ['LOYAL WEALTH (09/2015-03/2016) Shanghai,CN',
                  ':man_in_business_suit_levitating: *PE Fund Sales* <br>'
                  ':black_small_square: Phoned and visited customers to seek demands.<br>'
                  ':black_small_square: Found out high-quality customers and recommended suitable private equity '
                  'products. <br> '
                  ':black_small_square: Obtained the fund qualification certificate.'],
    'sixth_exp': ['MandarinEdu (05/2016-04/2018) Wuxi,CN',
                  ':man_in_business_suit_levitating: *Trainer* <br>'
                  ":black_small_square: Taught Mandarin, Korean and English. <br>"
                  ':black_small_square: Provided feedback to students on productivity and progress. <br>'],
    'seventh_exp': ['DailyEdu (06/2018-present) Shanghai,CN',
                    ':man_in_business_suit_levitating: *Department Manager / Trainer / Courseware Designer / Product '
                    'Designer / Data Analyst* <br> '
                    ':black_small_square: According to the market demand, I designed and produced a systematical '
                    'English course, over 330 classes, with the teaching team, including fixed, pre-selected, '
                    'group class and other online learning modes. <br> '
                    ':black_small_square: Led a team of part-time teachers to produce a series of industry courses, '
                    'including automotive, medical, mechanical, marketing, etc., with about 328 classes <br> '
                    ':black_small_square: Taught more than 300 online classes. <br>'
                    ':black_small_square: Responsible for the management and operation of wechat mini program called '
                    'Dailyedu daily practice,involving the production of learning content, daily sentence, '
                    'various special topics, classification design, learning flow, program optimization, etc. It now '
                    'has more than 37,000 students, growing by an average of 200 students a week. <br> '
                    ':black_small_square: Manage teaching team, train teachers on courseware design ideas, teaching '
                    'flow, etc. <br> '
                    ''':black_small_square: Set up the company's part-time platform, designed the employment metrics, 
                    formulated performance metrics, made demand forms, project process, quotation forms, 
                    part-time personnel list, etc. <br>'''
                    ''':black_small_square: Make weekly data analytics, such as the class situation of each course, 
                    students' topic preference, students' completion of the topic in the mini program, make visual 
                    charts and analysis reports, etc. <br>'''
                    ''':black_small_square: Work with development and product team to optimize and design the 
                    company's learning applications, such as student learning curve, UX, prototype design, 
                    product design, etc. <br>'''
                    ''':black_small_square: Make new product plan according to sales' feedback <br>'''
                    ':black_small_square: By taking advantage of spare time, I completed the several courses and '
                    'obtained the Google Data Analytics Professional Certificate and Certificate in Teaching English '
                    'to Speakers of Other Languages. ']
}
