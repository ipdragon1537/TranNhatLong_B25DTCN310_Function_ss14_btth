def display_grades(book):
    print("--- BẢNG ĐIỂM HỌC SINH ---")
    print(f"{'Mã SV':<5} | {'Tên Học Sinh':<20} | {'Điểm Toán':<10} | {'Điểm Anh':<10} | {'ĐTB':<5}")
    print("-"*70)
    for index in book:
        print(f"{index['id']:<5} | {index['name']:<20} | {index['info'][0]:<10} | {index['info'][1]:<10} | {(index['info'][0] + index['info'][1])/2:<5}")
    print("-"*70)
def add_student(book):
    while True:
        check = False
        input_id = input('Nhập mã sinh viên mới: ').strip().upper()
        for student in book:
            if student['id'] == input_id:
                check = True
                print('id đã tồn tại')
                break
        if not check:
            break
    add_student_name = input("Nhập tên sinh viên: ").strip().title()
    add_student_math = input("Nhập điểm toán: ")
    if add_student_math.isdigit():
        add_student_math = float(add_student_math)
    else:
        print("Điểm ko hợp lệ")
        return
    add_student_eng = input("Nhập điểm anh: ")
    if add_student_eng.isdigit():
        add_student_eng = float(add_student_eng)
    else:
        print("Điểm ko hợp lệ")
        return
    book.append({'id':input_id,'name':add_student_name,'info':(add_student_math,add_student_eng)})
    print(f"Thành công: Đã thêm học sinh {input_id} vào hệ thống! ")
def update_scores(book):
    update_id = input("Nhập mã cần cập nhật: ").strip().upper()
    update_math = input("Nhập điểm toán mới: ")
    if update_math.isdigit():
        update_math = float(update_math)
    else:
        print("Điểm ko hợp lệ")
        return
    update_eng = input("Nhập điểm anh mới: ")
    if update_eng.isdigit():
        update_eng = float(update_eng)
    else:
        print("Điểm ko hợp lệ")
        return 
    for index in book:
        if index['id'] == update_id:
            if 0 <= update_math <= 10 and 0 <= update_eng <= 10:
                index['info'] = (update_math,update_eng)
                print(f"Thành công: Đã cập nhật điểm cho học sinh {update_id}!")
                return
def delete_student(book):
    delete_id = input("Nhập mã cần xóa: ").strip().upper()
    if not delete_id:
        print("Mã sinh viên ko hợp lệ!")
        return
    for index in book:
        if index['id'] == delete_id:
            book.remove(index)
            print(f"Thành công: Đã xóa hồ sơ học sinh {delete_id} khỏi hệ thống!")
            return
    else:
        print("Mã sinh viên ko tồn tại")
def main():
    grade_book = [
    {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]
    while True:
        print("""=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===
1. Xem bảng điểm học sinh
2. Thêm hồ sơ học sinh mới
3. Cập nhật điểm số
4. Xóa hồ sơ học sinh
5. Thoát chương trình
================================
Chọn chức năng (1-5):""")
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                display_grades(grade_book)
            case "2":
                add_student(grade_book)
            case "3":
                update_scores(grade_book)
            case "4":
                delete_student(grade_book)
            case "5":
                print("Cảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!")
                break
            case _:
                print("Lựa chọn ko hợp lệ")
main()