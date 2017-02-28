start: <br>
`wd = webdriver.Firefox()`<br>
`wd.get("http://google.com/")`<br>
<br>
**Find element by id** - `element = wd.find_element_by_id('hplogo')` <br>
**Find element in other element** -`element.find_element_by_id`
<br>

**Get page title** - `wd.title`
<br>
**Find element by xpath** - `wd.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]')`
<br>
**Find element by tag name** - `wd.find_element_by_tag_name('div')`
<br>
**Clear text input** - `element.clear()`
<br>
**Forward and back in browser** -`driver.forward();
driver.back()`
<br>
**Working with alerts** - `alert = driver.switch_to_alert()`
<br>
`driver.current_url`
<br>
`driver.page_source`
<br>
**Close current window** - `driver.close()`
<br>
`driver.quit()`
<br>
`driver.refresh()`
<br>
`driver.get_cookie('my_cookie')`
<br>
`driver.delete_cookie('my_cookie')`
<br>
`driver.delete_all_cookies()`
<br>
`driver.add_cookie({'foo': 'bar',})`
<br>
**Time to wait** - `driver.implicitly_wait(30)`
<br>
**Make screenshot** - `driver.get_screenshot_as_file('/Screenshots/foo.png')`
<br>

<br>