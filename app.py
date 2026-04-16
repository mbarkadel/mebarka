from flask import Flask, render_template, request, redirect, url_for
from models import db, Book, Member

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/book/<int:book_id>')
def book_details(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book.html', book=book)

@app.route('/borrow/<int:book_id>', methods=['GET'])
def borrow_form(book_id):
    book = Book.query.get_or_404(book_id)
    if book.is_borrowed:
        return "هذا الكتاب غير متاح حالياً."
    return render_template('borrow.html', book=book)

@app.route('/confirm/<int:book_id>', methods=['POST'])
def confirm_borrow(book_id):
    book = Book.query.get_or_404(book_id)
    new_member = Member(
        fname=request.form['fname'],
        lname=request.form['lname'],
        email=request.form['email'],
        year=request.form['year'],
        phone=request.form['phone'],
        borrowed_book_title=book.title
    )
    book.is_borrowed = True
    db.session.add(new_member)
    db.session.commit()
    return render_template('success.html', book=book)

@app.route('/members')
def members_page():
    all_members = Member.query.all()
    return render_template('members.html', members=all_members)

# دالة المعلومات (تأكد أنها موجودة مرة واحدة فقط)
@app.route('/info/<int:book_id>')
def user_info(book_id):
    book = Book.query.get_or_404(book_id)
    member = Member.query.filter_by(borrowed_book_title=book.title).first()
    return render_template('about.html', member=member, book=book)

# دالة إعادة الكتاب (لجعل الكتاب متاحاً مرة أخرى)
@app.route('/return_item/<int:member_id>')
def return_book_logic(member_id):
    member = Member.query.get_or_404(member_id)
    book = Book.query.filter_by(title=member.borrowed_book_title).first()
    if book:
        book.is_borrowed = False
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for('members_page'))

if __name__ == '__main__':
    app.run(debug=True)