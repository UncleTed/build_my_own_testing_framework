from was_run_parent_class import  WasRunParentClass


class WasRun(WasRunParentClass):
    def __init__(self, method_under_test):
        self.test_was_run = None
        WasRunParentClass.__init__(self, method_under_test)

    def run_test_method(self):
        self.test_was_run = 1






