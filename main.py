from appGui import AppGUI
from pyautogui import alert


def main():
    gui = AppGUI()
    gui.startApp()


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        alert(f"Error: {e}. File not found.")
    except Exception as e:
        alert(f"An unexpected error has occurred: {e}")
    finally:
        exit()

exit()
