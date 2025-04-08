from was_run import WasRun


class WasRunParentTest():
    def testRunning(self):
        test = WasRun("run_test_method")
        print(test.test_was_run)
        test.run()
        print(test.test_was_run)