# Custom imports
import cn_resume
import en_resume
import stock_price
from multipage import MultiPage

# Create an instance of the app 
app = MultiPage()

# Title of the main page
# st.title("")

# Add all your applications (pages) here
app.add_page("中文简历", cn_resume.app)
app.add_page("English", en_resume.app)
app.add_page("Project1: Stock Price", stock_price.app)
# app.add_page("Data Analysis",data_visualize.app)
# app.add_page("Y-Parameter Optimization",redundant.app)

# The main app
app.run()
