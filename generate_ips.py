import random
import os
import sys

def generate_random_ips():
    """生成10个随机IP地址，尾数在0-200之间"""
    try:
        base_ip = "172.64.229"
        tails = set()
        while len(tails) < 10:
            tails.add(random.randint(0, 200))
        return [f"{base_ip}.{tail}" for tail in tails]
    except Exception as e:
        print(f"生成IP时出错: {str(e)}")
        return []

def clear_existing_ips(file_path):
    """如果存在之前的IP文件，则清空内容"""
    try:
        if os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("")
            print(f"检测到并清空了之前的IP文件: {file_path}")
            return True
        return False
    except Exception as e:
        print(f"清空文件时出错: {str(e)}")
        return False

if __name__ == "__main__":
    try:
        # 获取当前工作目录
        current_dir = os.getcwd()
        output_file = os.path.join(current_dir, "generated_ips.txt")
        print(f"工作目录: {current_dir}")
        print(f"输出文件路径: {output_file}")
        
        # 1. 检测并清空之前的IP文件
        existed = clear_existing_ips(output_file)
        
        # 2. 生成新的随机IP
        ips = generate_random_ips()
        
        if not ips:
            print("错误: 未能生成任何IP地址")
            sys.exit(1)
            
        # 3. 写入新IP到文件
        with open(output_file, "w") as f:
            f.write("\n".join(ips))
        
        # 4. 输出结果
        print("\n成功生成的随机IP地址 (尾数0-200且不重复):")
        for ip in ips:
            print(ip)
        
        status = "覆盖" if existed else "创建"
        print(f"\n结果已{status}保存到 {output_file}")
        print(f"文件大小: {os.path.getsize(output_file)} 字节")
        
    except Exception as e:
        print(f"主程序发生错误: {str(e)}")
        sys.exit(1)