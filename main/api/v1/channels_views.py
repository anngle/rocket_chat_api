#coding=utf-8
from flask_restful import Resource
from main.extensions import api,rocket

from flask import request

from .version import dev_1
v1 = dev_1



class AddAll(Resource):
    """将Rocket.Chat服务器的所有用户添加到该频道。

    https://rocket.chat/docs/developer-guides/rest-api/channels/addall/

    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/addall
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道id
            * - activeUsersOnly
              - true
              - 0,或者1
              - 仅添加激活用户

        **请求示例**::

            r = get(url,{'roomId':roomId,'activeUsersOnly':1})

        **请求结果**:
         - success:boolean
         - channels:json

        """
        roomId = request.args.get('roomId','')
        activeUsersOnly = request.args.get('activeUsersOnly',0)
        if activeUsersOnly:
            activeUsersOnly = True
        else:
            activeUsersOnly = False
        try:
            r = rocket.channels_add_all(room_id=roomId,activeUsersOnly=activeUsersOnly)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'添加失败。'},401

        r = r.json()
        return {
            'success': True,
            'channels': r['channel']
        },200  


class Archive(Resource):
    """保存 频道

    https://rocket.chat/docs/developer-guides/rest-api/channels/archive/

    """
    def get(self): 
        """

        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/archive
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道id

        **请求示例**::

            r = get(url,{'roomId':roomId})

        **请求结果**:
         - success:boolean

        """
        roomId = request.args.get('roomId','')
        
        try:
            r = rocket.channels_archive(room_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'存档失败。'},401

        r = r.json()
        return {
            'success': True,
        },200  


class CleanHistory(Resource):
    """清理频道的历史记录，需要特殊许可。插件无该接口
    """
    pass 


class Close(Resource):
    """关闭频道

    https://rocket.chat/docs/developer-guides/rest-api/channels/close/
    """
    def get(self): 
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/close
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道id

        **请求示例**::

            r = get(url,{'roomId':roomId})

        **请求结果**:
         - success:boolean

        """
        roomId = request.args.get('roomId','')
        
        try:
            r = rocket.channels_close(roomId=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'关闭失败。'},401

        r = r.json()
        return {
            'success': True,
        },200  
 

class Counters(Resource):
    """获取频道计数 插件无该接口

    https://rocket.chat/docs/developer-guides/rest-api/channels/counters/

    """
    pass 


class Create(Resource):
    """创建频道

    https://rocket.chat/docs/developer-guides/rest-api/channels/create/

    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/create
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - name
              - channelname
              - 必须
              - 频道名称
            * - members
              - "rocket.cat,admin"
              - 默认为[]
              - 创建时要添加的用户
            * - readOnly
              - 1
              - 默认0
              - 设置频道是否只读

        **请求示例**::

            r = put(url,data={'name':'channelname','members':"rocket.cat,admin",readOnly:1})

        **请求结果**:
         - success:boolean
         - channel:json


        """ 
        name = request.form['name']
        members = request.form['members']
        readOnly = request.form['readOnly']

        members = members.split(',')
        if readOnly:
            readOnly = True
        else:
            readOnly = False 

        try:
            r = rocket.channels_create(name=name,members=members,readOnly=readOnly)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'创建失败。'},401

        return {
            'channel':r.json()['channel'],
            'success':True
        }


class ChannelsDelete(Resource):
    """删除频道

    https://rocket.chat/docs/developer-guides/rest-api/channels/delete/

    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/channels_delete
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomName
              - general
              - 必须
              - 频道名称
            

        **请求示例**::

            r = put(url,data={'roomName':'general'})

        **请求结果**:
         - success:boolean
         - channel:json


        """ 
        roomName = request.form['roomName']
        
        try:
            r = rocket.channels_delete(channel=roomName)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'删除失败。'},401

        return {
            'channel':r.json()['channel'],
            'success':True
        }


class Files(Resource):
    """获取频道文件

    https://rocket.chat/docs/developer-guides/rest-api/channels/files/
    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/files
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomName
              - general
              - 必须
              - 频道名称
            

        **请求示例**::

            r = put(url,data={'roomName':'general'})

        **请求结果**:
         - success:boolean
         - files:json
         - count
         - offset
         - total


        """ 
        roomName = request.form['roomName']
        
        try:
            r = rocket.channels_files(room_name=roomName)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'获取失败。'},401

        return {
            'files':r.json()['files'],
            'count':r.json()['count'],
            'offset':r.json()['offset'],
            'total':r.json()['total'],
            'success':True
        } 


class GetAllUserMentionsByChannel(Resource):
    """获取所有用户的频道信息

    https://rocket.chat/docs/developer-guides/rest-api/channels/getallusermentionsbychannel/

    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/get_all_user_mentions_by_channel
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道id

        **请求示例**::

            r = get(url,data={'roomId':'ByehQjC44FwMeiLbX'})

        **请求结果**:
         - success:boolean
         - mentions:json
         - count
         - offset
         - total

        """ 
        roomId = request.form['roomId']
        
        try:
            r = rocket.channels_files(room_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'获取失败。'},401

        return {
            'mentions':r.json()['mentions'],
            'count':r.json()['count'],
            'offset':r.json()['offset'],
            'total':r.json()['total'],
            'success':True
        }  


class GetIntegrations(Resource):
    """获取频道的集成。

    https://rocket.chat/docs/developer-guides/rest-api/channels/getintegrations/    

    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/get_integrations
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道id

        **请求示例**::

            r = get(url,data={'roomId':'ByehQjC44FwMeiLbX'})

        **请求结果**:
         - success:boolean
         - integrations:json

        """ 
        roomId = request.form['roomId']
        
        try:
            r = rocket.channels_get_integrations(room_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'获取失败。'},401

        return {
            'integrations':r.json()['integrations'],
            'success':True
        }   


class History(Resource):
    """历史频道

    https://rocket.chat/docs/developer-guides/rest-api/channels/history/
    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/history
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道id
            * - latest
              - 2018-10-15T16:42:25.304Z
              - 默认 现在
              - 要检索的时间范围
            * - oldest
              - 2018-10-15T17:42:25.304Z
              - 默认 n/a
              - 要检索的时间范围
            * - inclusive
              - 1
              - 默认0
              - 是否应包括最新和最旧的消息
            * - count
              - 100
              - 默认20
              - 要检索的消息数量
            * - unreads
              - 1
              - 默认0
              - 是否应包括未读数量。

        **请求示例**::

            data = {
                'room_id'=roomId,
                'latest'=latest,
                'oldest'=oldest,
                'inclusive'=inclusive,
                'count'=count,
                'unreads'=unreads,
            }
            r = get(url,data=data)

        **请求结果**:
         - success:boolean
         - messages:json

        """ 
        roomId = request.args.get('roomId')
        latest = request.args.get('latest')
        oldest = request.args.get('oldest')
        inclusive = request.args.get('inclusive',0)
        count = request.args.get('count')
        unreads = request.args.get('unreads',0)

        if inclusive:
            inclusive = True
        else:
            inclusive = False
        if unreads:
            unreads = True
        else:
            unreads = False

        try:
            r = rocket.channels_history(
                    room_id=roomId,
                    latest=latest,
                    oldest=oldest,
                    inclusive=inclusive,
                    count=count,
                    unreads=unreads,
                )
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'获取失败。'},401

        return {
            'messages':r.json()['messages'],
            'success':True
        }    


class ChannelsInfo(Resource):
    """频道信息

    https://rocket.chat/docs/developer-guides/rest-api/channels/info/
    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/channels_info
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomName
              - general
              - 必须
              - 频道名称

        **请求示例**::

            r = get(url,data={'roomName':'general'})

        **请求结果**:
         - success:boolean
         - channel:json

        """ 
        roomName = request.form['roomName']
        
        try:
            r = rocket.channels_info(channel=roomName)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'获取失败。'},401

        return {
            'channel':r.json()['channel'],
            'success':True
        }    


class Invite(Resource):
    """添加用户到频道

    https://rocket.chat/docs/developer-guides/rest-api/channels/invite/    

    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/invite
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道id
            * - userId
              - nSYqWzZ4GsKTX4dyK
              - 必须
              - 用户id


        **请求示例**::

            r = put(url,data={'roomId':'ByehQjC44FwMeiLbX'，'userId':'nSYqWzZ4GsKTX4dyK'})

        **请求结果**:
         - success:boolean
         - channel:json

        """ 
        roomId = request.form['roomId']
        userId = request.form['userId']
        
        try:
            r = rocket.channels_invite(room_id=roomId,user_id=userId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'添加失败。'},401

        return {
            'channel':r.json()['channel'],
            'success':True
        }     


class Kick(Resource):
    """从频道中删除用户。

    https://rocket.chat/docs/developer-guides/rest-api/channels/kick/    

    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/kick
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道id
            * - userId
              - nSYqWzZ4GsKTX4dyK
              - 必须
              - 用户id


        **请求示例**::

            r = put(url,data={'roomId':'ByehQjC44FwMeiLbX'，'userId':'nSYqWzZ4GsKTX4dyK'})

        **请求结果**:
         - success:boolean
         - channel:json

        """ 
        roomId = request.form['roomId']
        userId = request.form['userId']
        
        try:
            r = rocket.channels_invite(room_id=roomId,user_id=userId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'删除失败。'},401

        return {
            'channel':r.json()['channel'],
            'success':True
        }      


class Leave(Resource):
    """从通道中删除主要用户。

    https://rocket.chat/docs/developer-guides/rest-api/channels/leave/    

    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/leave
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道id

        **请求示例**::

            r = put(url,data={'roomId':'ByehQjC44FwMeiLbX'})

        **请求结果**:
         - success:boolean
         - channel:json

        """ 
        roomId = request.form['roomId']
        
        try:
            r = rocket.channels_leave(room_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'删除失败。'},401

        return {
            'channel':r.json()['channel'],
            'success':True
        }       


class ChannelList(Resource):
    """频道列表

    https://rocket.chat/docs/developer-guides/rest-api/channels/archive/    

    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/channels_list
              - 需要auth
              - GET

        **请求示例**::

            r = get(url)
        
        请求结果：
         - count
         - total
         - offset
         - success:boolean
         - channels:json

        ::

            {
                "count": 1,
                "total": 1,
                "offset": 0,
                "success": true,
                "channels": [
                    {
                        "_id": "GENERAL",
                        "ts": "2018-10-08T07:04:50.112Z",
                        "t": "c",
                        "name": "general",
                        "usernames": [],
                        "msgs": 11,
                        "usersCount": 7,
                        "default": true,
                        "_updatedAt": "2018-10-13T02:38:32.253Z",
                        "lm": "2018-10-08T08:48:25.381Z",
                        "lastMessage": {
                            "alias": "Farnsworth",
                            "msg": "good news everyone!",
                            "attachments": [],
                            "parseUrls": true,
                            "bot": null,
                            "groupable": false,
                            "ts": "2018-10-08T08:48:25.381Z",
                            "u": {
                                "_id": "9wC7Q5QTaetLnQJi6",
                                "username": "6471750",
                                "name": "\u5b89\u4e8c"
                            },
                            "rid": "GENERAL",
                            "_id": "F4WijXnbX8S27BhQY",
                            "_updatedAt": "2018-10-08T08:48:25.400Z",
                            "editedBy": null,
                            "editedAt": null,
                            "emoji": null,
                            "avatar": null,
                            "customFields": null,
                            "reactions": null,
                            "mentions": [],
                            "channels": [],
                            "sandstormSessionId": null
                        }
                    }
                ]
            }

        """ 

        try:
            r = rocket.channels_list()
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'获取频道列表失败。'},401

        r = r.json()
        return {
            'count': r['count'],
            'total': r['total'],
            'offset': r['offset'],
            'success': True,
            'channels': r['channels']
        },200 
        

class ListJoined(Resource):
    """已加入的频道

    https://rocket.chat/docs/developer-guides/rest-api/channels/list-joined/
    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/list_joined
              - 需要auth
              - GET

        **请求示例**::

            r = get(url)
        
        请求结果：
         - success:boolean
         - channels:json

        """ 

        try:
            r = rocket.channels_list_joined()
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'获取失败。'},401

        r = r.json()
        return {
            'success': True,
            'channels': r['channels']
        },200   


class Members(Resource):
    """频道会员列表

    https://rocket.chat/docs/developer-guides/rest-api/channels/members/    

    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/members
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomName
              - general
              - 必须
              - 频道名称

        **请求示例**::

            r = get(url,data={'roomName':'general'})

        **请求结果**:
         - success:boolean
         - channel:json
         - count
         - offset
         - total

        """ 
        roomName = request.form['roomName']
        
        try:
            r = rocket.channels_members(channel=roomName)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'获取失败。'},401

        return {
            'members':r.json()['members'],
            'count':r.json()['count'],
            'offset':r.json()['offset'],
            'total':r.json()['total'],
            'success':True,
        } ,200    


class Messages(Resource):
    """频道消息 插件无该接口

    https://rocket.chat/docs/developer-guides/rest-api/channels/messages/    

    """
    pass 


class Moderators(Resource):
    """频道版主 插件无该接口

    https://rocket.chat/docs/developer-guides/rest-api/channels/moderators/    

    """
    pass 


class Open(Resource):
    """打开频道

    https://rocket.chat/docs/developer-guides/rest-api/channels/open/    

    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/open
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道名称

        **请求示例**::

            r = get(url,data={'roomId':'ByehQjC44FwMeiLbX'})

        **请求结果**:
         - success:boolean

        """ 
        roomId = request.form['roomId']
        
        try:
            r = rocket.channels_open(room_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'打开失败。'},401

        return {
            'success':True,
        } ,200     


class Rename(Resource):
    """频道命名

    https://rocket.chat/docs/developer-guides/rest-api/channels/rename/    

    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/rename
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道id
            * - name
              - new-name
              - 必须
              - 频道名称，唯一

        **请求示例**::

            r = put(url,data={'roomId':'ByehQjC44FwMeiLbX','name':'new name'})

        **请求结果**:
         - success:boolean
         - channel:json

        """ 
        roomId = request.form['roomId']
        name = request.form['name']
        
        try:
            r = rocket.channels_rename(room_id=roomId,name=name)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'命名失败。'},401

        return {
            'channel':r.json()['channel'],
            'success':True,
        },200    


class Roles(Resource):
    """列出频道中所有用户的角色

    https://rocket.chat/docs/developer-guides/rest-api/channels/roles/    

    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/roles
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道名称

        **请求示例**::

            r = get(url,data={'roomId':'ByehQjC44FwMeiLbX'})

        **请求结果**:
         - success:boolean
         - roles:json

        """ 
        roomId = request.form['roomId']
        
        try:
            r = rocket.channels_roles(room_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'获取角色失败。'},401

        return {
            'success':True,
            'roles':r.json()['roles']
        },200      


class SetCustomFields(Resource):
    """设置频道自定义字段

    https://rocket.chat/docs/developer-guides/rest-api/channels/setcustomfields/    

    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/setcustomfields
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - GENERAL
              - 必须
              - 频道id
            * - customFields
              - {"organization": "tra-la-la"}
              - 必须
              - 设置的自定义字段

        **请求示例**::

            data = {
                'roomId':'GENERAL',
                'customFields':{"organization": "tra-la-la"},
            }
            r = put(url,data=data)

        **请求结果**:
         - success:boolean
         - channel:json
         - developerWarning:string

        """ 
        roomId = request.form['roomId']
        # roomName = request.form['roomName']
        customFields = request.form['customFields']
        
        try:
            r = rocket.channels_set_custom_fields(rid=roomId,customFields=customFields)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'设置失败。'},401

        return {
            'success':True,
            'channel':r.json()['channel'],
            'developerWarning':r.json()['developerWarning'],
        },200      


class SetAnnouncement(Resource):
    """设置频道公告

    https://rocket.chat/docs/developer-guides/rest-api/channels/setannouncement/    

    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/setannouncement
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - GENERAL
              - 必须
              - 频道id
            * - announcement
              - Test out everything.
              - 必须
              - 设置的频道公告。

        **请求示例**::

            data = {
                'roomId':'GENERAL',
                'announcement':'Test out everything.',
            }
            r = put(url,data=data)

        **请求结果**:
         - success:boolean
         - announcement:string

        """ 
        roomId = request.form['roomId']
        announcement = request.form['announcement']
        
        try:
            r = rocket.channels_set_announcement(room_id=roomId,announcement=announcement)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'设置失败。'},401

        return {
            'success':True,
            'announcement':r.json()['announcement'],
        } ,200      
 

class SetDefault(Resource):
    """设置默认频道,插件无该接口

    https://rocket.chat/docs/developer-guides/rest-api/channels/setdefault/    

    """
    pass 


class SetDescription(Resource):
    """设置频道简介

    https://rocket.chat/docs/developer-guides/rest-api/channels/setdescription/    

    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/setdescription
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道id
            * - description
              - Test out everything.
              - 必须
              - 设置的频道描述。

        **请求示例**::

            data = {
                'roomId':'GENERAL',
                'description':'Test out everything.',
            }
            r = put(url,data=data)

        **请求结果**:
         - success:boolean
         - description:string

        """ 
        roomId = request.form['roomId']
        description = request.form['description']
        
        try:
            r = rocket.channels_set_description(room_id=roomId,description=description)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'设置失败。'},401

        return {
            'success':True,
            'description':r.json()['description'],
        } ,200       


class SetJoinCode(Resource):
    """设置频道需要连接的代码

    https://rocket.chat/docs/developer-guides/rest-api/channels/setjoincode/    

    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/setjoincode
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - GENERAL
              - 必须
              - 频道id
            * - joinCode
              - my-join-code
              - 必须
              - 设置频道需要连接的代码。

        **请求示例**::

            data = {
                'roomId':'GENERAL',
                'joinCode':'my-join-code.',
            }
            r = put(url,data=data)

        **请求结果**:
         - success:boolean
         - channel:json

        """ 
        roomId = request.form['roomId']
        joinCode = request.form['joinCode']
        
        try:
            r = rocket.channels_set_join_code(room_id=roomId,join_code=joinCode)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'设置失败。'},401

        return {
            'success':True,
            'channel':r.json()['channel'],
        } ,200       


class SetPurpose(Resource):
    """设置频道说明,插件无该接口

    https://rocket.chat/docs/developer-guides/rest-api/channels/setpurpose/    

    """
    pass 


class SetReadOnly(Resource):
    """设置频道只读

    https://rocket.chat/docs/developer-guides/rest-api/channels/setreadonly/    

    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/setreadonly
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道id
            * - readOnly
              - 1
              - 必须,0或者1
              - 频道是否只读

        **请求示例**::

            r = put(url,data={'roomId':'ByehQjC44FwMeiLbX','readOnly':1})

        **请求结果**:
         - success:boolean
         - channel:json

        """ 
        roomId = request.form['roomId']
        readOnly = request.form['readOnly']

        if readOnly:
            readOnly = True
        else:
            readOnly = False 

        try:
            r = rocket.channels_set_read_only(room_id=roomId,read_only=readOnly)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'设置失败。'},401

        return {
            'channel':r.json()['channel'],
            'success':True,
        },200     


class SetTopic(Resource):
    """设置频道主题

    https://rocket.chat/docs/developer-guides/rest-api/channels/settopic/    

    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/settopic
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道id
            * - topic
              - Discuss all of the testing
              - 必须
              - 频道的主题

        **请求示例**::

            r = put(url,data={'roomId':'ByehQjC44FwMeiLbX','topic':'Discuss all of the testing'})

        **请求结果**:
         - success:boolean
         - topic:string

        """ 
        roomId = request.form['roomId']
        topic = request.form['topic']

        try:
            r = rocket.channels_set_topic(room_id=roomId,topic=topic)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'设置失败。'},401

        return {
            'topic':r.json()['topic'],
            'success':True,
        },200     
 

class SetType(Resource):
    """设置频道类型

    https://rocket.chat/docs/developer-guides/rest-api/channels/settype/    

    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/settype
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道id
            * - type
              - r or p
              - 必须
              - 频道类型必须为p 或者 r

        **请求示例**::

            r = put(url,data={'roomId':'ByehQjC44FwMeiLbX','type':'r'})

        **请求结果**:
         - success:boolean
         - channel:json

        """ 
        roomId = request.form['roomId']
        a_type = request.form['type']
        if a_type!= 'p' or a_type != 'r':
            return {'success':False,'message':'设置频道类型错误,只能有p或者r两种类型。'},401

        try:
            r = rocket.channels_set_type(room_id=roomId,a_type=a_type)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'设置失败。'},401

        return {
            'channel':r.json()['channel'],
            'success':True,
        },200     
  

class Unarchive(Resource):
    """取消归档

    https://rocket.chat/docs/developer-guides/rest-api/channels/unarchive/

    """
    def get(self): 
        """

        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/unarchive
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道id

        **请求示例**::

            r = get(url,{'roomId':roomId})

        **请求结果**:
         - success:boolean

        """
        roomId = request.args.get('roomId','')
        
        try:
            r = rocket.channels_unarchive(room_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'取消存档失败。'},401

        r = r.json()
        return {
            'success': True,
        },200   



api.add_resource(ChannelList, f'/api/{v1}/channels/channels_list') 
api.add_resource(AddAll, f'/api/{v1}/channels/add_all') 
api.add_resource(Create, f'/api/{v1}/channels/create') 
api.add_resource(Archive, f'/api/{v1}/channels/archive') 
api.add_resource(Close, f'/api/{v1}/channels/close') 
api.add_resource(ChannelsDelete, f'/api/{v1}/channels/channels_delte') 
api.add_resource(Files, f'/api/{v1}/channels/files') 
api.add_resource(GetAllUserMentionsByChannel, f'/api/{v1}/channels/get_all_user_mentions_by_channel') 
api.add_resource(GetIntegrations, f'/api/{v1}/channels/get_integrations') 
api.add_resource(History, f'/api/{v1}/channels/history') 
api.add_resource(ChannelsInfo, f'/api/{v1}/channels/channels_info') 
api.add_resource(Invite, f'/api/{v1}/channels/invite') 
api.add_resource(Kick, f'/api/{v1}/channels/kick') 
api.add_resource(Leave, f'/api/{v1}/channels/leave') 
api.add_resource(ListJoined, f'/api/{v1}/channels/list_joined') 
api.add_resource(Members, f'/api/{v1}/channels/members') 
api.add_resource(Open, f'/api/{v1}/channels/open') 
api.add_resource(Rename, f'/api/{v1}/channels/rename') 
api.add_resource(Roles, f'/api/{v1}/channels/roles') 
api.add_resource(SetCustomFields, f'/api/{v1}/channels/setcustomfields') 
api.add_resource(SetAnnouncement, f'/api/{v1}/channels/setannouncement') 
api.add_resource(SetDescription, f'/api/{v1}/channels/setdescription') 
api.add_resource(SetJoinCode, f'/api/{v1}/channels/setjoincode') 
api.add_resource(SetReadOnly, f'/api/{v1}/channels/setreadonly') 
api.add_resource(SetTopic, f'/api/{v1}/channels/settopic') 
api.add_resource(SetType, f'/api/{v1}/channels/settype') 
api.add_resource(Unarchive, f'/api/{v1}/channels/unarchive') 






