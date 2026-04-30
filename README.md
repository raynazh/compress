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


## 压缩示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `"AA"` | `"AA"` | 重复2次，不压缩 |
| `"AAA"` | `"A3"` | 重复3次，压缩 |
| `"AAAA"` | `"A4"` | 重复4次，压缩 |
| `"AAABBBBAACC"` | `"A3B4AACC"` | 多段压缩 |
| `"ABCD"` | `"ABCD"` | 无连续重复 |
| `"AABBCC"` | `"AABBCC"` | 每段只重复2次 |

## 测试

```bash
python test.py
```
