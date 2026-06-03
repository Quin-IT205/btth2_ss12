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
            isValid = False;
            account_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ")
            for i in range(len(saving_accounts)):
                if account_id.strip().upper() == saving_accounts[i].get("account_id") and saving_accounts[i].get("status") == "active":
                    interest = saving_accounts[i].get("balance") * saving_accounts[i].get("interest_rate") / 100 * saving_accounts[i].get("term_months") / 12
                    total_amount_received = interest + saving_accounts[i].get("balance")
                    print(f"Tiền lãi (VNĐ): {interest}")
                    print(f"Tiền nhận được khi đến hạn (VNĐ): {total_amount_received}")
                    isValid = True;
                    break
            if isValid == False:
                print(f"Không tìm thấy mã sổ tiết kiệm {account_id}!")
        case 6:
            isValid = False;
            account_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ")
            month_send = int(input("Nhập số tháng thực gửi: "))
            for i in range(len(saving_accounts)):
                if account_id.strip().upper() == saving_accounts[i].get("account_id") and saving_accounts[i].get("status") == "active":
                    if month_send >= saving_accounts[i].get("term_months"):
                        interest = saving_accounts[i].get("balance") * saving_accounts[i].get("interest_rate") / 100 * saving_accounts[i].get("term_months") / 12
                        total_amount_received = interest + saving_accounts[i].get("balance")
                        print("Vì bạn đã rút khi đủ kỳ hạn nên tính lãi theo lãi suất ban đầu của sổ")
                        print(f"Tiền lãi thực nhận (VNĐ): {interest}")
                        print(f"Tổng tiền thực nhận (VNĐ): {total_amount_received}")
                        isValid = True;
                        break
                    elif month_send < saving_accounts[i].get("term_months"):
                        interest = saving_accounts[i].get("balance") * 5 / 100 * saving_accounts[i].get("term_months") / 12
                        total_amount_received = interest + saving_accounts[i].get("balance")
                        print("Vì bạn đã trước hạn nên tính lãi là 0.5%")
                        print(f"Tiền lãi thực nhận (VNĐ): {interest}")
                        print(f"Tổng tiền thực nhận (VNĐ): {total_amount_received}")
                        isValid = True;
                        break
            if isValid == False:
                print(f"Không tìm thấy mã sổ tiết kiệm {account_id}!")
        case 7:
            print('Thoát chương trình!')
            break
        case _:
            print('Lựa chọn không hợp lệ!')
            continue
