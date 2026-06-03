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
            account_id = input('Nhập mã sổ tiết kiệm: ').strip().upper()
            is_exist = False
            for item in saving_accounts:
                if item["account_id"] == account_id:
                    is_exist = True
                    break
            if is_exist:
                print('Mã sổ tiết kiệm đã tồn tại!')
                continue
            customer_name = input('Nhập tên khách hàng: ').strip()
            if customer_name == "":
                print('Tên khách hàng không được để trống')
                continue
            balance = input('Nhập số tiền gửi: ').strip()
            term_months = input('Nhập kỳ hạn gửi theo tháng: ').strip()
            if (not balance.isdigit() or not term_months.isdigit() or int(balance) <= 0 or int(term_months) <= 0):
                print('Số tiền gửi hoặc kỳ hạn không hợp lệ')
                continue
            interest_rate = input('Nhập lãi suất năm: ').strip()
            if not interest_rate.replace(".", "", 1).isdigit():
                print('Lãi suất không hợp lệ!')
                continue
            interest_rate = float(interest_rate)
            if interest_rate <= 0:
                print('Lãi suất không hợp lệ!')
                continue
            saving_accounts.append(
                {
                    "account_id": account_id,
                    "customer_name": customer_name,
                    "balance": int(balance),
                    "term_months": int(term_months),
                    "interest_rate": interest_rate,
                    "status": "active"
                }
            )
            print('Mở sổ tiết kiệm thành công!')
        case 3:
            found = False
            account_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()
            for item in saving_accounts:
                if (item["account_id"] == account_id):
                    found = True
                    break
            if (not found):
                print("Không tìm thấy mã sổ tiết kiệm!")
            elif (item["status"] != "active"):
                print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
            else:
                customer_name = input("Nhập tên khách hàng mới: ").strip()
                if (customer_name == ""):
                    print("Tên khách hàng không được để trống")
                else:
                    balance = input("Nhập số tiền gửi mới: ").strip()
                    if (not balance.isdigit() or int(balance) <= 0):
                        print("Số tiền gửi không hợp lệ")
                    else:
                        term_months = input("Nhập kỳ hạn mới theo tháng: ").strip()
                        if (not term_months.isdigit() or int(term_months) <= 0):
                            print("Số kỳ hạn không hợp lệ")
                        else:
                            interest_rate = input("Nhập lãi suất năm mới: ").strip()
                            if (not interest_rate.replace(".", "", 1).isdigit() or float(interest_rate) <= 0):
                                print("Lãi suất không hợp lệ!")
                            else:
                                item["customer_name"] = customer_name
                                item["balance"] = int(balance)
                                item["term_months"] = int(term_months)
                                item["interest_rate"] = float(interest_rate)
                                print("Cập nhật thông tin sổ tiết kiệm thành công!")
        case 4:
            found = False
            account_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()
            for item in saving_accounts:
                if (item["account_id"] == account_id):
                    found = True
                    break
            if (not found):
                print("Không tìm thấy mã sổ tiết kiệm!")
            elif (item["status"] == "closed"):
                print("Sổ tiết kiệm đã tất toán")
            else:
                item["status"] = "closed"
                print("Tất toán sổ tiết kiệm thành công")
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
