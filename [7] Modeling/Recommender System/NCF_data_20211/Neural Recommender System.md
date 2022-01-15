---
title: Neural Recommender System
---
The codes to run Neural Collaborative Filtering methods (GMF, MLP, NMF) are available [here](https://colab.research.google.com/drive/1P8zrsmsWM8-WYmhsHhRIbWjQmq8dDeE7?usp=sharing)


---

## How to run
Simply click Runtime -> Run All


## Modify config
If you need to modify the config for each model, simply replace the corresponding config values with yours in the Config Cell (separated into GMF, MLP and NMF respectively). 

Additional datas are provided [here](https://drive.google.com/drive/folders/1zZcdOmYenr501_hbG4ztQfkukJnBYi5P?usp=sharing)

* `tiki_rating_10.csv`: user-item interaction data (users with fewer than 10 interactions were removed) 
* `test.csv`: test data, with 99 negative items already sampled
* `rating_with_entities.csv`: original rating datas, with entities extracted from reviews
* `missing_items.json`: items that appear in `tiki_rating_10.csv` but are missing in `item_info.json`
* `item_info.json`: details about each item in `tiki_rating_10.csv`
* `id2item.json`: dictionary, provides conversion from indexed itemId to original id crawled from tiki.vn

## Reference
1. `He, X., Liao, L., Zhang, H., Nie, L., Hu, X., & Chua, T. (2017). Neural Collaborative Filtering. Proceedings of the 26th International Conference on World Wide Web.`
2. [yihong-chen/neural-collaborative-filtering](https://github.com/yihong-chen/neural-collaborative-filtering)