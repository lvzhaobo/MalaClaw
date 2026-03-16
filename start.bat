@echo off
echo ========================================
echo MalaClaw - AI Agent 平台启动脚本
echo ========================================
echo.

REM 检查 Python 是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到 Python，请先安装 Python
    pause
    exit /b 1
)

echo [1/3] 检查 Python 依赖...
pip install -r requirements.txt >nul 2>&1
if errorlevel 1 (
    echo [警告] 依赖安装失败，请手动执行：pip install -r requirements.txt
) else (
    echo [成功] Python 依赖已安装
)

echo.
echo [2/3] 检查 Playwright 浏览器...
playwright install chromium >nul 2>&1
if errorlevel 1 (
    echo [警告] Playwright 浏览器安装失败，请手动执行：playwright install chromium
) else (
    echo [成功] Playwright 浏览器已安装
)

echo.
echo [3/3] 启动 MalaClaw...
echo.
echo ========================================
echo 访问地址：http://localhost:5000
echo 按 Ctrl+C 停止服务
echo ========================================
echo.

python app.py

pause
