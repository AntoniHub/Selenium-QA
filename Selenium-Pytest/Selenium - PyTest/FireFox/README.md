<h1 align="center"> Selenium Client Driver </h1>
<b>Python</b> language bindings for Selenium WebDriver.

The selenium package is used to automate web browser interaction from Python.
&nbsp;

<pre><blockquote>
<b>Home:</b> https://selenium.dev/ &nbsp;
<b>Docs:</b> selenium package API &nbsp;
<b>Dev:</b> https://github.com/SeleniumHQ/Selenium &nbsp;
<b>PyPI:</b> https://pypi.org/project/selenium/ &nbsp;
</blockquote></pre>
&nbsp;

<h1 align="center">Installing</h1>
If you have <a href="https://pip.pypa.io/">pip</a> on your system, you can simply install or upgrade the Python bindings:

<pre><blockquote>
pip install -U selenium
</blockquote></pre>

Alternately, you can download the source distribution from <a href="https://pypi.org/project/selenium/#files">PyPI</a> (e.g. selenium-4.7.0.tar.gz), unarchive it, and run:

<pre><blockquote>
python setup.py install
</blockquote></pre>
<i>Note: You may want to consider using virtualenv to create isolated Python environments.</i>

&nbsp;

<h1 align="center"> Run WebDriver in Firefox </h1>
Firefox can be controlled by <b>Python</b>. To do this you need the selenium module and a web driver. The <b>Python</b> code starts the web browser and then completely controls it.
The code can then do anything you can do with a web browser, like opening a page, sending key presses or button clicks.

&nbsp;

<h2 align="left">Selenium Firefox Example</h2>
To make Firefox work with Python selenium, you need to install the <a href="https://github.com/mozilla/geckodriver/releases">geckodriver.</a> The geckodriver driver will start the real firefox browser and supports Javascript.
From python you can load the Firefox browser with one line of code:
&nbsp;

<pre><blockquote>
from selenium import webdriver
</blockquote></pre>
&nbsp;

Take a look at the selenium firefox code. First import the webdriver, then make it start firefox.
Open a webage with the get page and optionally send keypresses.
&nbsp;

<pre><blockquote>
# coding=utf-8
from selenium import webdriver
 
driver = webdriver.Firefox()
driver.get("https://es-testing.cyberguardian.tech")
 
driver.find_element_by_id("nav-search").send_keys("CyberGuardian")
</blockquote></pre>
&nbsp;

<h4 align="left">LINKs or FYI:</h4>
<li>https://www.selenium.dev/documentation/webdriver/browsers/firefox/</li>
<li>https://www.selenium.dev/selenium/docs/api/py/</li>
<li>https://pythonbasics.org/selenium-firefox/</li>
<li>https://github.com/mozilla/geckodriver</li>
<li>https://pypi.org/project/selenium/</li>