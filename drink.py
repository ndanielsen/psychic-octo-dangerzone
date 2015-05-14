###### Introduce yourself
"""
This is a simple script to looking at global drinking data

Data found on 538's github : https://github.com/fivethirtyeight/data

By Nathan and Sarah 

"""

###### Import modules


import csv



###### Input data 


countries = []
wine = []


with open('drinks.csv', 'rU') as csvfile:
	drinksreader = csv.reader(csvfile, delimiter=',')
	next(drinksreader, None)

	for country_row in drinksreader:
		countries.append(country_row[0])

		# print country_row[3]

		wine_num = int(country_row[3])

		wine.append(wine_num)


###### Do something cool with the data




###### Report your findings

print "Global Drinking Report: Wine"

print "We looked at this many country:", len(countries) 

print "They are together drank this much wine:", sum(wine)

print "The average wine consumption per country was:", sum(wine) / len(countries)


###### Test

#### 'country', 'beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol', 'continent']
#### ['Zimbabwe', '64', '18', '4', '4.7', 'AF']


# print 'hello world!'


# print countries[1:3]

# print sum(wine)





