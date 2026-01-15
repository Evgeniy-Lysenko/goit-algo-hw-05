# read log file
import sys
from pathlib import Path
from colorama import init,  Fore, Style
init(strip=False, convert=False)


def main(): # main function to handle input and exceptions
    if len(sys.argv) < 2:
        print("Вкажіть шлях до логфайлу як аргумент командного рядка")
        return

    path_to_log = Path(sys.argv[1]) # get path from command line argument

    if not path_to_log.exists(): # check if path exists
        print("Директорія не знайдена")
        return

    if not path_to_log.is_file(): # check if path is a directory
        print("Шлях не є файлом")
        return
    print(f"{Fore.RED}{path_to_log}/")
    

if __name__ == "__main__":
    main()