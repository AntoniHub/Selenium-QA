<h1 align="center"> Run Pytest in Chrome </h1>
<h3> Requeriments </h3>
<li> .- Download <a href="https://chromedriver.chromium.org/"> ChromeDriver </a> </li>
<li>.- Add route of chrome binary application to <b>PATH</b> : <i>C:\Program Files\Google\Chrome\Application</i></li>
<li>.- Configure IDE: <a href="https://www.jetbrains.com/es-es/pycharm/"> PyCharm </a> </li>
<li>.- Run test case from CMD as instructed in the main <a href="https://github.com/AntoniHub/Cyber#readme"> README </a></li>

## Example for start Selenium in [Python](https://www.python.org/downloads/)
[ChromeDriver - Chromium](https://chromedriver.chromium.org/getting-started)

<pre><blockquote>
import time

from selenium import webdriver


driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.

driver.get('https://antonio-rodriguez.tech');

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('Antonio Rodriguez')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()
</blockquote></pre>
