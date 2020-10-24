import requests
import sys

def get_data_to_disk(publishDateFrom, publishDateTo, filename):
    _ = 'http://torgi.gov.ru/opendata/7710349494-torgi/data-8-'
    data_url = _ + f'{publishDateFrom}-{publishDateTo}-structure-20130401T0000.xml'
    print(data_url)
    data = requests.get(data_url)

    _folder = sys.argv[0][:sys.argv[0].rfind('\\')] + '\\' + 'data' + '\\'
    path = _folder + filename
    with open(path, 'wb') as f:
        f.write(data.content)
    return path

# 'http://torgi.gov.ru/opendata/7710349494-torgi/data.xml?bidKind={bidKind}&publishDateFrom={publishDateFrom}&publishDateTo={publishDateTo}&lastChangeFrom={lastChangeFrom}&lastChangeTo={lastChangeTo}'
# 'http://torgi.gov.ru/opendata/7710349494-torgi/data-{bidKind}-{publishDateFrom}-{publishDateTo}-structure-20130401T0000.xml'
# 'http://torgi.gov.ru/opendata/7710349494-torgi/data-{publishDateFrom}-{publishDateTo}-structure-20130401T0000.xml'
# 'http://torgi.gov.ru/opendata/7710349494-torgi/data-{publishDateTo}-structure-20130401T0000.xml'

# bidKind = '8'
# publishDateFrom = '20201012T0000'
# publishDateTo = '20201018T0000'
# lastChangeFrom = '20150101T0000'
# lastChangeTo = '20150101T0000'

# _ = f'http://torgi.gov.ru/opendata/7710349494-torgi/data.xml?bidKind={bidKind}'
# _ = _ + f'&publishDateFrom={publishDateFrom}&publishDateTo={publishDateTo}&lastChangeFrom'
# s1 = _ + f'={lastChangeFrom}&lastChangeTo={lastChangeTo}'

# s2 = f'http://torgi.gov.ru/opendata/7710349494-torgi/data-{bidKind}-{publishDateFrom}-{publishDateTo}-structure-20130401T0000.xml'
# s3 = f'http://torgi.gov.ru/opendata/7710349494-torgi/data-{publishDateFrom}-{publishDateTo}-structure-20130401T0000.xml'
# s4 = f'http://torgi.gov.ru/opendata/7710349494-torgi/data-{publishDateTo}-structure-20130401T0000.xml'
# print(s2)

# 'http://torgi.gov.ru/opendata/7710349494-torgi/data-20201008T0000-20201022T0000-structure-20130401T0000.xml'