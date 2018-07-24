import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():

	## Import Data

	df = pd.read_csv('../Data/all.csv',sep=',')

	##Preliminary Analysis

	population = df[df.columns[1:6]] #Create Boxplot for Population
	population.plot(kind='box')
	plt.title('Population by District')
	plt.ylabel('Population')
	plt.savefig('../Plots/population_boxplot.png') #Check Plots directory for output

	growth = df['Growth..1991...2001.']	#Create Boxplot for Population Growth
	growth = pd.to_numeric(growth,errors='coerce')
	growth.plot(kind='box')
	plt.title('Population Growth by District')
	plt.ylabel('% Growth')
	plt.savefig('../Plots/population_growth_boxplot.png')

	urban = pd.to_numeric(df['Urban'],errors='coerce')	
	urban_percent = urban.divide(df['Persons'])
	urban_percent.plot(kind='box')
	plt.title('% Of Population in District Living in Urban Areas') #Create Boxplot for Urban Population
	plt.ylabel('% Urban Population')
	plt.savefig('../Plots/urban_population_boxplot.png')

	literacy_rates = df[df.columns[20:23]]		#Create Boxplot for Literacy Rates
	literacy_rates.plot(kind='box')
	plt.title('Literacy Rates')
	plt.ylabel('%')
	plt.savefig('../Plots/literacy_rate_boxplot.png') #Big Gap Between Male and Female Literacy Rates
	#Here's a thought - with more data we can delve into deeper analysis about gender inequality in India. 

	'''
	Suggestions:

	-Continue basic analysis of data to become comfortable with the dataset
	-Create more boxplots for different features
	-Identify states/districts that are most literate/illiterate, most educated/uneducated, religious, most rural/urban etc
	-Find correlations/regressions between different features. E.g. education vs literacy, the presence of amenities vs education/literacy
	-Later on we can try to find more data perhaps related to economic well being and poverty

	'''
main()
