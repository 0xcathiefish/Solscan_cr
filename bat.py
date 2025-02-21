from Sols_holders import Solscan_holders

# 创建包含多个代币的列表
tokens = [
    '2B4dZwaNRdRkkDoAA1mJd5cvTFrP2VnqcwvGfoLVpump',  # dib
    
    'CTJf74cTo3cw8acFP1YXF3QpsQUUBGBjh2k2e8xsZ6UL',  # Neiro
    
    'LowThCB2Fe8D7Myrj1vJfN44xvHw1XayQazQuAMwLwh',   # lowkey
    
    '9CJ7VnoLfJfHX3AW1NbJUqMX9nqwckEHvncexPAEpump',  # OCL
    
    '5SVG3T9CNQsm2kEwzbRq6hASqh1oGfjqTtLXYUibpump'  # Sigma
]

# 设置要抓取的页面数
pages_to_scrape = 20

# 循环遍历每个代币，并执行Solscan_holders函数
for token in tokens:
    url = f'https://solscan.io/token/{token}#holders'
    Solscan_holders(url, pages_to_scrape)
