import pyautogui
import pyperclip
import time 
import pandas 
pyautogui.PAUSE = 1.5



# abrir navegador
pyautogui.press('win')
time.sleep(2.0)
pyautogui.write('chrome')
time.sleep(2)   
pyautogui.press('enter')
time.sleep(3.5)



# entrar no site
pyautogui.click(x=160, y=61)
pyperclip.copy('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
pyautogui.press('enter')
time.sleep(3.5)

#logar no site 
pyautogui.click(x=395, y=377)
time.sleep(3.0)
pyautogui.write('rafaelquintinoamz@gmail.com')
time.sleep(1.0)
pyautogui.press('tab')
pyautogui.write('123456789')
time.sleep(1.0)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(2)

# ler tabela

tabela = pandas.read_csv("produtos.csv")
for linha in tabela.index: 

    pyautogui.click(x=388, y=263)
    pyautogui.click(clicks=2)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, 'obs']))
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter', presses=3)
    pyautogui.scroll(5000)

