import time
import pydirectinput as p
import keyboard

def PetOUT(TabNum,InputNum):
    
    #右スキルスロットに移動
    p.keyDown('ctrl')
    p.keyDown('tab')
    p.keyUp('ctrl')
    p.keyUp('tab')

    #タブを切り替え
    p.keyDown('ctrl')
    p.keyDown(TabNum)
    p.keyUp('ctrl')
    p.keyUp(TabNum)

    #数値を文字列に変換
    InputWord=str(InputNum)

    if InputNum == 10:InputWord = '0'#10の場合0を代入
    elif InputNum == 11:InputWord = '-'#11の場合ｰを代入

    p.keyDown(InputWord)#ペット呼び出し
    p.keyUp(InputWord)

    time.sleep(0.3)

    p.keyDown('u')#ペットを消す
    p.keyUp('u')

    #タブを戻す
    p.keyDown('ctrl')
    p.keyDown('2')
    p.keyUp('ctrl')
    p.keyUp('2')

    #スキルスロットを左に戻す
    p.keyDown('ctrl')
    p.keyDown('tab')
    p.keyUp('ctrl')
    p.keyUp('tab')

    InputNum+=1 #数値を＋１する
    
    if InputNum > 11:InputNum = 1 #12以上の場合は1に戻す

    return InputNum #戻り値


KeyNumber = 1
KeyNumber2 = 1
KeyNumber3 = 1

while True:
    if keyboard.is_pressed('.'):  # . キーが押された場合(ワイバーン)
        KeyNumber = PetOUT('5',KeyNumber)
    elif keyboard.is_pressed('+'):  # + キーが押された場合(ホワイトドラゴン)
        KeyNumber2 = PetOUT('6',KeyNumber2)
    elif keyboard.is_pressed('-'):  # - キーが押された場合(羊＆ダル)
        KeyNumber3 = PetOUT('7',KeyNumber3)