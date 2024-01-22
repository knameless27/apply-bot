from appGui import AppGUI
from pyautogui import alert
def main():
    gui = AppGUI()
    gui.startApp()

if __name__ == "__main__":
    try:
        main()
    except:
        alert("An unexpected error has occurred!")
    finally:
        exit()

exit()
# makeApplications()