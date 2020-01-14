import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.tree import export_graphviz
import pydotplus

from collections import defaultdict
from sklearn.metrics import r2_score

import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


#處理資料，需要那些欄位，不需要哪些欄位等等
def DataProcess():
    features = pd.read_csv('training_data.csv', index_col=[0])

    notUseFeatures = ['FT%', '3PA', 'ORB',]
    features = features.drop(notUseFeatures, axis=1)
    # features = features.drop('FT%', axis=1)
    # features = features.drop('3PA', axis=1)
    # features = features.drop('ORB', axis=1)
    allFeatures = features.copy()
    features = features.drop('Season', axis=1)
    features = features.drop('Name', axis=1)

    labels = np.array(features['Rank'])
    features = features.drop('Rank', axis=1)
    featureList = list(features.columns)
    features = np.array(features)

    return features, featureList, labels, allFeatures

def K_fold(model, features):
    seasonRange = [
        '2009-10',
        '2010-11',
        '2011-12',
        '2012-13',
        '2013-14',
        '2014-15',
        '2015-16',
        '2016-17',
        '2017-18',
        '2018-19'
    ]
    scores = []
    result = []
    features.set_index('Season', inplace = True)
    for season in seasonRange:
        training = features.drop(season)
        testing = features.loc[season]
        trainingFeatures, trainingLabels = np.array(training.drop(['Rank','Name'], axis = 1)), np.array(training['Rank'])
        testingFeatures, testingLabels = testing.drop(['Rank'], axis = 1), np.array(testing['Rank'])
        names = np.array(testingFeatures['Name'])
        testingFeatures = np.array(testingFeatures.drop(['Name'], axis = 1))
        model.fit(trainingFeatures, trainingLabels)
        result.append(model.predict(testingFeatures))
        scores.append(model.score(testingFeatures, testingLabels))

    predictIndices = np.argsort(result[9])
    correctIndices = np.argsort(testingLabels)

    # print(result[9])
    # print(testingLabels)
    # print(predictIndices)
    # print(correctIndices)

    for index in range(len(predictIndices)):
        print(index + 1, ")", names[predictIndices[index]] , "/", names[correctIndices[index]], "/", abs( (index + 1) -  testingLabels[predictIndices[index]]))
    print(scores)

def Training(model, features, labels):
    #拆分訓練、測試資料
    trainFeatures, testFeatures, trainLabels, testLabels = train_test_split(features, labels, test_size = 0.2, random_state = 42)
    model.fit(trainFeatures, trainLabels)

    predictions = model.predict(testFeatures)
    print("預測結果:",predictions)
    errors = abs(predictions - testLabels)
    print("正確答案:",testLabels)
    print(errors)
    print(np.mean(errors))

    print(model.score(testFeatures, testLabels))
    print(model.score(trainFeatures, trainLabels))

def main():
    # ndAdday, List, ndArray, ndArray
    features, featureList, labels, allFeatures = DataProcess()

    rf_model = \
        RandomForestRegressor(
        n_estimators = 12, 
        random_state = 42,
        max_features = 3,
        max_depth = 9,
        min_samples_leaf = 2,
        min_samples_split = 8,
        bootstrap = True
        )
    Training(rf_model, features, labels)
    
    K_fold(rf_model, allFeatures.copy())
if __name__ == '__main__':
    main()


#%%
