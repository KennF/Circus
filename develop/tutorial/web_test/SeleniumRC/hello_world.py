from selenium import selenium
import unittest, time, re
import time

class NewTest(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*firefox",
                "http://www.google.com.hk/")
        self.selenium.start()

    def test_new(self):
        sel = self.selenium
        sel.open("/")
        time.sleep(30)
        sel.type("q", "selenium rc")
        sel.click("btnG")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present("Results * for selenium rc"))

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main()