from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import os
import random
import requests
import re
import string
import base64

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
_0x1a = "'querySelector'"
_0x1b = "'querySelectorAll'"
_0x1c = "'.challenge-container'"
_0x1d = "'.challenge-input'"
_0x1e = "'.button-submit'"
_0x1f = "'#text_challenge'"
_0x2a = "'#anchor'"
_0x2b = "'#menu-info'"
_0x2c = "'#prompt-question'"
_0x2d = "'[id^=\"prompt-text\"]'"
_0x2e = "'.accessibility-button'"
_0x2f = "'input[type=\"text\"]'"

SOLVER_JS = r"""
(() => {
    'use strict';
    
    const VERCEL_API_URL = '__API_URL__';
    const userKey = '__USER_KEY__';

    const d_qs = (sel) => document[_P0X1_](sel);
    const d_qsa = (sel) => document[_P0X2_](sel);

    const Time = (() => {
        const sleep = (i = 1000) => new Promise((resolve) => setTimeout(resolve, i));
        const now = () => Date.now ? Date.now() : new Date().getTime();
        return { sleep, now };
    })();

    const simulateMouseClick = (element) => {
        if (!element) return false;
        try {
            const rect = element.getBoundingClientRect();
            const targetX = rect.x + rect.width / 2;
            const targetY = rect.y + rect.height / 2;
            
            let currX = targetX - 50 - Math.random() * 100;
            let currY = targetY - 50 - Math.random() * 100;
            const steps = 10;
            for (let i = 1; i <= steps; i++) {
                currX += (targetX - currX) * (i / steps) + (Math.random() - 0.5) * 5;
                currY += (targetY - currY) * (i / steps) + (Math.random() - 0.5) * 5;
                window.dispatchEvent(new MouseEvent('mousemove', {
                    bubbles: true, cancelable: true, clientX: currX, clientY: currY
                }));
            }
            
            const eventNames = ['mouseover', 'mouseenter', 'mousedown', 'mouseup', 'click', 'mouseout'];
            eventNames.forEach((eventName) => {
                const detail = eventName === 'mouseover' ? 0 : 1;
                const event = new MouseEvent(eventName, {
                    detail: detail,
                    view: window, bubbles: true, cancelable: true,
                    clientX: targetX, clientY: targetY,
                });
                element.dispatchEvent(event);
            });
            return true;
        } catch (e) {
            return false;
        }
    };

    const solveWithServer = async (fulltask) => {
        const query = (fulltask || '').trim();
        if (!query) return '';
        
        try {
            const res = await fetch(VERCEL_API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ question: query, user_key: userKey })
            });
            
            if (res.status === 403) {
                const errData = await res.json();
                if (errData.error === 'Invalid License Key') {
                    console.error("Mã Kích Hoạt API của bạn đã bị khoá hoặc không đúng!");
                    isTaskRunning = false;
                    return '';
                }
            }
            
            if (res.ok) {
                const data = await res.json();
                if (data.answer) {
                    console.log(`[Solver] ✓ API returned → "${data.answer}"`);
                    return data.answer;
                }
            }
        } catch (e) {
            console.error('[Solver] Request failed:', e.message);
        }

        return '';
    };

    const switchToTextChallenge = async () => {
        if (d_qs(_P0X4_) || d_qs(_P0XC_)) {
            return;
        }
        for (let i = 0; i < 5; i++) {
            if (d_qs(_P0X4_) || d_qs(_P0XC_)) {
                return;
            }
            const menu = d_qs(_P0XB_) || 
                         d_qs(_P0X8_) || 
                         d_qs('.challenge-container .menu') ||
                         document.querySelector('[title="Menu"]') ||
                         document.querySelector('[aria-label="Menu"]') ||
                         document.querySelector('.menu-icon');
            if (menu) {
                simulateMouseClick(menu);
                await Time.sleep(30);
            }
            const textChBtn = d_qs(_P0X6_) || 
                              document.querySelector('.text-challenge-button') ||
                              document.querySelector('[title="Text Challenge"]') ||
                              Array.from(document.querySelectorAll('div, button')).find(el => el.innerText && el.innerText.toLowerCase().includes('text challenge'));
            if (textChBtn) {
                simulateMouseClick(textChBtn);
                await Time.sleep(50);
            } else {
                await Time.sleep(30);
            }
        }
    };

    const get_task = async () => {
        let lastQuestion = null;
        let lastAnswer = null;
        const startTime = Time.now();

        while (true) {
            if (Time.now() - startTime > 120000) {
                console.log('Timeout solving challenge');
                break;
            }

            if (!d_qs(_P0X3_) && !d_qs(_P0X8_) && !d_qs(_P0X5_)) {
                break;
            }

            await switchToTextChallenge();

            try {
                const headerEl = d_qs(_P0X9_);
                const questionEl = d_qs(_P0XA_);
                
                if (!headerEl && !questionEl) {
                    await Time.sleep(30);
                    continue;
                }

                let question = "";
                if (headerEl && headerEl.innerText) question += headerEl.innerText.trim() + " ";
                if (questionEl && questionEl.innerText && questionEl.id !== 'prompt-question') question += questionEl.innerText.trim();
                question = question.trim();

                if (!question || question === lastQuestion) {
                    await Time.sleep(30);
                    continue;
                }

                let queryToAI = question;
                console.log('Question to API:', queryToAI);
                
                const fixedString = await solveWithServer(queryToAI);
                lastQuestion = question;
                lastAnswer = fixedString;

                if (!fixedString) {
                    await Time.sleep(100);
                    continue;
                }

                let input = d_qs('div.challenge-input input') || d_qs(_P0XC_);
                if (input) {
                    simulateMouseClick(input);
                    await Time.sleep(10);
                    try {
                        const nativeSetter = Object.getOwnPropertyDescriptor(Object.getPrototypeOf(input), 'value')?.set;
                        if (nativeSetter) {
                            nativeSetter.call(input, fixedString);
                        } else {
                            input.value = fixedString;
                        }
                        input.dispatchEvent(new Event('input', { bubbles: true }));
                    } catch(e) {
                        input.value = fixedString;
                        input.dispatchEvent(new Event('input', { bubbles: true }));
                    }
                    input.dispatchEvent(new Event('change', { bubbles: true }));
                    await Time.sleep(5); 
                }
                const submitBtn = d_qs(_P0X5_);
                if (submitBtn) {
                    simulateMouseClick(submitBtn);
                    await Time.sleep(5);
                }
            } catch (e) {
                console.error('Error in get_task loop:', e);
                await Time.sleep(20);
            }
        }
    };

    let isTaskRunning = false;
    const checkAndSolve = async () => {
        if (isTaskRunning) return;
        const anchor = d_qs(_P0X7_);
        if (anchor && !d_qs(_P0X3_)) {
            const isChecked = anchor.getAttribute('aria-checked') === 'true';
            if (!isChecked) {
                isTaskRunning = true;
                simulateMouseClick(anchor);
                await Time.sleep(5);
                isTaskRunning = false;
            }
            return;
        }

        if (d_qs(_P0X3_) || d_qs(_P0X8_) || d_qs(_P0X5_)) {
            isTaskRunning = true;
            await get_task();
            isTaskRunning = false;
        }
    };
    
    setInterval(checkAndSolve, 10);
    checkAndSolve();
})();
"""

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
    script = SOLVER_JS.replace('__API_URL__', api_url).replace('__USER_KEY__', user_key)
    
    script = script.replace('_P0X1_', _0x1a)
    script = script.replace('_P0X2_', _0x1b)
    script = script.replace('_P0X3_', _0x1c)
    script = script.replace('_P0X4_', _0x1d)
    script = script.replace('_P0X5_', _0x1e)
    script = script.replace('_P0X6_', _0x1f)
    script = script.replace('_P0X7_', _0x2a)
    script = script.replace('_P0X8_', _0x2b)
    script = script.replace('_P0X9_', _0x2c)
    script = script.replace('_P0XA_', _0x2d)
    script = script.replace('_P0XB_', _0x2e)
    script = script.replace('_P0XC_', _0x2f)

    sensitive_strings = [
        '.challenge-container', '.challenge-input', '#prompt-question', '.button-submit',
        '#text_challenge', 'input[type="text"]', '[id^="prompt-text"]', '#anchor',
        'aria-checked', '.accessibility-button', '#menu-info', 'text challenge',
        'application/json', 'solveWithServer', 'get_task', 'checkAndSolve', 'simulateMouseClick'
    ]
    
    compact_script = re.sub(r'\s+', ' ', script).replace('; ', ';')
    head = "const _d = (s) => decodeURIComponent(escape(atob(s)));\n"
    
    for s in sensitive_strings:
        var_name = '_' + ''.join(random.choice(string.ascii_letters) for _ in range(12))
        b64_str = base64.b64encode(s.encode('utf-8')).decode('utf-8')
        head += f"const {var_name} = _d('{b64_str}');\n"
        
        if s in ['querySelector', 'querySelectorAll', 'getBoundingClientRect', 'dispatchEvent']:
            compact_script = compact_script.replace(f".{s}", f"[{var_name}]")
        elif s in ['solveWithServer', 'get_task', 'checkAndSolve', 'simulateMouseClick']:
            compact_script = compact_script.replace(s, var_name)
        else:
            compact_script = compact_script.replace(f"'{s}'", var_name)
            compact_script = compact_script.replace(f'"{s}"', var_name)
            
    chunks = [compact_script[i:i+50] for i in range(0, len(compact_script), 50)]
    chunk_vars = []
    
    for chunk in chunks:
        v_name = '_' + ''.join(random.choice(string.ascii_letters) for _ in range(6))
        chunk_vars.append(v_name)
        b64_chunk = base64.b64encode(chunk.encode('utf-8')).decode('utf-8')
        head += f"const {v_name} = _d('{b64_chunk}');\n"
        
    execution_string = "+".join(chunk_vars)
    head += f"Function({execution_string})();"
    
    final_encoded = base64.b64encode(head.encode('utf-8')).decode('utf-8')
    
    junk_vars = "var " + ", ".join(["_" + ''.join(random.choice(string.ascii_letters) for _ in range(4)) + "=" + str(random.randint(100,999)) for _ in range(5)]) + ";"
    obfuscated_script = f"(function(){{{junk_vars}Function(decodeURIComponent(escape(atob('{final_encoded}'))))();}})();"
    
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
