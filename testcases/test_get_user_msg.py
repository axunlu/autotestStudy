import pytest
from API.all_api import AllApi
from common.get_log import get_log

logger = get_log()


# 获取用户信息的测试用例
class TestUserMsg(object):
    # 登录测试用例初始化，用于处理执行用例前后的数据
    @pytest.fixture(scope="class")
    def init_get_user_msg(self):
        logger.info("\n ==============================获取用户信息测试用例开始 ==============================")
        all_api = AllApi()
        return all_api

    @pytest.mark.parametrize("api_name", ["get_user_msg"])
    def test_get_user_msg(self, api_name, init_get_user_msg):
        # 发送请求
        res = init_get_user_msg.send_request(api_name)
        logger.info(F"res 的值为：{res}")
        # 断言后面添加提示信息，这样在断言失败时，会自动输出失败原因
        # 断言1：success的值为True
        assert res['success'] is True, "success的值为: %s" % res['success']
        # 断言2：access_token的值为不为空
        assert res['data'] is not None, 'data的值为：%s' % res['data']


if __name__ == "__main__":
    pytest.main(['-vs', 'test_get_user_msg.py'])
    # pytest版本过高，无法识别allure插件，需要降低pytest版本
    # pytest.main(['-v', '-q', '--alluredir', 'A../report/xml', 'test_login.py'])
    # pytest.main(['-v', 'test_login.py', '--html=report/login_report.html', '--self-contained-html'])
