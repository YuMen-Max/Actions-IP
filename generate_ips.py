import random

def generate_random_ips():
    # 基础IP段
    base_ip = "172.64.229"
    
    # 生成10个随机IP
    ip_list = []
    for _ in range(10):
        # 生成0-200之间的随机尾数
        tail = random.randint(0, 200)
        ip = f"{base_ip}.{tail}"
        ip_list.append(ip)
    
    return ip_list

if __name__ == "__main__":
    # 生成并打印IP列表
    ips = generate_random_ips()
    print("生成的随机IP地址:")
    for ip in ips:
        print(ip)
    
    # 可选：将结果保存到文件
    with open("generated_ips.txt", "w") as f:
        f.write("\n".join(ips))
    print("\n结果已保存到 generated_ips.txt")
