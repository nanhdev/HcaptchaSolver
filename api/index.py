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
/* Obfuscated by NanhXSolver */function _0x5ed9(_0x2faead,_0x4149e7){_0x2faead=_0x2faead-0x110;const _0x50dda6=_0x50dd();let _0x5ed907=_0x50dda6[_0x2faead];return _0x5ed907;}(function(_0xddd65f,_0x5c094e){const _0x426a1a=_0x5ed9,_0x56866f=_0xddd65f();while(!![]){try{const _0x2452f6=parseInt(_0x426a1a(0x11a))/0x1*(-parseInt(_0x426a1a(0x115))/0x2)+-parseInt(_0x426a1a(0x137))/0x3+parseInt(_0x426a1a(0x111))/0x4+parseInt(_0x426a1a(0x119))/0x5*(-parseInt(_0x426a1a(0x11b))/0x6)+parseInt(_0x426a1a(0x14b))/0x7+-parseInt(_0x426a1a(0x11f))/0x8*(parseInt(_0x426a1a(0x113))/0x9)+parseInt(_0x426a1a(0x13e))/0xa;if(_0x2452f6===_0x5c094e)break;else _0x56866f['push'](_0x56866f['shift']());}catch(_0x394d79){_0x56866f['push'](_0x56866f['shift']());}}}(_0x50dd,0xf292f),((()=>{'use strict';const _0x37b073=_0x5ed9;const _0x168897=window['__NANH_API_URL__'],_0x3b7ff=window[_0x37b073(0x12e)],_0x1a8a4c=((()=>{const _0x49459b=_0x37b073,_0x447686=(_0x2a01af=0x3e8)=>new Promise(_0x29534a=>setTimeout(_0x29534a,_0x2a01af)),_0x439f2b=()=>Date[_0x49459b(0x144)]?Date['now']():new Date()[_0x49459b(0x146)]();return{'sleep':_0x447686,'now':_0x439f2b};})()),_0x16c303=_0x28e613=>{const _0x195264=_0x37b073;if(!_0x28e613)return![];try{const _0x53aa74=_0x28e613['getBoundingClientRect'](),_0x2e2c2c=_0x53aa74['x']+_0x53aa74[_0x195264(0x14d)]/0x2,_0x17e5dd=_0x53aa74['y']+_0x53aa74[_0x195264(0x112)]/0x2;let _0x347646=_0x2e2c2c-0x32-Math[_0x195264(0x14a)]()*0x64,_0x745775=_0x17e5dd-0x32-Math['random']()*0x64;const _0x4eb0db=0xa;for(let _0x20b679=0x1;_0x20b679<=_0x4eb0db;_0x20b679++){_0x347646+=(_0x2e2c2c-_0x347646)*(_0x20b679/_0x4eb0db)+(Math['random']()-0.5)*0x5,_0x745775+=(_0x17e5dd-_0x745775)*(_0x20b679/_0x4eb0db)+(Math['random']()-0.5)*0x5,window['dispatchEvent'](new MouseEvent(_0x195264(0x129),{'bubbles':!![],'cancelable':!![],'clientX':_0x347646,'clientY':_0x745775}));}const _0x51c357=[_0x195264(0x139),'mouseenter','mousedown','mouseup',_0x195264(0x145),_0x195264(0x13b)];return _0x51c357[_0x195264(0x123)](_0x75383c=>{const _0x4baccd=_0x195264,_0x492760=_0x75383c===_0x4baccd(0x139)?0x0:0x1,_0x2271d5=new MouseEvent(_0x75383c,{'detail':_0x492760,'view':window,'bubbles':!![],'cancelable':!![],'clientX':_0x2e2c2c,'clientY':_0x17e5dd});_0x28e613['dispatchEvent'](_0x2271d5);}),!![];}catch(_0x59bcc2){return![];}},_0x332580=async _0x35964c=>{const _0x455587=_0x37b073,_0x59a561=(_0x35964c||'')['trim']();if(!_0x59a561)return'';try{const _0x19b4b2=await fetch(_0x168897,{'method':'POST','headers':{'Content-Type':_0x455587(0x114)},'body':JSON[_0x455587(0x153)]({'question':_0x59a561,'user_key':_0x3b7ff})});if(_0x19b4b2[_0x455587(0x12a)]===0x193){const _0x5e14f7=await _0x19b4b2[_0x455587(0x151)]();if(_0x5e14f7[_0x455587(0x13f)]==='Invalid\x20License\x20Key')return console['error'](_0x455587(0x134)),_0x400d51=![],'';}if(_0x19b4b2['ok']){const _0x124569=await _0x19b4b2['json']();if(_0x124569[_0x455587(0x120)])return console[_0x455587(0x110)]('[Solver]\x20✓\x20API\x20returned\x20→\x20\x22'+_0x124569[_0x455587(0x120)]+'\x22'),_0x124569[_0x455587(0x120)];}}catch(_0x42905a){console[_0x455587(0x13f)]('[Solver]\x20Request\x20failed:',_0x42905a[_0x455587(0x14f)]);}return'';},_0x3e503d=async()=>{const _0x5ef2d9=_0x37b073;if(document[_0x5ef2d9(0x142)](_0x5ef2d9(0x131))||document[_0x5ef2d9(0x142)](_0x5ef2d9(0x130)))return;for(let _0x3f4b3f=0x0;_0x3f4b3f<0x5;_0x3f4b3f++){if(document['querySelector'](_0x5ef2d9(0x131))||document['querySelector']('input[type=\x22text\x22]'))return;const _0x895ccb=document[_0x5ef2d9(0x142)](_0x5ef2d9(0x138))||document[_0x5ef2d9(0x142)]('#menu-info')||document[_0x5ef2d9(0x142)](_0x5ef2d9(0x152))||document[_0x5ef2d9(0x142)](_0x5ef2d9(0x126))||document[_0x5ef2d9(0x142)](_0x5ef2d9(0x122))||document[_0x5ef2d9(0x142)]('.menu-icon');_0x895ccb&&(_0x16c303(_0x895ccb),await _0x1a8a4c[_0x5ef2d9(0x14c)](0x1e));const _0x14dc12=document['querySelector'](_0x5ef2d9(0x143))||document[_0x5ef2d9(0x142)](_0x5ef2d9(0x12f))||document[_0x5ef2d9(0x142)](_0x5ef2d9(0x14e))||Array[_0x5ef2d9(0x12c)](document[_0x5ef2d9(0x135)](_0x5ef2d9(0x140)))[_0x5ef2d9(0x11d)](_0x3c50bd=>_0x3c50bd['innerText']&&_0x3c50bd[_0x5ef2d9(0x150)]['toLowerCase']()[_0x5ef2d9(0x117)](_0x5ef2d9(0x128)));_0x14dc12?(_0x16c303(_0x14dc12),await _0x1a8a4c['sleep'](0x32)):await _0x1a8a4c[_0x5ef2d9(0x14c)](0x1e);}},_0x220ac2=async()=>{const _0x528226=_0x37b073;let _0x3178ec=null,_0x54309c=null;const _0xd05e6f=_0x1a8a4c['now']();while(!![]){if(_0x1a8a4c[_0x528226(0x144)]()-_0xd05e6f>0x1d4c0){console['log'](_0x528226(0x127));break;}if(!document[_0x528226(0x142)](_0x528226(0x141))&&!document[_0x528226(0x142)](_0x528226(0x148))&&!document['querySelector'](_0x528226(0x124)))break;await _0x3e503d();try{const _0x375d92=document[_0x528226(0x142)](_0x528226(0x13d)),_0x1e73d7=document[_0x528226(0x142)](_0x528226(0x125));if(!_0x375d92&&!_0x1e73d7){await _0x1a8a4c['sleep'](0x1e);continue;}let _0x4235be='';if(_0x375d92&&_0x375d92[_0x528226(0x150)])_0x4235be+=_0x375d92['innerText'][_0x528226(0x132)]()+'\x20';if(_0x1e73d7&&_0x1e73d7[_0x528226(0x150)]&&_0x1e73d7['id']!==_0x528226(0x133))_0x4235be+=_0x1e73d7[_0x528226(0x150)][_0x528226(0x132)]();_0x4235be=_0x4235be[_0x528226(0x132)]();if(!_0x4235be||_0x4235be===_0x3178ec){await _0x1a8a4c[_0x528226(0x14c)](0x1e);continue;}let _0x49dc1f=_0x4235be;console[_0x528226(0x110)]('Question\x20to\x20API:',_0x49dc1f);const _0x358b2b=await _0x332580(_0x49dc1f);_0x3178ec=_0x4235be,_0x54309c=_0x358b2b;if(!_0x358b2b){await _0x1a8a4c[_0x528226(0x14c)](0x64);continue;}let _0x448f70=document[_0x528226(0x142)](_0x528226(0x13c))||document[_0x528226(0x142)]('input[type=\x22text\x22]');if(_0x448f70){_0x16c303(_0x448f70),await _0x1a8a4c[_0x528226(0x14c)](0xa);try{const _0x38a9fe=Object[_0x528226(0x12b)](Object[_0x528226(0x13a)](_0x448f70),_0x528226(0x149))?.[_0x528226(0x11c)];_0x38a9fe?_0x38a9fe['call'](_0x448f70,_0x358b2b):_0x448f70[_0x528226(0x149)]=_0x358b2b,_0x448f70[_0x528226(0x12d)](new Event('input',{'bubbles':!![]}));}catch(_0x3f3a72){_0x448f70[_0x528226(0x149)]=_0x358b2b,_0x448f70[_0x528226(0x12d)](new Event(_0x528226(0x154),{'bubbles':!![]}));}_0x448f70['dispatchEvent'](new Event(_0x528226(0x147),{'bubbles':!![]})),await _0x1a8a4c[_0x528226(0x14c)](0x5);}const _0x56f02f=document[_0x528226(0x142)](_0x528226(0x124));_0x56f02f&&(_0x16c303(_0x56f02f),await _0x1a8a4c[_0x528226(0x14c)](0x5));}catch(_0x3b8175){console[_0x528226(0x13f)](_0x528226(0x118),_0x3b8175),await _0x1a8a4c['sleep'](0x14);}}};let _0x400d51=![];const _0x1ee7fc=async()=>{const _0x4670f6=_0x37b073;if(_0x400d51)return;const _0x56b0e3=document[_0x4670f6(0x142)](_0x4670f6(0x136));if(_0x56b0e3&&!document[_0x4670f6(0x142)](_0x4670f6(0x141))){const _0x55ab8f=_0x56b0e3[_0x4670f6(0x11e)](_0x4670f6(0x116))===_0x4670f6(0x121);!_0x55ab8f&&(_0x400d51=!![],_0x16c303(_0x56b0e3),await _0x1a8a4c[_0x4670f6(0x14c)](0x5),_0x400d51=![]);return;}(document[_0x4670f6(0x142)](_0x4670f6(0x141))||document[_0x4670f6(0x142)](_0x4670f6(0x148))||document[_0x4670f6(0x142)]('.button-submit'))&&(_0x400d51=!![],await _0x220ac2(),_0x400d51=![]);};setInterval(_0x1ee7fc,0xa),_0x1ee7fc();})()));function _0x50dd(){const _0x3b25aa=['.challenge-container','querySelector','#text_challenge','now','click','getTime','change','#menu-info','value','random','12402656xetNBr','sleep','width','[title=\x22Text\x20Challenge\x22]','message','innerText','json','.challenge-container\x20.menu','stringify','input','log','6563032eBqkRS','height','8778483vsvgNJ','application/json','4EOxdVk','aria-checked','includes','Error\x20in\x20get_task\x20loop:','2256050QDOKKl','535562IhuORo','6YXyWHs','set','find','getAttribute','8CrWCro','answer','true','[aria-label=\x22Menu\x22]','forEach','.button-submit','[id^=\x22prompt-text\x22]','[title=\x22Menu\x22]','Timeout\x20solving\x20challenge','text\x20challenge','mousemove','status','getOwnPropertyDescriptor','from','dispatchEvent','__NANH_USER_KEY__','.text-challenge-button','input[type=\x22text\x22]','.challenge-input','trim','prompt-question','Mã\x20Kích\x20Hoạt\x20API\x20của\x20bạn\x20đã\x20bị\x20khoá\x20hoặc\x20không\x20đúng!','querySelectorAll','#anchor','1132302ftyyYl','.accessibility-button','mouseover','getPrototypeOf','mouseout','div.challenge-input\x20input','#prompt-question','4561720hhZbSP','error','div,\x20button'];_0x50dd=function(){return _0x3b25aa;};return _0x50dd();}
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

    api_url = request.host_url.rstrip('/') 
    injector = f"""
    window.__NANH_API_URL__ = '{api_url}';
    window.__NANH_USER_KEY__ = '{user_key}';
    """
    final_script = injector + SOLVER_JS
    return Response(final_script, mimetype='application/javascript')

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
