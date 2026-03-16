"""
MalaClaw 配置文件示例
复制此文件为 config.py 并填入你的配置信息
"""

# ==================== 百炼平台配置 ====================
BAILIAN_API_KEY = "sk-your-api-key-here"
BAILIAN_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"

# ==================== 飞书配置（二选一）====================

# 方式 1：Webhook（推荐，简单）
FEISHU_WEBHOOK = "https://open.feishu.cn/open-apis/bot/v2/hook/your-webhook-id"

# 方式 2：完整 API（功能更强）
FEISHU_APP_ID = "cli_xxxxxxxxxxxxx"
FEISHU_APP_SECRET = "your-app-secret"

# ==================== 邮件配置 ====================
EMAIL_CONFIG = {
    "smtp_server": "smtp.qq.com",      # SMTP 服务器
    "smtp_port": 465,                   # SSL 端口
    "username": "your_email@qq.com",    # 发件人邮箱
    "password": "your_auth_code"        # 授权码（不是密码）
}

# ==================== 数据库配置（待扩展）====================
DATABASE_CONFIG = {
    "type": "mysql",                    # 数据库类型
    "host": "localhost",
    "port": 3306,
    "username": "root",
    "password": "your-password",
    "database": "mydb"
}

# ==================== 其他配置 ====================
DEBUG = True                            # 调试模式
LOG_LEVEL = "INFO"                      # 日志级别
MAX_LOGS = 50                           # 最大日志条数
