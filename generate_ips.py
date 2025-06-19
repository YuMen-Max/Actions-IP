import random
import os

def generate_random_ips():
    """生成10个随机IP地址，尾数在0-200之间"""
    base_ip = "172.64.229"
    # 使用集合确保同一批IP尾数不重复
    tails = set()
    while len(tails) < 10:
        tails.add(random.randint(0, 200))
    
    return [f"{base_ip}.{tail}" for tail in tails]

def clear_existing_ips(file_path):
    """如果存在之前的IP文件，则清空内容"""
    if os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("")  # 清空文件内容
        print(f"检测到并清空了之前的IP文件: {file_path}")
        return True
    return False

if __name__ == "__main__":
    output_file = "generated_ips.txt"
    
    # 1. 检测并清空之前的IP文件
    existed = clear_existing_ips(output_file)
    
    # 2. 生成新的随机IP
    ips = generate_random_ips()
    
    # 3. 写入新IP到文件
    with open(output_file, "w") as f:
        f.write("\n".join(ips))
    
    # 4. 输出结果
    print("\n生成的随机IP地址 (尾数0-200且不重复):")
    for ip in ips:
        print(ip)
    
    status = "覆盖" if existed else "创建"
    print(f"\n结果已{status}保存到 {output_file}")
