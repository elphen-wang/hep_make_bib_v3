# -*- coding: utf-8 -*
import numpy as np
import random as rdm
import urllib.request
import requests
import json
import re
import os

def get_record(url):
    resp = urllib.request.urlopen(url)
    ele_json = json.loads(resp.read())
    return ele_json
 
print("Please input your keyword...");
keyword=input();
#keyword="JUNO+PRD+neutrino+2020";
#keyword="JUNO + IceCube +2019+ 1911.06745"
#keyword="JUNO+PRD+1609.07403"
#keyword="JUNO + IceCube +2020+1908.07249"
#keyword="IceCube+2002.00997"
#keyword="1911.06745"
#keyword="The Reactor Neutrino Energy Spectrum Measurement with a High Pressure Gas TPC Detector"
print("Your are searching: ",keyword);
keyword=urllib.parse.quote_plus(keyword);

search_what="literature";# authors, jobs, conferences
sort="mostrecent"; #or mostcited, sort method
size="25"; # maximum number of search results per page.
page_index="1";#  Page index of current search results.

domain_name="https://inspirehep.net/";
my_url=domain_name+"api/"+search_what+"?sort="+sort+"&size="+size+"&page="+page_index+"&q="+keyword;

#inspirehep_json=get_record(my_url)
#print(inspirehep_json)


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
data=requests.get(my_url,headers=headers)
inspirehep_json=json.loads(data.content)
#print(data.content)


total_num=inspirehep_json['hits']['total']
main_body=inspirehep_json['hits']['hits']
print("You got ",len(main_body)," result(s) in the index -",page_index," page. Total: ",total_num," result(s).");
print("\n");

cite=""
article_title=""
doi_title=""
doi_link="";
arXiv_title="";
arXiv_pdf_link="";
arXiv_abs_link="";
title_link="";
collaborations="";
authors="";
newlatex="";
index=0;

for mb in main_body:
  #metadata=mb['metadata'];
  cite=mb['metadata']['texkeys'][0]
  article_title=mb['metadata']['titles'][0]['title']
  title_link=domain_name+search_what+"/"+mb['id'];
  
  if("dois" in mb['metadata']):
    doi_link="https://doi.org/"+mb['metadata']['dois'][0]['value']
  if("arxiv_eprints" in mb['metadata']):
    arXiv_abs_link="https://arxiv.org/abs/"+mb['metadata']['arxiv_eprints'][0]['value'];
    arXiv_pdf_link="https://arxiv.org/pdf/"+mb['metadata']['arxiv_eprints'][0]['value'];
    arXiv_title="[arXiv:"+mb['metadata']['arxiv_eprints'][0]['value'] + "["+mb['metadata']['arxiv_eprints'][0]['categories'][0]+"]]"
    #cite="arXiv:"+mb['metadata']['arxiv_eprints'][0]['value'];//new style cite
  if("publication_info" in mb['metadata']):
    doi_title=(mb['metadata']['publication_info'][0]['journal_title'].replace(".", ".\ ") + "\ \\textbf{"+mb['metadata']['publication_info'][0]['journal_volume']+"}\ ("+str(mb['metadata']['publication_info'][0]['year'])+")\ "+(mb['metadata']['publication_info'][0]['journal_issue']+",\ " if "journal_issue" in mb['metadata']['publication_info'][0] else "")+((mb['metadata']['publication_info'][0]['artid']) if "artid" in mb['metadata']['publication_info'][0] else "" if "page_start" in mb['metadata']['publication_info'][0] else mb['metadata']['publication_info'][0]['page_start'] +"-"+mb['metadata']['publication_info'][0]['page_end'])) if "journal_title" in mb['metadata']['publication_info'][0] else ""
  
  #print(article_title,title_link,doi_link)
  #print(arXiv_title,arXiv_pdf_link,arXiv_abs_link)
  #print(doi_title)
  
  if("collaborations" in mb['metadata']):
    #print(mb['metadata']['collaborations'])
    collaborations_data=[mb['metadata']['collaborations'][i]['value'] for i in range(0,len(mb['metadata']['collaborations']))];
    collaborations="\ ["+",\ ".join(collaborations_data)+"]"
    authors=mb['metadata']['authors'][0]['first_name'][0]+".\ "+mb['metadata']['authors'][0]['last_name']+"\ \\textbf{et\ al.}"
  else:
    authors_data=[mb['metadata']['authors'][i]['first_name'][0]+".\ "+mb['metadata']['authors'][i]['last_name'] for i in range(0,len(mb['metadata']['authors']))];
    authors=",\ ".join(authors_data)
  
  #print(mb['metadata']['publication_info'])
  if("acronyms" in mb['metadata']['publication_info'][0]):#and doi_title==""
    doi_title=mb['metadata']['publication_info'][0]['acronyms'][0]+(",\ "+mb['metadata']['publication_info'][0]['page_start']+"-"+mb['metadata']['publication_info'][0]['page_end']) if "page_start" in mb['metadata']['publication_info'][0] else ""
    #print(doi_title)
  
  #print(collaborations,authors)
  cite_str="%\cite{"+cite+"}"
  bib_str="\\bibitem{"+cite+"}"
  newlatex=cite_str+"\n"+bib_str+"\n"+authors+collaborations+",\n"+"{\it{"+article_title+"}}"
  if(doi_title!=""):
    newlatex+=",\ {\color{blue}\href{"+doi_link+"}{"+doi_title+"}}"
  if(arXiv_title!=""):
    newlatex+=",\ {\color{blue}\href{"+arXiv_abs_link+"}{"+arXiv_title+"}}"
  if(arXiv_title=="" and doi_title==""):
    newlatex+=",\ [\href{"+title_link+"}{\scriptsize IN\\normalsize SPIRE}]";
  else:
    newlatex+="[\href{"+title_link+"}{\scriptsize IN\\normalsize SPIRE}]";
  
  index+=1
  print("Index. ",index,", ---------->title: ",article_title);
  print("\n");
  print(newlatex);
  print("\n");



