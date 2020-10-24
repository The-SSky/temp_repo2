from lib.crawler import TorgiCrawler
from lib.htm_parser import find_out_saved_htms, parse_htm_page

if __name__ == "__main__":
    # путь к драйверу селениум
    PATH = r'D:\chrome_parsing\chromedriver.exe'

    # создание и запуск обходчика
    unit = TorgiCrawler(PATH)
    unit.start(timer=3)

    # демонстрация работы парсера
    htms = find_out_saved_htms()
    parsed = parse_htm_page(htms[0])
    print(parsed[0], *parsed[1], sep='\n\n----------\n\n')

    input()