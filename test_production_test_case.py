from production_test_case import ProductionTestCase
from was_run import WasRun


class TestProductionTestCase():
    def testRunning(self):
        test = ProductionTestCase("run_test_method")
        print(test.test_was_run)
        test.run_test_method()
        print(test.test_was_run)