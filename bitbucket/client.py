""" Defines a client class for working with BitBucket with a set of auth credentials. """

from bitbucket.urls import current_user_url, repositories_url
from bitbucket.namespace import BitBucketNamespaceClient
from bitbucket.accounts import BitBucketAccountsClient

class BitBucketClient(object):
  """ A client for talking to the BitBucket API. """
  def __init__(self, dispatcher, access_token, access_token_secret):
    self._dispatcher = dispatcher
    self._access_token = access_token
    self._access_token_secret = access_token_secret

  def get_current_user(self):
    """ Returns information about the authorized user. """
    url = current_user_url()
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def get_visible_repositories(self):
    """ Returns a list of all repositories visible to the authorized user. """
    url = repositories_url()
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret, params={"role" : "member"})

  def for_namespace(self, namespace):
    """ Returns a client for accessing information for the given user or team. """
    return BitBucketNamespaceClient(self._dispatcher, self._access_token, self._access_token_secret,
                                    namespace)

  def accounts(self):
    """ Returns a client for accessing account information. """
    return BitBucketAccountsClient(self._dispatcher, self._access_token, self._access_token_secret)
