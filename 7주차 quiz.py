#Quiz1
import random
def generate_lotto_numbers():
    result = []
    while len(result) < 6:
        num = random.randint(1, 45)
        if num not in result:
            result.append(num)
    return result

print(generate_lotto_numbers())

#Quiz2
class MultiplicationTable:
    def __init__(self, num):
        self.num = num

    def output(self):
        for i in range(1, 10):
            print(f"{self.num} x {i} = {self.num * i}")

user_input = int(input("구구단을 출력할 숫자를 입력하세요: "))
multiplication_table = MultiplicationTable(user_input)
multiplication_table.output()

#Quiz3
# 책 정보를 관리 하는 클래스
class Book:
    def __init__(self, title, author, Book_number):
        self.title = title  # 책 제목
        self.author = author  # 저자
        self.isbn = Book_number  # 책 번호
        self.is_checked_out = False  # 대출 상태

# 책을 대출
    def check_out(self):
        self.is_checked_out = True
# 책을 반납
    def return_book(self):
        self.is_checked_out = False
# 책 대출 가능 확인
    def is_available(self):
        return not self.is_checked_out

# 회원 정보를 관리 하는 클래스
class Member:
    def __init__(self, name, member_id):
        self.name = name  # 회원 이름
        self.member_id = member_id  # 회원 ID
        self.checked_out_books = []  # 대출한 책 리스트
# 책을 대출합니다.
    def borrow_book(self, book):
        if book.is_available():
            book.check_out()
            self.checked_out_books.append(book)
            print(f"{self.name}이(가) '{book.title}'을(를) 대출했습니다.")
        else:
            print(f"{book.title}은(는) 현재 대출 중입니다.")
# 책을 반납합니다.
    def return_book(self, book):
        if book in self.checked_out_books:
            book.return_book()
            self.checked_out_books.remove(book)
            print(f"{self.name}이(가) '{book.title}'을(를) 반납했습니다.")
        else:
            print(f"{self.name}은(는) '{book.title}'을(를) 대출 하지 않았습니다.")

    def list_checked_out_books(self):   # 대출한 책 리스트 출력
        return [book.title for book in self.checked_out_books]

# 도서관 운영을 관리 하는 클래스
class Library:
    def __init__(self):
        self.books = []  # 도서관 책 리스트
        self.members = []  # 도서관 회원 리스트

    def add_book(self, book):  # 도서관 책 추가
        self.books.append(book)

    def add_member(self, member):  # 도서관 회원 정보 추가
        self.members.append(member)

# 사용 예시
library = Library()
book1 = Book("채식주의자", "한강", "1234567890")
book2 = Book("소년이 온다", "한강", "1234567891")
member1 = Member("홍길동", 1)
member2 = Member("김철수", 2)
library.add_book(book1)
library.add_book(book2)
library.add_member(member1)
library.add_member(member2)

member1.borrow_book(book1)  # 홍길동이 책을 대출
member2.borrow_book(book1)  # 김철수가 홍길동과 같은 책을 대출
member1.return_book(book1)  # 홍길동이 책을 반납
member2.borrow_book(book1)  # 김철수가 다시 책을 대출
