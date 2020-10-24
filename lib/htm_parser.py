from bs4 import BeautifulSoup
import sys
import os

def find_out_saved_htms():
    """
    возращает список файлов с расширением htm в папке data
    """
    _folder = _folder = sys.argv[0][:sys.argv[0].rfind('\\')] + '\\' + 'data'
    return [name for name in os.listdir(_folder) if name.rfind('.htm')]

def parse_htm_page(path):
    """
    Открывает htm страничку и парсит ее, возращает кортеж из заголовка и массива строк тпблицы
    """
    with open(r"D:\py\torgi\data\00001.htm", 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')
    
    soup = soup.findAll('table', {'class': 'list'})[0]

    _header = soup.find('thead')

    # будем сохранять в этот список заголовки из таблицы(у столбца ссылок на лот нет заголовка, добавим)
    parsed_headers = ["Подробнее"]
    for line in _header.findAll('th'):
        line = line.text.strip()
        
        if len(line) > 3 and line not in parsed_headers:
            # теперь добавлены 6 загоовков из шапки
            parsed_headers.append(line)

    # найдем таблицу без шапки
    _tbody = soup.findAll('tbody')[-1]
    # создадим из нее массив строк
    rows = _tbody.findAll('tr')

    parsed_rows = list()
    for row in rows:
        parsed_row = list()
        cells = row.findAll('td')
        parsed_row.append(cells[0].findAll('a')[1]['href'])
        
        for cell in cells[1:]:
            parsed_row.append(cell.text.strip())
        
        parsed_rows.append(parsed_row)

    return parsed_headers, parsed_rows
