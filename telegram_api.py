import requests
from datetime import datetime

BOT_TOKEN = '7429740172:AAEUV6A-YmDSzmL0b_0tnCCQ6SbJBEFDXbg'
ADMIN_BOT_TOKEN = '7547894309:AAH3zIzu5YfRDzcYBiFvzWAfW8FUTPum3g4'
ADMIN_CHAT_ID = '7929115529'

def send_reward_to_user(telegram_id, amount):
    text = f"🎉 You earned ₹{amount:.2f} from Spin & Earn!"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': telegram_id, 'text': text})

def notify_admin(telegram_id, amount):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"🔔 Spin Notification\n👤 User: {telegram_id}\n🎁 Earned: ₹{amount:.2f}\n🕒 Time: {now}"
    url = f"https://api.telegram.org/bot{ADMIN_BOT_TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': ADMIN_CHAT_ID, 'text': message})
