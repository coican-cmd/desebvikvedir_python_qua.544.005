import pyautogui as auto


def main():
    auto.PAUSE = 0.8

    auto.press("win")
    auto.write("firefox")
    auto.press("enter")
    auto.write("globo.com")
    auto.press("enter")
    auto.hotkey("ctrl","t")
    auto.write("sistemafibra.org.br/senai")
    auto.press("enter")
    auto.hotey("ctrl","shift","p")
    auto.sleep(3)
    auto.write("metropoles.com")
    auto.press("enter")

if __name__ == "__main__":
   main()