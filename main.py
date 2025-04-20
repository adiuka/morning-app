from scrapers import good_news
from services import calendar_service, quotes_service, weather_service
from jinja2 import Environment, FileSystemLoader
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from config import SMTP_PASS, SMTP_EMAIL, SMTP_RECEIVER


env = Environment(loader=FileSystemLoader("templates"))
quote = quotes_service.get_inspirational_quote()
average_temperature, will_rain = weather_service.get_weather()
calendar = calendar_service.fetch_calendar_data()
news = good_news.good_news_scrape()


def render_template(average_temperature, will_rain, calendar, news, quote):
    template = env.get_template("email_template.html")

    email_body = template.render(
        average_temperature=average_temperature,
        will_rain=will_rain,
        calendar=calendar,
        news=news,
        quote=quote
    )
    return email_body


email_body = render_template(average_temperature, will_rain, calendar, news, quote)
subject = f"Your Morning Briefing 🌤️ {datetime.now().strftime('%B %d, %Y')}"

msg = MIMEMultipart("alternative")
msg["From"] = SMTP_EMAIL
msg["To"] = SMTP_RECEIVER
msg["Subject"] = subject
msg.attach(MIMEText(email_body, "html"))


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(SMTP_EMAIL, SMTP_PASS)
    connection.sendmail(SMTP_EMAIL, SMTP_RECEIVER, msg.as_string())
