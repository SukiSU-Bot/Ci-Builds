[app]
title = My Python App
package.name = mypythonapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE
android.api = 36
android.minapi = 24
android.ndk = r29
android.gradle_dependencies = 

android.accept_sdk_license = True
android.arch = armeabi-v8a

[buildozer]
log_level = 2
warn_on_root = 1
