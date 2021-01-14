import pandas
import numpy

def listing (x, list1, list2):
    if (x in list1):
        return 1
    if (x in list2):
        return 2
    return 3

def preprocessing (x):
    x = x.replace('-', '')
    x = x.replace('&amp;amp;', '')
    x = x.strip()
    return x

if __name__ == '__main__':
    # reading contents
    users = pandas.read_csv('users.csv', names=['id', 'name', 'username'])
    with open('list_1.txt', 'r') as file:
        list1 = file.read().split('\n')
    with open('list_2.txt', 'r') as file:
        list2 = file.read().split('\n')
        
    # pre processing
    users['name'] = users['name'].apply(lambda x: preprocessing(x))
    users['name'].replace('', numpy.nan, inplace=True)
    users.dropna(subset=['name'], inplace=True)
    
    users['username'] = users['username'].apply(lambda x: preprocessing(x))
    users['username'].replace('', numpy.nan, inplace=True)
    users.dropna(subset=['username'], inplace=True)
    
    users['rank'] = users['id'].apply(lambda x: listing(x, list1, list2))
    
    # sorting
    users.sort_values(['name', 'rank'], ascending=[True, True], inplace=True)
    
    # saving
    users.drop('rank', 1, inplace=True)
    users.to_csv('users_new.csv', header=False, index=False)