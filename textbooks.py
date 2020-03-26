from bs4 import BeautifulSoup
import bs4
import requests
import wget

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillPdfList(bkName, bkUrl, html):
    soup = BeautifulSoup(html, "html.parser")
    for div in soup.find("div", id="container").children:
        if isinstance(div, bs4.element.Tag) and div.attrs['class'] == ["con_list_jcdzs2020"]:
            for ul in div.children:
                if isinstance(ul, bs4.element.Tag) and ul.attrs['class'] == ["clearfix"]:
                    for li in ul.children:
                        if isinstance(li, bs4.element.Tag):
                            names = li('h6')
                            links = li('a', title="下载")
                            for i in names:
                                bkName.append(i.string)
                            for i in links:
                                bkUrl.append("http://bp.pep.com.cn/jc/ptgzkcbzsyjks"+i.attrs['href'][1:])


def downloadPdf(bkName, bkUrl):
    for i in range(0, len(bkName)):
        url = bkUrl[i]
        print(i)
        print('\n')
        print(bkName[i])
        wget.download(url, bkName[i]+".pdf")

def main():
    bkName = []
    bkUrl = []
    url = 'http://bp.pep.com.cn/jc/ptgzkcbzsyjks/'
    html = getHTMLText(url)
    fillPdfList(bkName, bkUrl, html)
    downloadPdf(bkName, bkUrl)
main()
