from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import os
import random
import requests
import re

app = Flask(__name__)
CORS(app)

fake_404 = """
<!DOCTYPE html>
<html>
<head><title>404 Not Found</title></head>
<body>
<h1>404 - Page Not Found</h1>
<p>The requested URL was not found on this server.</p>
</body>
</html>
"""

def is_safe_request(req):
    user_agent = req.headers.get('User-Agent', '').lower()
    for bot in ['curl', 'postman', 'wget', 'python', 'urllib', 'httpclient', 'insomnia', 'node-fetch', 'axios', 'go-http-client', 'java', 'ruby', 'perl', 'php']:
        if bot in user_agent:
            return False
    if not user_agent or len(user_agent) < 40 or 'mozilla' not in user_agent:
        return False
    return True

def load_user_keys():
    keys = []
    possible_paths = ['user_keys.txt', '../user_keys.txt']
    for p in possible_paths:
        if os.path.exists(p):
            with open(p, 'r') as f:
                for line in f:
                    k = line.strip()
                    if k:
                        keys.append(k)
            if keys:
                break
                
    env_keys = os.getenv('USER_KEYS', '')
    if env_keys:
        for k in env_keys.split(','):
            k = k.strip()
            if k and k not in keys:
                keys.append(k)
                
    return keys

def load_keys():
    keys = []
    possible_paths = ['groq.txt', '../groq.txt']
    for p in possible_paths:
        if os.path.exists(p):
            with open(p, 'r') as f:
                for line in f:
                    k = line.strip()
                    if k:
                        keys.append(k)
            if keys:
                break
    env_keys = os.getenv('GROQ_KEYS', '')
    if env_keys:
        for k in env_keys.split(','):
            k = k.strip()
            if k and k not in keys:
                keys.append(k)
    return keys

# Code SOLVER_JS được chuyển vào trong hàm để sinh ngẫu nhiên mỗi lần gọi

@app.route('/nanhne', methods=['GET'])
def flask_serve_solver_js():
    if not is_safe_request(request):
        return Response(fake_404, status=404, mimetype='text/html')
    sec_fetch_dest = request.headers.get('Sec-Fetch-Dest', '')
    if sec_fetch_dest == 'document':
        return Response(fake_404, status=404, mimetype='text/html')
    user_key = request.args.get('user_key', '').strip()
    valid_user_keys = load_user_keys()
    if not user_key or (valid_user_keys and user_key not in valid_user_keys):
        return Response(fake_404, status=404, mimetype='text/html')

    api_url = request.host_url.rstrip('/') + '/api/solve'
    
    import string
    def r_name(length=6):
        return ''.join(random.choices(string.ascii_letters, k=length))
        
    _qS_ = r_name(8)
    _qSA_ = r_name(8)
    _Time_ = r_name(7)
    _sleep_ = r_name(7)
    _now_ = r_name(7)
    _simulateMouseClick_ = r_name(10)
    _solveWithServer_ = r_name(10)
    _switchToTextChallenge_ = r_name(10)
    _get_task_ = r_name(9)
    _isTaskRunning_ = r_name(9)
    _checkAndSolve_ = r_name(9)

    script = f"""
(() => {{
    'use strict';
    const VERCEL_API_URL = '{api_url}';
    const userKey = '{user_key}';

    const {_Time_} = (() => {{
        const {_sleep_} = (i = 1000) => new Promise((resolve) => setTimeout(resolve, i));
        const {_now_} = () => Date.now ? Date.now() : new Date().getTime();
        return {{ {_sleep_}, {_now_} }};
    }})();
    
    const {_qS_} = document.querySelector.bind(document);
    const {_qSA_} = document.querySelectorAll.bind(document);

    const {_simulateMouseClick_} = (element) => {{
        if (!element) return false;
        try {{
            const rect = element.getBoundingClientRect();
            const targetX = rect.x + rect.width / 2;
            const targetY = rect.y + rect.height / 2;
            
            let currX = targetX - 50 - Math.random() * 100;
            let currY = targetY - 50 - Math.random() * 100;
            const steps = 10;
            for (let i = 1; i <= steps; i++) {{
                currX += (targetX - currX) * (i / steps) + (Math.random() - 0.5) * 5;
                currY += (targetY - currY) * (i / steps) + (Math.random() - 0.5) * 5;
                window.dispatchEvent(new MouseEvent('mousemove', {{
                    bubbles: true, cancelable: true, clientX: currX, clientY: currY
                }}));
            }}
            
            const eventNames = ['mouseover', 'mouseenter', 'mousedown', 'mouseup', 'click', 'mouseout'];
            eventNames.forEach((eventName) => {{
                const detail = eventName === 'mouseover' ? 0 : 1;
                const event = new MouseEvent(eventName, {{
                    detail: detail,
                    view: window, bubbles: true, cancelable: true,
                    clientX: targetX, clientY: targetY,
                }});
                element.dispatchEvent(event);
            }});
            return true;
        }} catch (e) {{
            return false;
        }}
    }};

    const {_solveWithServer_} = async (fulltask) => {{
        const query = (fulltask || '').trim();
        if (!query) return '';
        try {{
            const res = await fetch(VERCEL_API_URL, {{
                method: 'POST',
                headers: {{'Content-Type': 'application/json'}},
                body: JSON.stringify({{ question: query, user_key: userKey }})
            }});
            if (res.status === 403) {{
                const errData = await res.json();
                if (errData.error === 'Invalid License Key') {{
                    console.error("Loi Key");
                    {_isTaskRunning_} = false;
                    return '';
                }}
            }}
            if (res.ok) {{
                const data = await res.json();
                if (data.answer) return data.answer;
            }}
        }} catch (e) {{}}
        return '';
    }};

    const {_switchToTextChallenge_} = async () => {{
        if ({_qS_}('.challenge-input') || {_qS_}('input[type="text"]')) return;
        for (let i = 0; i < 5; i++) {{
            if ({_qS_}('.challenge-input') || {_qS_}('input[type="text"]')) return;
            const menu = {_qS_}('.accessibility-button') || {_qS_}('#menu-info') || {_qS_}('.challenge-container .menu') || {_qS_}('[title="Menu"]') || {_qS_}('[aria-label="Menu"]') || {_qS_}('.menu-icon');
            if (menu) {{
                {_simulateMouseClick_}(menu);
                await {_Time_}.{_sleep_}(30);
            }}
            const textChBtn = {_qS_}('#text_challenge') || {_qS_}('.text-challenge-button') || {_qS_}('[title="Text Challenge"]') || Array.from({_qSA_}('div, button')).find(el => el.innerText && el.innerText.toLowerCase().includes('text challenge'));
            if (textChBtn) {{
                {_simulateMouseClick_}(textChBtn);
                await {_Time_}.{_sleep_}(50);
            }} else {{
                await {_Time_}.{_sleep_}(30);
            }}
        }}
    }};

    const {_get_task_} = async () => {{
        let lastQuestion = null;
        let lastAnswer = null;
        const startTime = {_Time_}.{_now_}();
        while (true) {{
            if ({_Time_}.{_now_}() - startTime > 120000) break;
            if (!{_qS_}('.challenge-container') && !{_qS_}('#menu-info') && !{_qS_}('.button-submit')) break;
            
            await {_switchToTextChallenge_}();
            try {{
                const headerEl = {_qS_}('#prompt-question');
                const questionEl = {_qS_}('[id^="prompt-text"]');
                if (!headerEl && !questionEl) {{
                    await {_Time_}.{_sleep_}(30);
                    continue;
                }}
                let question = "";
                if (headerEl && headerEl.innerText) question += headerEl.innerText.trim() + " ";
                if (questionEl && questionEl.innerText && questionEl.id !== 'prompt-question') question += questionEl.innerText.trim();
                question = question.trim();
                if (!question || question === lastQuestion) {{
                    await {_Time_}.{_sleep_}(30);
                    continue;
                }}
                
                const fixedString = await {_solveWithServer_}(question);
                lastQuestion = question;
                lastAnswer = fixedString;
                if (!fixedString) {{
                    await {_Time_}.{_sleep_}(100);
                    continue;
                }}
                
                let input = {_qS_}('div.challenge-input input') || {_qS_}('input[type="text"]');
                if (input) {{
                    {_simulateMouseClick_}(input);
                    await {_Time_}.{_sleep_}(10);
                    try {{
                        const nativeSetter = Object.getOwnPropertyDescriptor(Object.getPrototypeOf(input), 'value')?.set;
                        if (nativeSetter) {{ nativeSetter.call(input, fixedString); }} else {{ input.value = fixedString; }}
                        input.dispatchEvent(new Event('input', {{ bubbles: true }}));
                    }} catch(e) {{
                        input.value = fixedString;
                        input.dispatchEvent(new Event('input', {{ bubbles: true }}));
                    }}
                    input.dispatchEvent(new Event('change', {{ bubbles: true }}));
                    await {_Time_}.{_sleep_}(5); 
                }}
                const submitBtn = {_qS_}('.button-submit');
                if (submitBtn) {{
                    {_simulateMouseClick_}(submitBtn);
                    await {_Time_}.{_sleep_}(5);
                }}
            }} catch (e) {{
                await {_Time_}.{_sleep_}(20);
            }}
        }}
    }};

    let {_isTaskRunning_} = false;
    const {_checkAndSolve_} = async () => {{
        if ({_isTaskRunning_}) return;
        const anchor = {_qS_}('#anchor');
        if (anchor && !{_qS_}('.challenge-container')) {{
            const isChecked = anchor.getAttribute('aria-checked') === 'true';
            if (!isChecked) {{
                {_isTaskRunning_} = true;
                {_simulateMouseClick_}(anchor);
                await {_Time_}.{_sleep_}(5);
                {_isTaskRunning_} = false;
            }}
            return;
        }}
        if ({_qS_}('.challenge-container') || {_qS_}('#menu-info') || {_qS_}('.button-submit')) {{
            {_isTaskRunning_} = true;
            await {_get_task_}();
            {_isTaskRunning_} = false;
        }}
    }};
    
    setInterval({_checkAndSolve_}, 10);
    {_checkAndSolve_}();
}})();
"""
    
    import base64
    encoded = base64.b64encode(script.encode('utf-8')).decode('utf-8')
    obfuscated_script = f"Function(decodeURIComponent(escape(atob('{encoded}'))))();"
    
    return Response(obfuscated_script, mimetype='application/javascript')

@app.route('/api/solve', methods=['POST', 'OPTIONS'])
def solve_captcha():
    if request.method == 'OPTIONS':
        return '', 200
        
    if not is_safe_request(request):
        return Response(fake_404, status=404, mimetype='text/html')
        
    origin = request.headers.get('Origin', '')
    referer = request.headers.get('Referer', '')
    
    if origin and 'discord.com' not in origin and 'hcaptcha.com' not in origin:
        return Response(fake_404, status=404, mimetype='text/html')
    elif referer and 'discord.com' not in referer and 'hcaptcha.com' not in referer:
        return Response(fake_404, status=404, mimetype='text/html')
        
    data = request.json
    if not data or 'question' not in data:
        return Response(fake_404, status=404, mimetype='text/html')
        
    provided_user_key = data.get('user_key', '').strip()
    valid_user_keys = load_user_keys()
    
    if not provided_user_key or (valid_user_keys and provided_user_key not in valid_user_keys):
        return Response(fake_404, status=404, mimetype='text/html')
        
    question = data['question']
    keys = load_keys()
    
    if not keys:
        return jsonify({'error': 'No API keys available'}), 500
        
    api_key = random.choice(keys)
    is_vietnamese = any(c in question for c in 'àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴĐ')
    
    if is_vietnamese:
        system_prompt = f"Bạn là bot trả lời captcha. Trả lời BẰNG TIẾNG VIỆT, ngắn nhất có thể (1-3 từ tối đa).\nQuy tắc TUYỆT ĐỐI:\n- Chỉ trả lời từ/cụm từ, KHÔNG giải thích, KHÔNG câu đầy đủ\n- Toán học: chỉ ghi kết quả là số\n- Màu sắc, động vật, đồ vật: tên tiếng Việt\n- Không dùng dấu chấm, phẩy hay ký tự thừa\n- KHÔNG được trả lời bằng tiếng Anh\n\nCâu hỏi: {question}\nĐáp án:"
    else:
        system_prompt = f"Captcha bot. English answer only, 1-3 words max, no punctuation.\nMath: number only. Colors/animals: exact English name.\n\nQuestion: {question}\nAnswer:"
        
    models = ['llama-3.3-70b-versatile', 'llama-3.1-8b-instant']
    
    for model in models:
        try:
            resp = requests.post(
                'https://api.groq.com/openai/v1/chat/completions',
                headers={
                    'Authorization': f'Bearer {api_key}',
                    'Content-Type': 'application/json'
                },
                json={
                    'model': model,
                    'messages': [{'role': 'user', 'content': system_prompt}],
                    'temperature': 0,
                    'max_tokens': 12,
                    'stop': ['\n', '.', ',']
                },
                timeout=8
            )
            
            if resp.status_code == 200:
                resp_data = resp.json()
                answer = resp_data.get('choices', [{}])[0].get('message', {}).get('content', '')
                if answer:
                    answer = answer.strip().strip('"\'')
                    answer = re.sub(r'[.,!?;:()\[\]{}]', '', answer)
                    answer = re.sub(r'^(đáp án:|answer:|a:|ans:)\s*', '', answer, flags=re.IGNORECASE)
                    answer = answer.strip().lower()
                    if 0 < len(answer) < 50:
                        return jsonify({'answer': answer})
        except Exception as e:
            continue
            
    return jsonify({'error': 'Models failed'}), 500

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response(fake_404, status=404, mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
