from flask import Flask, request, jsonify

app = Flask(__name__)

def compress_string(s: str) -> str:
    """压缩连续重复字符，规则：重复次数>2时替换为'字符+次数'，否则保留原样"""
    if not s:
        return ""
    result = []
    count = 1
    prev = s[0]
    for ch in s[1:]:
        if ch == prev:
            count += 1
        else:
            # 处理上一段字符
            if count > 2:
                result.append(f"{prev}{count}")
            else:
                result.append(prev * count)
            prev = ch
            count = 1
    # 处理最后一段
    if count > 2:
        result.append(f"{prev}{count}")
    else:
        result.append(prev * count)
    return "".join(result)

@app.route('/compress', methods=['POST'])
def compress():
    """API端点：接收JSON {"text": "字符串"}，返回压缩结果"""
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing "text" field'}), 400
    text = data['text']
    if not isinstance(text, str):
        return jsonify({'error': 'text must be a string'}), 400
    if not text.isupper() or not all('A' <= c <= 'Z' for c in text):
        return jsonify({'error': 'Only uppercase letters A-Z are allowed'}), 400
    if len(text) < 1 or len(text) > 10000:
        return jsonify({'error': 'Length must be between 1 and 10000'}), 400

    compressed = compress_string(text)
    return jsonify({'compressed': compressed})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)