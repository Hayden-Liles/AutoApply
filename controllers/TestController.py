from services.TestServices import testServices


class TestController:
    def __init__(self):
        pass

    def test(self):
        print('I am a controller')
        testServices.test()


testController = TestController()
