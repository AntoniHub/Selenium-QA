<h1 align="center"> Requirements to execute Tests in Pytest </h1>
<h3> Tools: </h3>
<li> .- Install  <a href="https://www.python.org/downloads/"> Python </a></li>
<li>.- IDE: <a href="https://www.jetbrains.com/es-es/pycharm/download/"> PyCharm </a></li>
<li>.- Install packages in Pycharm: <i><a href="https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-reloading-interpreter-paths.html"> https://www.jetbrains.com </a></i></li>
<i>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; This packages are: Selenium, Pytest, Openpyxl, Requests, Flask</i>
<li>.- Download <a href="https://selenium-python.readthedocs.io/installation.html#drivers"> driver </a> for browser </li>
&nbsp;

<h1 align="center"> Gerate reports in Pytest </h1>
<h3> Requirements: </h3>
<li> .- Install <a href="https://www.python.org/downloads/"> Python </a></li>
<li>.- Install <a href="https://selenium-python.readthedocs.io/installation.html"> Selenium </a></li>
<li>.- Install <a href="https://docs.pytest.org/en/7.1.x/getting-started.html"> Pytest </a></li>
<li>.- Install <a href="https://pytest-html.readthedocs.io/en/latest/installing.html"> Pytest-html </a></li>

<li>.- <i>Run command (cmd in folder this project):</i></li>
	<li>&nbsp;&nbsp;&nbsp;&nbsp; <i>python3 -m pytest test_suiteName.py --html=report.html --self-contained-html</i></li>

### Steps:
* .- For some desktops 'python3 -m' is necessary
* .- 'pytest' -> to run command
* .- test_suiteName.py -> select a test for it test
* .- --html=report.html -> custom our name to report
* .- --self-contained-html -> apply for content security policy

### Links or FYI:
* https://pytest-html.readthedocs.io/en/latest/user_guide.html
* https://www.selenium.dev/documentation/webdriver/browsers/
* https://selenium-python.readthedocs.io/installation.html
* https://github.com/SeleniumHQ/Selenium
* https://pypi.org/project/selenium/

#### NOTE:
<h5>Automated GUI tests ensure the proper functioning of the web application and minimize the effort of performing long loop tests over and over again.</h5>
<h5>These guarantee timely and repeated regression tests that do not validate the current content but take care of the proper functioning of what has already been developed.</h5>