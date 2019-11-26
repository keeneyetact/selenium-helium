from helium.api_impl import TextImpl
from helium.selenium_wrappers import WebDriverWrapper
from helium_integrationtest.inttest_api import BrowserAT

class TextImplIT(BrowserAT):
	def get_page(self):
		return 'inttest_text_impl.html'
	def test_empty_search_text_xpath(self):
		xpath = TextImpl(WebDriverWrapper(self.driver))._get_search_text_xpath()
		text_elements = self.driver.find_elements_by_xpath(xpath)
		texts = [w.get_attribute('innerHTML') for w in text_elements]
		self.assertEquals(
			["A paragraph", "A paragraph inside a div",
			 "Another paragraph inside the div"],
			sorted(texts)
		)