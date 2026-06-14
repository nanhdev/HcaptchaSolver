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

SOLVER_JS = r"""
(() => {
    'use strict';
    
    const VERCEL_API_URL = '__API_URL__';
    
    let userKey = localStorage.getItem('nanh_license_key');
    if (!userKey) {
        userKey = prompt("Vui lòng nhập Mã Kích Hoạt API (License Key) để sử dụng HCaptcha Solver:");
        if (userKey) {
            localStorage.setItem('nanh_license_key', userKey);
        } else {
            console.error("Chưa nhập Mã Kích Hoạt!");
            return;
        }
    }

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
                    alert("Mã Kích Hoạt API của bạn đã bị khoá hoặc không đúng! Vui lòng làm mới trang và nhập lại.");
                    localStorage.removeItem('nanh_license_key');
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
        if (document.querySelector('.challenge-input') || document.querySelector('input[type="text"]')) {
            return;
        }
        for (let i = 0; i < 5; i++) {
            if (document.querySelector('.challenge-input') || document.querySelector('input[type="text"]')) {
                return;
            }
            const menu = document.querySelector('.accessibility-button') || 
                         document.querySelector('#menu-info') || 
                         document.querySelector('.challenge-container .menu') ||
                         document.querySelector('[title="Menu"]') ||
                         document.querySelector('[aria-label="Menu"]') ||
                         document.querySelector('.menu-icon');
            if (menu) {
                simulateMouseClick(menu);
                await Time.sleep(30);
            }
            const textChBtn = document.querySelector('#text_challenge') || 
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

            if (!document.querySelector('.challenge-container') && !document.querySelector('#menu-info') && !document.querySelector('.button-submit')) {
                break;
            }

            await switchToTextChallenge();

            try {
                const headerEl = document.querySelector('#prompt-question');
                const questionEl = document.querySelector('[id^="prompt-text"]');
                
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

                let input = document.querySelector('div.challenge-input input') || document.querySelector('input[type="text"]');
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
                const submitBtn = document.querySelector('.button-submit');
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
        const anchor = document.querySelector('#anchor');
        if (anchor && !document.querySelector('.challenge-container')) {
            const isChecked = anchor.getAttribute('aria-checked') === 'true';
            if (!isChecked) {
                isTaskRunning = true;
                simulateMouseClick(anchor);
                await Time.sleep(5);
                isTaskRunning = false;
            }
            return;
        }

        if (document.querySelector('.challenge-container') || document.querySelector('#menu-info') || document.querySelector('.button-submit')) {
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

    api_url = request.host_url.rstrip('/') + '/api/solve'
    script = SOLVER_JS.replace('__API_URL__', api_url)
    return Response(script, mimetype='application/javascript')

@app.route('/api/solve', methods=['POST', 'OPTIONS'])
def solve_captcha():
    if request.method == 'OPTIONS':
        return '', 200
        
    if not is_safe_request(request):
        return jsonify({'error': 'Unauthorized'}), 404
        
    origin = request.headers.get('Origin', '')
    referer = request.headers.get('Referer', '')
    
    if origin and 'discord.com' not in origin and 'hcaptcha.com' not in origin:
        return jsonify({'error': 'Unauthorized origin'}), 403
    elif referer and 'discord.com' not in referer and 'hcaptcha.com' not in referer:
        return jsonify({'error': 'Unauthorized referer'}), 403
        
    data = request.json
    if not data or 'question' not in data:
        return jsonify({'error': 'No question provided'}), 400
        
    provided_user_key = data.get('user_key', '').strip()
    valid_user_keys = load_user_keys()
    
    if not provided_user_key or (valid_user_keys and provided_user_key not in valid_user_keys):
        return jsonify({'error': 'Invalid License Key'}), 403
        
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
