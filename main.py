import requests

# Cài đặt token của bot và chat_id của kênh/nhóm cần lấy file
bot_token = '6472630978:AAGqCFNjrvP2xAiievA4_xMZBJBNHgITckA'
chat_id = '-1002069322619'  # Thay bằng ID của kênh/nhóm cần lấy file

# Function để lấy thông tin file từ một message trong kênh/nhóm
def get_file_info_from_message(message):
    if 'document' in message:
        file_info = message['document']
        return file_info
    elif 'photo' in message:
        # Lấy ảnh đầu tiên (kích thước lớn nhất) nếu có
        photos = message['photo']
        largest_photo = max(photos, key=lambda x: x['file_size'])
        file_info = largest_photo
        return file_info
    else:
        return None

# Function để tải file từ Telegram
def download_file(file_info):
    if file_info:
        file_id = file_info['file_id']
        file_path = file_info.get('file_path')

        # Nếu có file_path, tải file từ Telegram Servers
        if file_path:
            file_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path}"
            response = requests.get(file_url, stream=True)

            if response.status_code == 200:
                # Lưu file
                with open(file_info['file_name'], 'wb') as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)
                print(f"Đã tải file thành công: {file_info['file_name']}")
            else:
                print("Không thể tải file từ Telegram.")
        else:
            print("Không tìm thấy đường dẫn file.")
    else:
        print("Không tìm thấy thông tin file.")

# Function chính để lấy và tải file từ kênh/nhóm
def get_and_download_files():
    # Gửi request để lấy các message từ kênh/nhóm
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)
    if response.status_code == 200:
        messages = response.json()['result']
        
        # Lặp qua các message và lấy thông tin file từ message
        for message in messages:
            file_info = get_file_info_from_message(message)
            if file_info:
                download_file(file_info)
                # Dừng sau khi tải thành công file đầu tiên (có thể thay đổi logic tùy ý)
                break
    else:
        print("Không thể lấy các message từ kênh/nhóm.")

# Gọi function chính để thực hiện
get_and_download_files()
