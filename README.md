# TRACE Workflow Test
This is a front end workflow testing script. This relies on [chrome webdriver](https://splinter.readthedocs.io/en/latest/drivers/chrome.html) & [Splinter](https://splinter.readthedocs.io/en/latest/)
It’s important to note that you also need to have Google Chrome installed in your machine.

## Install software and modules
Required: __chrome-driver__, [splinter](https://pypi.python.org/pypi/splinter)

## Setup Environment
[WINDOWS 10 install Video Tutorial __Chrome-Driver__](https://youtu.be/dz59GsdvUF8)
* Create a folder `c:\webdrivers`
* System Properties > Advanced System Settings > Environment Variables > System Variables > Path > Edit > New
  * c:\webdrivers
  * Click OK/OK/OK
* Go to and download "Latest Release" > chromedriver_win32.zip
* Zip will extract to a single executable file 'chromedriver'
* Extract file to "c:\webdrivers/chromedriver"
* To test install open a command terminal and type `chromedriver` and it should start and press `ctrl c` to quit test.

### Install selenium
Chrome WebDriver is provided by Selenium2. To use it, you need to install Selenium2 via pip
```shell
$ pip install selenium
$ pip install splinter
```

#### Fail safe way (recommended)
```terminal
$ pip install pipenv

# this installs the modules
$ pipenv install splinter
$ pipenv install six

# To start the script in the pypenv and exit when complete
$ pipenv run python submit.py
```

## Modify pids.log
* Go to SERVER:8080/fedora/risearch
* find triples > language = spo | Response = N-Triples | Limit = Unlimited
* Query Text or URL = `* <info:islandora/islandora-system:def/scholar#embargo-until> * > launch`
* Results will look like: `<info:fedora/utk.ir.td:1> <info:islandora/islandora-system:def/scholar#embargo-until> "2018-12-16T05:00:00Z"^^<http://www.w3.org/2001/XMLSchema#dateTime> .`
* You will need to modify the output before you paste into the pids.log file
  * One PID per line
    * Example:
      - utk.ir.td:1
      - utk.ir.td:2
      - ...
