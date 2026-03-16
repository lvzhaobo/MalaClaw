# 🦞 MalaClaw 快速开始指南

## 3 分钟快速上手

### 步骤 1：安装依赖

```bash
cd MalaClaw
pip install -r requirements.txt
```

### 步骤 2：准备配置文件

```bash
# 复制配置示例
cp config.example.json config.json

# 或者在 Windows PowerShell 中
Copy-Item config.example.json config.json
```

### 步骤 3：（可选）配置第三方服务

编辑 `config.json` 文件，填写你的配置信息：

```json
{
  "bailian": {
    "api_key": "sk-your-api-key-here",
    "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1"
  },
  "feishu": {
    "webhook": "",
    "app_id": "",
    "app_secret": ""
  }
}
```

**提示**：不填写也可以运行，只是相关功能无法使用。

### 步骤 4：安装浏览器（可选）

```bash
playwright install chromium
```

这一步是为了支持网页截图功能，如果不需要可以跳过。

### 步骤 5：启动应用

```bash
python app.py
```

看到以下输出表示成功：

```
 * Running on http://127.0.0.1:5000
 * Running on http://YOUR_IP:5000
```

### 步骤 6：访问页面

打开浏览器访问：**http://localhost:5000**

---

## 🎯 快速体验功能

### 场景 1：创建定时任务

1. 访问 **控制台** 页面
2. 点击"添加任务"
3. 填写：
   - 任务 ID: `morning_hello`
   - 任务名称：每日问候
   - 选择助手：内容助手
   - 执行技能：hello
   - Cron 表达式：`0 9 * * 1-5`（工作日早上 9 点）
   - 技能参数：`{"message": "大家早上好！"}`
4. 点击"保存"

### 场景 2：飞书消息推送

1. 访问 **每日推送** 页面
2. 配置飞书 Webhook（获取方法见 README.md）
3. 填写消息内容
4. 点击"立即发送"

### 场景 3：大模型对话

1. 访问 **控制台** 页面
2. 选择"数据助手"
3. 执行技能：`bailian_llm`
4. 参数：`{"prompt": "什么是人工智能？"}`
5. 点击"执行"

---

## 🔧 常见问题

### Q: 端口被占用怎么办？

修改 `app.py` 最后一行：

```python
app.run(host='0.0.0.0', port=5001, debug=True)  # 改为 5001
```

### Q: 如何停止应用？

按 `Ctrl+C` 终止 Flask 进程

### Q: 查看日志？

控制台会实时输出日志，也可以在页面查看

### Q: 配置保存在哪里？

- 配置文件：`config.json`
- 任务配置：保存在内存中，重启后重置
- 日志：默认保留最近 50 条

---

## 📚 更多文档

- **完整文档**：README.md
- **配置示例**：config.example.json
- **代码示例**：test_basic.py

---

**祝你使用愉快！** 🎉
