# 字符串压缩 API

一个基于 Flask 的字符串压缩服务，用于压缩连续重复的字符。

## 功能说明

将字符串中连续重复的字符进行压缩，规则如下：
- 重复次数 ≤ 2：保留原样（如 `AA` → `AA`）
- 重复次数 > 2：压缩为 `字符+次数`（如 `AAA` → `A3`）

## 安装依赖

```bash
pip install flask
```

## 运行服务

```bash
python compress.py
```

服务将在 `http://localhost:9090` 启动。

## API 接口

### 压缩字符串

**接口路径**：`POST /compress`

**请求头**：
```
Content-Type: application/json
```

**请求体**：
```json
{
  "text": "AAABBBBAACC"
}
```

**参数说明**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `text` | string | 是 | 待压缩的字符串，仅支持大写字母 A-Z，长度 1-10000 |

**成功响应**（HTTP 200）：
```json
{
  "compressed": "A3B4AACC"
}
```

**错误响应**（HTTP 400）：

缺少字段：
```json
{
  "error": "Missing \"text\" field"
}
```

类型错误：
```json
{
  "error": "text must be a string"
}
```

字符无效：
```json
{
  "error": "Only uppercase letters A-Z are allowed"
}
```

长度超出范围：
```json
{
  "error": "Length must be between 1 and 10000"
}
```

## 使用示例

### cURL

```bash
curl -X POST http://localhost:9090/compress \
  -H "Content-Type: application/json" \
  -d '{"text": "AAABBBBAACC"}'
```

### Python

```python
import requests

response = requests.post(
    'http://localhost:9090/compress',
    json={'text': 'AAABBBBAACC'}
)
print(response.json())
```

### JavaScript

```javascript
fetch('http://localhost:9090/compress', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ text: 'AAABBBBAACC' })
})
  .then(res => res.json())
  .then(data => console.log(data));
```

## 压缩示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `"AA"` | `"AA"` | 重复2次，不压缩 |
| `"AAA"` | `"A3"` | 重复3次，压缩 |
| `"AAAA"` | `"A4"` | 重复4次，压缩 |
| `"AAABBBBAACC"` | `"A3B4AACC"` | 多段压缩 |
| `"ABCD"` | `"ABCD"` | 无连续重复 |
| `"AABBCC"` | `"AABBCC"` | 每段只重复2次 |

## 算法说明

压缩算法采用单次遍历方式：
1. 遍历字符串，统计连续重复字符的次数
2. 当字符变化时，处理上一段的压缩逻辑
3. 根据重复次数决定是否压缩
4. 时间复杂度：O(n)

## 测试

运行测试文件：

```bash
python test.py
```

## 许可证

MIT License
