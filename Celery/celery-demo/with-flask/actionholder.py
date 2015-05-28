def kirim(formargs):
    from tasks import sendmail

    recipient = formargs.get("to", "widnyana@sebangsa.com")
    subject = formargs.get("subject", "hello from flaskCelery")
    message = formargs.get("message", "ini body email")

    sendmail.delay(recipient, subject, message)
