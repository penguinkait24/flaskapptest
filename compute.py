import os, time, glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def import_data(filename):
	data = pd.read_csv(filename)
	data.columns = data.columns.str.strip()
	data['drug'][data['drug'] == 'Heparin'] = 0
	data['drug'][data['drug'] == 'Warfarin'] = 1
	data['gender'][data['gender'] == 'F'] = 0
	data['gender'][data['gender'] == 'M'] = 1
	data['ethnicity'][data['ethnicity'] == 'AMERICAN INDIAN/ALASKA NATIVE FEDERALLY RECOGNIZED TRIBE'] = 0
	data['ethnicity'][data['ethnicity'] == 'AMERICAN INDIAN/ALASKA NATIVE'] = 0
	data['ethnicity'][data['ethnicity'] == 'ASIAN'] = 1
	data['ethnicity'][data['ethnicity'] == 'ASIAN - ASIAN INDIAN'] = 1
	data['ethnicity'][data['ethnicity'] == 'ASIAN - CAMBODIAN'] = 1
	data['ethnicity'][data['ethnicity'] == 'ASIAN - CHINESE'] = 1
	data['ethnicity'][data['ethnicity'] == 'ASIAN - FILIPINO'] = 1
	data['ethnicity'][data['ethnicity'] == 'ASIAN - OTHER'] = 1
	data['ethnicity'][data['ethnicity'] == 'ASIAN - THAI'] = 1
	data['ethnicity'][data['ethnicity'] == 'ASIAN - VIETNAMESE'] = 1
	data['ethnicity'][data['ethnicity'] == 'BLACK/AFRICAN'] = 2
	data['ethnicity'][data['ethnicity'] == 'BLACK/AFRICAN AMERICAN'] = 2
	data['ethnicity'][data['ethnicity'] == 'BLACK/CAPE VERDEAN'] = 2
	data['ethnicity'][data['ethnicity'] == 'BLACK/HAITIAN'] = 2
	data['ethnicity'][data['ethnicity'] == 'HISPANIC OR LATINO'] = 3
	data['ethnicity'][data['ethnicity'] == 'HISPANIC/LATINO - CUBAN'] = 3
	data['ethnicity'][data['ethnicity'] == 'HISPANIC/LATINO - DOMINICAN'] = 3
	data['ethnicity'][data['ethnicity'] == 'HISPANIC/LATINO - GUATEMALAN'] = 3
	data['ethnicity'][data['ethnicity'] == 'HISPANIC/LATINO - PUERTO RICAN'] = 3
	data['ethnicity'][data['ethnicity'] == 'HISPANIC/LATINO - SALVADORAN'] = 3
	data['ethnicity'][data['ethnicity'] == 'MIDDLE EASTERN'] = 4
	data['ethnicity'][data['ethnicity'] == 'MULTI RACE ETHNICITY'] = 6
	data['ethnicity'][data['ethnicity'] == 'OTHER'] = 6
	data['ethnicity'][data['ethnicity'] == 'PATIENT DECLINED TO ANSWER'] = 7
	data['ethnicity'][data['ethnicity'] == 'PORTUGUESE'] = 5
	data['ethnicity'][data['ethnicity'] == 'UNABLE TO OBTAIN'] = 7
	data['ethnicity'][data['ethnicity'] == 'UNKNOWN/NOT SPECIFIED'] = 7
	data['ethnicity'][data['ethnicity'] == 'WHITE'] = 5
	data['ethnicity'][data['ethnicity'] == 'WHITE - BRAZILIAN'] = 5
	data['ethnicity'][data['ethnicity'] == 'WHITE - EASTERN EUROPEAN'] = 5
	data['ethnicity'][data['ethnicity'] == 'WHITE - OTHER EUROPEAN'] = 5
	data['ethnicity'][data['ethnicity'] == 'WHITE - RUSSIAN'] = 5
	data.apply(pd.to_numeric, errors='coerce')
	return(data)

def training(data):
	warfarin = data[data['drug'] == 1]
	heparin = data[data['drug'] == 0]

	warfarin_X = warfarin[['gender', 'ethnicity']]
	warfarin_Y = warfarin[['los']]

	heparin_X = heparin[['gender', 'ethnicity']]
	heparin_Y = heparin[['los']]

	print("hehehe")
	print(warfarin.shape)
	print("hohoho")
	print(heparin.shape)
	warfarin_model = LinearRegression().fit(warfarin_X, warfarin_Y)
	heparin_model = LinearRegression().fit(heparin_X, heparin_Y)

	return(warfarin_model, heparin_model)

def plot(gender_data, ethnicity_data):
        # update the file path
	filename = '/home/Picsesalg/hw5-penguinkait24-picsesalg-mma05/app/data.csv'
	data = import_data(filename)
	wm, hm = training(data)

	# change string for gender into int
	if (gender_data == '0'):
		gender = 0
	else:
		gender = 1

	# change string for ethnicity into int
	if (ethnicity_data == '0'):
		ethnicity = 0
	elif (ethnicity_data == '1'):
		ethnicity = 1
	elif (ethnicity_data == '2'):
		ethnicity = 2
	elif (ethnicity_data == '3'):
		ethnicity = 3
	elif (ethnicity_data == '4'):
		ethnicity = 4
	elif (ethnicity_data == '6'):
		ethnicity = 6
	elif (ethnicity_data == '5'):
		ethnicity = 5
	else:
		ethnicity = 7

	wy = wm.predict([[gender, ethnicity]])
	hy = hm.predict([[gender, ethnicity]])

	x = [0, 1]
	y = [wy[0][0], hy[0][0]]

	plt.bar(x, y, color='b')
	plt.xticks(x, ('Warfarin', 'Heparin'))
	plt.ylabel('Length of stay (days)')
	if not os.path.isdir('static'):
		os.mkdir('static')
	else:
		# Remove old plot files
		for filename in glob.glob(os.path.join('static', '*.png')):
		    os.remove(filename)
	# a unique filename that the browser has not chache
	plotfile = os.path.join('static', str(time.time()) + '.png')
	plt.savefig(plotfile)
	return plotfile
