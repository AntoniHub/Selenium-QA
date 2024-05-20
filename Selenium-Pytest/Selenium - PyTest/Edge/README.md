<h1 align="center"> Run WebDriver in Edge </h1>
To begin writing automated tests, make sure the Edge WebDriver version you install matches your browser version, as follows:
<li> 1.- Go to <i>edge://settings/help</i> and note your version of Microsoft Edge. </li>
<li> 2.- Go to <a href="https://learn.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python#:~:text=Go%20to%20Microsoft%20Edge%20WebDriver."> Microsoft Edge WebDriver. </a></li>
<li> 3.- In the <i>Get the latest version</i> section of the page, select a platform in the channel that matches your version number of Microsoft Edge. </li>
<li> 4.- After the download completes, extract the <i>msedgedriver</i> executable to your preferred location. Add the folder where the executable is located to your <i>PATH</i> environment variable. </li>
&nbsp;
&nbsp;
<h1 align="center"> Using Selenium 4 </h1>

Selenium WebDriver is an open-source testing framework that can be used on any platform, and provides language bindings for Java, `Python`, C#, Ruby, and JavaScript. <i>Note: Python 3 is required to run Selenium 4 tests. (Python 2.7 is not supported.)</i>&nbsp;

To use WebDriver to automate Microsoft Edge, if you use Selenium, you must use Selenium 4, which has built-in support for Microsoft Edge (Chromium).&nbsp;

To install Selenium 4, see Install a <a href="https://www.selenium.dev/documentation/webdriver/getting_started/install_library/">Selenium library.</a> In case you need it, the nuget packages page is <a href="https://www.nuget.org/packages/Selenium.WebDriver">Selenium WebDriver</a>

&nbsp;
&nbsp;

<h3 align="center"> Upgrading from Selenium 3 </h1>
To use WebDriver to automate Microsoft Edge, if you use Selenium, make sure you are using Selenium 4. Selenium 3 is no longer supported.

You must upgrade existing Selenium 3 tests to Selenium 4. To learn more about upgrading to Selenium 4, see <a href="https://www.selenium.dev/documentation/webdriver/getting_started/upgrade_to_selenium_4/">Upgrade to Selenium 4.</a>

If you're using <a href="https://github.com/microsoft/edge-selenium-tools">Selenium Tools for Microsoft Edge</a> to add Microsoft Edge (Chromium) support to your Selenium 3 browser tests, update your tests as follows:

<li> Remove Selenium Tools for Microsoft Edge from your project. You don't need to use Selenium Tools for Microsoft Edge with Selenium 4, because Selenium 4 already has built-in support for Microsoft Edge (Chromium).</li>
<li> Update your tests to use the built-in <i>EdgeDriver</i> and related classes that Selenium 4 provides instead.</li>
<li> Remove all usages of the <i>EdgeOptions.UseChromium</i> property. This property no longer exists in Selenium 4, because Selenium 4 supports only Microsoft Edge (Chromium).</li>

&nbsp;
&nbsp;
<h1 align="center"> Automate Microsoft Edge </h1>
Selenium uses the <i>EdgeDriver</i> class to manage a Microsoft Edge session. The following code:

<li>Starts a Microsoft Edge session.</li>
<li>Instructs Microsoft Edge to go to Bing.</li>
<li>Searches for "WebDriver".</li>
<li>Sleeps for a few seconds so you can see the results.</li>

&nbsp;

To get started automating Microsoft Edge with WebDriver:

&nbsp;
<pre><blockquote>
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get('https://antonio-rodriguez.tech')

element = driver.find_element(By.ID, 'sb_form_q')
element.send_keys('Antonio Rodriguez')
element.submit()

time.sleep(5)
driver.quit()
</blockquote></pre>

&nbsp;
<h4 align="left">LINKs or FYI:</h4>
<li>https://learn.microsoft.com/en-us/microsoft-edge/developer/</i>
<li>https://www.browserstack.com/guide/launch-edge-browser-in-selenium</li>
<li>https://www.selenium.dev/documentation/webdriver/browsers/edge/</li>
<li>https://github.com/SeleniumHQ/selenium/releases</li>