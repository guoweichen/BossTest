# -*- coding: cp936 -*-

from random import *







# �Զ���γ�ID
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

#����6λ��������
def get_account(num):
    accounts = []
    for index in range(1, num+1):
        accounts.append(
            {"username": "user%s" % index, "password": str(index) * 6},
        )

    return accounts

#���ѧԱ��id
def get_user_ids():
    return[
        {"user_ids":"1000001,10000003,10000005"}
        ]


#��ʽת��
#stringת����int��list
def str_list(str):
    results = str.split(",")  #��ָ���ָ�����str��Ƭ
    results = list(map(int, results))#strת��Ϊint��list
    return results

def excp(str,x):
    results = str.split(",")  #��ָ���ָ�����str��Ƭ
    results = list(map(int, results))#strת��Ϊint��list
    return results[x]


#�Զ�����Ӫ�γ�
def get_online_subject():
    return{
        #����
        "title": "������Ӫ��",
        #�γ̱�ǩ���Զ��壩
        "tags": [ "����","�ӿ�","���"],
        #�γ����� ��0-���� 2-ȫ�ܾ�ҵ��
        "type": 0,
        #���
        "brief": "���޼��",
        #���ǩ ��(null)/Ԥ���ػ�/��ʱ�ػ�
        "mark": "",
        #�Ƿ��շ� ��0-�շ�1-���
        "is_free": 0,
        #�ṩ��id
        "supplier_id": "34",
        # ����ͼƬ
        "images": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/135b208bb253e55.jpeg",
        # ��ƷͼƬ
        "goods_image": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/135b208bb609454.jpeg"
        }

#�Զ������¿Σ�url��
def offline_subject_url():
    return{
        # ����
        "title": "url��������",
        # �γ̱�ǩ���Զ��壩
        "tags": ["������", "�ӿ�", "���"],
        # �γ����� ��0-���� 1-���¿� 2-ȫ�ܾ�ҵ��
        "type": 1,
        # ���
        "brief": "",
        # ���ǩ �������γ̣��ޣ�
        "mark": "",
        # �ṩ��id
        "supplier_id": "34",
        # ����ͼƬ
        "images": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/135b208bb253e55.jpeg",
        #�Ƿ�����ת���� 0-�� 1-��
        "is_third_content": 1,
        #��ת����
        "url": "https://www.baidu.com"


    }
#�Զ������¿Σ�json��
def offline_subject_json():
    return{
        # ����
        "title": "json��������",
        # �γ̱�ǩ���Զ��壩
        "tags": ["������", "�ӿ�", "���"],
        # �γ����� ��0-���� 1-���¿� 2-ȫ�ܾ�ҵ��
        "type": 1,
        # ���
        "brief": "",
        # ���ǩ �������γ̣��ޣ�
        "mark": "",
        # �ṩ��id
        "supplier_id": "34",
        # ����ͼƬ
        "images": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/135b208bb253e55.jpeg",
        #�Ƿ�����ת���� 0-�� 1-��
        "is_third_content": 0

    }
#���¿�json����
def offline_json():
    return{
        "expand": "introduction",
        "profile": {
            "pageInfo": {
                "title": " ��Ӱ����ְҵ������ѵ",
                "keywords": " ��������,��Ӱ,��Ӱ����,ְҵ,��ѵ",
                "description": "���γ̲��á�ʦͽʽ����ѧ�������ְ��ֽ����Ϊһ���ϸ����Ӱ����Ѹ�����մ�ҵ���ܣ���ҵ�ṩ��ҵ���ᡣ"
            },
            "banner": {
                "image": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/015b11086e94346.jpeg",
                "wapImage": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/015b11086a7e4f9.jpeg"
            },
            "basicInfo": [
                {
                    "title": "�γ̼��",
                    "content": [
                        {
                            "type": "text",
                            "content": "���������Ӱ����ҵ��չ��ͷǿ�����������ݺ��˲Ŷ̰��������Ϊ��Ӱ�����λ������������й��г�����Ӱ�ӻ����˲ŵ����������վ���������Ӧ�󣬵���ҵ��Աˮƽ�β�롣��������Ӱ������һ��λ�ϣ�Ŀǰ��û��ȫ�桢ϵͳ�Ľ������ƺ��˲����������"
                        },
                        {
                            "type": "text",
                            "content": "�����һ������Ƭ��ѧԺ�̡���ҵ����������͡���ʳ��Ƶ��������������ʽ�����ˡ���Ӱ����ְҵ������ѵ����"
                        },
                        {
                            "type": "text",
                            "content": "���γ���һ�������Ӱ�����ְҵ������ѵ�Σ��ܹ���ѧϰ֮�����ռܻ�λ���������ࡢ�������Լ���е���㣨�����dolly���������ȶ�����ҡ�۵ȣ��ĸ������������ٳ�Ϊһ���ܱ��г����Ͽɵ���Ӱ��������Ϊδ������Ӱʦ֮·���¼�ʵ�Ļ�����"
                        },
                        {
                            "type": "title",
                            "content": "�ڿ��Ŷ�"
                        },
                        {
                            "type": "text",
                            "content": "��Ƭ��ѧԺ����Դ��רҵ��Ӱ�豸�����Ŷ��׿����Ŷ��ܼ��ר�ҵ�ʦ���Ŷ��ڿ�ģʽ��ÿһλ�Ŷ��ܼ඼ӵ�г���10�����Ŀ���鼰�ڿξ��飬ÿλ��ʦ�����Լ�רҵ���������ó��Ĳ��֣���ͬ����רҵ����Ӱ����γ̣����ۺ�ʵ�����ϣ����÷����г���ҵ��Ŀ������"
                        },
                        {
                            "type": "title",
                            "content": "��ҵ����"
                        },
                        {
                            "type": "text",
                            "content": "ÿ��ѧԱ��ҵ�󣬽�ѡ��5-10������ѧԱ������Ƭ����Դ����ýֱ�����͵���������ʵϰ�;�ҵ���޷��νӣ�����������ҵ����ҵ�����㹤��5-15������׬��ѧ�ѣ������ݽ������г����飬��Ӱ������н400-1500Ԫ���ȣ�"
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
                    "title": "��ѧչʾ",
                    "content": [
                        {
                            "type": "title",
                            "content": "��ѧ�ŶӺͳ���"
                        },
                        {
                            "type": "text",
                            "content": "Դ����ý�����ܼ����Դ�������Ŷ�ȫ�̸�����Ӱ����γ̣�����400ƽ����רҵ��Ӱ����Ӱ����ΪѧԱ�ڿγ��أ�Ϊ�ֳ���ѧ��ѧԱʵ���ṩ��ݡ�"
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
                            "content": "�豸�ṩ"
                        },
                        {
                            "type": "text",
                            "content": "��ѧȫ��ʹ�ö�����豸�����г��ӹ죬��ѧԱ�ܹ��Ӵ�����ҵ��ǰ�ص����ݣ�Ϊ��ҵ���¼�ʵ�Ļ�����"
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
                    "title": "��ʦ�Ŷ�",
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
                "title": "�γ�����",
                "intros": [
                    "���ۻ��ڣ�רҵ���豸���������˴��������˽���Ӱ����Ĺ�������Ӱ�������ʲô����Ӱ��������ص�25��ԭ���˽������ҵ�ڻ�����������Ʒ����Ӱ�����ܣ�������ʶ���ྵͷȺ��ȫ��λ�������Ӱ����ҵ֪ʶˮƽ���ؿ������Ұ����Ӱ�������ľ��Բ������ǡ���ש����",
                    "ʵ�����ڣ�����ѧԱ�ֳ�С�����ʵս������ÿ�������豸����Ա�ְ��ֽ̲����������ṩ��ҵ�����豸֧�֣�FS7��RED��ARRI��Ӱ������˾����ˡ����پ�ͷȺ�������ȶ����������ڡ�DOLLY�����������"
                ],
                "list": [
                    {
                        "title": "1",
                        "sub": [
                            {
                                "title": "��Ӱ����������",
                                "sub": [
                                    "1.���������ܣ���Ӱ����Ҫ��ʲô��",
                                    "2.��ҵ������֪������Ӱ�����;��",
                                    "3.����Ӱ������Ҫ����ԭ��",
                                    "4.����֪ʶѧϰ"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "2",
                        "sub": [
                            {
                                "title": "ѧϰ�����뾵ͷ����̨�ͽżܵ�ʹ��",
                                "sub": [
                                    "1.�������ڽ���",
                                    "2.��ͷ����",
                                    "3.��̨�żܽ���",
                                    "4.ʵ�����ݣ�������������SONY fs7  RED dragon  ALEXA mini ������̨�żܵĲ�װ�������ϰ"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "3",
                        "sub": [
                            {
                                "title": "��Ƭ�����������ڹ⶷�ȸ�����ʹ��",
                                "sub": [
                                    "1.��Ƭ�Ľ���",
                                    "2.�������Ľ���",
                                    "3.�ڹ⶷�Ľ���",
                                    "4.ʵ�����ݣ������Ĳ�װ��ϰ"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "4",
                        "sub": [
                            {
                                "title": "�ƶ����ĵ�ʹ��",
                                "sub": [
                                    "1.����Ľ���",
                                    "2.DOLLY���Ľ���",
                                    "3.ʵ�����ݣ�����������DOLLY���Ĳ�װ��ϰ"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "5",
                        "sub": [
                            {
                                "title": "�����豸��ʹ��",
                                "sub": [
                                    "1.�����ȶ����Ľ���",
                                    "2.ʵ�����ݣ������ȶ�����ƽ�������ȶ�������ҡ��DOLLY�������ʹ��"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "6",
                        "sub": [
                            {
                                "title": "��ҡ�۵����ڵ��豸��ʹ��",
                                "sub": [
                                    "1.ҡ�ۡ������Ľ���",
                                    "2.ʵ�����ݣ������ڣ���ҡ�ۣ��������İ�װ��ʹ��"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "7",
                        "sub": [
                            {
                                "title": "��Ӱ���˵���ѧϰ�͵ƹ�����˽�",
                                "sub": [
                                    "1.Red�����˵����⣻ARRI mini�˵����⣻�ƹ��豸����������ʶ",
                                    "2.ʵ�����ݣ������ڴ�����DOLLY����ʹ�ã�ARRIϵ�еƹ��豸��ħ���ȵȽżܵĲ�����ʹ��"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "8",
                        "sub": [
                            {
                                "title": "��ҵ����",
                                "sub": [
                                    "ѧԱ�Ƿ��þ�ҵ���Ὣ���ճ����ֺͽ�ҵ���Գɼ���ͬ����"
                                ]
                            },
                            {
                                "title": "��ҵ����"
                            }
                        ]
                    }
                ]
            },
            "registrationInfo": {
                "title": "������Ϣ",
                "list": [
                    {
                        "title": "�� 2 �� - ����",
                        "startTime": "7��21��",
                        "endTime": "7��28��",
                        "nums": "35-40��",
                        "price": "7800",
                        "originPrice": "",
                        "signupLink": "http://xinpianchangschool.mikecrm.com/UeSekpj"
                    },
                    {
                        "title": " �� 3 �� - ����",
                        "startTime": "8��24��",
                        "endTime": "8��31��",
                        "nums": "35-40��",
                        "price": "7800",
                        "originPrice": "",
                        "signupLink": "http://xinpianchangschool.mikecrm.com/UeSekpj"
                    }
                ],
                "extra": [
                    {
                        "title": "�Ż���Ϣ",
                        "content": [
                            {
                                "redTitle": "���޼���",
                                "subContentList": [
                                    "ת����ƪ����������Ȧ������ 66 ���޺���ϵ��Ƭ��ѧԺС����������֤������ǰ10���ύ��ͼ������Ƭ��ѧԺС��������΢�źţ�NSAcademy��������ѧ��β��֧��ʱ���� 300 Ԫѧ�ѡ�"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "��������",
                        "content": [
                            "1.������ҳ���ύ���ϣ���Ԥ��500Ԫ����Ѻ��",
                            "2.���ͨ���������ɹ��������ѽ�ֱ�ӵֳ�ѧ�ѡ�",
                            "3.����������ϵ����Ƭ��ѧԺС�������˶Ա�����Ϣ��",
                            "4.����ͨ����������޷��μӣ�����Ѻ�𽫲����˻�����ѡ��������ΰ༶����ѧϰ��ѧ��β��֧���ɹ���������ǰ�����������ԭ���޷��μӣ�ѧ�ѽ������˻����μӺ����γ�ʱ����Ӱ�칤�����ţ������֧��3000Ԫ��Ϊ��ǩ�ѡ�"
                        ]
                    },
                    {
                        "title": "β��֧��",
                        "content": [
                            "1.β��֧����ʽ���Թ�ת��/֧����ת��/΢��ת�ˣ�",
                            "2.�յ�β��֧����ʽ�� 3 �������ѧ��β��֧����"
                        ]
                    }
                ]
            },
            "qa": {
                "title": "��������",
                "list": [
                    {
                        "q": "����ʵѵӪѧ���ܷ���ڸ��",
                        "a": "��Ƭ��ѧԺ֧�ַ��ڸ������֧�����ÿ������ϻ������ַ��ڸ��ʽ����ÿ���˻������ͬ����Ƭ�����Է��ڶ�ȵ�������н��ͣ�������ο����м�֧������������ߡ�"
                    },
                    {
                        "q": "�����������ѧ����Ҫ��ô��",
                        "a": "���γ�����16���꼴�ɱ��������������ѧ���������ơ�"
                    },
                    {
                        "q": "ʲôʱ����֪�������Ƿ�ɹ���",
                        "a": "ÿ�ڱ�����ֹ�������ڣ����й�����Ա���㹵ͨ�Ƿ����ɹ���"
                    },
                    {
                        "q": "ʵѵ���ڼ�Ŀγ�ʱ�䰲�ţ�",
                        "a": "�Ͽ�ʱ��Ϊ9:00-18:00��ÿ��γ�����8Сʱ���ң�7�������ϿΡ�"
                    }
                ]
            },
            "sidebtn": {
                "qrImage": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/05/285b0b9c8ee0f54.jpeg",
                "desc": [
                    "��Ƭ��ѧԺС����",
                    "��΢�źţ�NSAcademy��"
                ]
            },
            "mobileShareConfig": {
                "shareTitle": "��Ƭ��ѧԺ��Ӱ����ְҵ������ѵ",
                "shareDesc": "�ְ��ֽ����Ϊһ���ϸ����Ӱ����Ѹ�����մ�ҵ���ܣ���ҵ�ṩ��ҵ����",
                "shareImg": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/06/015b112c706daa2.jpeg",
                "shareWeiboDesc": "��Ƭ��ѧԺ��Ӱ����ְҵ������ѵ���ְ��ֽ����Ϊһ���ϸ����Ӱ����Ѹ�����մ�ҵ���ܣ���ҵ�ṩ��ҵ���ᣡ"
            }
        }
    }



#�Զ���newtalk�γ�
def newtalk_course():
    return{
        # ����
        "title": "newtalk�γ�",
        #������
        "author":"����|��Ƭ��",
        # ���ݱ�ǩ���Զ��壩
        "tags": ["������", "�ӿ�", "���"],
        #����ͼ
        "cover":"https://oss-xpc0.xpccdn.com/Upload/edu/2018/07/135b48163b28cfe.jpg",
        #��������
        "url":"https://www.baidu.com"


    }

#�Զ������߰༶
def online_course_json(online_id):
    return{

            "title": "�ӿ��½��༶",
            "profile": {
                "notice": [
                    {
                        "type": "text",
                        "content": "�������ǹ���"
                    },
                    {
                        "type": "image",
                        "content": "https://oss-xpc0.xpccdn.com/Upload/edu/2018/07/175b4db5b7a3dbb.jpg"
                    }
                ]
            },
            "subject_id": online_id,
            "brief": "1��1ָ�� | ������Ⱥ | ������Ƶ�� | ֱ������ | ��Ʒ����",
            "start_time": 1531819419.628,
            "end_time": 0,
            "is_onshelf": 0,
            "priceout": 1066,
            "copy_course_id": 0


    }


#�µı���
def chapter_title():
    return [
        {"title": "����С��001"},
        {"title": "����С��002"}

    ]


#�µı���
def section_title():
    return [
        {"title": "����С��001"},
        {"title": "����С��002"}

    ]

#�������¼���γ�id��()��ֵΪid��Χ����
def library_id():
    library_id = randint(300,500)
    return library_id


