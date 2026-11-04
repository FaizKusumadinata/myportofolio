Nama : Faiz Kusumadinata
NPM : 2406426196
Kelas : PBP E
Tanggal Lahir: 6 November 2006

### Tugas 1

1. Iya, saya menggunakan salah satu elemen semantik HTML5, yaitu '<section>'. Elemen semantik tersebut sangat membantu dalam membagi bagian-bagian utama dalam bagian main, sehingga memudahkan proses mendekorasi website.

2. Tantangan yang sering saya hadapi adalah membuat penampilan elemen dan posisinya tampak lebih rapi dan bagus. Terdapat banyak elemen-elemen yang harus saya terus menerus ubah untuk menyesuaikan perubahan ukuran tampilan browser. Saya menyelesaikan masalah tersebut dengan mengganti beberapa properti elemen-elemen seperti gambar atau div dengan properti yang dapat menyesuaikan diri dengan tampilan browser.

3. Saya merasa static web membatasi saya dari melakukan update untuk konten-konten saya di dalamnya. Saya juga merasa terdapat banyak keterbatasan fungsionalitas. Untuk proyek selanjutnya, saya ingin menambahkan laman yang akan saya gunakan untuk menampilkan portofolio seni dan tulisan saya dan menambahkan fungsionalitas yang mempermudah saya mengupload dan mengupdatenya.

AI Disclosure.
Dalam pengerjaan Tugas-1 PBP ini, saya tidak menggunakan AI. Sumber utama saya dalam mempelajari materi untuk tugas ini adalah W3school.com dan StackOverflow.

### tugas 2

1. Ketika halaman portofolio, diakses, maka urls.py akan memanggil views.py untuk mencari fungsi yang sesuai request, kemudian fungsi tersebut akan mengambil data dari models.py dan menampilkannya pada templates.py yang sudah dikonfigurasikan padanya.

2. Data pada portofolio disimpan dalam Model untuk memberi kemudahan ketika ingin kembali menciptakan data dengan atribut yang sama. Hal ini mempermudah developer dalam menciptakan data baru tanpa harus membuatnya dari awal lagi, mengikuti prinsip DRY(Don't Repeat Yourself).

3. makemigrations membuat file yang berisi perubahan pada models.py, sedangkan migrations melakukan proses migrasi file tersebut ke database. Sebagai contoh, ketika seorang developer menambahkan atau menghapus atribut pada sebuah Class Model, atau menciptakan Class Model baru, dia harus melakukan makemigrations kemudian migrate.

AI Disclosure.
Dalam pengerjaan Tugas-2 PBP ini, saya tidak menggunakan AI. Sumber utama saya dalam mempelajari materi untuk tugas ini adalah W3school.com, geeksforgeeks.org, dan StackOverflow.

### tugas 3

1. Penggunaan ModelForm akan mempermudah developer untuk menciptakan form yang sesuai dengan setiap atribut model tanpa perlu melakukannya murni dari awal. Adapun csrf token berfungsi untuk menghasilkan sebuah token unik untuk mencegah request ke halaman developer ditiru oleh pihak lain, sehingga melindungi data yang pengguna kirim ke website.

2. Developer website lebih memilih JSON daripada XML karena JSON lebih efisien dan cepat dalam mengolah data. JSON juga lebih mudah untuk dibaca oleh manusia maupun komputer.

3. Ketika JSON mengambil data melalui fungsi dari views.py, data yang diambil masih berada dalam bentuk mentah dan belum bisa dibaca oleh manusia, sehingga memerlukan proses serialization terlebih dahulu.

AI Disclosure.
Dalam pengerjaan Tugas-3 PBP ini, saya tidak menggunakan AI. Sumber utama saya dalam mempelajari materi untuk tugas ini adalah W3school.com, geeksforgeeks.org, dan StackOverflow.

### tugas 4
AI Disclosure.
Dalam pengerjaan Tugas-4 PBP ini, saya tidak menggunakan AI. Sumber utama saya dalam mempelajari materi untuk tugas ini adalah W3school.com, geeksforgeeks.org, dan StackOverflow.

### tugas 5
1. Debouncing adalah teknik menghentikan sebuah fungsi untuk sementara hingga dapat dipastikan tidak ada event baru. Debouncing berguna untuk mencegah fungsi terus menerus berjalan selama user meng-input data untuk search AJAX.

2. await berfungsi untuk menahan kinerja sebuah fungsi async yang sedang berjalan tanpa memengaruhi javascript. Ketika menggunakan fetch() tanpa await, maka API akan mendapatkan sebuah promise, bukan Response HTTP.

3. XSS(Cross Site Scripting) adalah serangan ke script client-side sebuah web. Penyerang dapat mengambil data klien, membajak akun, me-redirect klien ke situs lain, dan bahkan mengirim malware. Javascript/AJAX lebih rentan terhadap serangan ini daripada template Django karena kurangnya fitur keamanan built-in.

AI Disclosure.
Dalam pengerjaan Tugas-5 PBP ini, saya tidak menggunakan AI. Sumber utama saya dalam mempelajari materi untuk tugas ini adalah W3school.com, geeksforgeeks.org, dan modul PBP yang disediakan di Scele.

Non-Admin Accounts and Passwords:
1. BatmanFan1939 : jonkler@74
2. stephen_king : tommyknockers8

### tugas 6
1. REST merupakan singkatan dari Representational State Transfer dan merupakan sebuah gaya arsitektur dalam merancang API sebuah web yang mengutamakan agar website menjadi RESTful. JSON saja belum cukup karena JSON yang dikembalikan dapat menjadi tidak terstruktur. Penggunaan RESTful API membantu JSON menjadi lebih terstruktur. Adapun perbedaan antara request PUT dan PATCH adalah PUT dapat menggantikan dan mengubah data secara keseluruhan, sedangkan PATCH hanya mengubah bagian-bagian tertentu saja dari data.

2. Serializer pada Django REST Framework berfungsi mengubah data Python ke bentuk JSON. Serializer ini memiliki keuntungan dibandingkan merakit dictionary secara manual pada JSONResponse karena serialzernya akan secara otomatis mengecek model Django yang digunakan untuk membuat field yang sesuai, sehingga developer tidak perlu membuat lagi dictionary field secara manual.

3. Dalam Django REST Framework, Autentikasi adalah proses mengidentifikasi pengguna untuk kemudian dicek menggunakan permissions untuk menentukan otorisasi pengguna yang merupakan hak aksesnya terkait data dalam website.

4. Session Authentication tidak mencegah CSRF pada request-request cross-origin karena browser mengirimkan request-request tersebut dengang cookienya masing-masing.

AI Disclosure.
Dalam pengerjaan Tugas-2 PBP ini, saya tidak menggunakan AI. Sumber utama saya dalam mempelajari materi untuk tugas ini adalah W3school.com, geeksforgeeks.org, dan modul PBP yang disediakan di Scele.