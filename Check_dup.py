import os
import pandas as pd
import csv
from collections import defaultdict

def find_duplicate_addresses(directory, exclude_addresses):
    # 获取目录下所有CSV文件
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

    # 用于存储所有地址及其对应的文件名
    address_to_files = defaultdict(set)

    for csv_file in csv_files:
        # 读取CSV文件
        df = pd.read_csv(os.path.join(directory, csv_file))
        
        # 提取地址列并记录其对应的文件名
        addresses = df['Address'].tolist()
        for address in addresses:
            if address not in exclude_addresses:
                address_to_files[address].add(csv_file)

    # 找出重复的地址
    duplicate_addresses = {address: files for address, files in address_to_files.items() if len(files) > 1}

    # 输出重复的地址及其对应文件名
    print("以下地址在多个CSV文件中重复出现：")
    for address, files in duplicate_addresses.items():
        print(f"{address} 出现在 {', '.join(files)}")

    # 如果需要将重复的地址保存到文件
    with open(os.path.join(directory, 'DUPLICATE.csv'), 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Address", "Files"])  # 写入CSV的标题行
        for address, files in duplicate_addresses.items():
            writer.writerow([address, ', '.join(files)])

    print("重复的地址已保存到 DUPLICATE.csv")

# 示例调用
directory = 'F:\\Pythonscript\\Solscan_cr\\csv'  # 替换为你的文件夹路径

# 排除列表，由用户输入
exclude_addresses = [
    'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA',
    '5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1',
    'dead111111111111111111111111111111111111111',
    'D27DgiipBR5dRdij2L6NQ27xwyiLK5Q2DsEM5ML5EuLK',
    '45ruCyfdRkWpRNGEqWzjCiXRHkZs8WXCLQ67Pnpye7Hp',
    # 添加更多要排除的地址
]

find_duplicate_addresses(directory, exclude_addresses)
