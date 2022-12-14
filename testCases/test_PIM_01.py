import time
from pageObjects.LoginPage import Login
from pageObjects.Pimpage import AddNewEmployee
from utilities import customlogger
from utilities.readproperties import ReadConfig


class Test_PIM_01:

    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = customlogger.test_logDemo()

    def test_add_new_employee(self, setup):
        self.logger.info("***************** TC_PIM_01****************************")
        self.logger.info("***************** Varifying Add a new employee ****************************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.loginpageobj = Login(self.driver)
        self.loginpageobj.setUserName(self.username)
        self.loginpageobj.setPassword(self.password)
        self.loginpageobj.clickLogin()
        self.logger.info("***************** Successfully Login ****************************")
        self.pimpageobj = AddNewEmployee(self.driver)
        self.pimpageobj.selectPim()
        self.pimpageobj.addPim()
        self.pimpageobj.firstName("pradeep")
        self.pimpageobj.lastName("G")
        self.pimpageobj.clickSave()
        self.logger.info("***************** Providing personal details ****************************")
        self.pimpageobj.nickName("bala")
        self.pimpageobj.otherId(17808)
        self.pimpageobj.drivingLicenseNumber("TN3437970806038")
        self.pimpageobj.licenseExpiryDate("2027-02-12")
        self.pimpageobj.ssnNumber(876949)
        self.pimpageobj.sinNumber(422667)
        self.pimpageobj.nationality()
        self.pimpageobj.maritalStatus()
        self.pimpageobj.dob("1999-02-09")
        self.pimpageobj.gender()
        self.pimpageobj.militaryService("No")
        self.pimpageobj.personalDetailSave()
        self.pimpageobj.bloodType()
        self.pimpageobj.customFieldsSave()
        self.save = self.pimpageobj.saveConformation()
        time.sleep(3)
        if self.save == True:
            self.logger.info("***************** Successfully Added New Employee ****************************")
            self.driver.close()
            assert True
        else:
            self.logger.info("***************** Add New Employee Unsuccessful  ****************************")
            self.driver.close()
            assert False
        self.logger.info("************** Completed TC_PIM_01 *********************")
