import csv,time
import operator

def search_schools(searchtext):
    search_list = searchtext.split()
    start_time = time.time()
    with open('school_data.csv') as f:
        reader = csv.reader(f, skipinitialspace=True)
        header = next(reader)
        data = [dict(zip(header, map(str, row))) for row in reader]

    data = [{'school':item['SCHNAM05'], 'city':item['LCITY05'], 'state':item['LSTATE05'],'found':0} for item in data]

    results = []
    for item in data:
        for x in search_list:
            if x.upper() in item['school'].upper() or x.upper() in item['state'].upper() or x.upper() in item['city'].upper():
                item['found']= int(item['found'])+1
        if int(item['found'])>0:
            results.append(item)

    results.sort(key=operator.itemgetter('found'),reverse=True)
    end_time = time.time()
    delta = end_time - start_time
    print(f'Results for "{searchtext}" (search took: {delta * 1000} ms)')
    for index,res in enumerate(results):
        if index>2:
            break
        print(f"{index+1}. {res['school']}")
        print(f"   {res['city']}, {res['state']}")



if __name__ == '__main__':
    search_schools("elementary school highland park")
    search_schools("jefferson belleville")
    search_schools("riverside school 44")
    search_schools("granada charter school")
    search_schools("foley high alabama")
    search_schools("KUSKOKWIM")