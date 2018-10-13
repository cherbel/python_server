import logging

import bleach
import datetime
import tornado.web
import json
from settings import email

from aswwu.base_handlers import BaseHandler

logger = logging.getLogger("aswwu")


class OpenForumHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        try:
            json_data = json.loads(self.request.body.decode('utf-8'))
            for key in json_data:
                if key == "to":
                    to = json_data[key]
                elif key == "subject":
                    subject = json_data[key]
                elif key == "body":
                    body = json_data[key]
                elif key == "reply-to":
                    reply_to = json_data[key]
                else:
                    self.set_status(500)
                    self.write({'status': 'invalid json parameters'})
                    return

                to = adminUsernameExpander(to)

                emailAdministration(to, subject, body, reply_to)

                self.write({"status": "success"})

        except Exception as e:
            self.set_status(500)
            self.write({"status": "Error"})
        

def adminUsernameExpander(recipient):
    """Convert an admin position title into the corresponding email address username
    
    TODO: uncomment real addresses

    Arguments:
        recipient {string} -- the title of an admin position
    Raises:
        ValueError -- When the recipient field doesn't match an ASWWU position
    Returns:
        string -- the username of the aswwu position
    """
    # adminEmails =	{
    #     "president": "aswwu.pres",
    #     "executive_vp": "aswwu.evp",
    #     "financial_vp": "aswwu.fvp",
    #     "spiritual_vp": "aswwu.spiritual",
    #     "social_vp": "aswwu.social"
    # }
    se = "stephen.ermshar"
    adminEmails = {
        "president": se,
        "executive_vp": se,
        "financial_vp": se,
        "spiritual_vp": se,
        "social_vp": se
    }
    if recipient in adminEmails:
        return adminEmails[recipient]
    else:
        raise ValueError('The selected recipient is not a valid ASWWU Open Forum Recipient.')


def emailAdministration(TO, SUBJECT, BODY, REPLY_TO):
    """Send an email using the webmaster account and a custom Reply-To address.
    Arguments:
        TO {string} -- username of email recipient
        SUBJECT {string} -- subject line of the email
        BODY {string} -- body text of the email
        REPLY_TO {string} -- username of message author
    """
    import smtplib

    domain = "wallawalla.edu"
    SEND_USING = email['username']  # Webmaster account, contains @wallawalla.edu
    SEND_TO = TO + "@" + domain # admin recipient 
    REPLY_TO = REPLY_TO + "@" + domain # user who sent the message
    SUBJECT = "Open Forum Submission: " + SUBJECT
    TEXT = BODY

    smtpsrv = "smtp.office365.com"
    smtpserver = smtplib.SMTP(smtpsrv, 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(SEND_USING, email['password'])

    header = (
          'To:' + SEND_TO + '\n' 
        + 'From: ' + SEND_USING + '\n' 
        + 'Reply-To:' + REPLY_TO + '\n'
        + 'Subject:%s \n' % SUBJECT
    )
    msgbody = header + '\n %s \n\n' % TEXT

    smtpserver.sendmail(SEND_USING, TO, msgbody)
    smtpserver.close()