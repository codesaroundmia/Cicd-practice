# سرور لوکال پایتون برای نمایش فایل index.html
# این کد از ماژول داخلی http.server استفاده می‌کند و نیازی به نصب پکیج‌های اضافی ندارد.

import http.server
import socketserver
import os

# تعیین پورت سرور. پورت 8000 یک انتخاب رایج است.
PORT = 8000

# اطمینان حاصل کنید که فایل index.html در همین دایرکتوری وجود دارد.
if not os.path.exists("index.html"):
    print("خطا: فایل index.html پیدا نشد.")
    print("لطفاً مطمئن شوید که index.html در همین دایرکتوری قرار دارد.")
else:
    # تعریف هندلر برای سرویس‌دهی فایل‌ها
    Handler = http.server.SimpleHTTPRequestHandler

    print(f"شروع سرور در پورت: {PORT}")
    print(f"برای مشاهده صفحه، مرورگر خود را به آدرس http://localhost:{PORT} باز کنید.")

    try:
        # ساخت سرور TCP
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            # شروع گوش دادن به درخواست‌ها
            httpd.serve_forever()
    except KeyboardInterrupt:
        # برای متوقف کردن سرور با Ctrl+C
        print("\nسرور متوقف شد.")
    except PermissionError:
        # در صورتی که پورت در حال استفاده باشد یا اجازه دسترسی وجود نداشته باشد
        print(f"\nخطا: اجازه استفاده از پورت {PORT} وجود ندارد یا پورت توسط برنامه دیگری اشغال شده است.")
        print("لطفاً یک پورت دیگر را امتحان کنید (مثلاً 8080) یا برنامه دیگری که از این پورت استفاده می‌کند را ببندید.")