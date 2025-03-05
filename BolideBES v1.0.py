import pyautogui
import time
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import threading
import random
from datetime import datetime

# 全局计数器，用于记录已发送邮件数
emails_sent = 0

# 设置控件的状态（'normal'或'disable'）
def set_widgets_state(state):
    recipients_text.config(state=state)
    min_interval_entry.config(state=state)
    max_interval_entry.config(state=state)
    subject_entry.config(state=state)
    message_text.config(state=state)
    send_button.config(state=state)
    save_log_button.config(state=state)

# 在日志框中添加带时间戳的消息
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_text.insert(tk.END, f"[{timestamp}] {message}\n")
    log_text.see(tk.END)

# 发送邮件的功能
def send_emails():
    global emails_sent
    # 锁定界面，防止用户在发送过程中干扰
    set_widgets_state("disable")
    
    # 获取收件人列表
    recipients = [r.strip() for r in recipients_text.get("1.0", tk.END).split("\n") if r.strip()]
    try:
        min_interval = int(min_interval_entry.get())
        max_interval = int(max_interval_entry.get())
    except ValueError:
        log_message("Invalid interval input, please enter integers.")
        set_widgets_state("normal")
        return

    subject = subject_entry.get()
    message_content = message_text.get("1.0", tk.END).strip()
    
    log_message("Starting bulk email sending...")
    emails_sent = 0
    
    for recipient in recipients:
        # 模拟等待用户切换到邮件客户端
        time.sleep(3)
        # 使用快捷键新建邮件
        pyautogui.hotkey("ctrl", "n")
        time.sleep(1)
        # 填写邮件信息
        pyautogui.write(recipient)
        pyautogui.press("tab")
        pyautogui.write(subject)
        pyautogui.press("tab")
        pyautogui.write(message_content)
        pyautogui.hotkey("ctrl", "enter")
        
        emails_sent += 1
        log_message(f"Email #{emails_sent} sent to: {recipient}")
        
        # 随机选择发送间隔
        random_interval = random.randint(min_interval, max_interval)
        time.sleep(random_interval)
    
    log_message("All emails sent!")
    # 重新启用界面
    set_widgets_state("normal")

# 启动邮件发送的线程
def start_sending():
    threading.Thread(target=send_emails, daemon=True).start()

# 保存日志文件
def save_log():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")],
                                             title="Save Log File")
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(log_text.get("1.0", tk.END))
            log_message("Log saved successfully.")
        except Exception as e:
            log_message(f"Error saving log: {e}")

# 检测软件版本是否过期
def check_version():
    # 获取当前本地时间
    current_date = datetime.now()
    expiration_date = datetime(2025, 4, 1)  # 设置版本过期日期
    if current_date > expiration_date:
        messagebox.showwarning("Version Expired", "Your software version has expired.")
        root.quit()  # 退出应用程序

# 显示软件免责声明
def show_disclaimer():
    result = messagebox.askyesno("Disclaimer", "This software is for educational purposes only. The author is not responsible for any legal issues arising from misuse. Do you agree to continue?")
    if not result:
        root.quit()

# 创建主窗口
root = tk.Tk()
root.title("Bolide BES - Bulk Email Sender v1.0")
root.geometry("650x750")
root.configure(bg="#F7F7F7")

# 检查版本是否过期
check_version()

# 显示免责声明对话框
show_disclaimer()

# 使用现代字体和扁平设计
default_font = ("Segoe UI", 11)
root.option_add("*Font", default_font)

# 标题
title_label = tk.Label(root, text="BES - Bulk Email Sender", bg="#F7F7F7", fg="#333333", font=("Segoe UI", 20, "bold"))
title_label.pack(pady=(20,10))

# 主容器
container = tk.Frame(root, bg="#F7F7F7")
container.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# 收件人输入区
tk.Label(container, text="Recipients (one per line):", bg="#F7F7F7", fg="#333333").pack(anchor="w", pady=(10,0))
recipients_text = scrolledtext.ScrolledText(container, height=5, wrap=tk.WORD, relief="flat", bd=2)
recipients_text.pack(fill=tk.BOTH, pady=(0,10))

# 发送间隔输入区
interval_frame = tk.Frame(container, bg="#F7F7F7")
interval_frame.pack(fill=tk.X, pady=(5,10))
tk.Label(interval_frame, text="Send Interval Range (seconds):", bg="#F7F7F7", fg="#333333").grid(row=0, column=0, sticky="w")
min_interval_entry = tk.Entry(interval_frame, width=5, relief="flat", bd=2)
min_interval_entry.grid(row=0, column=1, padx=(5,0))
min_interval_entry.insert(0, "1")
tk.Label(interval_frame, text="to", bg="#F7F7F7", fg="#333333").grid(row=0, column=2, padx=5)
max_interval_entry = tk.Entry(interval_frame, width=5, relief="flat", bd=2)
max_interval_entry.grid(row=0, column=3)
max_interval_entry.insert(0, "5")

# 邮件主题输入区
tk.Label(container, text="Email Subject:", bg="#F7F7F7", fg="#333333").pack(anchor="w", pady=(10,0))
subject_entry = tk.Entry(container, relief="flat", bd=2)
subject_entry.pack(fill=tk.X, pady=(0,10))

# 邮件内容输入区
tk.Label(container, text="Message Content:", bg="#F7F7F7", fg="#333333").pack(anchor="w", pady=(10,0))
message_text = scrolledtext.ScrolledText(container, height=5, wrap=tk.WORD, relief="flat", bd=2)
message_text.pack(fill=tk.BOTH, pady=(0,10))

# 控制按钮区
buttons_frame = tk.Frame(container, bg="#F7F7F7")
buttons_frame.pack(fill=tk.X, pady=10)
send_button = tk.Button(buttons_frame, text="Start Sending", command=start_sending, relief="flat", bg="#4CAF50", fg="white", activebackground="#45A049")
send_button.pack(side=tk.LEFT, padx=(0,10))
save_log_button = tk.Button(buttons_frame, text="Save Log", command=save_log, relief="flat", bg="#2196F3", fg="white", activebackground="#1976D2")
save_log_button.pack(side=tk.LEFT)

# 日志输出区
tk.Label(container, text="Log:", bg="#F7F7F7", fg="#333333").pack(anchor="w", pady=(10,0))
log_text = scrolledtext.ScrolledText(container, height=10, wrap=tk.WORD, relief="flat", bd=2)
log_text.pack(fill=tk.BOTH, pady=(0,10))

# 运行主循环
root.mainloop()
