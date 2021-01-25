"""

Date: 1/10/2021
Author: Edlee Ducay

Modified version of the old baby names main function file
that works with the demo web-app

"""
import fnmatch

def print_top_ten(topTen_dict, gender, year):
    '''
    (Command 4)
    This function prints the top ten list for 
    a certain gender and certain year (Command 4)

    Parameters:
    dictionary
        the top ten dictionary
    Returns:
        none
        
    '''

    if gender == 'b':
        gender = 'boys'
    else:
        gender = 'girls'

    if year not in topTen_dict[gender]:
        return None
        
    data = []
    for i in range(len(topTen_dict[gender][year])):
        name = topTen_dict[gender][year].pop(0)
        data.append({'rank': name[0],
            'name': name[1],
            'frequency': name[2]})
    
    return data

def names_search(names_dict, name):
    ''' 
    (Command 5)
    This function prints the frequencies of boys and girls given the name

    Parameters:
    dictionary
        the names dictionary
    Returns:
        none
    
    '''
    
    if name not in names_dict:
        print(f'There were no babies named {name} born in Alberta between 1980 and 2017')          
        return None
    
    data = []
    name = names_dict[name]
    for year in range(1980,2018):
        freq_b = 0
        freq_g = 0
        for info in name:
            if year in info and 'Boy' in info:
                freq_b = info[0]
            elif year in info and 'Girl' in info:
                freq_g = info[0]
        if freq_b == 0 and freq_g == 0:
            None
        else:
            data.append({'year': year,
            'freq_boy': freq_b,
            'freq_girl': freq_g})

    return data

def get_unique_names(names_dict, year):
    '''
    (Command 6)
    This function displays all names with a frequency of 1 for a specified year

    Parameters:
    dictionary
        the names dicitonary
    Returns:
    none
    
    '''
     
    boynames_list = []
    girlnames_list = []
    
    # Finding the names with frequency of 1
    for name, years in names_dict.items():
        for info in years:
            if year == info[2] and info[0] == 1 and info[1] == 'Girl':
                girlnames_list.append(name)
            elif year == info[2] and info[0] == 1 and info[1] == 'Boy':
                boynames_list.append(name)
    girlnames_list = sorted(girlnames_list)
    boynames_list = sorted(boynames_list)
    
    return boynames_list, girlnames_list
    girlsData = []
    boysData = []
    
    # Displaying the names with frequency of 1
    names = [girlnames_list[i:i+4] for i in range(0, len(girlnames_list), 4)]
    width = max(len(name) for row in names for name in row) + 2
    print(names)
    for row in names:
        girlsData.append({'col1': row[0],
        "col2": row[1],
        "col3": row[2],
        "col4": row[3]})
    
    names = [boynames_list[i:i+4] for i in range(0, len(boynames_list), 4)]
    width = max(len(name) for row in names for name in row) + 2
    for row in names:
        boysData.append({'col1': row[0],
        "col2": row[1],
        "col3": row[2],
        "col4": row[3]})

    return boysData, girlsData

def longest_names(names_dict):
    '''
    (Command 7)
    This function finds and displays the longest hyphenated & unhyphenated names

    Parameters:
    dictionary
        the names dicitonary
    Returns
    none
     
    '''
    
    # Finding the longest names
    gh_name = ''
    guh_name = ''
    bh_name = ''
    buh_name = ''
    data = [(),(),(),()]

    for name, years in names_dict.items():
        for info in years:
            if '-' in name and len(name) > len(gh_name) and info[1] == 'Girl':
                data[0] = (name, info[2])
            elif '-' not in name and len(name) > len(guh_name) and info[1] == 'Girl':
                data[1] = (name, info[2])
            elif '-' in name and len(name) > len(bh_name) and info[1] == 'Boy':
                data[2] = (name, info[2])
            elif '-' not in name and len(name) > len(buh_name) and info[1] == 'Boy':
                data[3] = (name, info[2])
    
    return data

def wildcard_search(names_dict, user_name):
    '''
    (Command 8)
    This function finds names that have what is inputted + any missing letters
    
    Parameters:
    dicitonary
        the names dictionary
    Returns:
    none
    
    '''
    
    has_name = False
    data = []

    # Looking for matching names and displaying if found
    for name, years in names_dict.items():
        if fnmatch.fnmatch(name, user_name) == True:
            has_name = True
            name_list = [name, []]        
            for year in range(1980,2018):
                freq_b = 0
                freq_g = 0    
                for info in years:
                    if 'Boy' in info and year in info:
                        freq_b = info[0]
                    elif 'Girl' in info and year in info:
                        freq_g = info[0]
                if freq_b == 0 and freq_g == 0:
                    None
                else:
                    name_list[1].append({'year': year,
                        'freq_boys': freq_b,
                        'freq_girls': freq_g})

            data.append(name_list)
                    
    return data