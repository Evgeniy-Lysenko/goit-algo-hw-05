# read log file
import sys
from pathlib import Path
import re
from colorama import init,  Fore, Style
init(strip=False, convert=False)
from collections import Counter

def load_logs(path: str) -> list: # load logs from file
    logs = []
    try:
        with open(path, "r", encoding='utf-8') as fh: # open file with utf-8 encoding
            for line in fh:
                log_entry = parse_log_line(line) # parse each line
                logs.append(log_entry)
    except UnicodeDecodeError:
        print(f"Файл не в форматі UTF-8: {path}")
    except OSError as e:
        print(f"Error reading file {path}: {e}")
    return logs

def display_log_counts(count_level: dict): # display the log counts
    print(f"{'Рівень логування':<16} | {'Кількість':>9}")
    print("-" * 28)
  
    for level, count in count_level.items():
        color = Fore.LIGHTMAGENTA_EX if level == "ERROR" else ""
        reset = Style.RESET_ALL if color else ""
        print(f"{color}{level:<16}{reset} | {count:>9}")
    

def parse_log_line(line: str) -> dict: # parse a single log line
    parts = re.split(r"[\s|;,]+", line.strip(), maxsplit=3) # split the line into date, timestamp, log level and message
    date = parts[0]
    timestamp = parts[1]
    log_level = parts[2]
    message = parts[3] if len(parts) > 3 else "" # handle case where message may be missing
    return {"date": date, "timestamp": timestamp, "log_level": log_level, "message": message}
    
def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = [log for log in logs if log["log_level"].upper() == level]
    return filtered_logs
    

def count_logs_by_level(logs: list) -> dict:
    log_levels = [log["log_level"] for log in logs]
    count_level = Counter(log_levels)
    return count_level
   

def main(): # main function to handle input and exceptions
    if len(sys.argv) < 2:
        print("Вкажіть шлях до логфайлу як аргумент командного рядка")
        return
    if len(sys.argv) > 3:
        print(sys.argv)
        print("Занадто багато аргументів.")
        return
    
    path_to_log = Path(sys.argv[1]) # get path from command line argument
    level = sys.argv[2].upper() if len(sys.argv) > 2 else None
    
    if not path_to_log.exists(): # check if path exists
        print("Файл не знайдено")
        return

    if not path_to_log.is_file(): # check if path is a directory
        print("Шлях не є файлом")
        return
    
    if len(sys.argv) > 2: # check if second argument exists
        if sys.argv[2].upper() not in ["DEBUG", "INFO", "WARNING", "ERROR"]:
            print("Невірний рівень логів")
            return
          
    
    print(f"{Fore.RED}{sys.argv[1]}/{Style.RESET_ALL}")
    logs = load_logs(path_to_log)
    counts = count_logs_by_level(logs)

    display_log_counts(counts)

    if level:
        filtered = filter_logs_by_level(logs, level)
        print(f"{Fore.GREEN}Деталі логів для рівня {level}:{Style.RESET_ALL}")
        for log in filtered:
            print(log)

if __name__ == "__main__":
    main()