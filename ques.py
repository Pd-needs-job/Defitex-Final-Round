test_case = 90


if (90 < test_case < 100) :
	print( f" You have got A grade: {test_case} ");

elif (80 < test_case < 90) :
	print ( f" You have got B grade: {test_case} ");

elif (60 < test_case < 80) :
	print( f" You have got C grade: {test_case} ");

else:
	print (f" You have failed it ")




import pandas as pd


data =  "c/Roughness_Value. csv"

df = pd.read_csv(data) 

