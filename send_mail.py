import ElasticEmail
from ElasticEmail.api import emails_api
from ElasticEmail.model .email_content import EmailContent
from ElasticEmail.model.body_part import BodyPart
from ElasticEmail.model.body_content_type import BodyContentType
from ElasticEmail.model.transactional_recipient import TransactionalRecipient
from ElasticEmail.model.email_transactional_message_data import EmailTransactionalMessageData
from pprint import pprint

def check_ending(address, end):
    ending = address[:-5:-1]
    ending = ending[::-1]
    if ending != end:
        return False
    return True

def send_email(recipient, subject_line, html_body):
    configuration = ElasticEmail.Configuration()
    configuration.api_key['apikey'] = '320AFEE6A10D141A9F07AA6C11E56F5FE5186412E0A7830F2B33C9DD97B249454FDAF46FCC09E4916B68B68C1FE390B1'
    with ElasticEmail.ApiClient(configuration) as api_client:
        api_instance = emails_api.EmailsApi(api_client)
        email_transactional_message_data = EmailTransactionalMessageData(
            recipients =TransactionalRecipient(
                to=[
                    recipient,
                ]
            ),
            content=EmailContent(
                body = [
                    BodyPart(
                        content_type=BodyContentType("HTML"),
                        content=html_body,
                        charset="utf-8"
                    ),
                ],
                _from="info@aubreyhayes.me",
                reply_to="info@aubreyhayes.me",
                subject=subject_line,
            )
        )

        try:
            api_response = api_instance.emails_transactional_post(email_transactional_message_data)
            print(api_response)
        except ElasticEmail.ApiException as e:
            print("Exception wehn calling EmailsApi->emails_post: %s\n" % e)