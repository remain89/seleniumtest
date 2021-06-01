# 계산기 실행을 위해서 subprocess import
import subprocess

# 계산기 실행
#subprocess.Popen('calc.exe')

# uiautomation을 auto로 import하기
import uiautomation as auto

# 계산기 창을 조작하기 위해서 계산기 창을 찾고 해당 객체값을 반환
emul = auto.WindowControl(searchDepth=1, Name='LTE 모뎀 에뮬레이터 V200626') #현재 기능상 파일 명이 변경될때마다 바꿔줘야할듯

# 계산기 창이 확인될때까지 총 3초를 1초간격으로 확인하기
# 못찾을 경우 못찾았다는 메시지와 함께 종료
if not emul.Exists(3, 1):
    print('Can not find Calculator window')
    exit(0)

print('Find it')
#LocalizedControltype
# ButtonControl을 통한 calculator의 Button속성의 자식 중 1인 값을 찾아서 Click수행
'''
emul.ButtonControl(Name="G-타입검침").Click() #잘됨
emul.RadioButtonControl(Name="Day Dump").Click()  #잘됨
emul.ComboBoxControl(Name="서브 코드").Select(itemName="0x04 : 순방향+역방향 LP") #Combobox control은 요딴식으로....
emul.ButtonControl(Name="G-type 검침데이터 요청").Click() #잘됨
'''
print('success11')

emul.ButtonControl(Name="LTE&모뎀관리").Click() #잘됨
emul.TextControl(Name="RegAvailCode").SetWindowText("12345")
#emul.ComboBoxControl(Name="목록 항목").Select(itemName="2 : 검침 Agent만 Reset") #Combobox control은 요딴식으로....
#"textBox_SysEncrypt"
#"WindowsForms10.EDIT.app.0.1ca0192_r20_ad1"
#"sysMIBEncrypt"
print('success22')