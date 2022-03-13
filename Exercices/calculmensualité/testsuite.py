# pip install xmlrunner
import unittest
# import xmlrunner

# import your test modules
import testTaux
import testMensualité

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(testTaux))
suite.addTests(loader.loadTestsFromModule(testMensualité))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
# runner = xmlrunner.XMLTestRunner(verbosity=3, output="..\\Results\\")
result = runner.run(suite)
