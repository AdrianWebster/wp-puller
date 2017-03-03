from bs4 import BeautifulSoup as bs
import requests
import pickle
import sys

#set recurison limit high for pickle
sys.setrecursionlimit(10000)

def main(postlist):
    '''
    pulls the html from each link in postlist into an array of dictionaries.
    array -> array(dict)
    '''
    list=[]
    for page in postlist:
        soup = get_soup(page)
        temp = parse(soup,page)
        list.append(temp)
    return list

def get_soup(site):
    '''
    Helper function to get the html from sites
    string -> soup
    '''

    res = requests.get(site)
    return bs(res.text, "html.parser")


def parse(soup,page):
    '''
    Turns the soup of a page into a dictionary,
    soup , string -> dict
    '''

    temp = {'url':page , 'title':soup.h1 ,
            'tags':soup.find_all('div',{'class':'entry-meta'}),
            'content' : soup.find_all('p')
            }
    return temp


postlist = ['http://web.archive.org/web/20161019165435/http://ottawaartsreview.com/literature-and-overcoming-book-biases/','http://web.archive.org/web/20161028092509/http://ottawaartsreview.com/calling-all-artists-enter-our-cover-contest/','http://web.archive.org/web/20161019163059/http://ottawaartsreview.com/interview-obi-simic/','http://web.archive.org/web/20161028083719/http://ottawaartsreview.com/black-words-matter-recap/','http://web.archive.org/web/20161028084339/http://ottawaartsreview.com/black-words-matter/','http://web.archive.org/web/20161028082453/http://ottawaartsreview.com/art-for-aid/','http://web.archive.org/web/20161028141613/http://ottawaartsreview.com/lost-and-found-rewriting-found-poetry/','http://web.archive.org/web/20161028080326/http://ottawaartsreview.com/blue-mondays-september-edition-draws-a-crowd/','http://web.archive.org/web/20161028081217/http://ottawaartsreview.com/blue-monday-reading-series-begins-again/','http://web.archive.org/web/20161028095533/http://ottawaartsreview.com/on-summer-reading/','http://web.archive.org/web/20161028095533/http://ottawaartsreview.com/on-summer-reading/',
           'http://web.archive.org/web/20160318023714/http://ottawaartsreview.com/rejection-means/','http://web.archive.org/web/20160318092356/http://ottawaartsreview.com/happens-submission/','http://web.archive.org/web/20160318024557/http://ottawaartsreview.com/postscripts-postscripts-darkness/','http://web.archive.org/web/20160505044938/http://ottawaartsreview.com/issue-launch-black-squirrel-books-ottawa-arts-review/','http://web.archive.org/web/20160505092616/http://ottawaartsreview.com/upcoming-issue-launch-throwback-7-1/']

data=main(postlist)

#dumps the parsed data into a pickle
pickle.dump( data, open( "englishHtml.p", "wb" ))

a=data[5]
print(a['url'])
print('---'*50)
print(a['content'])
