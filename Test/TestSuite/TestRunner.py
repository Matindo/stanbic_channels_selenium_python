### Test Runner to run all the test scripts required ###

import sys, os
sys.path.append(os.getcwd())
from unittest import TestLoader, TestSuite, TextTestRunner
from Test.Scripts.test_Login_Page import Stanchart_Login_Page
from Test.Scripts.test_Login import User_Login
import testtools as testtools

if __name__ == "__main__":
    
    test_loader = TestLoader()
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(Stanchart_Login_Page),
        test_loader.loadTestsFromTestCase(User_Login)
    ))
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
    
    parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())
    self.driver.set_page_load_timeout(30)