from infobip_channels.core.models import MessageBodyBase
from infobip_channels.sms.models.core.tfa_application import TFAApplication


class CreateTFAApplicationBody(MessageBodyBase, TFAApplication):
    pass
