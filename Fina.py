# đề: 002

class Student():
    def __init__(self, id, name, theory_score, practice_score, assignment_score):
        self.id=id
        self.name=name
        self.theory_score=theory_score
        self.practice_score=practice_score
        self.assignment_score=assignment_score
        self.average_score=0
        self.academic_type=""
        
    def calculate_average(self):
        self.average_score=round((self.theory_score*0.4)+(self.practice_score*0.4)+(self.assignment_score*0.2),2)
        return self.average_score
            
    def classify_academic(self):
        if self.average_score>8:
            self.academic_type="giỏi"
        elif self.average_score<8 and self.average_score>6.5:
            self.academic_type="khá"
        elif self.average_score<6.5 and self.average_score>5:
            self.academic_type="trung bình"
        else:
            self.academic_type="yếu"
            
        return self.academic_type
                
            
    
class StudentManager():
    def __init__(self):
        self.Students=[]
        
    def display_students(self):
        if self.Students==[]:
            print("Danh sách học sinh rổng !")
            return
        else:
            for item in self.Students:
                print(f"|MSV: {item.id} |Họ tên: {item.name} |theory_score: {item.theory_score} |practice_score: {item.practice_score} |assignment_score: {item.assignment_score}| Điểm tổng kết: {item.average_score} | Học lực: {item.academic_type}")
        return
    
    def add_student(self, new_student):
        self.Students.append(new_student)
    
    
    def update_student_score(self, student_id):
        if self.Students==[]:
            print("Danh sách học sinh rổng !")
            return
        else:
            for item in self.Students:
                if item.id==student_id:
 
                    try:   
                        new_theory_score=float(input("nhập vào điểm lý thuyết: "))
                        if new_theory_score < 0 or new_theory_score >10:
                            raise ValueError
                        
                    
                        new_practice_score=float(input("nhập vào điểm thực hành: "))
                        if new_practice_score < 0 or new_practice_score >10:
                            raise ValueError
                            
                        new_assignment_score=float(input("nhập vào điểm bài tập thường xuyên: "))
                        if new_assignment_score < 0 or new_assignment_score >10:
                            raise ValueError
                            
                            
            
                        item.theory_score=new_theory_score
                        item.practice_score=new_practice_score
                        item.assignment_score=new_assignment_score
                        
                        Student.calculate_average(item)
                        Student.classify_academic(item)
                        
                    except ValueError:
                        print("Các điểm số nhập vào phải lớn hơn 0 và nằm trong khoảng (0 - 10) và không được bỏ trống !")
                        return
                    
            print("không tìm thấy id sinh viên như vậy !")
            
    def delete_student_by_id(self, student_id):
        if self.Students==[]:
            print("Danh sách học sinh rổng !")
            return
        else:
            yn=input("bạn có thật sự muốn xóa sinh viên này không ? nhập (y) để xóa hoặc nhập (n) để dừng !").lower()
            if yn=="y":
                for item in self.Students:
                    if item.id==student_id:
                        self.Students.remove(item)
                        print(f"đã xóa thành công sinh viên với id: {student_id}")
                        return
                print(f"id :{student_id} không tông tại !")
                return
            elif yn=="n":
                print("Đã hủy thao tác xóa !")
            else: 
                print("lựa chọn không hợp lệ !!!")
                return
    
    def search_student_by_name(self, Student_name):
        if self.Students==[]:
            print("danh sách rổng ")
            return
        else:
            for item in self.Students:
                found=False
                if Student_name in item.name.lower():
                    print(f"|MSV: {item.id} |Họ tên: {item.name} |theory_score: {item.theory_score} |practice_score: {item.practice_score} |assignment_score: {item.assignment_score}| Điểm tổng kết: {item.average_score} | Học lực: {item.academic_type}")
                    found=True
                    
        if found==False:
            print(f"Không timg thấy sinh viên với tên {Student_name}")
            return
        
    def check_id_dupliucate(self, student_id):
        for item in self.Students:
            if item.id==student_id:
                return False
        return True   
        
manager=StudentManager()    
while True :
    print("\n====================================")
    print("STUDENT-SCORE-MANAGER".center(36))
    print("====================================")
    
    print("1. Hiển thị danh sách sinh viên")
    print("2. Thêm sinh viên mới")
    print("3. Cập nhật điểm sinh viên")
    print("4. Xóa sinh viên")
    print("5. Tìm kiếm sinh viên")
    print("6. Thoát")
    print("====================================")

    
    input_choice=input("Nhập vào lựa chọn của bạn: ")
    if input_choice not in ["1","2","3","4","5","6"]:
        print("Vui lòng chọn đúng lựa chọn có trong MENU chương trình !!")
        continue
    
    match (input_choice):
        case "1":
            manager.display_students()
            
        case "2":

            
            try:
                student_id=input("nhập vào id học sinh mới: ")
                

                if student_id=="":
                    print("id học sinh không được bỏ trống !")
                    continue
                
                found=manager.check_id_dupliucate(student_id)
                if found==False:
                    print("mã sinh viên này đã tồn tại vui lòng nhập lại !!!")
                    continue
            
                student_name=input("nhập vào tên học sinh mới: ")
                if student_name=="":
                    print("tên học sinh không được bỏ trống")
                    continue
                
                theory_score=float(input("nhập vào điểm lý thuyết: "))
                if theory_score < 0 or theory_score >10:
                    raise ValueError
                
            
                practice_score=float(input("nhập vào điểm thực hành: "))
                if practice_score < 0 or practice_score >10:
                    raise ValueError
                
                assignment_score=float(input("nhập vào điểm bài tập thường xuyên: "))
                if assignment_score < 0 or assignment_score >10:
                    raise ValueError
                    
     
                
            except ValueError:
                print("Các điểm số nhập vào phải lớn hơn 0 và nằm trong khoảng (0 - 10) và không được bỏ trống !")
                continue
                
            new_student=Student(student_id, student_name, theory_score, practice_score, assignment_score)
            new_student.calculate_average()
            new_student.classify_academic()
            
            manager.add_student(new_student)
            print("thêm thành công !!")
            
        case "3":
            id_to_update=input("nhập vào mã sinh viên bạn muốn cập nhật thông tin: ")
            manager.update_student_score(id_to_update)
            
        case "4":
            id_to_delete=input("nhâp vào mã sinh viên bạn muốn xóa khỏi danh sách: ")
            manager.delete_student_by_id(id_to_delete)
            
        case "5":
            name_to_search=input("nhập vào tên sinh viên bạn muốn tìm kiếm: ").lower()
            manager.search_student_by_name(name_to_search)
            
        case "6":
            print("Thoát chương trình ...")
            break