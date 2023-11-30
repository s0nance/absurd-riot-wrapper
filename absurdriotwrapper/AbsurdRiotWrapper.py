class AbsurdRiotWrapper:
    """
    Main class for the absurd riot wrapper.
    Base interaction point to access riot apis.
    """

    def __init__(
            self,
            api_key: str
    ):
        """
        Initialize a new instance of the AbsurdRiotWrapper

        :param string api_key: the API key to use for the created instance.
        """

        if not api_key:
            raise ValueError("no api_key has been provided")
