print("tool lọc url by Duc506")
def filter_lines_by_keyword():
    # Nhập tên file cần lọc
    input_file = input("Nhập tên file cần lọc: ")
    
    # Nhập từ khóa cần tìm
    keyword = input("Nhập url cần tìm: ")
    
    # Nhập tên file xuất kết quả
    
    output_file = f"{keyword}.txt"

    try:
        found = False  # Biến để kiểm tra xem có dòng nào chứa từ khóa không
        # Đọc file và lọc các dòng chứa từ khóa
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                if keyword in line:
                    outfile.write(line)
                    found = True  # Đánh dấu là đã tìm thấy ít nhất một dòng chứa từ khóa
        
        if found:
            print(f'Đã lọc các dòng chứa từ khóa "{keyword}" vào file "{output_file}".')
        else:
            print(f'Không tìm thấy bất kỳ dòng nào chứa từ khóa "{keyword}".')
    except FileNotFoundError:
        print(f'Tập tin "{input_file}" không tồn tại.')
    except Exception as e:
        print(f'Đã xảy ra lỗi: {e}')

# Gọi hàm để thực hiện lọc
filter_lines_by_keyword()
