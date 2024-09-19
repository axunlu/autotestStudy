import pytest
from API.all_api import AllApi
from common.get_log import get_log

logger = get_log()


def my():
    all_login = AllApi()
    res = all_login.send_request("login_code")
    logger.info(F"res 的值为：{res}")
    # 断言1：success的值为True
    assert res['success'] is True, "success的值为: %s" % res['success']


if __name__ == '__main__':
    my()
