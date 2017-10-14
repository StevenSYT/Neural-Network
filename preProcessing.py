import pandas as pd
import numpy as np
import numbers

# url= "adult.csv"
def preProcess(rawData, percent):
   # rawData = pd.read_csv(url, header=None)
   numOfAttributes= rawData.shape[1]

   #check if any instance has missing data
   for column in rawData:
      for index,row in rawData.iterrows():

         if rawData.loc[index][column]=="?" :
            rawData.drop(rawData.index[index], inplace = True)

   print("rawData.shape: ", rawData.shape)
   precessedDf = pd.DataFrame()


   for column in rawData:
      #standardize the data
      if isinstance(rawData.iloc[0,column], numbers.Number) :
         rawRow=rawData.iloc[:,column]
         rawRow=(rawRow-rawRow.mean())/rawRow.std()
         # rawData.iloc[:,column]=rawRow
         precessedDf=pd.concat([precessedDf, rawRow], axis=1)
         pass
      #convert the categorical data into numeric ones
      else:
         precessedDf=pd.concat([precessedDf, pd.get_dummies(rawData[column])], axis=1)
   print("dummy shape: ", precessedDf.shape[1])
   outSize=pd.get_dummies(rawData[numOfAttributes-1]).shape[1]
   print("outSize:",outSize)

   #split data
   return split(precessedDf, outSize, percent)

   # print(trainData[1])

def split(dataSet, outSize, percent):
   numpyData = dataSet.as_matrix()
   np.random.shuffle(numpyData)
   print("numpyData shape:",numpyData.shape)
   numpyData=np.transpose(numpyData)
   print("numpyData shape after transpose:",numpyData.shape)

   x=numpyData[0:-(outSize)]
   y=numpyData[-outSize:]
   print("x.shape= ", x.shape)
   print("y.shape= ", y.shape)
   numOfTraining = (int)(dataSet.shape[0]* percent)
   x_train = x[:,0:numOfTraining]
   x_test=x[:,numOfTraining:] #ndarray slice: [a,b] means [a,b)
   y_train = y[:,0:numOfTraining]
   y_test=y[:,numOfTraining:]
   print("numOfTraining=",numOfTraining," shape of x_train= ", x_train.shape)
   print("numOfTest=",dataSet.shape[0]-numOfTraining," shape of x_test= ", x_test.shape)
   print("y_train=" ,y_train)
   print("numOfTraining=",numOfTraining," shape of y_train= ", y_train.shape)
   print("numOfTest=",dataSet.shape[0]-numOfTraining," shape of y_test= ", y_test.shape)


   return (x_train, x_test, y_train, y_test)
