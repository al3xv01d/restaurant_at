`wd` == WebDriver<br>
**Use only xpath for locate elements**<br>

app fixture == selenium webdriver + destroy method. Maybe i will ad methods for session or tabs 

**Acronyms**

`atc` - add to cart<br>


**Page Objects**

app.page_obj.item(x).element<br>
**or**<br>
app.page_obj.element<br>

**app** - main fixture <br>
**page-obj** - page object<br>
**item(x)** - page object method - returns some element with many child elements.<br>
**element** - simple element

function_name + **_ms** - this functions make screenshots

#Tools

`get('http://ya.ru')`<br>
`find('xpath locator')`<br>
class Wait<br>
class Random<br>
`fullpage_screenshot('file_name.png')`<br>
`set_site_width(768)`<br>


**In first test in test_screenshooter.py must be this to functions**

`init_size(1920)`<br>
`make_folder_for_todays_date()`