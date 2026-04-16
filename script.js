// static/js/script.js

document.addEventListener('DOMContentLoaded', function() {
    // إيجاد كل الأزرار في الصفحة
    const buttons = document.querySelectorAll('.nav-item, .btn-borrow');

    buttons.forEach(btn => {
        // عند الضغط على الزر (تغيير اللون لحظياً)
        btn.addEventListener('mousedown', function() {
            this.style.backgroundColor = '#d7ccc8'; // لون بني فاتح جداً عند الضغط
        });

        // العودة للون الطبيعي عند رفع الضغط
        btn.addEventListener('mouseup', function() {
            this.style.backgroundColor = '';
        });
    });

    // تنبيه بسيط عند نجاح الاستعارة (إذا كنت في صفحة النجاح)
    if (window.location.pathname.includes('success')) {
        console.log("تمت عملية الاستعارة بنجاح!");
    }
});