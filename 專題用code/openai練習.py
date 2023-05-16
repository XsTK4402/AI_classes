import openai
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage   # 載入 TextSendMessage 模組
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi('你的 Channel access token')
        handler = WebhookHandler('你的 LINE Channel secret')
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']         # 取得 reply token
        msg = json_data['events'][0]['message']['text']   # 取得使用者發送的訊息
        text_message = TextSendMessage(text=msg)          # 設定回傳同樣的訊息
        line_bot_api.reply_message(tk,text_message)       # 回傳訊息
    except:
        print('error')
    return 'OK'

if __name__ == "__main__":
    app.run()






#庭豪本身的API_KEY
openai.api_key = "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"

#用戶首次輸入訊息
user_insert = input("")

while True:
    #訊息若為exit則停止運作
    if user_insert == "exit":
        break
    
    elif user_insert[0:7] == "/image ":
        user_insert = user_insert.replace("/image ","")
        
        image_resp = openai.Image.create(
            prompt = user_insert, 
            n=1, 
            size="512x512"
            )
        
        print(image_resp["data"][0]["url"])
        
        user_insert = input("你要輸入的訊息：")    
    
    else:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", 
                    "content": user_insert}]
            )
        
        gpt_reply = completion.choices[0].message.content
        print(gpt_reply)
        
        user_insert = input("你要輸入的訊息：")
        

