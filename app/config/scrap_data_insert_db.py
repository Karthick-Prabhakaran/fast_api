import schedule
import time
import pandas as pd
from bs4 import BeautifulSoup
import pandas as pd
from app.config.db import connection
# from db import connection
import selenium.webdriver


options = selenium.webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

def scheduler():
    driver = selenium.webdriver.Remote(command_executor='http://host.docker.internal:4444/wd/hub',options=options)
    # driver = selenium.webdriver.Chrome(executable_path=r"C:\Users\saras\.virtualenvs\saras-JNQJUT4_\Project_tangedco\chromedriver.exe",
    #                           service=Service(ChromeDriverManager().install()), chrome_options=options)
    driver.get("https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx")
    soup = BeautifulSoup(driver.page_source, 'lxml')
    tables = soup.find_all('table')
    dfs = pd.read_html(str(tables), header=None)
    print(f'Total tables: {len(dfs)}')
    print(dfs[1])
    #Creating db and appending data thorugh pandas
    dfs[1].index.name = 's_no'
    dfs[1].columns=["deal_Date","security_code","security_name","client_name","deal_type","quantity","price"]
    dfs[1].to_sql(con=connection,name='users',if_exists='append', index=False)
    connection.commit()
    print("---")
    
#running the scheduler for the first to commit the data in the db
#we can skip this first time if needed.
scheduler()

#Scheduling the web scrapper to pull data and upload to mysql everyday 12:00 PM
schedule.every().day.at("12:00:00").do(scheduler)
# schedule.every(1).minutes.do(scheduler)
while True:
    schedule.run_pending()
