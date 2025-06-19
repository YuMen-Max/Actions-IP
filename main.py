import random

# IP 前缀
prefix = "172.64.229"

# 生成 10 个随机 IP（尾段 1~200）
ips = [f"{prefix}.{random.randint(1, 200)}" for _ in range(10)]

# 写入到 random_ips.txt（覆盖旧内容）
with open("random_ips.txt", "w") as f:
    for ip in ips:
        f.write(ip + "\n")

# 可选：打印输出
print("已生成 IP：")
print("\n".join(ips))
