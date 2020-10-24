from bs4 import BeautifulSoup

def main():
    with open(r"D:\py\torgi\data\10.13.xml", 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml-xml')
        positions = soup.findAll('notification')
        for position in positions:
            print(position.find('bidKindName').text)
            print(position.find('bidNumber').text)
            print(position.find('organizationName').text)
            print(position.find('isArchived').text)
            print('---------')


        