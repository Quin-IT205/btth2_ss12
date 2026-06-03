saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("""
===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====
1. Xem danh sách sổ tiết kiệm
2. Mở sổ tiết kiệm mới
3. Cập nhật thông tin sổ tiết kiệm
4. Tất toán hoặc xóa sổ tiết kiệm
5. Tính lãi dự kiến khi đến hạn
6. Kiểm tra điều kiện rút trước hạn
7. Thoát chương trình
          """)
    choice = input('Mời bạn chọn chức năng (1-7): ')
    while not choice.isdigit():
        print('Không hợp lệ! Vui lòng nhập số')
        choice = input('Mời bạn chọn chức năng (1-7): ')
    
    choice = int(choice)
    match choice:
        case 1:
            stt = 0
            if (len(saving_accounts) == 0):
                print('Danh sách sổ tiết kiệm hiện đang trống')
            else:
                print('Danh sách sổ tiết kiệm:')
                for item in saving_accounts:
                    stt += 1
                    print(f'{stt}. Mã sổ: {item['account_id']:<10}  | Khách hàng: {item['customer_name']:<10} | Số tiền gửi: {item['balance']:<10} | Kì hạn: {item['term_months']:<5} | Lãi suất: {item['interest_rate']}%/năm | Trạng thái: {item['status']:<10}')
        case 2:
            print()
        case 3:
            print()
        case 4:
            print()
        case 5:
            print()
        case 6:
            print()
        case 7:
            print('Thoát chương trình!')
            break
        case _:
            print('Lựa chọn không hợp lệ!')
            continue
