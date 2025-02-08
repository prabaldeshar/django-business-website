import requests

from django.conf import settings
from helpers.logging_helper import logger


def verify_recaptcha(token):
    recaptcha_url = "https://www.google.com/recaptcha/api/siteverify"
    recaptcha_secret = settings.RECAPTCHA_SECRET_KEY

    response = requests.post(
        recaptcha_url, data={"secret": recaptcha_secret, "response": token}
    )
    logger.info(f"Recaptcha response: {response.json()}")
    logger.info(f"Recaptcha success status: {response.json().get('success')}")

    return response.json().get("success", False)
