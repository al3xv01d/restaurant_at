`wd` == WebDriver<br>
**Use only xpath for locate elements**<br>

App() fixture == selenium webdriver + destroy method + all Page objects + Screenshooter.

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
`find('xpath locator')` - returns selenium webelement  <br>
class Wait<br>
class Random<br>
`fullpage_screenshot('file_name.png')`<br>
`set_site_width(768)`<br>


**In first test in test_screenshooter.py must be this two functions**

`app.screenshooter.generate_folders()`<br>
`app.screenshooter.init_size(1920)`