[app]

# نام اپلیکیشن
title = mohadeseh gym

# نام پکیج
package.name = mohadesehgym

# دامنه پکیج (برای اندروید)
package.domain = com.mohadeseh

# مسیر فایل اصلی برنامه
source.dir = .

# پسوند فایل‌های برنامه
source.include_exts = py,png,jpg,jpeg,kv,json,atlas

# نسخه برنامه
version = 1.0

# نیازمندی‌های پایتون و Kivy
requirements = python3,kivy

# صفحه نمایش
orientation = portrait

# اجازه استفاده از اینترنت (در صورت نیاز)
android.permissions = INTERNET

# نسخه اندروید
android.api = 35
android.minapi = 24

# NDK پیشنهادی
android.ndk = 28c

# معماری‌ها
android.archs = arm64-v8a,armeabi-v7a

# فعال کردن اندروید جدید
android.enable_androidx = True

# نام فایل آیکون
# اگر نداری این خط را حذف کن
# icon.filename = %(source.dir)s/icon.png


[buildozer]

# سطح لاگ
log_level = 2

# هشدارها
warn_on_root = 1
