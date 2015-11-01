__author__ = 'wsf'
url = 'http://www.dianping.com/search/category/1/10/r839#nav-tab|0|0'
import urllib2
import re
import os
from bs4 import BeautifulSoup

current_dir=os.curdir
if not os.path.exists('parsing_result'):
 os.mkdir('parsing_result')
 os.makedirs('parsing_result'+os.sep+'html')
print os.curdir

def write_html(_data,i):#save webpage
    with open(current_dir+os.sep+'parsing_result'+os.sep+'html'+os.sep+str(i)+"_th_page.txt", "ab") as f:
     f.write(_data)



def get_pagecontent(url,i=1):#get html webpage
  headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
  request = urllib2.Request(url,headers = headers)
  response = urllib2.urlopen(request).read()
  write_html(response,i)
  print "Writing "+str(i)+" th webpage!"
  pattern_next=re.compile('<a href="(\S+)" \S+ \S+ class="next')
  next_page=re.findall(pattern_next,response)
  if len(next_page)==1:
        get_pagecontent('http://www.dianping.com'+next_page[0],i+1)






def parsing_dazhong(file_path):#extract useful info from html file
 result=[]
 html_doc2=open(file_path).read()
 soup = BeautifulSoup(html_doc2,"lxml")
 if len(soup.find_all('li',{"class":""})):
  for each in soup.find_all('li',{"class":""}):
     if len(each.find_all('div',{"class":"comment"})):
        temp=[]
        if each.find('h4'):
         name=each.find('h4').text
         temp.append(name)
        else:
         temp.append('-1')
        if each.find('div',{"class","tag-addr"}):
         if each.find('div',{"class","tag-addr"}).find("span",{"class":"addr"}):
           address=each.find('div',{"class","tag-addr"}).find("span",{"class":"addr"}).text
           temp.append(address)
         else:
           temp.append('-1')
         if each.find('div',{"class","tag-addr"}).find_all("a"):
           tag=each.find('div',{"class","tag-addr"}).find_all("a")[0].text
           temp.append(tag)
         else:
           temp.append('-1')
        else:
            temp.append('-1')
            temp.append('-1')
        if each.find('a',{"class","mean-price"}).find("b"):
         mean_price=each.find('a',{"class","mean-price"}).find("b").text
         temp.append(mean_price)
        else:
         temp.append('-1')
        if each.find('span',{"class","comment-list"}):
         taste_rank=each.find('span',{"class","comment-list"}).text[3:6]
         temp.append(taste_rank)
         env_rank=each.find('span',{"class","comment-list"}).text[9:12]
         temp.append(env_rank)
         serv_rank=each.find('span',{"class","comment-list"}).text[15:19]
         temp.append(serv_rank)
        else:
         temp.append('-1')
         temp.append('-1')
         temp.append('-1'+os.linesep)
        result.append(temp)
  return result
 else:

  return 0



def write_result(result,save_path,save_mode='ab'):
 with open(save_path, 'ab') as f:
    for row in result:
        for item in row:
           f.write("%s " %unicode(item).encode("utf-8"))






def save_parsing_result():
 for root,dirs,files in os.walk(os.curdir+os.sep+'parsing_result'+os.sep+'html'):
    for file in files:
       file_path=root+os.sep+file
       print "Paring No."+file.split('_')[0]+" web page !"
       result=parsing_dazhong(file_path)
       if result:
           write_result(result,current_dir+os.sep+'parsing_result'+os.sep+'parsed_result.txt')
       else:
           print "-------------------------Warning--------------------------"
           print "Paring No."+file.split('_')[0]+" failed !"
           print os.linesep


def dazhong_spider(url,i=1):
    print "Begin working.............."
    #get_pagecontent(url,i)
    save_parsing_result()
    print 'Result is saved in "currentpath/parsing_result"'
    print "Done!"

i=1
#....................................You only need to modify bleow..............................................#
dazhong_spider( 'https://www.dianping.com/search/category/1/10/r865#nav-tab|0|0',1)

