import csv
from itertools import groupby
from operator import itemgetter

def print_counts():
    with open('school_data.csv') as f:
        reader = csv.reader(f, skipinitialspace=True)
        header = next(reader)
        data = [dict(zip(header, map(str, row))) for row in reader]
    schools_list = [d["SCHNAM05"] for d in data]
    school_count = len(set(schools_list))
    print(f"Total Schools: {school_count}")
    print("Schools by State:")
    for key, value in groupby(data,key=itemgetter('LSTATE05')):
        print(f"{key} : {len(list(value))}")
    print("Schools by Metro-centric locale:")
    for key, value in groupby(data, key=itemgetter('MLOCALE')):
        print(f"{key} : {len(list(value))}")
    city_with_most_schools = [{'city':key,'count':len(list(value))} for key, value in groupby(data, key=itemgetter('LCITY05'))]
    city_with_max_school = max(city_with_most_schools, key=lambda x:x['count'])
    print(f"City with most schools: : {city_with_max_school['city']} ({city_with_max_school['count']} school(s))")
    unique_schools_with_atleast_one_school = list(filter(lambda x: int(x['count'])>0, city_with_most_schools))
    print(f"Unique cities with at least one school: {len(unique_schools_with_atleast_one_school)}")


if __name__ == '__main__':
    print_counts()
