
def hello_get(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
    Note:
        For more information on how Flask integrates with Cloud
        Functions, see the `Writing HTTP functions` page.
    """
     #  storage_client = storage.Client.from_service_account_json(json_credentials_path='manisha_service_account_JSON.json')
    return 'Hello World for client library!'