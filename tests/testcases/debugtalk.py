# -*- coding: cp936 -*-

from random import *







# 自定义课程ID
def get_course_id():
    return [
        {"course_id": 92},
        {"course_id": 93},
        {"course_id": 94},
        {"course_id": 95}
    ]

def get_subject_id():
    return [
        {"subject_id": 92},
        {"subject_id": 93},
        {"subject_id": 94},
        {"subject_id": 95}
    ]

#生成6位密码密码
def get_account(num):
    accounts = []
    for index in range(1, num+1):
        accounts.append(
            {"username": "user%s" % index, "password": str(index) * 6},
        )

    return accounts

#免费学员的id
def get_user_ids():
    return[
        {"user_ids":"1000001,10000003,10000005"}
        ]


#格式转换
#string转化成int型list
def str_list(str):
    results = str.split(",")  #按指定分隔符对str切片
    results = list(map(int, results))#str转换为int型list
    return results

def excp(str,x):
    results = str.split(",")  #按指定分隔符对str切片
    results = list(map(int, results))#str转换为int型list
    return results[x]


#自定义自营课程
def get_online_subject():
    return{
        #标题
        "title": "测试自营课",
        #课程标签（自定义）
        "tags": [ "测试","接口","添加"],
        #课程类型 ：0-线上 2-全能就业班
        "type": 0,
        #简介
        "brief": "暂无简介",
        #活动标签 无(null)/预售特惠/限时特惠
        "mark": "",
        #是否收费 ：0-收费1-免费
        "is_free": 0,
        #提供方id
        "supplier_id": "34",
        # 封面图片
        "images": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/135b208bb253e55.jpeg",
        # 商品图片
        "goods_image": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/135b208bb609454.jpeg"
        }

#自定义线下课（url）
def offline_subject_url():
    return{
        # 标题
        "title": "url第三方课",
        # 课程标签（自定义）
        "tags": ["第三方", "接口", "添加"],
        # 课程类型 ：0-线上 1-线下课 2-全能就业班
        "type": 1,
        # 简介
        "brief": "",
        # 活动标签 第三方课程（无）
        "mark": "",
        # 提供方id
        "supplier_id": "34",
        # 封面图片
        "images": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/135b208bb253e55.jpeg",
        #是否有跳转链接 0-否 1-是
        "is_third_content": 1,
        #跳转链接
        "url": "https://www.baidu.com"


    }
#自定义线下课（json）
def offline_subject_json():
    return{
        # 标题
        "title": "json第三方课",
        # 课程标签（自定义）
        "tags": ["第三方", "接口", "添加"],
        # 课程类型 ：0-线上 1-线下课 2-全能就业班
        "type": 1,
        # 简介
        "brief": "",
        # 活动标签 第三方课程（无）
        "mark": "",
        # 提供方id
        "supplier_id": "34",
        # 封面图片
        "images": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/135b208bb253e55.jpeg",
        #是否有跳转链接 0-否 1-是
        "is_third_content": 0

    }
#线下课json数据
def offline_json():
    return{
        "expand": "introduction",
        "profile": {
            "pageInfo": {
                "title": " 摄影助理职业技能培训",
                "keywords": " 新手入门,摄影,摄影助理,职业,培训",
                "description": "本课程采用“师徒式”教学方法，手把手教你成为一名合格的摄影助理，迅速掌握从业技能，毕业提供就业机会。"
            },
            "banner": {
                "image": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/015b11086e94346.jpeg",
                "wapImage": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/015b11086a7e4f9.jpeg"
            },
            "basicInfo": [
                {
                    "title": "课程简介",
                    "content": [
                        {
                            "type": "text",
                            "content": "近几年国内影视行业发展势头强劲，优质内容和人才短板待补。作为电影年产量位列世界第三，中国市场对于影视基础人才的需求量与日俱增，供不应求，但从业人员水平参差不齐。尤其在摄影助理这一岗位上，目前并没有全面、系统的教育机制和人才输出机构。"
                        },
                        {
                            "type": "text",
                            "content": "针对这一现象，新片场学院继《商业广告制作》和《美食视频制作》后，现在正式开设了《摄影助理职业技能培训》。"
                        },
                        {
                            "type": "text",
                            "content": "本课程是一门针对摄影助理的职业技能培训课，能够在学习之后掌握架机位、测量焦距、跟焦，以及器械拍摄（轨道、dolly车、三轴稳定器、摇臂等）的辅助工作，快速成为一名能被市场所认可的摄影助理，甚至为未来的摄影师之路打下坚实的基础。"
                        },
                        {
                            "type": "title",
                            "content": "授课团队"
                        },
                        {
                            "type": "text",
                            "content": "新片场学院联合源莱专业电影设备技术团队首开“团队总监和专家导师”团队授课模式，每一位团队总监都拥有超过10年的项目经验及授课经验，每位导师教授自己专业领域内最擅长的部分，共同打造专业的摄影助理课程，理论和实践相结合，随堂分享市场商业项目案例。"
                        },
                        {
                            "type": "title",
                            "content": "就业机会"
                        },
                        {
                            "type": "text",
                            "content": "每期学员毕业后，将选出5-10名优秀学员，由新片场和源莱传媒直接输送到各个剧组实习和就业，无缝衔接，真正做到毕业即就业，让你工作5-15天轻松赚回学费！（根据近几年市场行情，摄影助理日薪400-1500元不等）"
                        },
                        {
                            "type": "image",
                            "content": {
                                "image": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/015b110870a00dc.png",
                                "wapImage": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/015b11086a67a61.jpeg"
                            }
                        }
                    ]
                },
                {
                    "title": "教学展示",
                    "content": [
                        {
                            "type": "title",
                            "content": "教学团队和场地"
                        },
                        {
                            "type": "text",
                            "content": "源莱传媒技术总监带领源莱技术团队全程跟进摄影助理课程，更有400平方米专业电影级摄影棚作为学员授课场地，为现场教学和学员实践提供便捷。"
                        },
                        {
                            "type": "image",
                            "content": {
                                "image": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/015b11086d94c6e.jpeg",
                                "wapImage": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/015b11086a21625.jpeg"
                            }
                        },
                        {
                            "type": "title",
                            "content": "设备提供"
                        },
                        {
                            "type": "text",
                            "content": "教学全程使用顶尖的设备，与市场接轨，让学员能够接触到行业最前沿的内容，为就业打下坚实的基础。"
                        },
                        {
                            "type": "image",
                            "content": {
                                "image": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/015b11086bcc681.jpeg",
                                "wapImage": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/015b11086bb079d.jpeg"
                            }
                        }
                    ]
                },
                {
                    "title": "导师团队",
                    "content": [
                        {
                            "type": "image",
                            "content": {
                                "image": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/015b1163a8781e9.jpeg",
                                "wapImage": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/015b1163a86a6cd.jpeg"
                            }
                        }
                    ]
                }
            ],
            "subjectInfo": {
                "title": "课程设置",
                "intros": [
                    "理论环节：专业的设备技术负责人带你重新了解摄影助理的工作，摄影助理该做什么？摄影助理该遵守的25个原则，了解各种行业黑话，三大主流品牌摄影机介绍，带你认识各类镜头群。全方位提升你的影视行业知识水平，拓宽你的视野。摄影助理做的绝对不仅仅是“搬砖”！",
                    "实践环节：所有学员分成小组进行实战演练，每组配有设备技术员手把手教操作。我们提供行业顶尖设备支持！FS7、RED、ARRI摄影机，蔡司、库克、安琴镜头群，三轴稳定器、电子炮、DOLLY车任你操作！"
                ],
                "list": [
                    {
                        "title": "1",
                        "sub": [
                            {
                                "title": "摄影助理工作介绍",
                                "sub": [
                                    "1.助理工作介绍：摄影助理要做什么？",
                                    "2.行业基础认知：做摄影助理的途径",
                                    "3.做摄影助理需要遵守原则",
                                    "4.理论知识学习"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "2",
                        "sub": [
                            {
                                "title": "学习机器与镜头、云台和脚架的使用",
                                "sub": [
                                    "1.机器卡口介绍",
                                    "2.镜头介绍",
                                    "3.云台脚架介绍",
                                    "4.实践内容：三大主流机器SONY fs7  RED dragon  ALEXA mini 搭配云台脚架的拆装出入库练习"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "3",
                        "sub": [
                            {
                                "title": "灰片、跟焦器、遮光斗等附件的使用",
                                "sub": [
                                    "1.灰片的介绍",
                                    "2.跟焦器的介绍",
                                    "3.遮光斗的介绍",
                                    "4.实践内容：附件的拆装练习"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "4",
                        "sub": [
                            {
                                "title": "移动器材的使用",
                                "sub": [
                                    "1.轨道的介绍",
                                    "2.DOLLY车的介绍",
                                    "3.实践内容：轨道的铺设和DOLLY车的拆装练习"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "5",
                        "sub": [
                            {
                                "title": "特种设备的使用",
                                "sub": [
                                    "1.三轴稳定器的介绍",
                                    "2.实践内容：三轴稳定器调平，三轴稳定器搭配摇臂DOLLY车轨道的使用"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "6",
                        "sub": [
                            {
                                "title": "大摇臂电子炮等设备的使用",
                                "sub": [
                                    "1.摇臂、升降的介绍",
                                    "2.实践内容：电子炮（大摇臂），升降的安装及使用"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "7",
                        "sub": [
                            {
                                "title": "摄影机菜单的学习和灯光基础了解",
                                "sub": [
                                    "1.Red机器菜单讲解；ARRI mini菜单讲解；灯光设备及附件的认识",
                                    "2.实践内容：电子炮搭配轨道DOLLY车的使用，ARRI系列灯光设备和魔术腿等脚架的操作与使用"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "8",
                        "sub": [
                            {
                                "title": "结业考试",
                                "sub": [
                                    "学员是否获得就业机会将由日常表现和结业考试成绩共同决定"
                                ]
                            },
                            {
                                "title": "毕业典礼"
                            }
                        ]
                    }
                ]
            },
            "registrationInfo": {
                "title": "报名信息",
                "list": [
                    {
                        "title": "第 2 期 - 杭州",
                        "startTime": "7月21日",
                        "endTime": "7月28日",
                        "nums": "35-40人",
                        "price": "7800",
                        "originPrice": "",
                        "signupLink": "http://xinpianchangschool.mikecrm.com/UeSekpj"
                    },
                    {
                        "title": " 第 3 期 - 杭州",
                        "startTime": "8月24日",
                        "endTime": "8月31日",
                        "nums": "35-40人",
                        "price": "7800",
                        "originPrice": "",
                        "signupLink": "http://xinpianchangschool.mikecrm.com/UeSekpj"
                    }
                ],
                "extra": [
                    {
                        "title": "优惠信息",
                        "content": [
                            {
                                "redTitle": "集赞减免",
                                "subContentList": [
                                    "转发此篇文章至朋友圈，集满 66 个赞后联系新片场学院小豆渣进行验证。开课前10天提交截图至“新片场学院小豆渣”（微信号：NSAcademy），可在学费尾款支付时减免 300 元学费。"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "报名流程",
                        "content": [
                            "1.在申请页面提交资料，并预付500元报名押金。",
                            "2.审核通过即报名成功，报名费将直接抵充学费。",
                            "3.报名后请联系“新片场学院小豆渣”核对报名信息。",
                            "4.报名通过后，若因故无法参加，报名押金将不予退还，可选择后续开课班级进行学习；学费尾款支付成功后，若开课前三天内因个人原因无法参加，学费将不予退还，参加后续课程时，因影响工作安排，需额外支付3000元作为改签费。"
                        ]
                    },
                    {
                        "title": "尾款支付",
                        "content": [
                            "1.尾款支付方式：对公转账/支付宝转账/微信转账；",
                            "2.收到尾款支付方式起 3 日内完成学费尾款支付。"
                        ]
                    }
                ]
            },
            "qa": {
                "title": "常见问题",
                "list": [
                    {
                        "q": "线下实训营学费能否分期付款？",
                        "a": "新片场学院支持分期付款，具体支持信用卡、蚂蚁花呗两种分期付款方式，因每人账户情况不同，新片场不对分期额度等事项进行解释，详情请参考银行及支付宝的相关政策。"
                    },
                    {
                        "q": "报名对年龄或学历有要求么？",
                        "a": "本课程年满16周岁即可报名，对于申请的学历不设限制。"
                    },
                    {
                        "q": "什么时间能知道报名是否成功？",
                        "a": "每期报名截止后三天内，会有工作人员与你沟通是否报名成功。"
                    },
                    {
                        "q": "实训期期间的课程时间安排？",
                        "a": "上课时间为9:00-18:00，每天课程容量8小时左右，7天连续上课。"
                    }
                ]
            },
            "sidebtn": {
                "qrImage": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/05/285b0b9c8ee0f54.jpeg",
                "desc": [
                    "新片场学院小豆渣",
                    "（微信号：NSAcademy）"
                ]
            },
            "mobileShareConfig": {
                "shareTitle": "新片场学院摄影助理职业技术培训",
                "shareDesc": "手把手教你成为一名合格的摄影助理，迅速掌握从业技能，毕业提供就业机会",
                "shareImg": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/015b112c706daa2.jpeg",
                "shareWeiboDesc": "新片场学院摄影助理职业技术培训，手把手教你成为一名合格的摄影助理，迅速掌握从业技能，毕业提供就业机会！"
            }
        }
    }



#自定义newtalk课程
def newtalk_course():
    return{
        # 标题
        "title": "newtalk课程",
        #主讲人
        "author":"测试|新片场",
        # 内容标签（自定义）
        "tags": ["第三方", "接口", "添加"],
        #封面图
        "cover":"https://oss-xpc0.xpccdn.com/Upload/edu/2018/07/135b48163b28cfe.jpg",
        #内容链接
        "url":"https://www.baidu.com"


    }

#自定义在线班级
def online_course_json(online_id):
    return{

            "title": "接口新建班级",
            "profile": {
                "notice": [
                    {
                        "type": "text",
                        "content": "测试这是公告"
                    },
                    {
                        "type": "image",
                        "content": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/07/175b4db5b7a3dbb.jpg"
                    }
                ]
            },
            "subject_id": online_id,
            "brief": "1对1指导 | 线上社群 | 在线视频课 | 直播互动 | 作品点评",
            "start_time": 1531819419.628,
            "end_time": 0,
            "is_onshelf": 0,
            "priceout": 1066,
            "copy_course_id": 0


    }


#章的标题
def chapter_title():
    return [
        {"title": "测试小节001"},
        {"title": "测试小节002"}

    ]


#章的标题
def section_title():
    return [
        {"title": "测试小节001"},
        {"title": "测试小节002"}

    ]

#随机生成录播课程id，()内值为id范围区间
def library_id():
    library_id = randint(300,500)
    return library_id


