class ProductionTestCase:
    test_was_run = 0
    def __init__(self, method_under_test):
        self.method_under_test = method_under_test



    def run(self):
        pass
    
    def run_test_method(self):
        self.test_was_run = 1