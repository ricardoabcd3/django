# this is not executable file , is a complement of Smoke_tests.py



import	unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

class AssertionsTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Edge(executable_path = r"C:\Users\ricki\OneDrive\Escritorio\django\django\msedgedriver.exe")
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo.onestepcheckout.com/")

	def test_search_field(self):
		self.assertTrue(self.is_element_present(By.NAME, 'q'))
		
	def test_language_option(self):
		self.assertTrue(self.is_element_present(By.ID, 'select-language'))

	def tearDown(self):
		self.driver.quit()

	#para saber si está presente el elemento
	#how: tipo de selector
	#what: el valor que tiene
	def	is_element_present(self, how, what):
		try:  #busca los elementos según el parámetro
			self.driver.find_element(by = how, value = what) 
		except NoSuchElementException as variable:
			return False
		return True

