from mirai import Mirai, WebSocketAdapter, FriendMessage, GroupMessage, At
import re,time
from xpinyin import Pinyin

if __name__ == '__main__':
    bot = Mirai(
        qq=1429288774, # 改成你的机器人的 QQ 号
        adapter=WebSocketAdapter(
            verify_key='yirimirai', host='localhost', port=8080
        )
    )

    @bot.on(FriendMessage)
    def on_friend_message(event: FriendMessage):
        if str(event.message_chain) == '你好':
            return bot.send(event, 'Hello, World!')
            
    @bot.on(GroupMessage)
    def on_group_message(event: GroupMessage):
        p = Pinyin()
        if At(bot.qq) in event.message_chain:
            if not re.search('.*ji.*|.*じ.*|.*jl.*|.*bei-jing.*|.*ai.*|.*🐔.*',str(p.get_pinyin(str(event.message_chain))),re.IGNORECASE):
                return bot.send(event,[At(event.sender.id),str(event.message_chain).replace('@'+str(bot.qq), '', 1)])
    
    @bot.on(GroupMessage)
    async def text_censor_event(event: GroupMessage):
        '''if str(event.message_chain) == '急了':'''
        p = Pinyin()
        if re.search('.*ji-le.*|.*じ.*|.*jl.*|.*bei-jing.*|.*🐔.*|.*qi-le.*|bie-xue-le',str(p.get_pinyin(str(event.message_chain))),re.IGNORECASE):
            '''time.sleep(5)'''
            await bot.recall(event.message_chain.message_id)
            '''return bot.send(event,[At(event.sender.id),'cnm'])'''
    
    bot.run()