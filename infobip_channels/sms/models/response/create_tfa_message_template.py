from infobip_channels.core.models import ResponseBase
from infobip_channels.sms.models.core.tfa_message_template import TFAMessageTemplate


class CreateTFAMessageTemplateResponse(ResponseBase):
    template: TFAMessageTemplate
