from pywinauto import Application

app=Application(backend="uia").connect(title="LTE 모뎀 에뮬레이터 V200626")
dlg=app["LTE 모뎀 에뮬레이터 V200626"]
