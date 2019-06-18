import unittest

class TestParameters(unittest.TestCase):
    pars = []
    @classmethod
    def setUpClass(cls):
        cls.pars = ParametersInit().parameters_init()
        # print(pars)

    def setUp(self):
        pass

    def test_parameters(self):
        datas = self.pars

        for i in datas:
            with self.subTest(data=i):
                print(i[0] + ':' + i[1] + ':' + i[2] + ':' + i[3])
                self.assertEqual(i[0],'successful','验证失败')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


class ParametersInit:
    def __init__(self):
        pass

    def parameters_init(self):
        list = [('login-01','admin','123456','successful'),
                ('login-02','admin2','123457','successful2')]
        return list

if __name__ == '__main__':

    unittest.main(verbosity=2)


