[app]

title = mohadeseh gym

package.name = mohadesehgym

package.domain = com.mohadeseh

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,json,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2

warn_on_root = 1


[android]

android.api = 35

android.minapi = 23

android.ndk = 27c

android.build_tools_version = 35.0.0

android.accept_sdk_license = True

android.archs = arm64-v8a,armeabi-v7a


# فعال کردن AIDL و ابزارهای لازم
android.skip_update = False


[p4a]

android.bootstrap = sdl2

android.private_storage = True

android.ndk_api = 23
