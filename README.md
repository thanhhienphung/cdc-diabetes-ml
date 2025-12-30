# Project: Hệ thống Dự đoán Nguy cơ Tiểu đường (Diabetes Prediction System)

Dự án này sử dụng Machine Learning để dự đoán nguy cơ mắc bệnh tiểu đường dựa trên các chỉ số sức khỏe và thói quen sinh hoạt.

## 1. Thông tin Dataset

* **Nguồn dữ liệu:** CDC Diabetes Health Indicators.
* **Tên file:** `./diabetes_012_health_indicators_BRFSS2015.csv`
* **Mô tả:** Bộ dữ liệu bao gồm các chỉ số khảo sát sức khỏe từ hệ thống BRFSS.
* **Raw CSV Header (Danh sách cột nguyên bản):**
  ```text
  Diabetes_012,HighBP,HighChol,CholCheck,BMI,Smoker,Stroke,HeartDiseaseorAttack,PhysActivity,Fruits,Veggies,HvyAlcoholConsump,AnyHealthcare,NoDocbcCost,GenHlth,MentHlth,PhysHlth,DiffWalk,Sex,Age,Education,Income
  ```

---

## 2. Cấu trúc Dữ liệu (Data Structure)

Dữ liệu được chia thành 2 phần chính để đưa vào mô hình: **Input (X)** và **Output (y)**.

### Output (Target - y)
Đây là cột nhãn (Label) mà mô hình cần dự đoán.

* **Tên cột:** `Diabetes_012`
* **Ý nghĩa:**
    * `0`: Không bị tiểu đường (Non-diabetic)
    * `1`: Tiền tiểu đường (Pre-diabetic)
    * `2`: Bị tiểu đường (Diabetic)

### Input (Features - X)
Bao gồm **21 cột** thông tin dùng để phân tích.

| STT | Tên cột (Feature Name) | Mô tả ngắn gọn | Giá trị điển hình |
|:---:|:---|:---|:---|
| 1 | `HighBP` | Huyết áp cao | 0 = Không, 1 = Có |
| 2 | `HighChol` | Cholesterol cao | 0 = Không, 1 = Có |
| 3 | `CholCheck` | Kiểm tra Cholesterol trong 5 năm | 0 = Không, 1 = Có |
| 4 | `BMI` | Chỉ số khối cơ thể | Số thực (VD: 25.0, 30.0) |
| 5 | `Smoker` | Hút thuốc (ít nhất 100 điếu cả đời) | 0 = Không, 1 = Có |
| 6 | `Stroke` | Từng bị đột quỵ | 0 = Không, 1 = Có |
| 7 | `HeartDiseaseorAttack` | Bệnh tim mạch vành / Đau tim | 0 = Không, 1 = Có |
| 8 | `PhysActivity` | Hoạt động thể chất (trong 30 ngày) | 0 = Không, 1 = Có |
| 9 | `Fruits` | Ăn hoa quả (ít nhất 1 lần/ngày) | 0 = Không, 1 = Có |
| 10 | `Veggies` | Ăn rau xanh (ít nhất 1 lần/ngày) | 0 = Không, 1 = Có |
| 11 | `HvyAlcoholConsump` | Uống nhiều rượu bia | 0 = Không, 1 = Có |
| 12 | `AnyHealthcare` | Có bảo hiểm y tế | 0 = Không, 1 = Có |
| 13 | `NoDocbcCost` | Không đi khám vì thiếu tiền | 0 = Không, 1 = Có |
| 14 | `GenHlth` | Tự đánh giá sức khỏe chung | Thang 1 (Rất tốt) -> 5 (Rất kém) |
| 15 | `MentHlth` | Trong 30 ngày qua, có bao nhiêu ngày bạn cảm thấy tâm lý không tốt (như căng thẳng, trầm cảm, buồn bã, lo âu) | 0 -> 30 ngày |
| 16 | `PhysHlth` | Trong 30 ngày qua, có bao nhiêu ngày bạn cảm thấy cơ thể không khỏe (bị ốm, đau nhức, chấn thương) | 0 -> 30 ngày |
| 17 | `DiffWalk` | Khó khăn khi đi bộ/leo thang | 0 = Không, 1 = Có |
| 18 | `Sex` | Giới tính | 0 = Nữ, 1 = Nam |
| 19 | `Age` | Nhóm tuổi | 1 (18-24 tuổi) -> 13 (80+ tuổi) |
| 20 | `Education` | Trình độ học vấn | 1 (Chưa hết cấp 2) -> 6 (Đại học+) |
| 21 | `Income` | Mức thu nhập | 1 (<$10k) -> 8 (>$75k) |

---

## 3. Các bước cần thực hiện (To-Do List)

Dưới đây là lộ trình các bước kỹ thuật cần làm để training model:

### Bước 1: Chuẩn bị Dữ liệu (Data Preparation)
- [ ] Load file `.csv` bằng thư viện Pandas.
- [ ] Tách cột `Diabetes_012` ra làm biến **y** (Target).
- [ ] Tách 21 cột còn lại ra làm biến **X** (Features).
- [ ] Chia dữ liệu thành tập Train và Test (ví dụ: tỉ lệ 80/20).

### Bước 2: Xây dựng Model (Model Training)
- [ ] Lựa chọn thuật toán (Gợi ý: Random Forest, Decision Tree, hoặc Logistic Regression).
- [ ] Huấn luyện model trên tập Train (`model.fit(X_train, y_train)`).

### Bước 3: Đánh giá (Evaluation)
- [ ] Chạy thử dự đoán trên tập Test.
- [ ] Tính độ chính xác (Accuracy, Confusion Matrix).
- [ ] Kiểm tra xem model dự đoán đúng lớp bị bệnh (Class 2) tốt hay không.

### Bước 4: Lưu Model
- [ ] Lưu model đã train ra file (ví dụ `.pkl`) để sử dụng.

---
*File được tạo tự động hỗ trợ cho dự án Diabetes Prediction.*
---

## 4. Web Portal (Django)

This repository now includes a Django web portal that mirrors the structure of the
ml-deployment-starter project.

### Quick start
1. python -m venv .venv
2. .\.venv\Scripts\Activate
3. pip install -r requirements.txt
4. python src/train_diabetes_model.py
5. python manage.py migrate
6. python manage.py runserver 8000

Open http://127.0.0.1:8000/ to use the portal.

### API
POST http://127.0.0.1:8000/api/diabetes-predict

Body (JSON):
{
  "features": {
    "HighBP": 1,
    "HighChol": 1,
    "CholCheck": 1,
    "BMI": 31.4,
    "Smoker": 0,
    "Stroke": 0,
    "HeartDiseaseorAttack": 0,
    "PhysActivity": 1,
    "Fruits": 1,
    "Veggies": 1,
    "HvyAlcoholConsump": 0,
    "AnyHealthcare": 1,
    "NoDocbcCost": 0,
    "GenHlth": 3,
    "MentHlth": 2,
    "PhysHlth": 4,
    "DiffWalk": 0,
    "Sex": 1,
    "Age": 8,
    "Education": 4,
    "Income": 5
  }
}
