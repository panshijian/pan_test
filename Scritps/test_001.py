
import allure
class Test_Mico:
    @allure.step(title = "第一个测试步骤")
    def test_001(self):
        self.a = 10
        self.b = 20
        self.c = self.a + self.b
        assert self.c == 30