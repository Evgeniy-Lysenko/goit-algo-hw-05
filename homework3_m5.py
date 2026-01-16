# read log file
import sys
from pathlib import Path
import re
from colorama import init,  Fore, Style
init(strip=False, convert=False)

def load_logs(path: str) -> list:
    logs = []
    try:
        with open(path, "r", encoding='utf-8') as fh:
            for line in fh:
                log_entry = parse_log_line(line)
                logs.append(log_entry)
    except UnicodeDecodeError:
        print(f"Файл не в форматі UTF-8: {path}")
    except OSError as e:
        print(f"Error reading file {path}: {e}")
    else:
        for log in logs:
            print(log)
    return logs

def parse_log_line(line: str) -> dict:
    parts = re.split(r"[\s|;,]+", line.strip(), maxsplit=3)
    if len(parts) != 4:
        raise ValueError(f"Невірний формат рядка: {line}")
    date, timestamp, log_level, message = parts
    return {"date": date, "timestamp": timestamp, "log_level": log_level, "message": message}

def main(): # main function to handle input and exceptions
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Вкажіть шлях до логфайлу як аргумент командного рядка")
        return
    if len(sys.argv) > 3:
        print(sys.argv)
        print("Занадто багато аргументів.")
        return
    
    path_to_log = Path(sys.argv[1]) # get path from command line argument
    
    if not path_to_log.exists(): # check if path exists
        print("Файл не знайдено")
        return

    if not path_to_log.is_file(): # check if path is a directory
        print("Шлях не є файлом")
        return
    
    # if sys.argv[2] is not None: # check if second argument exists
    #     log_level_filter = sys.argv[2].upper()
    #     if log_level_filter not in ["DEBUG", "INFO", "WARNING", "ERROR"]:
    #         print("Невірний рівень логів")
    #         return
           
     
    
    print(f"{Fore.RED}{path_to_log}/{Style.RESET_ALL}")
    load_logs(path_to_log)    


if __name__ == "__main__":
    main()