[app]

# (str) Title of your application
title = mohadeseh gym


# (str) Package name
package.name = mohadesehgym


# (str) Package domain (used for android package)
package.domain = com.mohadeseh


# (str) Source code where the main.py live
source.dir = .


# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt


# (str) Application version
version = 1.0.0


# (list) Application requirements
requirements = python3,kivy


# (str) Supported orientation
orientation = portrait


# (bool) Hide Android status bar
fullscreen = 0



# -------------------------
# Android Configuration
# -------------------------


# (bool) Accept Android SDK licenses
android.accept_sdk_license = True


# (int) Android API target
android.api = 35


# (int) Minimum Android version
android.minapi = 23


# (str) Android NDK version
android.ndk = 27c


# (list) Architectures
android.archs = arm64-v8a,armeabi-v7a


# (str) Android build tools
android.build_tools_version = 35.0.0


# (bool) Use AndroidX
android.enable_androidx = True


# (list) Permissions
android.permissions = INTERNET



# -------------------------
# Build Settings
# -------------------------


# (str) Python executable
# python version
p4a.branch = master


# (bool) Show compiler warnings
warn_on_root = 1


# (str) Log level
log_level = 2



# -------------------------
# iOS (unused)
# -------------------------

ios.kivy_ios_dir = ../kivy-ios



# -------------------------
# Kivy Settings
# -------------------------

[buildozer]


# (int) Log level
log_level = 2


# (str) Warn if running as root
warn_on_root = 1
