"""
We are building code for whatsapp
"""


class WhatsAppFeatures:  # This is whatsapp feature class
    """
        A base class for WhatsApp features, containing common attributes.

        Attributes:
            mobile (int): The mobile number of the user.
            name (str): The name of the user.
            country (str): The country of the user.
        """

    def __init__(self, mobile, name, country, *args, **kwargs):
        """

        :param mobile: mobile int
        :param name: name str
        :param country: country str
        :param args: args if required
        :param kwargs: kwargs if required
        """
        self.mobile = mobile
        self.name = name
        self.country = country
        self.args = args
        self.kwargs = kwargs

    def chat(self, sender: int, receiver: int, message: str):
        """

        :param sender:
        :param receiver:
        :param message:
        :return:
        """
        pass

    def audio(self, sender: int, receiver: int, audio: bytes):
        """

                :param sender:
                :param receiver:
                :param audio:
                :return:
                """
        pass

    def video(self, sender: int, receiver: int, video: bytes):
        """

                :param sender:
                :param receiver:
                :param video:
                :return:
                """
        pass

    def get_person_details(self):
        """

        :return: dict

        """
        pass
