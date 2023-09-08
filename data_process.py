import os 
import tarfile
from tqdm import tqdm 

def extract_zip(zip_data_path):
    for file_name in tqdm(os.listdir(zip_data_path)): 
        file_path = os.path.join(zip_data_path, file_name) 
        target_file = file_name.split('.')[0]
        try:
            t = tarfile.open(file_path)
            t.extractall(os.path.join('unzip_data', target_file))
        except:
            print(file_path)


def arxiv_statics(unzip_data_path): 
    num = 0
    for file_name in os.listdir(unzip_data_path): 
        file_path = os.path.join(unzip_data_path, file_name) 
        if '.DS' in file_path:
            continue 
        for f in os.listdir(file_path): 
            if '.tex' in f: 
                num += 1
                break
    print(num)



data_path = 'data' 
unzip_data_path = 'unzip_data'
# extract_zip(data_path)
arxiv_statics(unzip_data_path)