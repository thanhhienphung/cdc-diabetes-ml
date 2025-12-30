1. Phần "1.2. Thách thức kỹ thuật" hoặc "2.1. Phân tích bộ dữ liệu"
Vấn đề: Người đọc khó hình dung mức độ nghiêm trọng của việc "mất cân bằng dữ liệu" chỉ qua con số.

Hình ảnh nên có: Biểu đồ tròn (Pie Chart) hoặc Biểu đồ cột (Bar Chart) so sánh tỷ lệ giữa lớp "Khỏe mạnh" và lớp "Tiểu đường".

Mục đích: Cho thấy miếng bánh "Người bệnh" nhỏ bé như thế nào so với miếng bánh "Người khỏe", minh họa trực quan cho khái niệm "Mò kim đáy bể".

2. Phần "4.1. Kiến trúc mô hình: Stacking Ensemble"
Vấn đề: Khái niệm "Xếp chồng", "Level-0", "Level-1" khá trừu tượng nếu chỉ diễn giải bằng lời.

Hình ảnh nên có: Sơ đồ khối (Flowchart/Block Diagram) của hệ thống Stacking.

Mô tả: Vẽ 3 mũi tên từ Dữ liệu gốc đi vào 3 mô hình (XGBoost, Random Forest, Logistic). Sau đó 3 mũi tên từ kết quả của chúng chụm lại đi vào mô hình tổng hợp (Meta Learner) rồi mới ra kết quả cuối cùng.

Mục đích: Giúp người xem hiểu ngay luồng đi của dữ liệu chỉ trong 1 giây.

3. Phần "4.2. Chiến lược xử lý mất cân bằng: SMOTE"
Vấn đề: Khó hiểu về việc "tạo ra người bệnh ảo" (sinh mẫu nhân tạo) hoạt động như thế nào.

Hình ảnh nên có: Biểu đồ phân tán (Scatter Plot) so sánh Trước và Sau.

Hình trái: Các điểm dữ liệu bệnh (màu đỏ) rất thưa thớt.

Hình phải (Sau khi SMOTE): Các điểm màu đỏ dày đặc hơn, xen kẽ vào các khoảng trống.

Mục đích: Minh họa cách SMOTE làm giàu dữ liệu.

4. Phần "4.3. Hậu xử lý: Hiệu chỉnh xác suất (Calibration)"
Vấn đề: Khái niệm "đường cong tin cậy" rất khó hình dung.

Hình ảnh nên có: Biểu đồ Đường cong tin cậy (Reliability Curve/Calibration Plot).

Mô tả: Một biểu đồ có đường chéo 45 độ (đường lý tưởng). Đường biểu diễn của mô hình chưa hiệu chỉnh sẽ cong lệch ra xa (hình chữ S), còn đường sau khi hiệu chỉnh sẽ bám sát đường chéo này.

Mục đích: Chứng minh trực quan rằng sai số dự báo đã được giảm thiểu.

5. Phần "5.2. Kết quả so sánh chi tiết"
Vấn đề: Bảng số liệu tuy chi tiết nhưng khó so sánh nhanh.

Hình ảnh nên có: Biểu đồ cột nhóm (Grouped Bar Chart).

Mô tả: So sánh chỉ số Recall giữa 3 phương pháp (XGBoost gốc vs Stacking vs Stacking+SMOTE). Cột của Stacking+SMOTE cao vọt lên sẽ tạo ấn tượng thị giác mạnh mẽ về hiệu quả nghiên cứu.

6. Phần "5.3. Khả năng giải thích"
Vấn đề: Liệt kê tên biến (BMI, Huyết áp...) thì hơi khô khan.
Hình ảnh nên có: Biểu đồ SHAP Summary Plot (Dạng Beeswarm).

Mục đích: Đây là biểu đồ tiêu chuẩn trong các báo cáo hiện đại. Nó thể hiện màu sắc (đỏ/xanh) tương ứng với giá trị cao/thấp của từng biến ảnh hưởng thế nào đến nguy cơ bệnh. Ví dụ: Các điểm BMI màu đỏ (cao) sẽ tập trung về phía bên phải (tăng nguy cơ).