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
/* Obfuscated by J2TEAM.org */(function(_0x2ac06f,_0x3176b8){const _0x227cde=_0x5e79,_0x17c92d=_0x2ac06f();while(!![]){try{const _0x559156=-parseInt(_0x227cde(0x1cc))/0x1+parseInt(_0x227cde(0x1d2))/0x2*(-parseInt(_0x227cde(0x1d5))/0x3)+parseInt(_0x227cde(0x172))/0x4+parseInt(_0x227cde(0x185))/0x5*(-parseInt(_0x227cde(0x17a))/0x6)+-parseInt(_0x227cde(0x1a6))/0x7*(-parseInt(_0x227cde(0x1d0))/0x8)+parseInt(_0x227cde(0x188))/0x9*(-parseInt(_0x227cde(0x183))/0xa)+parseInt(_0x227cde(0x18f))/0xb*(parseInt(_0x227cde(0x1ae))/0xc);if(_0x559156===_0x3176b8)break;else _0x17c92d['push'](_0x17c92d['shift']());}catch(_0x27137d){_0x17c92d['push'](_0x17c92d['shift']());}}}(_0x4057,0x6280c));function _0x4057(){const _0xaea089=['toString','ned\x20→\x20\x22','46288yGBIpr','nge-input\x20','28442dZxuDA','lenge','bmit','72rgrkPR','length','getBoundin','json','value','includes','mousemove','message','.text-chal','trim','tor','\x20API\x20retur','toLowerCas','2956684CtUulK','\x20.menu','stringify','chain','.menu-icon','.accessibi','xt\x20Challen','[title=\x22Me','28920QNiGeK','op:','ertyDescri','nu\x22]','sleep','-container','#menu-info','dispatchEv','random','6671350qCQshi','stateObjec','525sizfWa','__API_URL_','action','9XlEuxB','set','applicatio','height','pt-text\x22]','\x20bạn\x20đã\x20bị','prompt-que','55bGpUgF','Invalid\x20Li','status','ent','now','\x5c(\x20*\x5c)','led:','constructo','et_task\x20lo','change','[id^=\x22prom','ptor','mouseout','init','call','-input','mouseup','input[type','estion','stion','o\x20API:','aria-check','test','854SRufgQ','while\x20(tru','error','true','getTime','Question\x20t','torAll','innerText','2299020wxyaGG','debu','$]*)','input','ạt\x20API\x20của','lving\x20chal','log','mousedown','a-zA-Z_$][','.button-su','apply','querySelec','mouseenter','text\x20chall','(((.+)+)+)','click','\x20không\x20đún','lity-butto','mouseover','search','l=\x22Menu\x22]','answer','.challenge','#anchor','[title=\x22Te','[Solver]\x20✓','=\x22text\x22]','gger','POST','enge','484981YQfHAR','Timeout\x20so'];_0x4057=function(){return _0xaea089;};return _0x4057();}const _0x331e87=(function(){let _0x436944=!![];return function(_0xb8e8ef,_0xc6c788){const _0x5c534e=_0x436944?function(){const _0x5845e1=_0x5e79;if(_0xc6c788){const _0x5a68b5=_0xc6c788[_0x5845e1(0x1b8)](_0xb8e8ef,arguments);return _0xc6c788=null,_0x5a68b5;}}:function(){};return _0x436944=![],_0x5c534e;};}()),_0x14e952=_0x331e87(this,function(){const _0x22b768=_0x5e79;return _0x14e952[_0x22b768(0x1ce)]()[_0x22b768(0x1c1)](_0x22b768(0x1bc)+'+$')[_0x22b768(0x1ce)]()[_0x22b768(0x196)+'r'](_0x14e952)['search'](_0x22b768(0x1bc)+'+$');});_0x14e952();const _0x76e999=(function(){let _0x15258b=!![];return function(_0x532964,_0x119f2e){const _0x30c861=_0x15258b?function(){const _0x14c0a0=_0x5e79;if(_0x119f2e){const _0x4bee38=_0x119f2e[_0x14c0a0(0x1b8)](_0x532964,arguments);return _0x119f2e=null,_0x4bee38;}}:function(){};return _0x15258b=![],_0x30c861;};}());function _0x5e79(_0x54a6a1,_0x1379ab){_0x54a6a1=_0x54a6a1-0x16c;const _0x537ef8=_0x4057();let _0x13cd12=_0x537ef8[_0x54a6a1];return _0x13cd12;}(function(){_0x76e999(this,function(){const _0x270b23=_0x5e79,_0x11a291=new RegExp('function\x20*'+_0x270b23(0x194)),_0xb6bcd4=new RegExp('\x5c+\x5c+\x20*(?:['+_0x270b23(0x1b6)+'0-9a-zA-Z_'+_0x270b23(0x1b0),'i'),_0x2d6508=_0x13cd12(_0x270b23(0x19c));!_0x11a291['test'](_0x2d6508+_0x270b23(0x175))||!_0xb6bcd4[_0x270b23(0x1a5)](_0x2d6508+'input')?_0x2d6508('0'):_0x13cd12();})();}()),((()=>{'use strict';const _0x4d34b1=_0x5e79;const _0x184971=_0x4d34b1(0x186)+'_',_0x737db8='__USER_KEY'+'__',_0x138af2=((()=>{const _0x4112c9=_0x4d34b1,_0x1e8707=(_0x272125=0x3e8)=>new Promise(_0x2e3baa=>setTimeout(_0x2e3baa,_0x272125)),_0xd624a=()=>Date[_0x4112c9(0x193)]?Date[_0x4112c9(0x193)]():new Date()[_0x4112c9(0x1aa)]();return{'sleep':_0x1e8707,'now':_0xd624a};})()),_0x17a7e1=_0x47fdb7=>{const _0x39f287=_0x4d34b1;if(!_0x47fdb7)return![];try{const _0xedf054=_0x47fdb7[_0x39f287(0x1d7)+'gClientRec'+'t'](),_0x4f109b=_0xedf054['x']+_0xedf054['width']/0x2,_0x475f45=_0xedf054['y']+_0xedf054[_0x39f287(0x18b)]/0x2;let _0x4f3862=_0x4f109b-0x32-Math[_0x39f287(0x182)]()*0x64,_0x3ed763=_0x475f45-0x32-Math['random']()*0x64;const _0x204326=0xa;for(let _0x5dd023=0x1;_0x5dd023<=_0x204326;_0x5dd023++){_0x4f3862+=(_0x4f109b-_0x4f3862)*(_0x5dd023/_0x204326)+(Math[_0x39f287(0x182)]()-0.5)*0x5,_0x3ed763+=(_0x475f45-_0x3ed763)*(_0x5dd023/_0x204326)+(Math[_0x39f287(0x182)]()-0.5)*0x5,window[_0x39f287(0x181)+_0x39f287(0x192)](new MouseEvent(_0x39f287(0x1db),{'bubbles':!![],'cancelable':!![],'clientX':_0x4f3862,'clientY':_0x3ed763}));}const _0x504996=[_0x39f287(0x1c0),_0x39f287(0x1ba),_0x39f287(0x1b5),_0x39f287(0x19f),_0x39f287(0x1bd),_0x39f287(0x19b)];return _0x504996['forEach'](_0x5333fe=>{const _0x5493e3=_0x39f287,_0x3a4a39=_0x5333fe===_0x5493e3(0x1c0)?0x0:0x1,_0x457a14=new MouseEvent(_0x5333fe,{'detail':_0x3a4a39,'view':window,'bubbles':!![],'cancelable':!![],'clientX':_0x4f109b,'clientY':_0x475f45});_0x47fdb7[_0x5493e3(0x181)+'ent'](_0x457a14);}),!![];}catch(_0x4dabf3){return![];}},_0x34c0d0=async _0x1a9a7b=>{const _0x58f04c=_0x4d34b1,_0x9d3cd2=(_0x1a9a7b||'')[_0x58f04c(0x16e)]();if(!_0x9d3cd2)return'';try{const _0xbada3a=await fetch(_0x184971,{'method':_0x58f04c(0x1ca),'headers':{'Content-Type':_0x58f04c(0x18a)+'n/json'},'body':JSON[_0x58f04c(0x174)]({'question':_0x9d3cd2,'user_key':_0x737db8})});if(_0xbada3a[_0x58f04c(0x191)]===0x193){const _0x653ee4=await _0xbada3a[_0x58f04c(0x1d8)]();if(_0x653ee4[_0x58f04c(0x1a8)]===_0x58f04c(0x190)+'cense\x20Key')return console[_0x58f04c(0x1a8)]('Mã\x20Kích\x20Ho'+_0x58f04c(0x1b2)+_0x58f04c(0x18d)+'\x20khoá\x20hoặc'+_0x58f04c(0x1be)+'g!'),_0x4e9be5=![],'';}if(_0xbada3a['ok']){const _0x552c6f=await _0xbada3a[_0x58f04c(0x1d8)]();if(_0x552c6f[_0x58f04c(0x1c3)])return console['log'](_0x58f04c(0x1c7)+_0x58f04c(0x170)+_0x58f04c(0x1cf)+_0x552c6f['answer']+'\x22'),_0x552c6f[_0x58f04c(0x1c3)];}}catch(_0x1835ff){console[_0x58f04c(0x1a8)]('[Solver]\x20R'+'equest\x20fai'+_0x58f04c(0x195),_0x1835ff[_0x58f04c(0x16c)]);}return'';},_0x1d0377=async()=>{const _0x181283=_0x4d34b1;if(document['querySelec'+_0x181283(0x16f)](_0x181283(0x1c4)+_0x181283(0x19e))||document[_0x181283(0x1b9)+_0x181283(0x16f)](_0x181283(0x1a0)+_0x181283(0x1c8)))return;for(let _0x4a86d5=0x0;_0x4a86d5<0x5;_0x4a86d5++){if(document[_0x181283(0x1b9)+_0x181283(0x16f)](_0x181283(0x1c4)+_0x181283(0x19e))||document[_0x181283(0x1b9)+_0x181283(0x16f)](_0x181283(0x1a0)+_0x181283(0x1c8)))return;const _0xbd9cbb=document['querySelec'+_0x181283(0x16f)](_0x181283(0x177)+_0x181283(0x1bf)+'n')||document[_0x181283(0x1b9)+'tor']('#menu-info')||document[_0x181283(0x1b9)+'tor'](_0x181283(0x1c4)+_0x181283(0x17f)+_0x181283(0x173))||document[_0x181283(0x1b9)+_0x181283(0x16f)](_0x181283(0x179)+_0x181283(0x17d))||document['querySelec'+'tor']('[aria-labe'+_0x181283(0x1c2))||document[_0x181283(0x1b9)+_0x181283(0x16f)](_0x181283(0x176));_0xbd9cbb&&(_0x17a7e1(_0xbd9cbb),await _0x138af2[_0x181283(0x17e)](0x1e));const _0x3f052c=document[_0x181283(0x1b9)+_0x181283(0x16f)]('#text_chal'+_0x181283(0x1d3))||document['querySelec'+'tor'](_0x181283(0x16d)+'lenge-butt'+'on')||document[_0x181283(0x1b9)+_0x181283(0x16f)](_0x181283(0x1c6)+_0x181283(0x178)+'ge\x22]')||Array['from'](document[_0x181283(0x1b9)+_0x181283(0x1ac)]('div,\x20butto'+'n'))['find'](_0x81ddfb=>_0x81ddfb[_0x181283(0x1ad)]&&_0x81ddfb[_0x181283(0x1ad)][_0x181283(0x171)+'e']()[_0x181283(0x1da)](_0x181283(0x1bb)+_0x181283(0x1cb)));_0x3f052c?(_0x17a7e1(_0x3f052c),await _0x138af2[_0x181283(0x17e)](0x32)):await _0x138af2[_0x181283(0x17e)](0x1e);}},_0x2103a0=async()=>{const _0x3d3615=_0x4d34b1;let _0x3b644e=null,_0x2c9999=null;const _0x26ed26=_0x138af2['now']();while(!![]){if(_0x138af2['now']()-_0x26ed26>0x1d4c0){console['log'](_0x3d3615(0x1cd)+_0x3d3615(0x1b3)+_0x3d3615(0x1d3));break;}if(!document[_0x3d3615(0x1b9)+_0x3d3615(0x16f)](_0x3d3615(0x1c4)+_0x3d3615(0x17f))&&!document[_0x3d3615(0x1b9)+'tor']('#menu-info')&&!document[_0x3d3615(0x1b9)+_0x3d3615(0x16f)](_0x3d3615(0x1b7)+_0x3d3615(0x1d4)))break;await _0x1d0377();try{const _0x2aecef=document[_0x3d3615(0x1b9)+'tor']('#prompt-qu'+_0x3d3615(0x1a1)),_0x26da49=document[_0x3d3615(0x1b9)+'tor'](_0x3d3615(0x199)+_0x3d3615(0x18c));if(!_0x2aecef&&!_0x26da49){await _0x138af2[_0x3d3615(0x17e)](0x1e);continue;}let _0x50eb5c='';if(_0x2aecef&&_0x2aecef['innerText'])_0x50eb5c+=_0x2aecef[_0x3d3615(0x1ad)]['trim']()+'\x20';if(_0x26da49&&_0x26da49[_0x3d3615(0x1ad)]&&_0x26da49['id']!==_0x3d3615(0x18e)+_0x3d3615(0x1a2))_0x50eb5c+=_0x26da49[_0x3d3615(0x1ad)][_0x3d3615(0x16e)]();_0x50eb5c=_0x50eb5c[_0x3d3615(0x16e)]();if(!_0x50eb5c||_0x50eb5c===_0x3b644e){await _0x138af2['sleep'](0x1e);continue;}let _0x146c34=_0x50eb5c;console[_0x3d3615(0x1b4)](_0x3d3615(0x1ab)+_0x3d3615(0x1a3),_0x146c34);const _0x523dcc=await _0x34c0d0(_0x146c34);_0x3b644e=_0x50eb5c,_0x2c9999=_0x523dcc;if(!_0x523dcc){await _0x138af2[_0x3d3615(0x17e)](0x64);continue;}let _0x115858=document['querySelec'+_0x3d3615(0x16f)]('div.challe'+_0x3d3615(0x1d1)+'input')||document[_0x3d3615(0x1b9)+_0x3d3615(0x16f)](_0x3d3615(0x1a0)+'=\x22text\x22]');if(_0x115858){_0x17a7e1(_0x115858),await _0x138af2[_0x3d3615(0x17e)](0xa);try{const _0x396acb=Object['getOwnProp'+_0x3d3615(0x17c)+_0x3d3615(0x19a)](Object['getPrototy'+'peOf'](_0x115858),_0x3d3615(0x1d9))?.[_0x3d3615(0x189)];_0x396acb?_0x396acb[_0x3d3615(0x19d)](_0x115858,_0x523dcc):_0x115858[_0x3d3615(0x1d9)]=_0x523dcc,_0x115858[_0x3d3615(0x181)+'ent'](new Event(_0x3d3615(0x1b1),{'bubbles':!![]}));}catch(_0x28131d){_0x115858[_0x3d3615(0x1d9)]=_0x523dcc,_0x115858[_0x3d3615(0x181)+_0x3d3615(0x192)](new Event(_0x3d3615(0x1b1),{'bubbles':!![]}));}_0x115858[_0x3d3615(0x181)+'ent'](new Event(_0x3d3615(0x198),{'bubbles':!![]})),await _0x138af2['sleep'](0x5);}const _0x207528=document[_0x3d3615(0x1b9)+_0x3d3615(0x16f)](_0x3d3615(0x1b7)+'bmit');_0x207528&&(_0x17a7e1(_0x207528),await _0x138af2[_0x3d3615(0x17e)](0x5));}catch(_0x2596f7){console[_0x3d3615(0x1a8)]('Error\x20in\x20g'+_0x3d3615(0x197)+_0x3d3615(0x17b),_0x2596f7),await _0x138af2[_0x3d3615(0x17e)](0x14);}}};let _0x4e9be5=![];const _0x5dfa57=async()=>{const _0xb1078e=_0x4d34b1;if(_0x4e9be5)return;const _0x5a9e81=document['querySelec'+_0xb1078e(0x16f)](_0xb1078e(0x1c5));if(_0x5a9e81&&!document[_0xb1078e(0x1b9)+'tor'](_0xb1078e(0x1c4)+'-container')){const _0x1b599a=_0x5a9e81['getAttribu'+'te'](_0xb1078e(0x1a4)+'ed')===_0xb1078e(0x1a9);!_0x1b599a&&(_0x4e9be5=!![],_0x17a7e1(_0x5a9e81),await _0x138af2[_0xb1078e(0x17e)](0x5),_0x4e9be5=![]);return;}(document[_0xb1078e(0x1b9)+'tor'](_0xb1078e(0x1c4)+_0xb1078e(0x17f))||document[_0xb1078e(0x1b9)+_0xb1078e(0x16f)](_0xb1078e(0x180))||document[_0xb1078e(0x1b9)+_0xb1078e(0x16f)]('.button-su'+_0xb1078e(0x1d4)))&&(_0x4e9be5=!![],await _0x2103a0(),_0x4e9be5=![]);};setInterval(_0x5dfa57,0xa),_0x5dfa57();})());function _0x13cd12(_0x5e5fac){function _0x7003ae(_0x50db6e){const _0x50d507=_0x5e79;if(typeof _0x50db6e==='string')return function(_0x9048a2){}[_0x50d507(0x196)+'r'](_0x50d507(0x1a7)+'e)\x20{}')[_0x50d507(0x1b8)]('counter');else(''+_0x50db6e/_0x50db6e)[_0x50d507(0x1d6)]!==0x1||_0x50db6e%0x14===0x0?function(){return!![];}['constructo'+'r'](_0x50d507(0x1af)+'gger')[_0x50d507(0x19d)](_0x50d507(0x187)):function(){return![];}[_0x50d507(0x196)+'r'](_0x50d507(0x1af)+_0x50d507(0x1c9))[_0x50d507(0x1b8)](_0x50d507(0x184)+'t');_0x7003ae(++_0x50db6e);}try{if(_0x5e5fac)return _0x7003ae;else _0x7003ae(0x0);}catch(_0x99c4fa){}}
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
    
    import base64
    encoded = base64.b64encode(script.encode('utf-8')).decode('utf-8')
    obfuscated_script = f"Function(decodeURIComponent(escape(atob('{encoded}'))))();"
    
    return Response(obfuscated_script, mimetype='application/javascript')

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
