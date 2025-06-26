from flask import Flask, render_template, request, redirect, session, jsonify
from spin_logic import get_random_prize
from telegram_api import send_reward_to_user, notify_admin
import json
import os
from datetime import datetime

app = Flask(name)
app.secret_key = 'your_secret_key_here'

DB_FILE = 'database.json'

def load_data():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as f:
            json.dump({}, f)
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        telegram_id = request.form['telegram_id']
        session['telegram_id'] = telegram_id
        return redirect('/spin')
    return render_template('login.html')

@app.route('/spin')
def spin():
    if 'telegram_id' not in session:
        return redirect('/login')
    return render_template('spin.html', telegram_id=session['telegram_id'])

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/spin-result', methods=['POST'])
def spin_result():
    if 'telegram_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    telegram_id = session['telegram_id']
    prize = get_random_prize()
    
    data = load_data()
    user_data = data.get(telegram_id, {'spins': [], 'total_earned': 0})
    user_data['spins'].append({'amount': prize['amount'], 'time': str(datetime.now())})
    user_data['total_earned'] += prize['amount']
    data[telegram_id] = user_data
    save_data(data)

    send_reward_to_user(telegram_id, prize['amount'])
    notify_admin(telegram_id, prize['amount'])

    return jsonify(prize)

if name == 'main':
    app.run(host='0.0.0.0', port=3000)
