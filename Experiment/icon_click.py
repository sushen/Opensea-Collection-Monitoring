import pyautogui

icon = r"C:\Users\user\PycharmProjects\Opensea-Collection-Monitoring\OpenseaBusinessLogic\userdata\Profile 8\Extensions\\nkbihfbeogaeaoehlefnkodbefgpgknn\\10.18.0_0\images\icon-32.png"

# get the extension box
# extn = pyautogui.locateOnScreen(icon)
# print(extn)
# click on extension
x, y = 1740, 50
pyautogui.moveTo(x, y)
pyautogui.click(x, y)
# pyautogui.click(x=extn[0], y=extn[1], clicks=1, interval=0.0, button="left")