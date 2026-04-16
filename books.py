# books.py
from app import app
from models import db, Book

def init_books():
    with app.app_context():
        db.create_all()  # إنشاء قاعدة البيانات library.db
        
        # 1. تعريف القائمة داخل الدالة
        book_list = [
    Book(title="Learn Python", author="Mark Lutz", image="python.jpg"),
    Book(title="Flask Web Development", author="Miguel Grinberg", image="flask.jpg"),
    Book(title="Data Science from Scratch", author="Joel Grus", image="datascience.jpg"),
    Book(title="Introduction to Algorithms", author="Thomas H. Cormen", image="algorithms.jpg"),
    Book(title="Grokking Algorithms", author="Aditya Bhargava", image="grokking.jpg"),
]

# 2. التأكد من أن قاعدة البيانات فارغة قبل الإضافة
        if Book.query.count() == 0:
            # 3. إضافة الكائنات إلى الجلسة
            db.session.add_all(book_list) # استخدمنا add_all بدلاً من bulk_save_objects لضمان التوافق
            db.session.commit()
            print("✅ تم إنشاء قاعدة البيانات وإضافة الكتب بنجاح!")
        else:
            print("⚠️ قاعدة البيانات تحتوي بالفعل على كتب.")

if __name__ == "__main__":
    init_books()