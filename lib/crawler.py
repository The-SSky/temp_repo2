from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import sys


def times_failed_counter(func):
    time.sleep(1)
    def wrapper(self, times_failed=0):
        try:
            func(self)
        except:
            if times_failed > 20: sys.exit(404)
            time.sleep(1)
            times_failed += 1
            wrapper(self, times_failed)
    return wrapper

class TorgiCrawler():
    """
    for opening torgi.gov.ru, filling form, stepping over content
    """
    def __init__(self, path, pos=1):
        self.url = 'https://torgi.gov.ru/lotSearch1.html?bidKindId=8'
        self.driver = webdriver.Chrome(path)
        self.starting_page = pos
        self.last_page = pos

    @times_failed_counter
    def wait_untill_page_is_loaded(self):
        """
        """
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[6]/p/a')

    @times_failed_counter
    def click_next(self):
        """
        """
        self.driver.find_element_by_xpath("//a[@title='Перейти на одну страницу вперед']").click()

    def start(self, timer=3):
        """
        Открывается хром, настраиваем и нажимаем поиск, вводим число получившихся страниц
        потом скрипт продолжает работу, обходя и сохраняя каждую страницу в папку data
        """
        self.driver.get(self.url)
        self.wait_untill_page_is_loaded()

        print('Введите общее количество страниц')
        self.last_page = int(input())

        _folder = sys.argv[0][:sys.argv[0].rfind('\\')] + '\\' + 'data' + '\\'
        for i in range(1, self.last_page + 1):
            with open(f'{_folder}{i:05d}.htm', 'w', encoding='utf-8') as f:
                f.write(self.driver.page_source)
            
            if i == self.last_page: break

            self.click_next()
            time.sleep(timer)
            self.wait_untill_page_is_loaded()

            


