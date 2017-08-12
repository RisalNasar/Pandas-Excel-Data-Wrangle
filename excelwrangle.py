
# Author: Risal Nasar - mail.risal@gmail.com - https://sg.linkedin.com/in/risalnasar



import os, sys
import numpy as np 
import pandas as pd
from pandas import Series, DataFrame
import datetime 
import time 

startTime = time.time()

def epochToDate(value):
	return pd.to_datetime(value).date()


def formatDate(value):
	if type(value) == pd.tslib.Timestamp:
		return value.to_pydatetime().date()
	elif type(value) == datetime.datetime:
		return value.date()
	elif type(value) == datetime.date:
		return value
	elif type(value) == int:
		return pd.to_datetime(value).date()
	elif type(value) == str:
		if value != '':
			return datetime.datetime.strptime(value, "%Y-%m-%d").date()
	else:
		return ''


def readExcel(fileName, sheetName):
	do_df = pd.read_excel(fileName, sheetname=sheetName)
	do_df = do_df.replace(np.nan, '', regex=True)
	return do_df


def correctDateFormat(do_df):
	for col in do_df.columns:
		if col in dateCols:
			do_df[col] =  do_df[col].apply(lambda x: formatDate(x))
	return do_df


def writeExcel(fileName, sheetName, df):
	writer = pd.ExcelWriter(fileName, date_format='dd-mmm-yyyy')
	df.to_excel(writer,sheetName)
	writer.save()


def readCSV(fileName, sheetName):
	do_df = pd.read_csv(fileName, parse_dates=True)
	do_df = do_df.replace(np.nan, '', regex=True)
	return do_df


selectedColsVAOutput1 = [ #Example Column List
	'Asset IP Address',
	'Host Name',
	'OS Name',
	'OS Version',
	'Vulnerability Category',
	'Vulnerability Title',
	'Application Names',
	'Head Application Manager',
	'Infra Person',
	'Remediation Status',
	'Remediation Planned Date',
	'Exception Classification',
	'Remarks',
	'Exception Approval Status',
	'Application Review Status',
	'VLAN Type',
	'Location',
	'Out-Of-Tolerance Date',
	'Service Protocol',
	'Service Port',
	'Site Name',
	'Vulnerability ID',
	'Vulnerability Description',
	'Vulnerability Proof',
	'Vulnerability CVE IDs',
	'Vulnerability Solution',
	'Vulnerability Test Date',
	'Vulnerable Since',
	'Status In New Scan',
	'Unique ID',
	'Device Type',

]

dateCols = [ # Example Date Columns

	'Remediation Planned Date',
	'Out-Of-Tolerance Date',
	'Vulnerability Test Date',
	'Vulnerable Since',
]





def arrangeInOrder(do_df):
	colList = do_df.columns
	for col in selectedColsVAOutput1:
		if not col in colList:
			print('[*] Column \'%s\' is not in existing column list.  So creating it.' % (col))
			do_df[col] = ''
	do_df = do_df[selectedColsVAOutput1]
	return do_df



def crossTab(df, col1, col2):
	t = pd.crosstab(df[col1], df[col2])
	t = t.assign(Total = t.sum(axis=1))
	t['Percentage'] = t['Total'] * 100 / t['Total'].sum(axis=0)
	t['Percentage'] = t['Percentage'].round(2)
	t = t.sort(columns='Total', ascending=False)
	return t





def getMonth(datetimeValue):
	if type(datetimeValue) == datetime.date:
		return datetimeValue.strftime("%B")
	else:
		return 'Nil'



def getTimeStamp():
	return datetime.datetime.now().strftime('%Y-%b-%d-%H-%M')






