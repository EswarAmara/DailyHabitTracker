

### **4. Implement the Basic Application**

#### **Example Code Impleme


from flask import Flask, request, render_template_string # type: ignore
import smtplib

app = Flask(__name__)

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Email Reminder Scheduler</title>
</head>
<body>
    <h1>Email Reminder Scheduler</h1>
    <form method="POST" action="/schedule">
        <label for="email">Email Address:</label>
        <input type="email" name="email" required><br>
        <label for="task">Task Description:</label>
        <input type="text" name="task" required><br>
        <label for="time">Reminder Time (HH:MM):</label>
        <input type="time" name="time" required><br>
        <button type="submit">Schedule Reminder</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/schedule', methods=['POST'])
def schedule_reminder():
    email = request.form['email']
    task = request.form['task']
    time = request.form['time']

    # Mock email sending (you can expand this later)
    send_email(email, task, time)
    return f"Reminder for '{task}' scheduled for {time} to {email}!"

def send_email(email, task, time):
    # Email credentials (Use environment variables for secure storage in production)
    sender_email = "your-email@example.com"
    sender_password = "your-password"
    subject = "Daily Reminder"
    body = f"Task: {task}\nTime: {time}"

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(sender_email, email, message)
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    app.run(debug=True)
