import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Credkart_login_param():
    def test_login_param (self, setup, getDataForLogin):
        self.driver = setup ;

        self.driver.find_element(By.XPATH, "//a[text()='Login']").click();
        time.sleep(1) ;

        self.driver.find_element(By.XPATH,'//input[@id="email"]').send_keys(getDataForLogin[0]);
        time.sleep(1) ;

        self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(getDataForLogin[1]);
        time.sleep(1) ;

        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click();
        time.sleep(1) ;

        try :
            self.driver.find_element(By.XPATH, '//h2[text()="CredKart"]') ;
            print ( 'Login Test Case Is Passed' ) ;
            self.driver.save_screenshot("D:\\CREDKART_LOGIN_COMMON\\Screenshot\\"+getDataForLogin[0]+"_"+getDataForLogin[1]+"CredKart_login_002.png") ;
            self.driver.close() ;
            assert True ;
        except :
            print ( 'Login Test Case Is Failed' ) ;
            self.driver.save_screenshot("D:\\CREDKART_LOGIN_COMMON\\Screenshot\\"+getDataForLogin[0]+"_"+getDataForLogin[1]+"CredKart_login_002.png") ;
            self.driver.close() ;
            assert False ;
