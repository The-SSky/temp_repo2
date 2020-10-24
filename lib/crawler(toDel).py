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
    def __init__(self, path, pos=1, step=1):
        self.url = 'https://torgi.gov.ru/lotSearch1.html?bidKindId=8'
        self.driver = webdriver.Chrome(path)
        self.starting_page = pos
        self.step = step
        self.last_page = pos

    @times_failed_counter
    def click_active_sale(self):
        """
        clicks active sales only option
        """
        _xpath = r'/html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div/div/div' \
                    + r'/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/ul/a[1]/div/li'
        self.driver.find_element_by_xpath(_xpath).click()

    @times_failed_counter
    def set_property_type_movable_checkbox(self):
        """
        it clicks on img to pop up the window where property type can be set
        clicks checkbox inside popup window
        """
        self.driver.find_element_by_xpath('//*[@id="id5d"]').click()
        time.sleep(1)
        _name = 'common:propertyTypes:multiSelectPopup:content:panel:container:checkListForm:list:0:selected'
        self.driver.find_element_by_name(_name).click()

    @times_failed_counter
    def click_select_out_property_type(self):
        """
        click "select" btn for leaving property type window
        """
        self.driver.find_element_by_xpath('//*[@id="id8f"]').click()

    @times_failed_counter
    def make_input_for_region(self):
        """
        click on img to pop up the window where region can be set
        sends "samarskay (obl)" to the input line
        """
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="id5e"]').click()
        time.sleep(1)
        self.driver.find_element_by_name("container1:level1").send_keys('Самарская (обл)')

    @times_failed_counter
    def click_select_out_region(self):
        """
        click "select" btn for leaving region window
        """
        self.driver.find_element_by_xpath('//*[@id="id9a"]').click()

    @times_failed_counter
    def click_russia(self):
        """
        it sets country on "russia"
        """
        self.driver.find_element_by_xpath('//*[@id="id46"]/option[2]').click()

    @times_failed_counter
    def click_search_btn(self):
        """
        subj
        """
        self.driver.find_element_by_xpath('//*[@id="id63"]').click()

    @times_failed_counter
    def wait_untill_page_is_loaded(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[6]/p/a')

    @times_failed_counter
    def click_next(self):
        self.driver.find_element_by_xpath('//*[@id="id39"]').click()

    def start(self):
        # переходим по ссылке
        self.driver.get(self.url)

        # выбираем активные продажи
        self.click_active_sale()
        time.sleep(4)

        # выбираем машины
        self.set_property_type_movable_checkbox()
        time.sleep(1)
        self.click_select_out_property_type()
        time.sleep(1)

        # выбираем россию
        self.click_russia()
        time.sleep(1)

        # выбираем самарскую обл
        self.make_input_for_region()
        time.sleep(1)        
        self.click_select_out_region()
        time.sleep(1)

        # нажимаем кнопку поиск
        self.click_search_btn()

        # driver.find_element_by_xpath('//*[@id="id38"]/span').text

    def start2(self):
        self.driver.get(self.url)
        self.wait_untill_page_is_loaded()

        print('Введите общее количество страниц')
        self.last_page = input()

        _folder = sys.argv[0][:sys.argv[0].rfind('\\')] + '\\' + 'data' + '\\'
        for i in range(self.last_page - 1):
            with open(f'{_folder}{i:05d}.htm', 'w', encoding='utf-8') as f:
                f.write(self.driver.page_source)
            
            self.click_next()
            self.wait_untill_page_is_loaded()
            


