from urllib import request
from bs4 import BeautifulSoup

def get_arxiv(url_str):
    # 検索して取ってきます
    return BeautifulSoup(request.urlopen(url=url_str).read(), "html.parser")

def search_maker(search_dict):
    # 辞書型を渡せば検索URLを吐きます
    # search_dict = {'ti':'xxx', 'abs':'yyy', ...}
    base_url = 'http://export.arxiv.org/api/query?search_query='
    out_url = base_url
    if len(search_dict) >= 2:
        for k, v in search_dict.items():
            if out_url != base_url:
                out_url += '&'
            out_url += k + ':' + v
    else:
        for k, v in search_dict.items():
            out_url += k + ':' + v
    
    return out_url

def data_dict_maker(datas, use_datas=['title', 'published', 'link']):
    data_dict = dict()
    for i in datas.find_all('title'):
        data_dict['title'] = i

def sort_of_date(json_datas):
    for out in data.find_all(''):
        return ''

if __name__ == '__main__':
    search_dict = {'abs':'generative', 'cat':'Computer Science'}
    url = search_maker(search_dict)
    data = get_arxiv(url)
    #print(data)
    #data_json_maker(data)
    for out in data.find_all('link', attrs={'title':'pdf'}):
        print(out)