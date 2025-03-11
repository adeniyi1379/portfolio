from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import aiosmtplib
from email.message import EmailMessage

app = FastAPI()

# Serve static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Jinja2 for rendering HTML templates
templates = Jinja2Templates(directory="templates")

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"  # Change if using another provider
SMTP_PORT = 587
EMAIL_USER = "your-email@gmail.com"
EMAIL_PASS = "your-email-password"

async def send_email(name, email, message):
    """Send email asynchronously using SMTP."""
    msg = EmailMessage()
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_USER  # Send to yourself
    msg["Subject"] = "New Contact Form Submission"
    msg.set_content(f"Name: {name}\nEmail: {email}\nMessage: {message}")

    await aiosmtplib.send(msg, hostname=SMTP_SERVER, port=SMTP_PORT, use_tls=False, start_tls=True,
                          username=EMAIL_USER, password=EMAIL_PASS)

@app.get("/", response_class=HTMLResponse)
async def serve_homepage(request: Request):
    """Serve the homepage with the contact form."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/send_email")
async def contact_form(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    """Handle form submission and send email."""
    await send_email(name, email, message)
    return {"message": "Email sent successfully!"}

# Run with: uvicorn app:app --reload
