from production_test_case import  ProductionTestCase


class WasRun(ProductionTestCase):
    def __init__(self, method_under_test):
        self.test_was_run = None
        ProductionTestCase.__init__(self, method_under_test)







