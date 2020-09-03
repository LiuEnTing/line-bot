from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessag, StickerSendMessage#多加圖片功能記得import
)

app = Flask(__name__)

line_bot_api = LineBotApi('ajbEfdZHugCOm0+rc3RG+STFGWjh6XzNHtTdfRW0YaLxqiQOX4cReUbF52e9yPswfNNLZdRwOtbIJciRdv8rYvkE+TQKrkzaUwgvnXgwmWasnBfROkd2lVSyi8T5ifRd27mkAIurmFJLgggbMaHBCAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('dd81b334b44543566c22f968005389c3')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text #使用者傳送訊息
        r = '挖跨謀啦!?'

        if '貼圖' in msg:
            sticker_message = StickerSendMessage(
                package_id = '2',
                sticker_id = '23'
                )
            line_bot_api.reply_message(
            event.reply_token,
            sticker_message)

            return
            
        if msg in ['hi', 'Hi']:
            r = '哩賀阿!'
        elif msg == '中午了':
            r = '假霸咩?'
        elif msg == '下午了':
            r = '該瘦了不要吃下午茶!'
        elif '訂位' in msg:
            r = '你是想訂位? 我長得像google?'
        elif '女朋友' in msg:
            r = '醒醒吧!你只有右手'
        elif ['大哥', '蔡秉俊'] in msg
            r = '標價錢的都不算貴~'

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text= r ))


if __name__ == "__main__":
    app.run()