import requests


class RunMethod:

    def post_man(self, url, headers, data):
        # 忽略不安全的请求警告信息
        requests.packages.urllib3.disable_warnings()
        # verify参数的作用是检查 SSL 证书认证，参数的默认值为 True，如果设置为 False 则表示不检查 SSL证书
        response = requests.post(url=url, headers=headers, data=data, verify=False)
        return response

    def get_main(self, url, headers, data=None):
        # 忽略不安全的请求警告信息
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url, headers=headers, data=data, verify=False)
        return response

    def run_main(self, method, url, headers, data=None):
        # 调用者调用这个函数时，可以选择不传入data这个参数,data为默认参数
        # 忽略不安全的请求警告信息
        requests.packages.urllib3.disable_warnings()
        # 设置默认的重试次数为 5 次。
        requests.adapters.DEFAULT_RETRIES = 5

        if method == "Post":
            res = self.post_main(url, headers, data)
        elif method == "Get":
            res = self.get_main(url, headers, data)
        # 将 Python 对象编码成 JSON 字符串
        # return json.dumps(response, ensure_ascii=False, sort_keys=False, indent=2)
        # 将响应的的数据以字典数据结构和json数据格式返回
        return res.json()
