# ĐỀ TÀI: ỨNG DỤNG KỸ THUẬT ENSEMBLE LEARNING VÀ CALIBRATION TRONG SÀNG LỌC SƠ CẤP NGUY CƠ TIỂU ĐƯỜNG
*(Data Mining Application for Primary Diabetes Risk Screening using Ensemble Learning & Probability Calibration)*

## 1. Lý do chọn đề tài và Xác định phạm vi tiếp cận
### 1.1. Vấn đề thực tế
Bệnh tiểu đường là bệnh mạn tính phổ biến nhưng thường phát hiện muộn. Các phương pháp chẩn đoán lâm sàng chính xác (như xét nghiệm máu HbA1c, OGTT) thường xâm lấn, tốn kém và đòi hỏi thiết bị y tế chuyên dụng.

### 1.2. Phạm vi tiếp cận: Từ "Chẩn đoán Y khoa" sang "Sàng lọc Dữ liệu"
Dựa trên phản hồi về tính chuyên môn, đề tài xác định rõ giới hạn nghiên cứu để tận dụng thế mạnh của Khai phá dữ liệu (Data Mining):

*   **Không làm chẩn đoán (Diagnosis):** Đề tài không thay thế bác sĩ hay xét nghiệm sinh hóa để kết luận bệnh.
*   **Tập trung vào sàng lọc (Screening):** Mục tiêu là xây dựng công cụ **phi xâm lấn, chi phí thấp** để phân loại nhóm nguy cơ cao trong cộng đồng. Những trường hợp này sau đó mới được khuyến nghị đi xét nghiệm y tế.
*   **Dựa trên bằng chứng dữ liệu (Data-driven):** Các biến đầu vào (Huyết áp, BMI, thói quen) được kế thừa từ bộ chuẩn khảo sát **BRFSS của CDC Hoa Kỳ**, đảm bảo tính tin cậy y học mà không cần người thực hiện phải tự định nghĩa các yếu tố nguy cơ.

## 2. Mô tả bộ dữ liệu (Dataset Description)
*   **Tên dataset:** `diabetes_012_health_indicators_BRFSS2015.csv`
*   **Nguồn dữ liệu:** *Behavioral Risk Factor Surveillance System (BRFSS 2015)* - CDC Hoa Kỳ.
*   **Quy mô:** Khoảng **250.000 bản ghi**.
*   **Đặc điểm:** Dữ liệu dạng bảng (tabular), bao gồm 22 đặc trưng (features).

### 2.1. Biến mục tiêu (Target Variable)
Biến `Diabetes_012` phân loại 3 lớp:
*   `0`: Không tiểu đường
*   `1`: Tiền tiểu đường
*   `2`: Tiểu đường
*(Thách thức kỹ thuật: Dữ liệu có sự mất cân bằng lớp nghiêm trọng cần xử lý)*

### 2.2. Các đặc trưng đầu vào (Input Features)
Dữ liệu bao gồm các nhóm biến được y học công nhận là yếu tố nguy cơ:

*   **Chỉ số sức khỏe:** `HighBP` (Huyết áp), `HighChol` (Mỡ máu), `BMI` (Chỉ số cơ thể), `Stroke` (Tiền sử đột quỵ), `HeartDiseaseorAttack` (Bệnh tim)...
*   **Lối sống:** `Smoker` (Hút thuốc), `PhysActivity` (Vận động), `Fruits`/`Veggies` (Chế độ ăn), `HvyAlcoholConsump` (Rượu bia), `SleepTime` (Giấc ngủ).
*   **Nhân khẩu & Xã hội:** `Age`, `Sex`, `Education`, `Income`.

## 3. Câu hỏi nghiên cứu và Hướng giải quyết (Research Questions & Hypotheses)
Đề tài tập trung giải quyết các thách thức kỹ thuật trong khai phá dữ liệu y tế:

### RQ1: Tối ưu hóa độ nhạy (Recall) trong dữ liệu mất cân bằng
**Câu hỏi:** *Việc áp dụng các kỹ thuật học máy (Cost-sensitive learning / Resampling) giải quyết vấn đề **mất cân bằng dữ liệu** như thế nào để tối đa hóa chỉ số **Recall**, giảm thiểu tỷ lệ âm tính giả (False Negative) trong bài toán sàng lọc y tế?*

**Trả lời & Hướng giải quyết:**
*   Trong y tế, việc bỏ sót người bệnh (False Negative) nguy hiểm hơn báo nhầm người khỏe (False Positive). Tuy nhiên, các mô hình mặc định thường tối ưu Accuracy và bỏ qua lớp thiểu số (người bệnh).
*   **Giải pháp:** Sử dụng kỹ thuật **SMOTE** (Synthetic Minority Over-sampling Technique) để sinh dữ liệu mẫu cho lớp bệnh, kết hợp với gán trọng số lớp (**Class Weights**) trong hàm mất mát của thuật toán để "phạt" nặng hơn khi mô hình dự đoán sai người có bệnh. Mục tiêu là đẩy **Recall lên mức cao nhất có thể** chấp nhận được.

### RQ2: Độ tin cậy của xác suất dự báo (Probability Calibration)
**Câu hỏi:** *Kỹ thuật **Stacking Ensemble** kết hợp với **Probability Calibration** có cải thiện độ chính xác và độ tin cậy của xác suất dự báo (Calibration Curve) so với các mô hình đơn lẻ hay không?*

**Trả lời & Hướng giải quyết:**
*   Các mô hình phức tạp như Random Forest hay Boosting thường cho kết quả phân lớp tốt nhưng xác suất dự báo (probability score) thường không chuẩn (bị lệch, over-confident). Ví dụ: Mô hình báo 90% nguy cơ, nhưng thực tế nhóm đó chỉ có 60% bị bệnh.
*   **Giải pháp:**
    1.  Dùng **Stacking Ensemble**: Kết hợp điểm mạnh của Logistic Regression (tuyến tính) và XGBoost (phi tuyến) để tạo biên quyết định vững chắc hơn.
    2.  Áp dụng **Calibration (Isotonic Regression/Platt Scaling):** Hiệu chỉnh đầu ra để xác suất dự báo khớp với tần suất mắc bệnh thực tế. Điều này giúp ứng dụng Web đưa ra con số % rủi ro đáng tin cậy cho người dùng tham khảo.

## 4. Phương pháp nghiên cứu (Methodology)

### 4.1. Pipeline xử lý dữ liệu
1.  **Preprocessing:** Mã hóa biến category, chuẩn hóa (Scaling) các biến số như BMI, SleepTime.
2.  **Imbalance Handling:** Xử lý dữ liệu mất cân bằng (như đã nêu ở RQ1).
3.  **Data Splitting:** Chia tập Train/Test theo phương pháp phân tầng (Stratified) để giữ nguyên tỷ lệ nhãn bệnh.

### 4.2. Chiến lược mô hình hóa (Modeling Strategy)
Hệ thống sử dụng kiến trúc **Stacking Ensemble**:
*   **Lớp cơ sở (Base Learners):** Logistic Regression, Random Forest, XGBoost.
*   **Lớp tổng hợp (Meta Learner):** Logistic Regression để tổng hợp kết quả.
*   **Hậu xử lý (Post-processing):** Probability Calibration để làm mượt xác suất.

## 5. Đánh giá và Giải thích (Evaluation & Explainability)

### 5.1. Chỉ số đánh giá (Metrics)
*   **Recall (Sensitivity):** Chỉ số quan trọng nhất (trả lời RQ1).
*   **F1-Score:** Đánh giá tổng quát.
*   **ROC-AUC:** Đánh giá khả năng phân loại.
*   **Brier Score & Calibration Curve:** Đánh giá độ tin cậy của xác suất (trả lời RQ2).

### 5.2. Khả năng giải thích (Explainable AI)
Sử dụng **SHAP (SHapley Additive exPlanations)** để minh bạch hóa mô hình:
*   **Feature Importance:** Xác định yếu tố nào (BMI, Tuổi, Huyết áp...) ảnh hưởng lớn nhất đến mô hình.
*   **Local Interpretation:** Giải thích lý do tại sao một người cụ thể bị dự báo nguy cơ cao, từ đó đưa ra gợi ý thay đổi lối sống.

## 6. Sản phẩm dự kiến
1.  **Mô hình học máy:** Đạt AUC > 0.85, Recall lớp bệnh cao và Brier Score thấp.
2.  **Web Application:** Giao diện cho phép người dùng nhập chỉ số và nhận về:
    *   Mức độ rủi ro (Low / Medium / High).
    *   Xác suất mắc bệnh đã được hiệu chỉnh (%).
    *   Phân tích SHAP: "Bạn có nguy cơ cao chủ yếu do chỉ số BMI > 30 và Tiền sử huyết áp cao".

## 7. Kế hoạch thực hiện (Timeline)
*   **Tuần 1:** Phân tích dữ liệu (EDA), nghiên cứu phân phối biến.
*   **Tuần 2:** Xây dựng pipeline, thực nghiệm các kỹ thuật xử lý mất cân bằng.
*   **Tuần 3:** Huấn luyện Stacking Ensemble, thực hiện Calibration và đánh giá SHAP.
*   **Tuần 4:** Đóng gói mô hình, xây dựng giao diện Web demo.