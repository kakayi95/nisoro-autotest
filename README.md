# Nisoro 基本購物流程自動化測試

這個項目的目的是驗證 Nisoro 電商平台的核心購物流程，確保平台的功能穩定性。

## 測試流程

- 進到 [Nisoro 商店](https://www.nisoro.com/) 官網
- 搜尋商品（搜尋字串：`花椰菜米`）
- 點擊第一個商品
- 進到商品頁點擊加入購物車
- 進入購物車頁面查看

## 使用工具

- Python3
- Pytest
- Selenium

## 瀏覽器需求

- Google Chrome 瀏覽器
- ChromeDriver

### 安裝 ChromeDriver

1. 前往 [ChromeDriver 下載頁面](https://developer.chrome.com/docs/chromedriver?hl=zh-tw)。
2. 下載與你的 Chrome 瀏覽器版本相匹配的 ChromeDriver。
3. 解壓下載的文件，並將 ChromeDriver 可執行文件添加到系統 PATH 中。


## 專案結構

採用頁面物件模型（Page Object Model, POM）的設計模式來編寫自動化測試程式。每個網頁都有一個對應的頁面物件，封裝了與該頁面互動的方法（例如：元素定位、操作）。這樣的設計將測試邏輯與網頁介面的元素分離，提高測試程式的可讀性和維護性。

```
project_root/
├── pytest.ini           # pytest 設定文件
├── requirements.txt     # 專案依賴列表
├── README.md            # 專案說明文件
├── tests/               # 測試文件目錄
│   ├── __init__.py
│   ├── conftest.py           # pytest 的全局測試 fixture，存放可於全局使用的變數
│   ├── test_shopping_flow.py # 測試基本購物流程的功能
├── pages/                    # 頁面物件模型（Page Object Model，POM）目錄
│   ├── __init__.py
│   ├── base_page.py          # 為所有頁面物件提供通用的方法和工具（例如：find_element, click 等基本元素定位操作方法）
│   ├── home_page.py          # 首頁 POM
│   ├── product_list_page.py  # 產品列表頁面 POM (搜尋後出現的產品列表)
│   ├── product_page.py       # 產品詳情頁面 POM
│   └── shopping_cart_page.py # 購物車頁面 POM
└── utils/                   
    ├── __init__.py
    ├── constants.py          # 存放常用常量
```


### `conftest.py` 文件說明

`conftest.py` 文件是 pytest 的一部分，用於定義 fixtures 和一些配置設定。這些 fixtures 和配置可以在整個測試套件中使用，而不需要在每個測試文件中單獨引入。
在專案中，我定義以下兩種 fixtures:

1. driver : 用於在每個測試模組期間啟動和關閉瀏覽器
2. shared_data : 用於在測試模組期間存儲和共享資料
    - 在 test_add_product_to_cart() 時將商品詳情頁的資訊儲存進 shared_data
    - 在 test_verify_product_in_cart() 時將購物車中的商品與 shared_data 的資料進行比較


## 安裝

1. **Clone the repository**
    ```sh
    git clone https://github.com/kakayi95/nisoro-autotest.git
    cd nisoro-autotest
    ```
    
2. **Create a virtual environment**:
    - **Windows**：
      ```sh
      python -m venv venv
      ```
    - **macOS/Linux**：
      ```sh
      python3 -m venv venv
      ```

3. **Activate the virtual environment**:
    - **Windows**：
      ```sh
      .\venv\Scripts\activate
      ```
    - **macOS/Linux**：
      ```sh
      source venv/bin/activate
      ```

4. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Running Tests**:
    ```sh
    pytest
    ```
