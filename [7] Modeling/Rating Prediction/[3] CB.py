import pandas as pd;
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np;
from sklearn.linear_model import Ridge
from sklearn import linear_model
import seaborn as sns
import os
import math

class Metrics():
    def computeMSE(y_true, y_pred):
        return np.mean((y_true-y_pred)**2)

    def computeMAE(y_true, y_pred):
        return np.mean(np.abs(y_true-y_pred))

    def computeSIA(y_true, y_pred, eps=1): 
        error = np.abs(y_true - y_pred)
        bina = [1 if err <= eps else 0 for err in error]
        res = np.mean(bina)
        return res

if not os.path.exists('../../result'):
    os.makedirs('../../result')
if not os.path.exists('../../result/CB'):
    os.makedirs('../../result/CB')

if not os.path.exists(f'../../result/CB/threshold_10'):
    os.makedirs(f'../../result/CB/threshold_10')

items = pd.read_csv('../../data/datasets/item_10/detail_list.csv', sep=',', encoding='utf-8')
items = items.drop(columns=['item index', 'name', 'category', 'brand', 'price', 'discount', 'discount_rate', 'mota', 'image_url', 'n_sold', 'rank'])
no_items = items.shape[0]
print('No item themes: ', no_items)

cates = pd.read_csv('../../data/datasets/categories.csv', sep=',', encoding='utf-8')['category'].tolist()
X_train = items[cates].values[:,:]
transformer = TfidfTransformer(smooth_idf=True, norm='l2')
tfidf = transformer.fit_transform(X_train).toarray()
no_item_theme = tfidf.shape[1]
n_users = len(pd.read_csv(f'../../data/datasets/rating_10/rating_list.csv', sep=',', encoding='utf-8')['user index'].unique())


def get_items_rated_by_user(utility_matrix, user_index):
    user_index_list = utility_matrix[:, 2]
    row_ids = np.where(user_index_list == user_index)[0]
    item_index_util_list = utility_matrix[row_ids, 1]
    rating_list = utility_matrix[row_ids, 0]
    return (item_index_util_list, rating_list)

avg_mae_test = 0
avg_mse_test = 0
avg_rmse_test = 0
avg_sia_1_test = 0
avg_sia_0_5_test = 0
avg_sia_0_25_test = 0

avg_mae_train = 0
avg_mse_train = 0
avg_rmse_train = 0
avg_sia_1_train = 0
avg_sia_0_5_train = 0
avg_sia_0_25_train = 0


for fold in range(1, 6):
    train_path = f'../../data/datasets/rating_10/kfold/u{fold}.base.csv'
    test_path = f'../../data/datasets/rating_10/kfold/u{fold}.test.csv'
    ratings_base = pd.read_csv(train_path, sep=',', encoding='utf-8').drop_duplicates(subset=['user index', 'item index'], keep='first')
    ratings_test = pd.read_csv(test_path, sep=',', encoding='utf-8').drop_duplicates(subset=['user index', 'item index'], keep='first')
    
    ratings_base.columns= ['user id', 'id', 'rating', 'timestamp', 'comment', 'item index', 'user index']
    ratings_test.columns= ['user id', 'id', 'rating', 'timestamp', 'comment', 'item index', 'user index']
    ratings_base = ratings_base.drop(columns=['user id', 'timestamp', 'comment']) 
    ratings_test = ratings_test.drop(columns=['user id', 'timestamp', 'comment']) 
    ratings_base = pd.merge(ratings_base, items, how='inner', left_on='id', right_on="id")
    ratings_test = pd.merge(ratings_test, items, how='inner', left_on='id', right_on="id")

    ratings_base = ratings_base.drop(columns=['main_category', 'id'])
    ratings_test = ratings_test.drop(columns=['main_category', 'id'])

    ratings_train_arr = ratings_base.values[1:, :]
    ratings_test_arr = ratings_test.values[1:, :]

    user_index_list = ratings_base['user index'].value_counts().index.tolist()
    w = np.zeros((no_item_theme, n_users))
    b = np.zeros((1, n_users))

    for i in user_index_list:
        item_index_util_list, rating_list = get_items_rated_by_user(ratings_train_arr, i)
        item_index_util_list = [int(index) for index in item_index_util_list]
        
        ridge = Ridge(alpha=100, fit_intercept=True, max_iter=20000, normalize=True)
        tfdif_by_user = tfidf[item_index_util_list]
        
        ridge.fit(tfdif_by_user, rating_list)

        w[:, i] = ridge.coef_
        b[0, i] = ridge.intercept_

    Y = tfidf.dot(w)  + b

    item_indexes = ratings_train_arr[:, 1]
    user_indexes = ratings_train_arr[:, 2]
    true_scores = ratings_train_arr[:, 0]

    if not os.path.exists(f'../../result/CB/threshold_10/train'):
        os.makedirs(f'../../result/CB/threshold_10/train')

    if not os.path.exists(f'../../result/CB/threshold_10/test'):
        os.makedirs(f'../../result/CB/threshold_10/test')

    y_true_train = []
    y_predict_train = []
    for i in range(len(item_indexes)):
        item_index = int(item_indexes[i])
        user_index = int(user_indexes[i])
        true_score = true_scores[i]
        if (Y[item_index][user_index] != 0):
            y_true_train.append(true_score)
            y_predict_train.append(Y[item_index][user_index])
    y_predict_train = [4 if y > 4 else y for y in y_predict_train]
    y_predict_train = [1 if y < 0 else y for y in y_predict_train]
    y_predict_train = np.array(y_predict_train)
    y_true_train = np.array(y_true_train)

    result = pd.DataFrame(columns=['true', 'predict'])
    result['true'] = y_true_train.tolist()
    result['predict'] = y_predict_train.tolist()
    result.to_csv(f'../../result/CB/threshold_10/train/fold_{fold}.csv', index=False, sep=',')

    #Compute MAE metrics
    mae_train = Metrics.computeMAE(y_true_train, y_predict_train)
    avg_mae_train += mae_train
    #Compute MSE metrics
    mse_train = Metrics.computeMSE(y_true_train, y_predict_train)
    avg_mse_train += mse_train

    #Compute SIA metrics
    sia_train_1 = Metrics.computeSIA(y_true_train, y_predict_train, 1)
    avg_sia_1_train += sia_train_1

    sia_train_0_5 = Metrics.computeSIA(y_true_train, y_predict_train, 0.5)
    avg_sia_0_5_train += sia_train_0_5

    sia_train_0_25 = Metrics.computeSIA(y_true_train, y_predict_train, 0.25)
    avg_sia_0_25_train += sia_train_0_25

    item_indexes = ratings_test_arr[:, 1]
    user_indexes = ratings_test_arr[:, 2]
    true_scores = ratings_test_arr[:, 0]

    y_true_test = []
    y_predict_test = []
    for i in range(len(item_indexes)):
        item_index = int(item_indexes[i])
        user_index = int(user_indexes[i])
        true_score = true_scores[i]
        if (Y[item_index][user_index] != 0):
            y_true_test.append(true_score)
            y_predict_test.append(Y[item_index][user_index])
    y_predict_test = [4 if y > 4 else y for y in y_predict_test]
    y_predict_test = [1 if y < 0 else y for y in y_predict_test]
    y_predict_test = np.array(y_predict_test)
    y_true_test = np.array(y_true_test)

    result = pd.DataFrame(columns=['true', 'predict'])
    result['true'] = y_true_test.tolist()
    result['predict'] = y_predict_test.tolist()
    result.to_csv(f'../../result/CB/threshold_10/test/fold_{fold}.csv', index=False, sep=',')

    #Compute MAE metrics
    mae_test = Metrics.computeMAE(y_true_test, y_predict_test)
    avg_mae_test += mae_test
    #Compute MSE metrics
    mse_test = Metrics.computeMSE(y_true_test, y_predict_test)
    avg_mse_test += mse_test

    #Compute SIA metrics
    sia_test_1 = Metrics.computeSIA(y_true_test, y_predict_test, 1)
    avg_sia_1_test += sia_test_1

    sia_test_0_5 = Metrics.computeSIA(y_true_test, y_predict_test, 0.5)
    avg_sia_0_5_test += sia_test_0_5

    sia_test_0_25 = Metrics.computeSIA(y_true_test, y_predict_test, 0.25)
    avg_sia_0_25_test += sia_test_0_25


print("mae_train:", avg_mae_train / 5)
print("mse_train:", avg_mse_train / 5)
print("sia_1_train:", avg_sia_1_train / 5)
print("sia_0_5_train:", avg_sia_0_5_train / 5)
print("sia_0_25_train:", avg_sia_0_25_train / 5)

print("mae_test:", avg_mae_test / 5)
print("mse_test:", avg_mse_test / 5)
print("sia_1_test:", avg_sia_1_test / 5)
print("sia_0_5_test:", avg_sia_0_5_test / 5)
print("sia_0_25_test:", avg_sia_0_25_test / 5)