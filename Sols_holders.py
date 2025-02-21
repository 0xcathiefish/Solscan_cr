from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv
import re

def Solscan_holders(url, pages_to_scrape):
    # 设置Chrome选项
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 无头模式，不打开浏览器窗口

    # 指定ChromeDriver路径
    chrome_service = Service('F:/Pythonscript/Selenium/chromedriver.exe')  # 使用你的实际路径

    # 初始化webdriver
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # 打开指定网页
    driver.get(url)

    # 等待页面加载
    time.sleep(3)  # 适当的等待时间，视具体情况而定

    # 提取SIGMA值
    try:
        name_element = driver.find_element(By.XPATH, "//meta[@property='og:title']")
        name = name_element.get_attribute('content')
        
        match = re.search(r'\((.*?)\)', name)
        if match:
            valid_name = match.group(1)
        else:
            valid_name = 'name_special'
        
        print(f"TokenName: {valid_name}")
        
        csv_filename = f'csv/{valid_name}_holders.csv'
        
    except Exception as e:
        print(f"Exception occurred while extracting TokenName: {e}")
        name = None

    # 初始化一个变量来存储所有地址
    all_addresses = []

    for _ in range(pages_to_scrape):
        # 提取当前页面的所有持币地址
        addresses = driver.find_elements(By.XPATH, "//a[contains(@href, '/account/')]")
        for address in addresses:
            href = address.get_attribute('href')
            # 提取地址部分并添加到all_addresses列表中
            all_addresses.append(href.split('/')[-1])
        
        try:
            # 查找“下一页”按钮并点击
            next_button = driver.find_element(By.XPATH, "//button[./span[@aria-label='right']]")
            
            # 滚动页面以使“下一页”按钮可见
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            time.sleep(1)  # 等待滚动完成
            
            # 点击“下一页”按钮
            next_button.click()
            
            # 等待新页面加载
            time.sleep(5)
        except Exception as e:
            print(f"Exception occurred: {e}")
            # 如果找不到“下一页”按钮，则退出循环
            break

    # 保存所有地址到CSV文件
    with open(csv_filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Address"])  # 写入CSV的标题行
        for address in all_addresses:
            writer.writerow([address])

    # 关闭webdriver
    driver.quit()

    print(f"所有持币地址已下载到 {csv_filename}")


if __name__ == '__main__':
    
    token = 'LowThCB2Fe8D7Myrj1vJfN44xvHw1XayQazQuAMwLwh'  # Example token
    
    url = f'https://solscan.io/token/{token}#holders'
    
    pages_to_scrape = 2

    Solscan_holders(url, pages_to_scrape)
