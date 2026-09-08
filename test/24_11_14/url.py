import requests
import time
import os

# 服务器地址与上报密码通过环境变量配置，避免硬编码敏感信息
SERVER_HOST = os.getenv("SEAT_SERVER_HOST", "<SERVER_HOST>")
SERVER_PASSWORD = os.getenv("SEAT_SERVER_PASSWORD", "")

def send_data_to_server(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        print("数据发送成功")
    except requests.RequestException as e:
        print(f"数据发送失败: {e}")

def main():
    # 输入设备序列ID
    device_id = input("请输入设备序列ID: ")

    # 构建服务器URL
    server_url = f"http://{SERVER_HOST}/update_data_{device_id}"

    # 输入座位数据和密码
    occupied = input("请输入已占用座位数: ")
    available = input("请输入可用座位数: ")
    password = SERVER_PASSWORD

    # 构建数据字典
    data = {
        "occupied": int(occupied),
        "available": int(available),
        "password": password
    }

    # 发送数据
    while True:
        send_data_to_server(server_url, data)
        #print("数据已发送")
        time.sleep(60)  # 每60秒发送一次数据

if __name__ == "__main__":
    main()
