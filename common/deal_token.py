from common import base
import os
import yaml
import json
from common.run_method import RunMethod
from common.get_log import get_log

logger = get_log()


# 把token值写到配置文件access_token.yml中
def write_token(res):
    cur_path = os.path.abspath(os.path.dirname(__file__))
    yaml_path = os.path.abspath(os.path.dirname(cur_path) + os.path.sep + "configs/access_token.yml")
    token_value = {
        'authorization': res["authorization"]
    }
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(token_value, f)

    logger.info("\n token值已保存至配置文件中")


# 把token值从配置文件access_token.yml读出来
def read_token():
    cur_path = os.path.abspath(os.path.dirname(__file__))
    yaml_path = os.path.abspath(os.path.dirname(cur_path) + os.path.sep + "configs/access_token.yml")
    file = open(yaml_path)
    read = file.read()
    load = yaml.load(read, Loader=yaml.FullLoader)
    file.close()
    return load['authorization']


if __name__ == "__main__":
    '''
    
    run = RunMethod()
    url = "http://localhost:8080/api/user/1ogin/"
    data = {
        "phone": "13119822212",
        "code": "526006",
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": ""
    }

    res = run.run_main("Post", url, data, headers)
    # print(res)
    response = json.loads(res)
    write_token(response)
    print("token的值： ", read_token())
    
    '''