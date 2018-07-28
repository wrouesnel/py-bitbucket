""" Defines a client class for working with BitBucket repositories. """

from bitbucket.urls import repositories_for_namespace_url, repository_for_namespace_url
from bitbucket.repository import BitBucketRepositoryClient

class BitBucketRepositoriesClient(object):
  """ Client class representing the repositories under a namespace in bitbucket. """
  def __init__(self, dispatcher, access_token, access_token_secret, namespace):
    self._dispatcher = dispatcher
    self._access_token = access_token
    self._access_token_secret = access_token_secret
    self._namespace = namespace

  @property
  def namespace(self):
    """ Returns the namespace. """
    return self._namespace

  def __iter__(self):
    url = repositories_for_namespace_url(self.namespace)
    sucess, data, error = self._dispatcher.dispatch(url, access_token=self._access_token,
                              access_token_secret=self._access_token_secret)
    for repo_data in data:
      yield self.get(repo_data['name'])

  def get(self, repository_name):
    """ Returns a client for interacting with a specific repository. """
    return BitBucketRepositoryClient(self._dispatcher, self._access_token,
                                     self._access_token_secret, self._namespace,
                                     repository_name)
  def delete(self, repository_name):
    """ Deletes a repository and returns the result """
    url = repository_for_namespace_url(self.namespace, repository_name)

    return self._dispatcher.dispatch(url, method='DELETE', access_token=self._access_token,
                                     access_token_secret=self._access_token_secret)