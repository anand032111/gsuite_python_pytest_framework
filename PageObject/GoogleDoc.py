class DocHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.doc_title_css_selector = "input[class='docs-title-input']"
        self.document_title_xpath = "//*[@id='docs-title-widget']/input"
        # driver.find_element_by_css_selector("input[class='docs-title-input']").click()
        # driver.find_element_by_xpath("//*[@id='docs-title-widget']/input").send_keys("Automation Doc Experiment")

    def click_on_title(self):
        self.driver.find_element_by_css_selector(self.doc_title_css_selector).click()
    def document_title(self, title):
        self.driver.find_element_by_xpath(self.document_title_xpath).send_keys(title)

