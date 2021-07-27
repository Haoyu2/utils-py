from rich import print
from utils.my_log import log

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    di = {1:2, 3:4}
    log.info(locals())
    log.debug(di)
    log.error("[bold red blink]Server is shutting down![/]", extra={"markup": True})
    print(locals())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
