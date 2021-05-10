
import yagmail
conn = yagmail.SMTP(
        user="467938742@qq.com",
        password="authcode",
        host="smtp.qq.com",
        port=465
        )


content = "内容填充"
body = f"模版 {content}"
conn.send("467938742@qq.com", "主题", body, "receive_email.py")
