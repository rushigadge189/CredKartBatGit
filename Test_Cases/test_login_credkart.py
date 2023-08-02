import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Credkart_login():
    def test_page_title(self, setup) :
        self.driver = setup ;

        if ( self.driver.title == 'CredKart' ) :
            self.driver.save_screenshot('D:\\CREDKART_LOGIN_COMMON\\Screenshot\\title.png') ;
            self.driver.close() ;
            assert True;
        else :
            self.driver.save_screenshot('D:\\CREDKART_LOGIN_COMMON\\Screenshot\\title.png') ;
            self.driver.close() ;
            assert False;

    def test_login(self, setup):
        self.driver = setup ;

        self.driver.find_element(By.XPATH, "//a[text()='Login']").click();
        time.sleep(1) ;

        self.driver.find_element(By.XPATH,'//input[@id="email"]').send_keys('Credencetest@test.com');
        time.sleep(1) ;

        self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('Credence@123');
        time.sleep(1) ;

        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click();
        time.sleep(1) ;

        try :
            self.driver.find_element(By.XPATH, '//h2[text()="CredKart"]') ;
            print ( 'Login Test Case Is Passed' ) ;
            self.driver.save_screenshot('D:\\CREDKART_LOGIN_COMMON\\Screenshot\\loginpass.png') ;
            self.driver.close() ;
            assert True ;
        except :
            print ( 'Login Test Case Is Failed' ) ;
            self.driver.save_screenshot( 'D:\\CREDKART_LOGIN_COMMON\\Screenshot\\loginfail.png' ) ;
            self.driver.close() ;
            assert False ;
