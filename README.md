Link markdown: https://hackmd.io/5nTpY6teSEyI3ICU3PepMg?view
# Khoa học dữ liệu
- [Tự đánh giá project](#)
- [Về chúng tôi](#khoa-h-c-d--li-u)
  * [Thành viên của nhóm](#tha-nh-vi-n-nho-m)
  * [Phân công công việc](#ph-n-c-ng-c-ng-vi--c)
- [Đề tài](#Đề-tài)
- [Thu thập dữ liệu](#thu-th-p-d--li-u)
- [Tích hợp dữ liệu](#tiki-datasets)
- [Làm sách và tiền xử lý dữ liệu](#tiki-datasets)
- [Tiki datasets](#tiki-datasets)
- [Khám phá dữ liệu](#kha-m-pha--d---li--u)

- [Một số khái niệm và độ đo cần thiết trong project](#)
    + [SIA](#)
    + [MAE](#)
    + [MSE](#)
    + [RMSE](#)
    + [Confusion Matrix](#)
    + [Precision và Recall](#)
  
- [Sold Quantity Prediction And Recommend These Items To User](#Sold-Quantity-Prediction-Recommend)
    + [Random Forest Regression](#random-forest-regression)
    + [Linear Regression](#linear-regression)
    + [Neural Network Regression](#neural-network-regression)
- [Rating Prediction](#)
    + [Matrix Factorization](#)
    + [Content-Based](#)

- [Áp dụng mạng neural cải thiện kết quả dự đoán rating](#neural-network)
  + [GMF](#tiki-product-image-classification)
  + [MLP](#analyzing-user-behaviours)
  + [NeuMF](#analyzing-user-behaviours)
- [Bài toán hệ gợi ý](#)
     + [Yêu cầu của bài toán](#)
     + [Phương pháp sử dụng](#)
     + [Chi tiết cài đặt](#)
     + [Thử nghiệm](#)
     + [Một vài Case Study](#)
      

## Tự đánh giá project

|Nội dung||
|-|-|
|Thu thập dữ liệu bằng cách sử dụng API| Hoàn thành |
| Tích hợp dữ liệu|Hoàn thành|
| Làm sạch và tiền xử lý dữ liệu, xây dựng bộ datasets|Hoàn thành|
| Phân tích và khám phá dữ liệu sản phẩm tiki|Đang hoàn thiện|
|Phân tích sự ảnh hưởng của các thuộc tính lên người dùng| Hoàn thành| 
| Sử dụng 2 mô hình Content Based và Matrix Factorization đơn giản cho bài toán dự đoán rating|Hoàn thành|
|Cái thiện kết quả dự đoán rating bằng cách sử dụng mạng neural nhân tạo|Hoàn thành|
|Hệ gợi ý|Hoàn thành|

**Kết quả:** Nhóm đã có những góc nhìn 1 cách tổng quan về các phương pháp dự đoán rating và từ đó liên hệ qua bài toán gợi ý sản phẩm cho người dùng, đống thời cũng phân tích xem những yếu tố gì ảnh hưởng tối lượng mua của 1 sản phẩm.

## Về chúng tôi

### Thành viên nhóm

|Họ & tên|MSSV|
|-|-|
|Lê Thành Long| 20194099
|Lê Đại Thắng | 20194166
|Ninh Văn Nghĩa| 20190060

### Phân công công việc

|Họ & tên|Nội dung công việc|
|-|-|
|Lê Thành Long| Crawl data từ trang https://tiki.vn/, phân tích sự ảnh hưởng của 1 số thuộc tính lên hành vi của người dùng và cài đặt 1 số mô hình cho bài toán dự đoán rating
|Lê Đại Thắng | Tìm hiểu và cài đặt, áp dụng các mô hình neural network cho bài toán gợi ý sản phẩm cho người dùng
|Ninh Văn Nghĩa|Làm sạch, tích hợp, tiền xử lý dữ liệu và khám phá, visualize dữ liệu và làm slide|
|Cả nhóm|Làm báo cáo đồ án môn học|


## Đề tài
***Phân tích hành vi người dùng trong các trang thương mại điện tử***
Củ thể: ***dự đoán rating*** của người dùng lên các sản phẩm. Từ đó liên quan đến bài toán ***gợi ý sản phẩm*** cho người dùng, phân tích yếu tố ảnh hưởng tới ***lượng mua sản phẩm*** của người dùng, ***phân tích cảm xúc*** dựa vào bình luận của người dùng

## Thu thập dữ liệu:

Nhóm chúng tôi đã thu thập dữ liệu từ trang thương mại nổi tiếng https://tiki.vn/ mặc dù trên mạng đã có rất nhiều bộ data về thương mại điện tử  tuy nhiên bộ datasets của nhóm chúng tôi rất dồi dào về các thông tin chi tiết sản pha và thông tin rating và đặc biệt các sản phẩm trên bộ dataset của nhóm chúng tôi toàn là các sản phẩm mới mới đồng nghĩa là các review ở các bộ phim này cũng là gần đây.

***Thư viện để thu thập dữ liệu là BeautifulSoup và thu thập dữ liệu bằng cách call API của tiki***

## Tích hợp dữ liệu

Sau khi crawl data về ta có được thông tin chi tiết, thông tin về id, thông tin tổng quan của các sản phẫm thuộc vào từng category, khi đó nhóm chúng tôi tích hơp các thư mục category lại và tạo thành các file data lớn hơn: ***intergrated_data/item/detail_list.csv***, ***intergrated_data/item/overall_list.csv*** và ***intergrated_data/rating/rating_list.csv***

## Làm sạch và tiền xử lý dữ liệu

***Các bước làm sạch và tiền xử lý dữ liệu:***
* Loại bỏ các hàng trùng nhau cho tất cả các file
* Loại bỏ các hàng trong detail_list.csv có trường price <= 0 và lowercase các trường là string
* Tạo ra các cột tương ứng với mỗi cột là 1 category, giá trị của hàng i và tại cột ấy sẽ là 1 nếu sản phẩm i thuộc vào category đó và là 0 nếu ngược lại
* Loại bỏ tất cả người dùng có lịch sử tường tác < 10, thay vào đó ta sẽ suggest cho những người này các sản phẩm nổi bật
* Rescale lại rating của người dùng đối với 1 số mô hình trong project, ***củ thể***, nhóm chúng tối gộp 1, 2 thành 1 rating là 1 và rating 3, 4, 5 sẽ trở thành 2, 3, 4. Kết quả sau khi dự đoán sẽ cộng thêm 1.


## TIKI datasets

Gồm 4 bộ chính item/detail_list.csv, item/overall_list.csv và rating/rating_list.csv với ý nghĩa của các bộ dữ liệu lần lượt là thông tin chi tiết của sản phẩm, các thông số tổng quan về sản phẩm  và thông tin bình luận đối với sản phẩm.

**Chú ý:** Nhóm chúng tôi đã chia các file csv trên thành ***5-fold*** và tính toán kết quả triung bình của 5 fold này để làm kết quả chính

## Khám phá dữ liệu


                                    
## Một số khái niệm và độ đo cần thiết trong project

### SIA - Soft Interval Accuracy
Một dự đoán được gói là đúng nói chênh lệch giữa dự đoán và thực tế <= siêu tham số epsilon:
$|y_i - \hat{y_i}| <= eps$
Và ***SIA*** sẽ bằng số mẫu đúng trên toàn bộ mẫu

---

### MAE - Mean Absolute Error

$MAE(y, \hat{y}) = \frac{1}{m} \sum\limits_{i = 1}^{m}|y_i - \hat{y_i}|$

---

### MSE - Mean Squared Error

$MSE(y, \hat{y}) = \frac{1}{m} \sum\limits_{i = 1}^{m}(y_i - \hat{y_i})^2$

---

### RMSE - Root Mean Squared Error

$RMSE(y, \hat{y}) = \sqrt{\frac{1}{m} \sum\limits_{i = 1}^{m}(y_i - \hat{y_i})^2}$

---

### Confusion Matrix
Đặc biệt sử dụng cho các bài toán phân lớp và đây là 1 ma trận vuông có có size là ***số lớp * số lớp***.

Tại hàng i côt j của ma trận có giá trị thuộc khoản từ ***0-1*** có ý nghĩa là số lượng mẫu ***đáng ra là thuộc lớp i nhưng đã dự đoán thuộc lớp j***

---

### Precision và Recall

Với bài toán phân loại 2 lớp thì:
* Precision là tỷ lệ sô mẫu đoán đúng lớp thứ nhất trên số lượng ta dự đoán thứ 1
* Recall là tỷ lệ số mẫu đoán đúng lớp thứ nhất trên số lượng mẫu thực sự thuộc lớp thứ 1

***Chú ý:***
* Precision cao nghĩa là xác suất tìm được các điểm đúng là cao
* Recall cao nghĩa là xác suất mình bỏ sót các điểm đúng là thấp


## Sold Prediction And User Behaviour Based On Item's Features
Metrics đánh giá mà nhóm sử dụng: ***Mean Absolute Error (MAE)*** hoặc ***Soft Interval Accuracy (SIA)***
Các features sử dụng cho việc dự đoán: 

|Feature name | Type | 
|---|---|
|category |categorical|
|price|numerical|
|avg_rating|numerical|
|n_rate_5|numerical|
|n_rate_4|numerical|
|n_rate_3|numerical|
|n_rate_2|numerical|
|n_rate_1|numerical|
|rate_with_img|numerical|
|discount|numerical|
|discount_rate|numerical|
|n_reviews|numerical|

Ta sẽ phân chia dữ liệu thành các tập `train - validation - test` set theo tỉ lệ: `60% - 20% - 20%`
### Random Forest Regression
#### Dự đoán sử dụng toàn bộ features (one hot + numeric)

Kết quả:

|Dataset|MAE|
|-|-|
|train|162.19769|
|val|377.55629|
|test|366.07174|


***Ghi chú***: do kết quả dự đoán có thể lên đến đơn vị nghìn (lượt bán), để dễ giải thích, ta sẽ sử dụng độ đo `MAE` (thay vì `MSE` như thông thường). Do đó ta có thể đánh giá `MAE` trên tập test ~366 có nghĩa là mô hình dự đoán trung bình sai số khoảng 366 cho một sản phẩm trong tập test.

Bây giờ ta sẽ xét `SIA` metric. 

- Với `epsilon = 1000` (cho phép sai số dự đoán lên đến 1k lượt bán):
    |Dataset | SIA-1000|
    |-|-|
    |train |  0.97237|
    |val   | 0.92814|
    |test  | 0.93728|
    
    
- `epsilon = 500` (cho phép sai số dự đoán lên đến 500 lượt bán):
    |Dataset | SIA-500|
    |-|-|
    |train|   0.94480|
    |val  | 0.87425|
    |test | 0.88197|
 

- `epsilon = 200` (cho phép sai số dự đoán lên đến 200 lượt bán):
    |Dataset | SIA-200|
    |-|-|
    | train| 0.88470|
    | val  | 0.78389|
    | test | 0.78114|
    
***Nhận xét***: ta thấy mô hình đạt được độ chính xác khá tốt. Hiệu năng trên tập `val` và `test` xấp xỉ nhau. 

### Linear Regression

---

#### Chỉ sử dụng các numerical features:
`price, avg_rating, n_reviews, discount, discount_rate`
(Bỏ đi `category`)

Kết quả:

|Dataset|MAE|SIA-1000|SIA-500|SIA-200|
|---|---|---|---|---|
|train|694.18673|0.89600|0.78934|0.50681|
|val|615.25603|0.89222|0.79205|0.50599|
|test|558.55912|0.90026|0.79486|0.50675|



***Nhận xét***: Ta thấy mô hình Linear Regression có `SIA` thấp hơn so với khi sử dụng Random Forest khá nhiều. Hơn nữa, ta thấy mô hình có `MAE` trên tập `val` và tập `test` cao bất thường. Sau khi tìm hiểu nguyên nhân thì ta nhận thấy có một vài hệ số (coefficient) của một số feature có giá trị rất cao . Hơn nữa, ta nhận thấy các hệ số này thuộc về feature `n_reviews` và số lượng rating theo từng điểm. Ta sẽ sử dụng `L2 Regularization` (Ridge) để giới hạn giá trị của các hệ số.

Kết quả khi sử dụng Ridge Regression (cùng với việc tinh chỉnh hyperparameter $\alpha$ tốt nhất sử dụng phương pháp GridSearch trên tập `val`), ta có kết quả như sau:

`Best cross-validation MAE: 505.34610839045035
with alpha = 100`

|Dataset|MAE|SIA-1000|SIA-500|SIA-200|
|---|---|---|---|---|
|train|681.87641|0.87953|0.78512|0.61469|
|val|602.002647|0.87616|0.77844|0.59771|
|test|541.09581|0.88327|0.78724|0.61476|

***Nhận xét:*** Khi sử dụng hồi quy ridge thì ta thấy kết quả tốt hơn so với ki sử dụng hồi quy tuyến tính các weight cũng nhỏ hơn so với mô hình hồi quy tuyến tính do sự ảnh hưởng của siêu tham số $\alpha$


Ta thấy hiệu năng của mô hình ***thấp hơn*** phương pháp Random Forest khá nhiều (kể cả trên tập `train`). Điều này có thể là do mô hình vẫn chưa đủ phức tạp để nắm bắt được hết các thông tin từ input

---

#### Linear Regression sử dụng Mean Encoding cho các categorical features:
Kết quả:

|Dataset|MAE|SIA-1000|SIA-500|SIA-200|
|---|---|---|---| --- |
|train|817.73390|0.84025|0.745440|0.61203|
|val|736.71263|0.84186|0.737890|0.60452|
|test|674.41237|0.84495|0.74107|0.61324|


Ta thấy kết quả trên tập train cũng xấp xỉ kết quả trên tập val và test (ngược lại với mô hình Random Forest có độ lỗi trên tập train thấp hơn rất nhiều so với val và test). Có thể là do mô hình Linear Regression chưa phải là phù hợp nhất với tập dữ liệu của ta (***lưu ý là Linear Regression có thể đưa ra kết quả dự đoán mang giá trị âm***),
đặc biệt là đối với các ***categorical feature*** ? (Ta sẽ kiểm chứng điều này trong phần Neural Network)


### Neural Network

Tương tự như Linear Regression , ta sẽ tiền xử lý input bằng việc chuẩn hóa các features theo phương pháp Z-score normalization.
Ta sẽ thực nghiệm với 1 mạng Neural Network nhỏ như sau:

```
Input Vector -> FC(32 units) + ReLU -> FC(64 units) + ReLU -> Output (1 unit) + ReLU
```

Nguyên nhân ta sử dụng hàm ReLU activation lên output (thay vì Linear) là do ta muốn các giá trị dự đoán đều không âm.
Với weights của mỗi layer, ta sẽ sử dụng `L2-Regularization` với $\alpha$ =0.1 để hạn chế việc overfitting.
Hàm mất mát ta sẽ sử dụng là hàm `MAE`:

\begin{equation}
    L(y, \hat{y}) = \frac{1}{N} \sum_{i=0}^{N}|y -     {\hat{y}}_i|
\end{equation}


#### Sử dụng toàn bộ features (Onehot Encoding + numeric):

|Dataset|MAE|SIA-1000|SIA-500|SIA-200|
|---|---|---|---|---|
|train|424.32375|0.94671|0.90634|0.82453|
|val|335.20732|0.94502|0.90011|0.81818|
|test|302.48544|0.94773|0.90571|0.81446|


---

#### Sử dụng features (Onehot Encoding + numeric) trừ avg_rating và n_reviews:

+ Mô hình RandomForest
    + Khi không loại bỏ avg_rating và n_reviews

         |Dataset|MAE|SIA-1000|SIA-500|SIA-200|
        |---|---|---|---|---|
        |train|162.19769| 0.97237|0.94480|0.88470|
        |val|377.55629|0.92814|0.87425|0.78389|
        |test|366.071744|0.93728|0.88197|0.78114|
      
    
     + Khi loại bỏ avg_rating và n_reviews
    
         |Dataset|MAE|SIA-1000|SIA-500|SIA-200|
        |---|---|---|---|---|
        |train|490.71191|0.93908|0.88647|0.77151|
        |val|745.28144|0.88051|0.80240|0.63745|
        |test|695.62715|0.88219|0.80096|0.63371|

---


***Nhận xét***: 

Khi ta loại bỏ các thuộc tính như ***số lượng bán ra*** của các sản phẩm hay là ***điểm số trung bình*** người dùng cho sản phẩm đó thì kết quả của các độ đo tệ 1 cách trông thấy. Hay có nghĩa là khi giao diện tiki hiển thị các thông số này thì nó cũng phần nào ***ảnh hưởng đến quyết định mua hàng*** của người dùng trên sản phẩm đó



**KẾT LUẬN**: Ta thấy hầu hết các sản phẩm đều có số lượt bán thấp (91.4% dữ liệu có số lượt bán dưới 1000). Do đó mà việc chúng ta làm giới hạn sai số dự đoán (epsilon) thấp sẽ giúp cho ta đánh giá một cách khách quan và phù hợp với bài toán và nhóm mình chọn metric SIA-200

Đối với mô hình Neural Network, khi ta sử dụng Onehot Encoding thì xem kết quả có vẻ hợp lý hơn so với khi sử dụng Mean Encoding cho các categorical features.

Theo các kết quả trên ta thấy 2 mô hình cho kết quả tốt nhất là Random Forest và Neural Network và đã sử dụng toàn bộ các features. ***Tuy nhiên*** mô hình Neural Network có thời gian ***train lâu*** hơn nhiều so với Random Forest. 

Ta thấy khi ta loại bỏ 2 thuộc tính ***numerical avg_rating và n_reviews*** thì ta thấy hiệu quả khi dự đoán được sold giảm xuống đáng kể hầu hết trên các mô hình và SIA-200 rất thấp. Điều đó chứng tỏ khi mua hàng trên tiki 2 giá trị avg_rating(Điểm rating trung bình) và n_reviews(Số lượng người reviews) đã ảnh hưởng 1 cách khách quan tới họ khi quyết định có mua sản phẩm hay không. 

***Vì vậy để có thể tăng lượng mua hàng thì phải cải thiện sao cho điểm avg_rating càng lớn càng tốt***

## Rating Prediction
---

### Phương pháp phân rã ma trận matrix factorization
#### Phân tích ma trận thành nhân tử

##### Xấp xỉ bằng 2 ma trận tiềm ẩn

***Ý tưởng*** :Với ma trận user-item và giá trị của mỗi ô là điểm rating mà user đánh giá cho item, trong đó có các ô trống vì có những sản phẩm mà người dùng chưa mua. Ta sẽ xấp xỉ ma trận kết quả bằng 2 ma trận ẩn gọi là ma trận người dùng ẩn và ma trận sản phẩm ẩn

Gọi ma trận R là ma trận user-item chúng ta thành lập được khi đó ta sẽ xấp xỉ ma trận này bằng tích 2 ma trận ẩn P và Q.

Ma trận R có kích thước m x n với m người dùng và n sản phẩm.
Gọi 2 ma trận ẩn là ma trận P có kích thước m x k và ma trận Q có kích thước n x k (lấy k << m, n)

Khi đó:

\begin{equation}
\hat{R}  = PQ^T
\end{equation}


Củ thể đối với điểm rating người dùng u đánh giá sản phẩm i ta có:
\begin{equation}
\hat{R_\text{ui}}  = p_u q_i^T
\end{equation}





##### Ý nghĩa của 2 ma trận tiềm ẩn

Ma trận tiềm ẩn P của người dùng trong đó hàng pu của ma trận sẽ chứa các giá trị là mức dộ yêu thích của người dùng u với các đặc trưng của 1 sản phẩm ví dụ như miêu tả, giá, hình ảnh, ...

Ma trận tiềm Q của các sản phẩm trong đó hàng qi sẽ chứa các giá trị đo lường mức độ sở hữu các đặc trưng như  là tiêu đề, miểu tả hay là hình ảnh sản phẩm

***Chú ý***: Ở các công thức trên có đề cập thì ta có thêm bias bu.
Vì sao lại phải thêm bias cho từng user?

Tùy thuộc vào tính cách đối với các sản phẩm của mỗi người mà họ có thể quyết định số điểm mà họ đánh giá cho sản phẩm đó.

***Lý do:*** Có người dễ tính, có người khó tính, dễ tính 1 cuốn sách hay có thể cho 5 sao nhưng mà khó tính có thể chỉ cho 4 sao hoặc thậm chí là 3 sao chẳng hạn.

Vậy để giải quyết vấn đề này nhóm chúng tôi đã lấy bias của mỗi user là trung bình cộng số điểm mà người đó rating cho những sản phẩm mà người ấy mua.



#### Hàm mất mát

Hàm lỗi nhóm chúng tôi sử dụng là trung bình cộng của bình phương độ chênh lệch kết quả dự doán và kết quả thực tế và dùng thêm l2 regularization để tránh overfitting

$\text{RSS}(y, \hat{y}) = {\frac{1}{m} \sum\limits_{i=1}^{m} (y_i - \hat{y}_i)^2}$

$Loss(y, \hat{y}) = \text{RSS}(y, \hat{y}) + \text{Regularization_Func(P, Q)}$

***Chú ý:*** Ở đây nhóm chúng tôi chọn hàm hiệu chỉnh có công thức là:

$\text{Regularization_Func(P, Q)} = \frac{1}{2} * {\lambda} *  (\sqrt{\sum\limits_{i=1}^m \sum\limits_{j=1}^k |p_{ij}|^2} + \sqrt{\sum\limits_{i=1}^n \sum\limits_{j=1}^k |q_{ij}|^2} )$



#### Đánh giá mô hình

Kết quả:
* ***Khi lamda=0***

|Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
|-|-|-|-|-|-|
|train|1.04395|1.98347|0.62074|0.35644|0.27500|
|test|1.17288|2.42820|0.58087|0.32911|0.26582|


* ***Khi lamda=0.1***

|Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
|-|-|-|-|-|-|
|train|0.50272|0.53481|0.84673|0.62301|0.42093|
|test|0.55700|0.65482|0.81935|0.58907|0.39576|


* ***Khi lamda=0.5***

|Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
|-|-|-|-|-|-|
|train|0.50272|0.53481|0.85770|0.55698|0.43130|
|test|0.55698|0.65482|0.83460|0.60736|0.40702|


* ***Khi lamda=1***

|Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
|-|-|-|-|-|-|
|train|0.50272|0.53481|0.85770|0.63992|0.43130|
|test|0.55698|0.65482|0.83458|0.60736|0.40702|


***Nhận xét***: 

Khi ***lamda=0***, ta thấy mô hình đạt độ chính xác khá thấp cả tập train và tập test, đặc biệt tập tain có độ chính xác còn cao hơn tập test. Việc loại bỏ hiệu chỉnh l2 khiến cho mô hình học khá tệ


Khi cho ***lamda != 0*** ta thấy mô hình đạt được độ chính xác khá tốt và tập test và tập train không chênh lệch nhiều Hiệu năng trên tập `val` và `test` lệch nhau khá ít ở các độ đo MAE và MSE. 

Khi ***lamda=0.1, 0.5, 1*** kết quả gần nhữ xấp xỉ nhau nên nhóm chon ***lamda=0.5*** làm kết quả cuối cùng

Đối với SIA metric thì ta thấy 83% mẫu test mình dự đoán trong vùng chấp nhận được với sai số là 1 và tiếp tục 2 độ đo SIA 0.5 và 0.25 ở mức trung bình lần lượt là 61% và 41%  trên tập test. Mô hình cho kết quả tốt hơn khi thêm hiểu chỉnh l2. Nhóm dự đoán có thể do trong quá trình review sản phẩm thì rất là khó để chúng ta phân biêt được khi nào nên rating 2, khi nào nên rating 3, nên nhóm quyết định sẽ lấy độ đo SIA 1 làm độ đo chính cho các mô hình phía sau và bên cạnh đó có 2 độ đo giúp ta giám sát nữa là MAE tính trung bình trị tuyệt đối độ chênh lệch và MSE trung bình phương độ chênh lệch.

***Với lamda=0.5:***
* learning_rate=0.1:

|Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
|-|-|-|-|-|-|
|train|0.50273|0.53481|0.84595|0.62260|0.421023|
|test|0.55699|0.65482|0.82091|0.59001|0.39600|


* learning_rate=0.5:

|Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
|-|-|-|-|-|-|
|train|0.50272|0.53481|0.85770|0.63992|0.43130|
|test|0.55698|0.65482|0.83458|0.60736|0.40702|

* learning_rate=0.75:

|Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
|-|-|-|-|-|-|
|train|0.50272|0.53481|0.85770|0.63992|0.43130|
|test|0.55698|0.65482|0.83458|0.60736|0.40702|

* learning_rate=1:

|Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
|-|-|-|-|-|-|
|train|0.50272|0.53481|0.85770|0.63992|0.43130|
|test|0.55698|0.65482|0.83458|0.60736|0.40702|

***Nhận xét:*** Khi thay đổi các giá trị learning rate thì ta thấy các với các giá trị 0.5 trờ lên thì giá trị giữa các độ đo khá xấp xỉ nhau nên ta chọn ***learning_rate=0.75*** làm giá trị cuối cùng
       
        
---

### Phương pháp gợi ý dựa trên nội dung content-based
#### Xây dựng feature vector bằng TF-IDF

Trong bộ dataset item/detail_list.csv, thì chúng ta có hơn 1000 cột chi tiết là 1000 cột lĩnh vực, 1 sản phẩm có thể thuộc nhiều lĩnh vực

***VD:*** Lĩnh vực của 1 sản phẩm là ***bách hóa online/sữa và các sản phẩm từ sữa/sữa nước/sữa chua uống & ăn*** khi đó các cột bách hóa online, sữa và các sản phẩm từ sữa và sữa nước, sữa chua uống & ăn của sản phẩm có giá trị là 1 và các cột lĩnh vực còn lại có giá trị 0.

Ta sẽ xây dựng ma trận feature vector bằng TF-IDF trong đó từng hàng của  ma trận chính là feature vector của từng sản phẩm

#### Xây dựng mô hình cho mỗi user

Sau khi có được ma trận feature vector, ta sẽ xây dựng mô hình cho riêng từng user, ở đây nhóm chúng tôi dùng mô hình hồi quy đơn giản, củ thể ở đây bọn em dùng các mô hình như hỗ quy tuyến tính (Linear Regression)  và  thêm mô hình hồi quy Ridge (Ridge Regression)

#### Hàm lỗi

$\text{RSS}(y, \hat{y}) = {\frac{1}{m} \sum\limits_{i=1}^{m} (y_i - \hat{y}_i)^2}$

$Loss(y, \hat{y}) = \text{RSS}(y, \hat{y}) + \text{Regularization_Func}$


***Đầu vào:***

* Đầu vào X của user u là feature extractor của các sản phẩm mà u đánh giá
* Đầu vào y của user u là các điểm đánh giá cho các sản phẩm mà u đã mua hoặc xem

#### Đánh giá mô hình

Kết quả:

* Mô hình Linear Regression

|Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
|-|-|-|-|-|-|
|train|0.01832|0.01603|0.99609|0.98568|0.97560|
|test|0.56011|0.69510|0.81685|0.58751|0.42547|


* Mô hình Ridge Regression:
    + ***(${\lambda}$=0.1)***

        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.03094|0.01281|0.99592|0.98588|0.97865|
        |test|0.55879|0.69046|0.81912|0.58844|0.42476|
        

    + ***(${\lambda}$=1)***
        
        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.13520|04596|0.99572|0.96206|0.83152|
        |test|0.55710|0.67331|0.82107|0.59055|0.41554|
        
        
    + ***(${\lambda}$=5)***

        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.31184|0.20825|0.94661|0.77916|0.55950|
        |test|0.55544|0.65578|0.82326|0.59001|0.40194|
    
    + ***(${\lambda}$=10)***

        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.38261|0.31053|0.90810|0.71436|0.49440|
        |test|0.55554|0.65317|0.82381|0.59102|0.39811|
        
        
    + ***(${\lambda}$=100)***

        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.48703|0.50171|0.85758|0.63940|0.43034|
        |test|0.55688|0.65435|0.82459|0.59141|0.39803|
        

        
     + ***(${\lambda}$=500)***

        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.49953|0.52794|0.85741|0.63891|0.43009|
        |test|0.55714|0.65491|0.82451|0.59181|0.39826|
    
    + ***(${\lambda}$=1000)***

         |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.49953|0.52794|0.85741|0.63891|0.43009|
        |test|0.55714|0.65491|0.82451|0.59181|0.39826|

    
                

***Nhận xét***: 

Xét trên độ đo chính mà nhóm chúng tôi sử dụng thì trên cả 2 mô hình Ridge và Linear Regression là SIA 1, ta thấy mô hình Linear Regession có 81.6% mẫu trên tập test được dự đoán thuộc vùng chấp nhận được còn mô hình Ridge với ${\lambda} = 5, 100, 100, 500, 1000$ thì cao hơn 1 chút, khoảng 82.5% mẫu trên tập test được dự đoán thuộc vùng chấp nhận được.

Tuy nhiên thì khi sử dụng mô hình linear regression thì ta thấy mô hình bị ***overfit*** quá nặng vì vậy ta sử dụng hồi quy ridge, mô hình có vẻ hiểu quả hơn hồi quy tuyến tính, sở dĩ là vì có siêu tham số alpha giúp cho hồi quy ridge chống hiện tượng overfitting.
Ta chọn ***${\lambda} = 100$***. Dễ thấy mô hình này tệ hơn mô hình Matrix factorization ở trên

---

### Ứng dụng 1 số neural network đơn giản cho bài toán rating prediction

#### Áp dụng MLP và GMF cho phương pháp phân rã ma trận matrix factorization

##### Ý tưởng

Như các bạn đã biết thì phương pháp phân rã ma trận đã đề cập ở trên thì chúng ta đi tìm 2 ma trận ẩn của người dùng và phim sao cho tích của chúng làm sao để sát với ma trận đánh giá nhất có thể là càng tốt.

Tính đơn giản của phép nhân tích vô hướng của 2 ma trận, rất khó để học được các thuộc tính ẩn của cả user và phim.

Vì vậy ở mục này nhóm chúng tôi xin đề cập tới 1 mạng phân rã ma trận nơ ron có tên là NeuMF. Sở dĩ nhóm chúng tôi đề cập tới mạng nơ ron nhân tạo ở đây bởi vì tính linh hoạt và tính phi tuyến của nó.

Ở trong mục này nhóm chúng tôi sẽ đề cập tới 2 mạng con có tên là phân rã ma trận tổng quát (***Generalized Matrix Factorization) hay GMF*** và 1 mạng con nữa là ***MLP***

nhóm chúng tôi sẽ sử dụng từng mạng một và kết hợp chúng lại với nhau và đánh giá kết quả của các mạng này ở mục sau

##### GMF - Generalized Matrix Factorization

###### Mô hình
Mạng con GMF tương tự như cấu trúc ở phương pháp Matrix Factorization nhóm chúng tôi đã đề cập ở trước với 2 ma trận tiềm ẩn user embedding của user và item embedding của film với size lần lượt là ***(num_users + 1) * latent_dim và (num_items + 1) * latent_dim***

***Trong đó:*** num_users và num_items là số lượng user và item, latent_dim là ***số đặc trưng ẩn*** của phim và user mà bạn muốn   model của bạn học.

***Vì sao lại cộng 1 trong num_users và num_items?***

Như chúng ta đã biết thì hệ thống không có số lượt user và item cố định vì vậy khi đâu vào là 1 user hoặc 1 item mới mà không có trong hệ thống trước đó thì user hoặc item đó sẽ mang giá trị là ***<OOV>(Tương tự như 1 từ không tồn tại trong từ điển)***
    
***Chú ý:*** trong quá trình cài đặt thuật toán nhóm chúng tôi có thể thêm ***Embedding regularizer l2*** để có thể tránh overfitting cho cả user và item
    
Sau khi tạo 2 ma trận tiềm ẩn cho user và item thì ta làm dãn 2 ma trận này và thực hiện tính tích 2 ma trận này (element-wise) và cuối cùng cho qua 1 lớp ***Dense size 1*** và đó chính là điểm rating được predict.
    
Cấu trúc mạng và tính toán tham số:

![](https://i.imgur.com/xEdJ6HQ.png)


    
###### Đánh giá mô hình

* Matrix Factorization đơn giản    
    |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
    |-|-|-|-|-|-|
    |train|0.50272|0.53481|0.85770|0.63992|0.43130|
    |test|0.55698|0.65482|0.83458|0.60736|0.40702|
    
* Matrix Factorization khi áp dụng thêm GMF
    ***Kernels:***
    
    * ***Glorot-normal***
    
        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.47750|1.01940|0.81559|0.77183|0.71557|
        |test|1.74336|4.13424|0.27227|0.12539|0.04804|
    
    * ***Glorot-uniform***
        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.46440|0.94953|0.81784|0.77584|0.72456|
        |test|1.64592|3.66682|0.26914|0.14102|0.06289|
    
    * ***He-normal***
        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.46788|0.97932|0.82077|0.77300|0.72133|
        |test|1.69154|3.88677|0.26914|0.13828|0.05703|
    
    * ***He-uniform***
        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.47529|1.01240|0.81657|0.77330|0.72280|
        |test|1.728366|4.03914|0.26055|0.13008|0.04805|
    
    

***Nhận xét:*** 
Hầu hết trên toàn bộ độ đo trên tập train, test, GMF tệ hơn mô hình matrix factorization. Mô hình đang bị overfit quá nặng và nhìn qua mô hình là vẫn chưa có thêm nhiều ***tính phi tuyến của mạng neural network*** như ta đã nói từ trước.
    
Ta sẽ cải thiện với mô hình dưới.    

##### MLP - Multilayer perceptron

###### Mô hình

Mô hình MLP là 1 mạng neural network đa tầng, cũng như GMF nhóm chúng tôi cũng tạo ra 2 ma trận tiềm cho user và item.
    
Sau khi qua 2 ma trận tiềm ẩn thì flatten 2 ma trận này và concatenate chúng lại với nhau.
    
***Phần chính của MLP ở đây:***
Xây dụng 1 neural network có ***num_layer(là 1 list các số nguyên mà mỗi số ứng với số node ẩn của từng tầng trừ tâng đàu tiên ra vì đó là tống số chiều đầu ra của 2 lớp embedding ẩn )*** với hàm kích hoạt là ***relu***

Và lớp cuối cùng chắc chắn là lớp ***Dense size 1*** có giá trị đầu ra là rating được dự đoán
    
Cấu trúc mạng và tính toán tham số

![](https://i.imgur.com/2OhHI6B.png)




###### Đánh giá mô hình
* Matrix Factorization đơn giản    
  |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
    |-|-|-|-|-|-|
    |train|0.50272|0.53481|0.85770|0.63992|0.43130|
    |test|0.55698|0.65482|0.83458|0.60736|0.40702|
* Mô hình MLP
    Ta sẽ đánh giá mô hình khi sử dụng 1 trong 4 kernel dưới đây
    ***Kernels:***
    
    * ***Glorot-normal***
    
        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.43510|0.36747|0.894621|0.68207|0.43407|
        |test|0.60170|0.63101|0.81680|0.53594|0.29844|
    
    * ***Glorot-uniform***
    
        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.42707|0.35788|0.89930|0.69496|0.44013|
        |test|0.58926|0.61756|0.81641|0.53790|0.30312|
    
    * ***He-normal***
    
        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.43921|0.3719|0.89529|0.68197|0.43153|
        |test|0.59377|0.62359|0.81640|0.53789|0.30313|
    
    * ***He-uniform***
    
        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.43018|0.36220|0.89744|0.69135|0.44374|
        |test|0.58838|0.61102|0.82227|0.53867|0.30977|

***Nhận xét:*** Khi sử dụng thêm mạng neural đa tầng ta thấy ngay hiệu quả , tất cả độ đo đều tốt hơn so với mô hình ***Matrix Factorization đơn giản đã đề cập trước đó***.

Khi sử dụng mạng neural ta đã thấy thêm tính phi tuyến nó hiệu quả như thế nào và trong bài toán của nhóm tôi, ***đối với mô hình MLP*** thì ***kernel He-uniform*** có vẻ ***hiểu quả hơn các kernel còn lại***   

##### Áp dụng cả GMF và MLP    

###### Mô hình
Khi ta áp dụng của GMF và MLP mô hình sẽ có cấu trúc như sau:

![](https://i.imgur.com/1Rub0MR.png)

Do áp dụng 2 mô hình lại với nhau nên ở đầu ra của mỗi mạng sẽ có 1 ma trận , khi đó ta tiếp tục concatenate 2 matrix này và cho đi qua lớp ***Dense size 1 cuối cùng*** để đưa ra kết quả rating.

Cấu trúc mạng và tính toán tham số:

![](https://i.imgur.com/gzgpZV0.png)


###### Đánh giá mô hình
* Matrix Factorization đơn giản    
   |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
    |-|-|-|-|-|-|
    |train|0.50272|0.53481|0.85770|0.63992|0.43130|
    |test|0.55698|0.65482|0.83458|0.60736|0.40702|
* Matrix Factorization khi áp dụng cả GMF và MLP 
    
    * ***Glorot-normal***
        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.37036|0.37036|0.89627|0.69398|0.43944|
        |test|0.58681|0.61751|0.82148|0.55195|0.31445|
    
    * ***Glorot-uniform***
        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.42704|0.36558|0.89695|0.69906|0.44774|
        |test|0.58149|0.61674|0.82070|0.55313|0.32461|
    
    * ***He-normal***
        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.43520|0.37083|0.89402|0.68715|0.44042|
        |test|0.59795|0.63042|0.81406|0.53789|0.30273|
    
    * ***He-normal***
        |Dataset|MAE|MSE|SIA 1|SIA 0.5|SIA 0.25|
        |-|-|-|-|-|-|
        |train|0.42195|0.35408|0.90076|0.69936|0.45106|
        |test|0.59106|0.62197|0.82266|0.53984|0.308984|



***Nhận xét:*** Khi sử dụng cả GMF và NLP ta thấy mặc dù nó hiểu quả so với mô hình ***Matrix Factorization*** thông thường nhưng mà nó gần như xấp xỉ các độ đo so với mô hình khi chi dùng MLP. Điều này chứng minh để mô hình học tốt các đặc trưng ẩn của người dùng và phim thì mô hình nên cải thiện các tham số ở NLP vì có thêm mạng GMF thì kết quả vẫn không thay đổi nhiều.
    
Đặc biệt thì ***kernel Glorot-normal*** có vẻ tốt hơn trong trường hợp này so với những kernel khác


## Hệ gợi ý

### Yêu cầu bài toán

Với nhu cầu tăng lượng doanh thu cũng như khai thác tối đa các mặt hàng hiện có sao cho phù hợp với sở thích người dùng, bài toán hệ gợi ý đang được các doanh nghiệp chú trọng phát triển. 

Trong đồ án môn học này, nhóm xét đến bài toán gợi ý top-k (Top-K Recommendation), với mô tả bài toán như sau: Với 1 user u và lịch sử tương tác {a, b, c,…}, cần đưa ra top k items mà user u có khả năng quan tâm nhất.

### Phương pháp sử dụng
Nhóm triển khai các mô hình gợi ý dựa trên mạng nơ-ron nhân tạo được đề xuất bởi He et al., 2017[1], bao gồm:
*    Generalized Matrix Factorization (GMF)
*    Multi-Layer Perceptron (MLP)
*    Neural Matrix Factorization (NMF)

Ý tưởng chính của các mô hình này đều dựa trên việc học ra biểu diễn ẩn của user và item thông qua các kiến trúc mạng nơ-ron, từ đó mô hình hoá được sở thích của user, cũng như tương tác giữa user và item.

(Phần lý thuyết của các mô hình này nhóm chúng tôi đã đề cập trong phần ***Áp dụng mạng neural cải thiện kết quả dự đoán rating***)

### Chi tiết cài đặt 

#### Huấn luyện

Phỏng theo Quyen et al., 2021[2], nhóm thực hiện huấn luyện với phương pháp negative sampling, trong đó tỉ lệ negative/positive = 4
Hàm lỗi sử dụng ở đây là Cross Entropy.

#### Xử lý dữ liệu

Với tập dữ liệu rating ban đầu thu được từ trang thương mại Tiki, nhóm thực hiện loại bỏ các user với lịch sử tương tác ít hơn 10. Thống kê chung về tập dữ liệu được trình bày trong bảng sau:

| Dataset | Tiki-Ecommerce | 
| -------- | -------- | 
| Explicit    | 56480 |
| Users    | 3450|
| Items    | 11312 |
| Sparisity    | 99.85%|

***Xử lý:***

Dựa trên phân bố rating, có thể thấy phần đa các rating thuộc vào đoạn 4-5 (chiếm gần 80%) dẫn đến việc mất cân bằng dữ liệu nghiêm trọng khi sử dụng dữ liệu tường minh (explicit). Do đó, nhóm lựa chọn chỉ sử dụng dữ liệu tiềm ẩn (implicit), trong đó một cặp user-item sẽ được gán nhãn có tương tác (1-positive) nếu tồn tại rating và không tương tác (0-negative) nếu không tồn tại rating tương ứng

#### Đánh giá:

Nhóm thực hiện đánh giá theo chiến lược leave-one-out. Item cuối trong chuỗi tương tác được dùng để đánh giá, các item còn lại dùng để huấn luyện. Sau cùng, mỗi ground-truth item (item cuối) được trộn với 99 negative items. Bài toán trở về việc xếp hạng 100 items và đánh giá theo thứ tự xếp hạng của ground-truth item.

Trong đây, nhóm sử dụng 2 độ đo phổ biến là ***Hit Ratio (HR@K)*** và ***Normalized Discounted Cumulative Count (nDCG)***.

***Hit Ratio*** là độ đo phản ánh dựa trên việc item cuối có nằm trong top K item gợi ý ra bởi hệ thống gợi ý hay không.
    ![](https://i.imgur.com/I6dXJ7f.png)


Mặt khác, ***nDCG*** đánh trọng số cao hơn cho các hệ thống gợi ý trong đó item cuối (ground-truth item) được xếp hạng cao hơn các item khác, khi nằm trong top K item được gợi ý ra.
    
![](https://i.imgur.com/KZvLGXW.png)


#### Thông số cài đặt 

Nhóm thử nghiệm với các thông số cài đặt sau:
Giải thuật học: Adam (β_1=0.9, β_2=0.999)
* Eta = {10, 1, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6}
* Latent Size = {4, 8, 16, 32, 64}
* Batch Size = 512
* Negative Sampling Ratio = 4


Kết quả tuning tham số chỉ ra các bộ tham số phù hợp với từng mô hình ***(Eta, Latent Size)***:
* GMF: Eta = 1e-1, Latent Size = 8
* MLP: Eta = 1e-2, Latent Size = 32
* NMF: Eta = 1e-2, Latent Size = 16

#### Thử nghiệm

##### Eta
    
![](https://i.imgur.com/9PUO7OE.png)


***Nhận xét:***

Nhóm thực hiện tuning tham số Eta (tốc độ học, hay learning rate), sử dụng item kề cuối làm đánh giá (validation). Từ trên đồ thị dễ thấy với cả ba mô hình, giá trị Eta hoặc quá lớn (10, 1) hoặc quá nhỏ (1e-5, 1e-6) khiến quá trình học không ổn định, hoặc quá chậm, dẫn đến kết quả chỉ ra không tốt. Với GMF, giá trị Eta tốt nhất là 1e-1, trong khi với MLP và NMF, giá trị này là 1e-2.

##### Latent Size
    
![](https://i.imgur.com/tkxfcq9.png)


***Nhận xét:***

Thực hiện tuning tương tự, ta thu được biểu đồ như trên với Latent Size (kích thước vectơ embedding của user và item trong mỗi mô hình).
Từ trên biểu đồ, có vẻ Latent Size ở mức 16 và 32 cho kết quả ổn nhất cho cả 3 mô hình. Tuy nhiên kết quả chi tiết trên tập test (trình bày ngay sau đây) cho thấy cần thực hiện tuning sát sao hơn.

##### Quá trình chạy với 50 epochs
    
![](https://i.imgur.com/KABbZss.png)


***Nhận xét:***

Với Latent Size (K) = 8, cả 3 mô hình đều cho thấy quá trình học ổn định. Về Hit Ratio, MLP cho kết quả nhỉnh hơn NMF, và thấp nhất là GMF. Về nDCG, trái lại, NMF cho kết quả tốt nhất, trong khi MLP thấp hơn, còn GMF ngang ngửa MLP. Như vậy, với K=8, NMF cho thấy khả năng mô hình hoá cặn kẽ hơn, tức các item liên quan khi được tìm thấy, có xu hướng được xếp hạng cao hơn, biểu thị sự mô hình hoá chi tiết hơn về sở thích người dùng, tuy không bao quát bằng MLP (các item liên quan được tìm thấy nhiều hơn, nhưng xu hướng xếp hạng không cao). GMF cũng cho thấy biểu hiện tương tự với K=8.

![](https://i.imgur.com/zvp7rqv.png)


***Nhận xét:***

Với K=16, MLP tiếp tục đạt kết quả tốt nhất về khía cạnh Hit Ratio, tuy nhiên vẫn thấp hơn chút so với NMF về nDCG. GMF cho kết quả hơi thấp hơn với K=8, đồng thời chênh lệch đáng kể với NMF và MLP.

![](https://i.imgur.com/CLSwPz4.png)


***Nhận xét:***

Với K=32, quá trình học của GMF trở nên bất ổn định, điều này biểu thị rõ ràng trên đồ thị, khi mà kết quả dao động liên tục ở cả hai độ đo. Như vậy, GMF không hoạt động tốt với K=32, và nhìn chung, kết quả cũng không cao với K=16, khi so với K=8. Trái lại, MLP vẫn cho kết quả tốt, thậm chí nhỉnh hơn một chút, so với K=16. NMF có kết quả thấp hơn, thậm chí chêch lệnh lớn với MLP theo Hit Ratio và chỉ ngang bằng với MLP theo nDCG. Ở giai đoạn giữa thậm chí NMF bị MLP vượt lên trước với nDCG.

***Qua đây, có thể thấy được, các giá trị Latent Size tốt nhất với GMF, MLP, NMF lần lượt là 8, 32, 16.***


##### Negative Sampling

![](https://i.imgur.com/toUyX3w.png)
    
***Nhận xét:***

Tuy nhóm không thực hiện tuning với Negative Sampling Ratio, một thí nghiệm nhỏ khác chứng minh hiệu quả của việc dùng Negative Sampling so với chỉ huấn luyện thông thường.
Cả 3 mô hình được huấn luyện và kiểm thử trên tập test sau 10 epochs, ký hiệu 0- đối với huấn luyện thường và 4- với việc dùng Negative Sampling (ratio = 4). Đồ thị biểu hiễn rõ ràng khi dùng Negative Sampling, kết quả của các mô hình được cải thiện đáng kể.

##### Top-K

![](https://i.imgur.com/O4d4AD0.png)

***Nhận xét:***

Ở phần chạy thử với 50 epochs, ta thấy được NMF có xu hướng cho giá trị nDCG tốt hơn MLP, tuy hơi thấp hơn về Hit Ratio. Ở đây thực hiện một thử nghiệm khác, với số epochs ít hơn để tiết kiệm thời gian, khi cho K (Top-K) thay đổi từ 1-10, ta thu được đồ thị như hình. Dễ thấy với K thấp, thì Hit Ratio của NMF cao hơn hẳn MLP, tương tự GMF cũng cao hơn (K=1, 2) nhưng khi K tăng thì MLP lại vượt lên, tuy ở đây vẫn giữ ngang mức với NMF chứ chưa vượt hẳn như thí nghiệm trên. Song, chỉ từ Hit Ratio, ta lý giải được tại sao NMF cho giá trị nDCG cao hơn hẳn MLP ở đồ thị con bên phải, từ đó có một góc nhìn thú vị.

##### Đánh giá sau cùng:

![](https://i.imgur.com/Kcj5gGW.png)


***Nhận xét:***

Về kết quả cuối trên tập test, MLP cho kết quả cao nhất với HR@10, trong khi NMF-Pretrain (khởi tạo trọng số từ weight của MLP và GMF) cho kết quả tốt nhất với nDCG@10, tuy không cải thiện nhiều với NMF. GMF đạt kết quả thấp nhất, có thể do kiến trúc đơn giản nhất trong các mô hình trên, do đó chưa mô hình hoá được tốt biểu diễn của người dùng. NMF tuy thấp hơn MLP về HR@10, nhưng cho kết quả cao hơn về nDCG@10.

#### Một vài case study

* Case study 1:

![](https://i.imgur.com/sNsvmTE.png)


Nhìn chung, người dùng này có sở thích với đồ gia dụng và bách hoá, chăm sóc sức khoẻ và làm đẹp. Một số sản phẩm kể đến như máy xay thịt, tông đơ, đồ ăn (khô gà, mực sợi), vật phẩm dưỡng da (tinh chất dưỡng ẩm, sữa rửa mặt, kem dưỡng ẩm). Đây là một người dùng có sở thích khá đa dạng

![](https://i.imgur.com/edzyGzS.png)


Với GMF, về khía cạnh thể loại, đã gợi ý ra một vài sản phẩm khá hợp lý, như sữa đậu nành (người dùng có mua sữa chua), bắp giò heo, cơm cháy (đồ ăn), dầu gội (liên hệ với tông đơ), đèn bàn học (liên hệ với do-choi-me-be). Tuy nhiên, một số sản phẩm còn chưa hợp lý, như gợi ý TP-Link, hay Cát Vệ Sinh cho Mèo (dù cùng thể loại bách hoá nhưng không gần với sở thích người dùng).

![](https://i.imgur.com/out3UY3.png)


Bên cạnh các gợi ý tốt (chanh, đèn bàn học, kem chống nắng, tất nữ, bông trang điểm), thì MLP cũng có những gợi ý chưa hợp lý như cảm biến áp suất oto, hay áo bóng đá (người dùng có sở thích với fitness, chứ chưa hẳn là với bóng đá)

![](https://i.imgur.com/loEMjDM.png)


Được cho là kết hợp của cả 2, NMF cũng có những kết quả hợp lý (nồi chiên không dầu, sữa đậu nành, sữa bột, yến mạch, đồ chơi lắp ráp, kem chống nắng) và chưa hợp lý (USB, Ví nam da bò, đồng hồ nam).

* Case study 2:

![](https://i.imgur.com/ODaH331.png)


Case Study 2 thuộc về một người dùng có sở thích nội trợ, toàn bộ đều là về thực phẩm

![](https://i.imgur.com/1szXEiz.png)


Kết quả gợi ý của GMF khá tệ, ngoại trừ trà oolong có một ít liên quan, còn lại đều là các vật phẩm không liên hệ với sở thích người dùng.

![](https://i.imgur.com/kyN9heD.png)


Kết quả của MLP có một chút trùng với GMF, nhưng đã tốt hơn với các gợi ý hợp lý như tỏi, chả giò.
![](https://i.imgur.com/osP8RXi.png)


NMF cũng có hai kết quả liên quan (Bánh bột lọc, cam sành), nhưng còn lại thì chưa hợp lý.

* Case study 3:

![](https://i.imgur.com/3mlZLss.png)

Case Study cuối thuộc về một người dùng nữ, có sở thích về thời trang, làm đẹp, và nội trợ chung (quan tâm về máy giặt, nồi chảo).

![](https://i.imgur.com/IYaVsN1.png)


GMF gợi ý ra một vài kết quả hợp lý (Kem dưỡng giảm mụn, giày vải nữ, mặt dây chuyền), nhưng phần đa vẫn là các gợi ý không liên quan.

![](https://i.imgur.com/1sgGcWT.png)

    
Với MLP, hầu hết vẫn là các kết quả gợi ý không liên quan, ngoại trừ áo thun.

![](https://i.imgur.com/LtK50a3.png)

    
Với NMF, kết quả khá khẩm hơn chút khi gợi ý ra được dụng cụ cho nội trợ, việc nhà như cây lau nhà, dép đi trong  nhà, nước rửa tay hay kệ chén bát, bên cạnh áo thun. Tuy nhiên, các kết quả khác như dây mạng, quần lót nam, vốn không liên hệ đến lịch sử người dùng, biểu thị chúng ta cần xây dựng hệ gợi ý phù hợp hơn và cải tiến nhiều hơn, trước khi cài đặt trong hệ thống thực.
















