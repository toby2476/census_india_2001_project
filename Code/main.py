import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_boxplots(df):

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

	return


def correlation_matrix(data,filename):

	df = data.copy()
	s = df.count()
	df['Rural'] = pd.to_numeric(df['Rural'],errors='coerce')
	df['Growth..1991...2001.'] = pd.to_numeric(df['Growth..1991...2001.'],errors='coerce')
	for i,col in enumerate(df):
		if s[i] < 578:
			df.drop(col,inplace=True,axis=1) #Remove columns that have too many missing values

	df.drop(['Unnamed: 0'],axis=1,inplace=True)
	df = df._get_numeric_data() #Remove columns with non numeric data
	df.dropna(how="any",inplace=True)
	cols = df.columns
	arr = np.array(df)
	corr_mat = np.corrcoef(np.transpose(arr))
	corr_mat = np.around(corr_mat,decimals=3)
	np.savetxt("../Plots/"+filename+".csv", corr_mat,fmt = '%.3f',delimiter="\t") #Saved as a CSV file in plots folder
	
	return cols, corr_mat
	

	

def main():

	## Import Data

	df = pd.read_csv('../Data/all.csv',sep=',')

	##Preliminary Analysis
	
	#generate_boxplots(df)
	
	##Find Correlation Matrix
	
	cols, corr_mat = correlation_matrix(df,'corr_mat')

	
	##Modify df to include per capita values:
	df_norm = df.copy()


	#Find per capita values so that attributes don't depend too much on population

	df_norm.drop(['Males','Females','Scheduled.Caste.population','Scheduled.Tribe.population','Number.of.households','Persons..literate','Males..Literate','Females..Literate'],axis=1,inplace=True)
	
	to_normalize = ['Rural','Urban','Total.Educated','Data.without.level','Below.Primary','Primary','Middle','Matric.Higher.Secondary.Diploma','Graduate.and.Above','X0...4.years','X5...14.years', \
		'X15...59.years','X60.years.and.above..Incl..A.N.S..','Total.workers','Main.workers','Marginal.workers','Non.workers','SC.1.Population','SC.2.Population','SC.3.Population', \
		'Religeon.1.Population','Religeon.2.Population','Religeon.3.Population','ST.1.Population','ST.2.Population','ST.3.Population']

	amenities = ['Drinking.water.facilities','Safe.Drinking.water','Electricity..Power.Supply.','Electricity..domestic.','Electricity..Agriculture.','Primary.school','Middle.schools', \
		'Secondary.Sr.Secondary.schools','College','Medical.facility','Primary.Health.Centre','Primary.Health.Sub.Centre','Post..telegraph.and.telephone.facility','Bus.services', \
		'Paved.approach.road','Mud.approach.road','Permanent.House','Semi.permanent.House','Temporary.House']


	for i in to_normalize:
		df_norm[i] = pd.to_numeric(df_norm[i],errors='coerce')
		df_norm[i] = df_norm[i].divide(df['Persons'])

	for i in amenities:
		df_norm[i] = pd.to_numeric(df_norm[i],errors='coerce')
		df_norm[i] = df_norm[i].divide(df['Total.Inhabited.Villages'])
		
	cols_n, corr_mat_n = correlation_matrix(df_norm,'corr_mat_norm')	#Generate another correlation matrix for the modified data

	
	



	'''
	Suggestions:

	-Continue basic analysis of data to become comfortable with the dataset
	-Create more boxplots for different features
	-Identify states/districts that are most literate/illiterate, most educated/uneducated, religious, most rural/urban etc
	-Find correlations/regressions between different features. E.g. education vs literacy, the presence of amenities vs education/literacy
	-Later on we can try to find more data perhaps related to economic well being and poverty

	'''
main()
