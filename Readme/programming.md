<h2>Mô hình triển khai</h2>
<br>Người thực hiện: Nguyễn đình thái
<br>Ngày: 12/07/2017

<h3>Mô hình triển khai</h3>
Triển khai theo mô hình 2 lớp
Presentation Layers
Lớp này làm nhiệm vụ giao tiếp với người dùng cuối để thu thập dữ liệu và hiển thị kết quả/dữ liệu thông qua các thành phần trong giao diện người sử dụng.

Business Logic Layer

Đây là layer xử lý chính các dữ liệu trước khi được đưa lên hiển thị trên màn hình hoặc xử lý các dữ liệu.
Đây là nơi đê kiểm tra ràng buộc, các yêu cầu nghiệp vụ, tính toán, xử lý các yêu cầu và lựa chọn kết quả trả về cho Presentation Layers.

Cách vận hành của mô hình

Yêu cầu được xử lý tuần tự qua các layer như hình.
- Đầu tiên User giao tiếp với Presentation Layers (GUI) để gửi đi thông tin và yêu cầu. Tại layer này, các thông tin sẽ được kiểm tra, nếu OK chúng sẽ được chuyển xuống Business Logic Layer (BLL).

- Tại BLL, các thông tin sẽ được nhào nặn, tính toán theo đúng yêu cầu đã gửi, BLL sẽ gửi trả kết quả về GUI
<img src='/img/2_TIER.png'>


<h2>chuẩn lập trình</h2>

Code chúng ta viết cần phải theo phong cách, quy định chung để mọi người đều có thể dễ dàng đọc hiểu, kết hợp, kiểm tra, bảo trì và tái sử dụng. 
Code được viết theo phong cách chung là thể hiện cách làm việc chuyên nghiệp, cẩn thận, có nguyên tắc Khi làm việc với ngôn ngữ lập trình nào, nên tuân thủ phong cách lập trình cụ thể của ngôn ngữ đó, tránh việc phối hợp nhiều phong cách trong một ngôn ngữ Phong cách lập trình được xem là một “nền văn hóa chung” mà chắc chắn là các lập trình viên cần tìm hiểu “nền văn hóa chung đó”. 
Các phong cách này theo tiêu chuẩn PEP 8 - được công bố chính thức trên website Python
 
Một số quy tắc
	Thụt đầu dòng
* Mỗi khối lệnh thụt vào 4 dấu cách
* Ngắt dòng code dài bằng cách xuống dòng, thụt vào 8 dấu cách
	Không được phép sử dụng tab và dấu cách trắng lẫn lộn. Ưu tiên chương trình sử dụng nguyên dấu cách trắng, không sử dụng dấu tab. Để làm điều này bạn cài đặt trên trình soạn thảo (Editor/ IDE) của bạn để khi gõ tab thì tạo ra 4 dấu cách trắng
	Sử dụng 2 dòng trắng trước mỗi class và 1 dòng trắng trước mỗi hàm
	Tránh sử dụng dấu cách trắng trong các trường hợp:
	Ngay sau dấu mở ngoặc và ngay trước khi đóng ngoặc.
	Ngay trước dấu : ; , các phép toán
	Ngay trước dấu mở ngoặc của hàm
	Ngay trước dấu mở ngoặc của dict
	Chỉ một dấu cách cho mỗi khoảng trắng

xem chi tiết tại <a href="http://csc.edu.vn/lap-trinh-di-dong/tin-tuc/Tin-dao-tao-LTDD/10-dieu-nen-biet-ve-phong-cach-viet-code-Python-Theo-tieu-chuan-PEP8-776
">đây </a>

