import unittest
from lxml import etree as tree
from random import randint

from BuyMeObjects import BuyMeObjects


class BuyMeTests(unittest.TestCase):
    tree = None
    objects = None
    title = None
    random = randint(1, 10000)

    @classmethod
    def setUpClass(cls):
        cls.tree = tree.parse("config_buy_me_ex").getroot()
        cls.objects = BuyMeObjects(cls.tree.find("browser_type").text)
        cls.title = cls.objects.get_page_title()
        print(cls.title)

    def test_title(self):
        self.assertEqual(self.title, self.tree.find("excepted_title").text)

    def test_subscription(self):
        self.subscription()
        self.assertTrue(self.objects.check_subscription())
        self.assertEqual(self.tree.find("first_name").text, self.objects.get_subscribed_first_name())
        self.assertEqual(str(self.random) + self.tree.find("email").text, self.objects.get_subscribed_email_address())

    def subscription(self):
        self.objects.set_first_name(self.tree.find("first_name").text)
        self.objects.set_mail_element(str(self.random) + self.tree.find("email").text)
        self.objects.set_password(self.tree.find("password").text)
        self.objects.set_password_verification(self.tree.find("password_confirm").text)
        self.objects.set_subscribe_element()

    @classmethod
    def tearDownClass(cls):
        cls.objects.close_page()


if __name__ == '__main__':
    log_file = 'log_file.txt'
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
