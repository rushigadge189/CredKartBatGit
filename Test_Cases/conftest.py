import time

import pytest
from selenium import webdriver

def pytest_addoption( parser ) :
    parser.addoption("--browser") ;

@pytest.fixture()
def browser(request) :
    return request.config.getoption("--browser") ;
@pytest.fixture()
def setup (browser) :

    if ( browser == 'chrome' ) :
        driver = webdriver.Chrome();
        time.sleep(1);
        print ('Launching Chrome Browser') ;
    elif ( browser == 'edge' ) :
        driver = webdriver.Edge() ;
        time.sleep(1);
        print ('Launching The Edge Browser') ;
    else :
        print ('Running In Headless Mode') ;
        chrome_options = webdriver.ChromeOptions();
        chrome_options.add_argument("headless");
        driver = webdriver.Chrome(options=chrome_options) ;

    driver.get('https://automation.credence.in/shop');
    time.sleep(1) ;

    driver.maximize_window();
    time.sleep(1) ;

    return driver ;

def pytest_metadata( metadata ) :
    metadata ["class"] = "Credence" ;
    metadata ["Batch"] = "CT#15" ;
    metadata ["URL"] = "httpos://automation.credence.in" ;
    metadata.pop ("platform", "None") ;

@pytest.fixture(params=[
    ( "Credencetest@test.com" , "Credence@123" ),
    ( "Credencetest@test.com1" , "Credence@123"),
    ( "Credencetest@test.com" , "Credence@1231"),
    ( "Credencetest@test.com1" , "Credence@1231")
])

def getDataForLogin(request) :
    return request.param ;