from pywinauto.application import Application
app = Application(backend="uia").start("notepad.exe")
#app['Dialog']['Edit'].set_text("LTE 모뎀 에뮬레이터 V200626")