#!/usr/bin/env python
import click
from bs4 import BeautifulSoup
from urllib.request import urlopen
@click.command()
@click.option("--name", prompt='Your Name')

def hello(name):
    click.echo(f'Hello {name}!! Here is the current Sports Headlines from NYPost\n')
    url='https://nypost.com/sports/'
    ihtml=urlopen(url)
    isoup = BeautifulSoup(ihtml,"html.parser")
    ispan=isoup.find("div", {"class" : "content-area section-content sports-content left-column landing-page desktop"}).find("div", {"class" : "site-content box"})
    ispan1=ispan.find("div",{"class":"sports-latest sports-latest-desktop"})
    ispan2=ispan1.find_all("div",{"class":"entry-header"})

    titles=[]
    for i in ispan2:    
        titles.append(i.text.strip())
    
    for a in range(len(titles)):
        pos=titles[a].find('\n')
        titles[a]=titles[a][:pos]
    count=1    
    for t in titles:
        
        click.echo(str(count)+". "+t)
        count+=1
    
if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    hello()