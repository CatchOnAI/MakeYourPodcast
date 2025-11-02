AI播客_SDK中心
OpenAPI 门户
AI播客
云产品主页
文档中心
工具中心
服务广场
MCP
HOT
了解 OpenAPI
⌘ K
AI

云产品主页
文档
API 文档
RAM 鉴权文档
调试
SDK
安装
示例
诊断
SDK 中心/
AI播客
AI播客
 吐槽
API 版本 :
SDK 代系 :
查看代系区别
所有语言:Java（异步）JavaTypeScriptGoPHPPython.NETC++Swift
没有我想要的语言, 点击  反馈
快速入门
进阶文档
SDK 示例
历史版本
概述
环境要求
发布地址
源码仓库地址
安装方式
示例背景
完整代码示例
步骤介绍
概述
文档中 SDK 关于 API 的示例代码仅供参考，各 API 的完整使用步骤与说明请参见SDK 示例 和 OpenAPI 文档。
PyPI version

环境要求
Python >= 3.7
发布地址
https://pypi.org/project/alibabacloud_aipodcast20250228/1.0.4
源码仓库地址
https://github.com/aliyun/alibabacloud-python-sdk/tree/master/aipodcast-20250228
安装方式
PyPI PIP
pip install alibabacloud_aipodcast20250228==1.0.4
示例背景
以下代码详细介绍了升级版 SDK 的使用步骤，仅作步骤示范。示例展示了如何调用 PodcastTaskSubmit API 进行播客任务提交请求。
完整代码示例
以下为本文示例的完整 Python SDK 代码。

# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List

from alibabacloud_aipodcast20250228.client import Client as AIPodcast20250228Client
from alibabacloud_credentials.client import Client as CredentialClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_aipodcast20250228 import models as aipodcast_20250228_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> AIPodcast20250228Client:
        """
        使用凭据初始化账号 Client
        @return: Client
        @throws Exception
        """
        # 工程代码建议使用更安全的无 AK 方式，凭据配置方式请参见：https://help.aliyun.com/document_detail/378659.html。
        credential = CredentialClient()
        config = open_api_models.Config(
            credential=credential
        )
        # Endpoint 请参考 https://api.aliyun.com/product/AIPodcast
        config.endpoint = f'aipodcast.cn-beijing.aliyuncs.com'
        return AIPodcast20250228Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        podcast_task_submit_request = aipodcast_20250228_models.PodcastTaskSubmitRequest(
            workspace_id='your_value',
            topic='your_value',
            text='your_value',
            source_lang='your_value'
        )
        headers = {}
        try:
            # 复制代码运行请自行打印 API 的返回值
            client.podcast_task_submit_with_options(podcast_task_submit_request, headers, util_models.RuntimeOptions())
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        podcast_task_submit_request = aipodcast_20250228_models.PodcastTaskSubmitRequest(
            workspace_id='your_value',
            topic='your_value',
            text='your_value',
            source_lang='your_value'
        )
        headers = {}
        try:
            # 复制代码运行请自行打印 API 的返回值
            await client.podcast_task_submit_with_options_async(podcast_task_submit_request, headers, util_models.RuntimeOptions())
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])

步骤介绍
初始化配置对象 alibabacloud_tea_openapi.Config 。 Config 对象存放存放 access_key_id 、access_key_secret 和 endpoint 等配置，Endpoint 如示例中的 aipodcast.cn-beijing.aliyuncs.com 。
import os
from alibabacloud_tea_openapi import models as open_api_models

config = open_api_models.Config(
    # 您的 AccessKey ID,
    access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
    # 您的 AccessKey Secret,
    access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
)
# 访问的域名
config.endpoint = 'aipodcast.cn-beijing.aliyuncs.com'
实例化一个客户端，从 alibabacloud_aipodcast20250228.Client 类生成对象 client 。 后续 request、response 从 alibabacloud_aipodcast20250228.models 中获得。
from alibabacloud_aipodcast20250228.client import Client as Client
from alibabacloud_aipodcast20250228 import models as models

client = Client(config)
创建对应 API 的 Request 。 方法的命名规则为 API 名称加上 Request 。例如：
request = models.PodcastTaskSubmitRequest()
设置请求类 request 的参数。 通过设置 request 类的属性设置参数，即 API 中必须要提供的信息。例如：

# 该参数值为假设值，请您根据实际情况进行填写
request.workspace_id = "your_value";

# 该参数值为假设值，请您根据实际情况进行填写
request.topic = "your_value";

# 该参数值为假设值，请您根据实际情况进行填写
request.text = "your_value";

# 该参数值为假设值，请您根据实际情况进行填写
request.source_lang = "your_value";

通过 client 对象获得对应 request 响应 response 。
response = client.podcast_task_submit(request)
print(response)
调用 response 中对应的属性获得返回的参数值。 假设您需要获取 request_id ：
request_id = response.body.request_id
print(request_id)
使用 try...except... 处理报错。
from Tea.exceptions import UnretryableException

try:
    response = client.podcast_task_submit(request)
except UnretryableException as e:
    # 网络异常
    print(e)
except TeaException as e:
    # 业务异常
    print(e)
except Exception as e:
    # 其他异常
    print(e)