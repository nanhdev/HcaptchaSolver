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
    def r_name(length=10):
        return ''.join(random.choices(string.ascii_letters, k=length))
        
    def js_str(s):
        chars = [str(ord(c)) for c in s]
        return f"String.fromCharCode({','.join(chars)})"
        
    v = {k: r_name() for k in [
        'qS', 'qSA', 'Time', 'sleep', 'now', 'simulateMouseClick', 
        'solveWithServer', 'switchToTextChallenge', 'getTask', 
        'isTaskRunning', 'checkAndSolve', 'rect', 'targetX', 'targetY', 
        'currX', 'currY', 'steps', 'eventNames', 'eventName', 'detail', 
        'evt', 'fulltask', 'query', 'res', 'errData', 'data', 'menu', 
        'textChBtn', 'lastQuestion', 'lastAnswer', 'startTime', 'headerEl', 
        'questionEl', 'fixedString', 'inp', 'nativeSetter', 'submitBtn', 
        'anchor', 'isChecked', 'apiUrl', 'uKey', 'i', 'el'
    ]}

    script = f"""
(() => {{
    'use strict';
    const {v['apiUrl']} = '{api_url}';
    const {v['uKey']} = '{user_key}';

    const {v['Time']} = (() => {{
        const {v['sleep']} = ({v['i']} = 1000) => new Promise((resolve) => setTimeout(resolve, {v['i']}));
        const {v['now']} = () => Date.now ? Date.now() : new Date().getTime();
        return {{ '{v['sleep']}': {v['sleep']}, '{v['now']}': {v['now']} }};
    }})();
    
    const {v['qS']} = document.querySelector.bind(document);
    const {v['qSA']} = document.querySelectorAll.bind(document);

    const {v['simulateMouseClick']} = ({v['el']}) => {{
        if (!{v['el']}) return false;
        try {{
            const {v['rect']} = {v['el']}.getBoundingClientRect();
            const {v['targetX']} = {v['rect']}.x + {v['rect']}.width / 2;
            const {v['targetY']} = {v['rect']}.y + {v['rect']}.height / 2;
            
            let {v['currX']} = {v['targetX']} - 50 - Math.random() * 100;
            let {v['currY']} = {v['targetY']} - 50 - Math.random() * 100;
            const {v['steps']} = 10;
            for (let {v['i']} = 1; {v['i']} <= {v['steps']}; {v['i']}++) {{
                {v['currX']} += ({v['targetX']} - {v['currX']}) * ({v['i']} / {v['steps']}) + (Math.random() - 0.5) * 5;
                {v['currY']} += ({v['targetY']} - {v['currY']}) * ({v['i']} / {v['steps']}) + (Math.random() - 0.5) * 5;
                window.dispatchEvent(new MouseEvent({js_str('mousemove')}, {{
                    bubbles: true, cancelable: true, clientX: {v['currX']}, clientY: {v['currY']}
                }}));
            }}
            
            const {v['eventNames']} = [{js_str('mouseover')}, {js_str('mouseenter')}, {js_str('mousedown')}, {js_str('mouseup')}, {js_str('click')}, {js_str('mouseout')}];
            {v['eventNames']}.forEach(({v['eventName']}) => {{
                const {v['detail']} = {v['eventName']} === {js_str('mouseover')} ? 0 : 1;
                const {v['evt']} = new MouseEvent({v['eventName']}, {{
                    detail: {v['detail']},
                    view: window, bubbles: true, cancelable: true,
                    clientX: {v['targetX']}, clientY: {v['targetY']},
                }});
                {v['el']}.dispatchEvent({v['evt']});
            }});
            return true;
        }} catch (e) {{
            return false;
        }}
    }};

    const {v['solveWithServer']} = async ({v['fulltask']}) => {{
        const {v['query']} = ({v['fulltask']} || '').trim();
        if (!{v['query']}) return '';
        try {{
            const {v['res']} = await fetch({v['apiUrl']}, {{
                method: {js_str('POST')},
                headers: {{ [{js_str('Content-Type')}]: {js_str('application/json')} }},
                body: JSON.stringify({{ question: {v['query']}, user_key: {v['uKey']} }})
            }});
            if ({v['res']}.status === 403) {{
                {v['isTaskRunning']} = false;
                return '';
            }}
            if ({v['res']}.ok) {{
                const {v['data']} = await {v['res']}.json();
                if ({v['data']}.answer) return {v['data']}.answer;
            }}
        }} catch (e) {{}}
        return '';
    }};

    const {v['switchToTextChallenge']} = async () => {{
        if ({v['qS']}({js_str('.challenge-input')}) || {v['qS']}({js_str('input[type="text"]')})) return;
        for (let {v['i']} = 0; {v['i']} < 5; {v['i']}++) {{
            if ({v['qS']}({js_str('.challenge-input')}) || {v['qS']}({js_str('input[type="text"]')})) return;
            const {v['menu']} = {v['qS']}({js_str('.accessibility-button')}) || {v['qS']}({js_str('#menu-info')}) || {v['qS']}({js_str('.challenge-container .menu')}) || {v['qS']}({js_str('[title="Menu"]')}) || {v['qS']}({js_str('[aria-label="Menu"]')}) || {v['qS']}({js_str('.menu-icon')});
            if ({v['menu']}) {{
                {v['simulateMouseClick']}({v['menu']});
                await {v['Time']}['{v['sleep']}'](30);
            }}
            const {v['textChBtn']} = {v['qS']}({js_str('#text_challenge')}) || {v['qS']}({js_str('.text-challenge-button')}) || {v['qS']}({js_str('[title="Text Challenge"]')}) || Array.from({v['qSA']}({js_str('div, button')})).find(e => e.innerText && e.innerText.toLowerCase().includes({js_str('text challenge')}));
            if ({v['textChBtn']}) {{
                {v['simulateMouseClick']}({v['textChBtn']});
                await {v['Time']}['{v['sleep']}'](50);
            }} else {{
                await {v['Time']}['{v['sleep']}'](30);
            }}
        }}
    }};

    const {v['getTask']} = async () => {{
        let {v['lastQuestion']} = null;
        let {v['lastAnswer']} = null;
        const {v['startTime']} = {v['Time']}['{v['now']}']();
        while (true) {{
            if ({v['Time']}['{v['now']}']() - {v['startTime']} > 120000) break;
            if (!{v['qS']}({js_str('.challenge-container')}) && !{v['qS']}({js_str('#menu-info')}) && !{v['qS']}({js_str('.button-submit')})) break;
            
            await {v['switchToTextChallenge']}();
            try {{
                const {v['headerEl']} = {v['qS']}({js_str('#prompt-question')});
                const {v['questionEl']} = {v['qS']}({js_str('[id^="prompt-text"]')});
                if (!{v['headerEl']} && !{v['questionEl']}) {{
                    await {v['Time']}['{v['sleep']}'](30);
                    continue;
                }}
                let {v['query']} = "";
                if ({v['headerEl']} && {v['headerEl']}.innerText) {v['query']} += {v['headerEl']}.innerText.trim() + " ";
                if ({v['questionEl']} && {v['questionEl']}.innerText && {v['questionEl']}.id !== {js_str('prompt-question')}) {v['query']} += {v['questionEl']}.innerText.trim();
                {v['query']} = {v['query']}.trim();
                if (!{v['query']} || {v['query']} === {v['lastQuestion']}) {{
                    await {v['Time']}['{v['sleep']}'](30);
                    continue;
                }}
                
                const {v['fixedString']} = await {v['solveWithServer']}({v['query']});
                {v['lastQuestion']} = {v['query']};
                {v['lastAnswer']} = {v['fixedString']};
                if (!{v['fixedString']}) {{
                    await {v['Time']}['{v['sleep']}'](100);
                    continue;
                }}
                
                let {v['inp']} = {v['qS']}({js_str('div.challenge-input input')}) || {v['qS']}({js_str('input[type="text"]')});
                if ({v['inp']}) {{
                    {v['simulateMouseClick']}({v['inp']});
                    await {v['Time']}['{v['sleep']}'](10);
                    try {{
                        const {v['nativeSetter']} = Object.getOwnPropertyDescriptor(Object.getPrototypeOf({v['inp']}), {js_str('value')})?.set;
                        if ({v['nativeSetter']}) {{ {v['nativeSetter']}.call({v['inp']}, {v['fixedString']}); }} else {{ {v['inp']}.value = {v['fixedString']}; }}
                        {v['inp']}.dispatchEvent(new Event({js_str('input')}, {{ bubbles: true }}));
                    }} catch(e) {{
                        {v['inp']}.value = {v['fixedString']};
                        {v['inp']}.dispatchEvent(new Event({js_str('input')}, {{ bubbles: true }}));
                    }}
                    {v['inp']}.dispatchEvent(new Event({js_str('change')}, {{ bubbles: true }}));
                    await {v['Time']}['{v['sleep']}'](5); 
                }}
                const {v['submitBtn']} = {v['qS']}({js_str('.button-submit')});
                if ({v['submitBtn']}) {{
                    {v['simulateMouseClick']}({v['submitBtn']});
                    await {v['Time']}['{v['sleep']}'](5);
                }}
            }} catch (e) {{
                await {v['Time']}['{v['sleep']}'](20);
            }}
        }}
    }};

    let {v['isTaskRunning']} = false;
    const {v['checkAndSolve']} = async () => {{
        if ({v['isTaskRunning']}) return;
        const {v['anchor']} = {v['qS']}({js_str('#anchor')});
        if ({v['anchor']} && !{v['qS']}({js_str('.challenge-container')})) {{
            const {v['isChecked']} = {v['anchor']}.getAttribute({js_str('aria-checked')}) === {js_str('true')};
            if (!{v['isChecked']}) {{
                {v['isTaskRunning']} = true;
                {v['simulateMouseClick']}({v['anchor']});
                await {v['Time']}['{v['sleep']}'](5);
                {v['isTaskRunning']} = false;
            }}
            return;
        }}
        if ({v['qS']}({js_str('.challenge-container')}) || {v['qS']}({js_str('#menu-info')}) || {v['qS']}({js_str('.button-submit')})) {{
            {v['isTaskRunning']} = true;
            await {v['getTask']}();
            {v['isTaskRunning']} = false;
        }}
    }};
    
    setInterval({v['checkAndSolve']}, 10);
    {v['checkAndSolve']}();
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
