import arxiv
import json 
import matplotlib.pyplot as plt
from tqdm import tqdm 

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def arxiv_filter(): 
    data_list = []
    with open('arxiv-abstracts.jsonl', 'r', encoding="utf-8") as f: 
        for line in f: 
            item = {}
            data = json.loads(line) 
            # print(data) 
            if 'cs.AI' in data['categories'][0]:
                # category_list.append(data['categories'])
                item['id'] = data['id']
                item['categories'] = data['categories'] 
                item['title'] = data['title'] 
                data_list.append(item) 

    print(len(data_list)) 
    with open('arxiv-filter.json', 'w') as f:
        json.dump(data_list, f, indent=4)


def arxiv_download():
    with open('arxiv-filter.json', 'r') as f: 
        data_list = json.load(f) 
    
    id = 10000
    for data in tqdm(data_list[10000:]): 
        try:
            paper = next(arxiv.Search(id_list=[data["id"]]).results())
            paper.download_source(dirpath="./data", filename= str(id) + ".tar.gz")
            id += 1
        except:
            print(data["id"])

arxiv_download() 