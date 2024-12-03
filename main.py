import csv
import os
from tqdm import tqdm

TI = 'TI' #title
DE = 'DE' #keywords
AB = 'AB' #abstract
WC = 'WC' #WoS category
#SC = 'SC' #subject category

search_target = [
    'environmental studies',
    'urban studies',
    'geography',
    'regional & urban planning',
    'development studies',
    'economics',
    'regional and urban planning',
    'business management',

    'political science',
    'mining and mineral processing',
    'international relations',

    'computer science, artificial intelligence',
    'computer science, information systems',
    'computer Science, interdisciplinary applications'
]

def process_change_record(file_path):
    results = []

    cur_TI = ''
    cur_DE = ''
    cur_AB = ''
    cur_WC = ''
    #cur_SC = ''

    with open(file_path, 'r', encoding='ascii', errors='ignore') as file:

        for line in file:
            processed = False
            space_index = line.find(' ')
            if(space_index!=-1):
                first_part = line[:space_index]  # Filter the content before the first space
                #second_part = line[space_index+1:]
                if(first_part == TI):
                    cur_TI = line
                elif(first_part == DE):
                    cur_DE = line
                elif(first_part == AB):
                    cur_AB = line
                elif(first_part == WC):
                    cur_WC = line

                    cur_WC_splited_list = cur_WC.split('; ')


                    for cur_WC_splited in cur_WC_splited_list:
                        if(cur_WC_splited.lower() in search_target):
                            processed = True
                            break
            
            if(processed):
                results.extend([cur_TI, cur_DE, cur_AB, cur_WC, '\n'])
    
    return results

if __name__ == "__main__":
    base_path = './data'
    out_file_path = './out.txt'

    files = [os.path.join(base_path, file) for file in os.listdir(base_path) if os.path.isfile(os.path.join(base_path, file))]
    print(files)

    results = []

    for file in files:
        result = process_change_record(file)
        results.extend(result)

    with open(out_file_path, 'w', encoding='utf-8') as file:
        for item in results:
            file.write(item)
