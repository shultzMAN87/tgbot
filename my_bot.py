import requests
import time
import os
# from dotenv import load_dotenv

# load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}/"

def get_updates(offset=None):
    url = URL + "getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()

def send_message(chat_id, text):
    url = URL + "sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.post(url, params=params)
    return response.json()

def main():
    print("Эхо-бот запущен...")
    last_update_id = None
    
    while True:
        updates = get_updates(last_update_id)
        
        if "result" in updates:
            for update in updates["result"]:
                last_update_id = update["update_id"] + 1
                
                if "message" in update and "text" in update["message"]:
                    chat_id = update["message"]["chat"]["id"]
                    text = update["message"]["text"]
                    
                    print(f"Получено сообщение: {text}")
                    response = send_message(chat_id, f"Эхо: {text}")
                    print(f"Ответ отправлен: {response}")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
       