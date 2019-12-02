import re
import time


def get_token(json_data):
    lst = re.split(r'},\s{', json_data)
    data_list = []
    for j in lst:
        mass = re.split(r'"(.*?)"', j)
        del mass[0]
        del mass[-1]
        for id, i in enumerate(mass):
            null = re.match(r':\snull,\s', i)
            number = re.match(r':\s\d+,\s', i)
            # find null
            if null:
                mass[id] = None
            # find numerate
            elif number:
                mass[id] = int(re.search(r'\d+', i).group(0))
            else:
                if i[0] in "[{,:}]":
                    del mass[id]
        data_list.append(mass)
    return data_list


def get_dict(tokens):
    data = []
    for mass in tokens:
        lst = [mass[i:i + 2] for i in range(0, len(mass), 2)]
        data.append(dict(lst))
    return data


def transform_list_to_string(data):
    string = ''
    if type(data) == list:
        string = '['
        for i, s in enumerate(data):
            string += transform_list_to_string(s)
            if i == len(data) - 1:
                string += ']'
            else:
                string += ', '
        return string
    elif type(data) == dict:
        string += '{'
        for i, (key, value) in enumerate(data.items()):
            string += f'"{key}": {transform_list_to_string(value)}'
            if i == len(data) - 1:
                string += '}'
            else:
                string += ', '
        return string
    elif type(data) == str:
        return f'"{data}"'
    else:
        return f'{data}'


def merge_lists(first, second):
    merge_dict = first + second
    title = set()
    result_dict = []
    for i in merge_dict:
        if i['title'] not in title:
            title.add(i['title'])
            result_dict.append(i)
    return result_dict


def sorting(dictionary):
    # Replace None for sort
    for value in dictionary:
        if not value['price']:
            value['price'] = 0
        if not value['variety']:
            value['variety'] = 'zzz'

    # Sort by variety
    dictionary.sort(key=lambda x: x['variety'])
    # Sort by price, collisions will be sorted by variety
    dictionary.sort(key=lambda x: x['price'], reverse=True)

    # Return None
    for value in dictionary:
        if not value['price']:
            value['price'] = None
        if value['variety'] == 'zzz':
            value['variety'] = None
    return dictionary


def find_most_expensive_wine(data):
    max_price = 0
    most_expensive_wine = []
    for i, value in enumerate(data):
        if value['price'] and value['price'] > max_price:
            most_expensive_wine = []
            most_expensive_wine.append(value['title'])
            max_price = value['price']
        elif value['price'] and value['price'] == max_price:
            most_expensive_wine.append(value['title'])
    return most_expensive_wine, max_price


def find_cheapest_wine(data):
    min_price = None
    cheapest_wine = []
    for i, value in enumerate(data):
        if not i:
            min_price = value['price']
            cheapest_wine = []
            cheapest_wine.append(value['title'])
        else:
            if not min_price:
                min_price = value['price']
                cheapest_wine = []
                cheapest_wine.append(value['title'])
            elif min_price and value['price'] and value['price'] < min_price:
                min_price = value['price']
                cheapest_wine = []
                cheapest_wine.append(value['title'])
            elif min_price and value['price'] and value['price'] == min_price:
                cheapest_wine.append(value['title'])
    return cheapest_wine, min_price


def find_highest_score(data):
    highest_score = 0
    wines = []
    for i, value in enumerate(data):
        if value['points'] and int(value['points']) > highest_score:
            wines = []
            wines.append(value['title'])
            highest_score = int(value['points'])
        elif value['points'] and int(value['points']) == highest_score:
            wines.append(value['title'])
    return wines, highest_score


def find_lowest_score(data):
    lowest_score = None
    wines = []
    for i, value in enumerate(data):
        if not i:
            lowest_score = value['points']
            wines = []
            wines.append(value['title'])
        else:
            if not lowest_score:
                lowest_score = value['points']
                wines = []
                wines.append(value['title'])
            elif lowest_score and value['points']\
                    and int(value['points']) < int(lowest_score):
                lowest_score = value['points']
                wines = []
                wines.append(value['title'])
            elif lowest_score and value['points']\
                    and int(value['points']) == int(lowest_score):
                wines.append(value['title'])
    return wines, lowest_score


def find_most_active_commentator(data):
    commentators_dict = {}
    for i, value in enumerate(data):
        if value['taster_name'] in commentators_dict:
            commentators_dict[value['taster_name']] += 1
        else:
            if value['taster_name']:
                commentators_dict[value['taster_name']] = 1
    max_comments = 0
    commentators = []
    for key in commentators_dict:
        if commentators_dict[key] > max_comments:
            max_comments = commentators_dict[key]
            commentators = []
            commentators.append(key)
        elif commentators_dict[key] == max_comments:
            commentators.append(key)
    return commentators, max_comments


def find_average_price(data, variety):
    summa = 0
    counter = 0
    for i, value in enumerate(data):
        if value['variety'] == variety:
            if value['price']:
                summa += value['price']
                counter += 1
    return summa/counter if counter != 0 else -1


def find_average_score(data, variety):
    sum = 0
    counter = 0
    for i, value in enumerate(data):
        if value['variety'] == variety:
            if value['points']:
                sum += int(value['points'])
                counter += 1
    return sum / counter if counter != 0 else -1


def find_min_price(data, variety):
    min_price = None
    for i, value in enumerate(data):
        if variety == value['variety']:
            if not min_price:
                min_price = value['price']
            else:
                if value['price'] and value['price'] < min_price:
                    min_price = value['price']
    return min_price


def find_max_price(data, variety):
    max_price = 0
    for i, value in enumerate(data):
        if variety == value['variety']:
            if value['price'] and value['price'] > max_price:
                max_price = value['price']
    return max_price


def find_most_common_region(data, variety):
    region_dict = {}
    for i, value in enumerate(data):
        if variety == value['variety']:
            if value['region_1']:
                if value['region_1'] in region_dict:
                    region_dict[value['region_1']] += 1
                else:
                    region_dict[value['region_1']] = 1
            elif value['region_2']:
                if value['region_2'] in region_dict:
                    region_dict[value['region_2']] += 1
                else:
                    region_dict[value['region_2']] = 1
    max_region = 0
    region = ''
    for key in region_dict:
        if region_dict[key] > max_region:
            max_region = region_dict[key]
            region = key
    return region


def find_most_expensive_and_cheapest_country(data):
    country = {}
    country_counter = {}
    for i, value in enumerate(data):
        if not value['country'] in country:
            if value['price']:
                country[value['country']] = value['price']
                country_counter[value['country']] = 1
            else:
                country[value['country']] = 0
                country_counter[value['country']] = 0
        else:
            if value['price']:
                country[value['country']] += value['price']
                country_counter[value['country']] += 1
            else:
                pass
    for key in country:
        if country_counter[key]:
            country[key] /= country_counter[key]
    max_country = 0
    max_country_dict = []
    min_country_dict = []
    for key in country:
        if country[key] > max_country:
            max_country_dict = []
            max_country_dict.append(key)
            max_country = country[key]
        elif country[key] == max_country:
            max_country_dict.append(key)
    min_country = max_country
    for key in country:
        if country[key] < min_country and country[key]:
            min_country_dict = []
            min_country_dict.append(key)
            min_country = country[key]
        elif country[key] == min_country:
            min_country_dict.append(key)
    return max_country_dict, max_country, min_country_dict, min_country


def find_most_rated_and_underrated_country(data):
    country = {}
    country_counter = {}
    for i, value in enumerate(data):
        if not value['country'] in country:
            if value['points']:
                country[value['country']] = int(value['points'])
                country_counter[value['country']] = 1
            else:
                country[value['country']] = 0
                country_counter[value['country']] = 0
        else:
            if value['points']:
                country[value['country']] += int(value['points'])
                country_counter[value['country']] += 1
            else:
                pass
    for key in country:
        country[key] /= country_counter[key]
    max_country = 0
    max_country_dict = []
    min_country_dict = []
    for key in country:
        if country[key] > max_country:
            max_country_dict = []
            max_country_dict.append(key)
            max_country = country[key]
        elif country[key] == max_country:
            max_country_dict.append(key)
    min_country = max_country
    for key in country:
        if country[key] < min_country:
            min_country_dict = []
            min_country_dict.append(key)
            min_country = country[key]
        elif country[key] == min_country:
            min_country_dict.append(key)
    return max_country_dict, max_country, min_country_dict, min_country


def find_most_common_country(data, variety):
    country_dict = {}
    for i, value in enumerate(data):
        if variety == value['variety']:
            if value['country']:
                if value['country'] in country_dict:
                    country_dict[value['country']] += 1
                else:
                    country_dict[value['country']] = 1
    max_country = 0
    country = ''
    for key in country_dict:
        if country_dict[key] > max_country:
            max_country = country_dict[key]
            country = key
    return country


def write_to_statsjson(wine, stat):
    statistic_str = '{"statictics:" {\n\t"wine": {\n'
    for key, val in wine.items():
        str = f'"{key}": {val}'
        statistic_str += '\t\t' + str + '\n'
    statistic_str += '\t},\n'
    for key, val in stat.items():
        str = f'"{key}": {val}'
        statistic_str += '\t' + str + '\n'
    statistic_str += '\t}\n}'

    # write to file
    statistic = open("stats.json", "w")
    statistic.write(statistic_str)
    statistic.close()


# open and read files
json1 = open("winedata_1.json", "r")
json2 = open("winedata_2.json", "r")
data1 = json1.read()
data2 = json2.read()

# close files
json1.close()
json2.close()

# time
t = time.time()

# get tokens
result1 = get_token(data1)
result2 = get_token(data2)

# get dicts
dictionary1 = get_dict(result1)
dictionary2 = get_dict(result2)

# merge list and sorting
merge_dictionary = merge_lists(dictionary1, dictionary2)
result_dictionary = sorting(merge_dictionary)

# write to file merge data
winedata_full = open("winedata_full.json", "w")
winedata_full.write(transform_list_to_string(result_dictionary))
winedata_full.close()

# Find for varieties:
wine_dict = dict.fromkeys(('Gew\\u00fcrztraminer', 'Riesling', 'Merlot',
                           'Madeira Blend', 'Tempranillo', 'Red Blend'), None)
for key in wine_dict:
    wine_dict[key] = {}
    wine_dict[key]['average_price'] = find_average_price(result_dictionary, key)
    wine_dict[key]['max_price'] = find_max_price(result_dictionary, key)
    wine_dict[key]['min_price'] = find_min_price(result_dictionary, key)
    wine_dict[key]['most_common_region'] =\
        find_most_common_region(result_dictionary, key)
    wine_dict[key]['most_common_country'] =\
        find_most_common_country(result_dictionary, key)
    wine_dict[key]['average_score'] = find_average_score(result_dictionary, key)

# find most expensive wine
most_expensive_wine = find_most_expensive_wine(dictionary1)

# find cheapest wine
cheapest_wine = find_cheapest_wine(dictionary1)

# find highest score
highest_score = find_highest_score(result_dictionary)

# find lowest score
lowest_score = find_lowest_score(dictionary1)

# find most expensive and cheapest country
most_expensive_and_cheapest_country =\
    find_most_expensive_and_cheapest_country(result_dictionary)
most_expensive_country = most_expensive_and_cheapest_country[0]
cheapest_country = most_expensive_and_cheapest_country[2]

# find most rated and underrated country
most_rated_and_underrated_country =\
    find_most_rated_and_underrated_country(result_dictionary)
most_rated_country = most_rated_and_underrated_country[0]
underrated_country = most_rated_and_underrated_country[2]

# find most active commentator
most_active_commentator = find_most_active_commentator(result_dictionary)

stat_dict = {'most_expensive_wine': most_expensive_wine[0],
             'cheapest_wine': cheapest_wine[0],
             'highest_score': highest_score[0],
             'lowest_score': lowest_score[0],
             'most_expensive_country': most_expensive_country,
             'cheapest_country': cheapest_country,
             'most_rated_country': most_rated_country,
             'underrated_country': underrated_country,
             'most_active_commentator': most_active_commentator[0]}

write_to_statsjson(wine_dict, stat_dict)

# print time
print(time.time() - t)
