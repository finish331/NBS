#%%
import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.tree import export_graphviz
import pydotplus

from collections import defaultdict
from sklearn.metrics import r2_score


#Graphviz一直抓不到 改成直接指定路徑給他
import os 
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

  

features = pd.read_csv('training_data.csv', index_col=[0])
print(features.shape)
#%%
notUseFeatures = ['ORB', '3PA']
features = features.drop(notUseFeatures, axis=1)

#保留一份DataFrame的資料
features_temp = features.copy()

features = features.drop('Season', axis = 1)
features = features.drop('Name', axis = 1)
labels = np.array(features['Rank'])
features = features.drop('Rank', axis = 1)
feature_list = list(features.columns)
features = np.array(features)
print(type(features))
print(len(features))
print(features.shape)

#%%
#計算特徵間的相關性
# featureList = [
#         'Age',
#         'PTS',
#         'FG%',
#         '3P%',
#         '3PA',
#         'FT%',
#         'ORB',
#         'DRB',
#         'AST',
#         'STL',
#         'BLK',
#         'TOV',
#         'PF',
#     ]
# import matplotlib.pyplot as plt
# import seaborn as sns
# fig = plt.figure(figsize=(10, 10))
# fig.set_facecolor('black')
# plt.rcParams.update({'font.size': 10})
# sns.heatmap(features_temp[featureList].corr(), annot=True, cmap="RdYlGn")

# for data in features:
#   for index in range(len(data)):
#     last = len(data) - index - 1
#     if(index != last):
#       temp = data[index]
#       data[index] = data[last]
#       data[last] = temp
#     if index == last or index+1 == last:
#       break
# for index in range(len(feature_list)):
#   last = len(feature_list) - index - 1
#   if index != last:
#     temp = feature_list[index]
#     feature_list[index] = feature_list[last]
#     feature_list[last] = temp
#   if index == last or index+1 == last:
#     break
# print(features[0])
# print(feature_list)

#%%
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.2, random_state = 42)

print("train_features:",train_features.shape)
print(train_features[0])
print("test_features:",test_features.shape)
print(test_features[0])
print("train_labels:",train_labels.shape)
print(train_labels[0])
print("test_labels:",test_labels.shape)
print(test_labels[0])

#%%
#做參數調整(Random做法)
# random_grid = {'n_estimators': [5000, 10000, 15000],
#                'max_features': ['auto', 'sqrt'],
#                'max_depth': [50, 60, 70, 80, 90, 100, None],
#                'min_samples_leaf': [1, 10, 20, 50],
#                'min_samples_split': [2, 5, 10, 20],
#                'bootstrap': [True, False]}
# rf = RandomForestRegressor()
# rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, 
#                                 n_iter = 100, cv = 3, verbose=2, 
#                                 random_state=42, n_jobs = -1)
# rf_random.fit(train_features, train_labels)
# rf_random.best_params_

#%%
# param_grid = {'n_estimators': [10, 12, 14, 16],
#                'max_features': [2, 3, 4],
#                'max_depth': [4, 6, 8, 10, None],
#                'min_samples_leaf': [1, 2, 3, 4],
#                'min_samples_split': [4, 5, 6, 7, 8],
#                'bootstrap': [True]}
# rf = RandomForestRegressor()
# grid_search = GridSearchCV(estimator = rf, param_grid = param_grid, 
#                           cv = 10, n_jobs = -1, verbose = 2)
# grid_search.fit(features, labels)
# grid_search.best_params_

#%%
rf_model = \
RandomForestRegressor(
  n_estimators = 10,
  random_state = 42,
  max_features = 5,
  max_depth = 8,
  min_samples_leaf = 3,
  min_samples_split = 7,
  bootstrap = True,
  n_jobs = -1
)
# rf_model = grid_search.best_estimator_

#%%
#利用K-fold驗證資料
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
labelList = []
result = []
features_test = features_temp.copy()
features_test.set_index('Season', inplace = True)
for season in seasonRange:
  training = features_test.drop(season)
  testing = features_test.loc[season]
  
  trainingFeatures, trainingLabels = np.array(training.drop(['Rank','Name'], axis = 1)), np.array(training['Rank'])
  testingFeatures, testingLabels = testing.drop(['Rank'], axis = 1), np.array(testing['Rank'])
  names = np.array(testingFeatures['Name'])
  testingFeatures = np.array(testingFeatures.drop(['Name'], axis = 1))
  rf_model.fit(trainingFeatures, trainingLabels)
  result.append(rf_model.predict(testingFeatures))
  labelList.append(testingLabels)
  scores.append(rf_model.score(testingFeatures, testingLabels))

#%%
predictIndices = np.argsort(result[9])
correctIndices = np.argsort(labelList[9])

difference = []
for index in range(len(predictIndices)):
  difference.append(abs((index + 1) -  labelList[9][predictIndices[index]]))
  print(index + 1, ")", names[predictIndices[index]] , "/", names[correctIndices[index]], "/", difference[index])
print(scores)
print("mean:",np.mean(scores))
print("std:",np.std(difference))

#%%
seasonPick = {'9':'2018-19'}#2012-13 2013-14 2018-19
outputJson = {}
for season in seasonPick:
  temp = {}
  index = int(season)
  predictIndices = np.argsort(result[index])
  correctIndices = np.argsort(labelList[index])
  for index in range(len(predictIndices)):
    temp[names[predictIndices[index]]] = names[correctIndices[index]]
  outputJson[seasonPick[season]] = temp

with open('expect.json','w') as file_object:
  json.dump(outputJson,file_object)


#%%
print(feature_list)
rf = RandomForestRegressor()
rf.fit(features, labels)
print(rf.feature_importances_)
featureDataFrame = pd.DataFrame(rf.feature_importances_, feature_list)
print(featureDataFrame)

#%%
#<editor-fold desc="摺疊後要顯示的內容">
#%%
# #訓練及預測
# rf_model.fit(train_features, train_labels)
# predictions = rf_model.predict(test_features)
# print("預測結果:",predictions)
# errors = abs(predictions - test_labels)
# print("正確答案:",test_labels)
# print(errors)
# print(len(predictions))
# print(len(test_labels))
# print(np.mean(errors))
# #%%
# print(rf_model.score(test_features, test_labels))
# print(rf_model.score(train_features, train_labels))
# #%%
# #Pull out one tree from the forest
tree = rf_model.estimators_[5]
# Export the image to a dot file
data = export_graphviz(tree, out_file = None, feature_names = feature_list, rounded = True, precision = 1)
# Use dot file to create a graph
graph = pydotplus.graph_from_dot_data(data)
# Write graph to a png file
graph.write_png('test.png')
#</editor-fold>

#%%
#找出哪個特徵較不需要
#先進行正常的訓練跟預測，再把某個特徵隨機給，看與原本的結果是否相差很多
from sklearn.model_selection  import ShuffleSplit

X = features
Y = labels
rf = RandomForestRegressor()
scores = defaultdict(list)
rs = ShuffleSplit(10, .2, .8)

for train_idx, test_idx in rs.split(X):
    X_train, X_test = X[train_idx], X[test_idx]
    Y_train, Y_test = Y[train_idx], Y[test_idx]
    r = rf.fit(X_train, Y_train)
    acc = r2_score(Y_test, rf.predict(X_test))
    for i in range(X.shape[1]):
        X_t = X_test.copy()
        np.random.shuffle(X_t[:, i])
        shuff_acc = r2_score(Y_test, rf.predict(X_t))
        scores[feature_list[i]].append((acc-shuff_acc)/acc)
print ("Features sorted by their score:")
print (sorted([(round(np.mean(score), 4), feat) for
              feat, score in scores.items()], reverse=True))


#%%
