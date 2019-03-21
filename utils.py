import emails

from configs import EmailConfig


def send_email(mail_to, subject='Registration', text='Welcome'):
    message = emails.Message(mail_from=EmailConfig.HOST_USER, mail_to=mail_to, subject=subject, text=text)
    resp = message.send(smtp=EmailConfig.make_config())

    if resp.status_code not in (250,):
        raise ValueError('Email was not sent correctly')
