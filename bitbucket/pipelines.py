""" Defines a client class for working with a specific BitBucket repository's pipelines. """

from bitbucket.urls import repository_pipelines_url

from bitbucket.variables import BitBucketRepositoryPipelinesConfigVariablesClient


class BitBucketRepositoryPipelinesClient(object):
  """ Client class representing the links under a repository in bitbucket. """
  def __init__(self, dispatcher, access_token, access_token_secret, namespace, repository_name):
    self._dispatcher = dispatcher
    self._access_token = access_token
    self._access_token_secret = access_token_secret
    self._namespace = namespace
    self._repository_name = repository_name

  @property
  def namespace(self):
    """ Returns the namespace. """
    return self._namespace

  @property
  def repository_name(self):
    """ Returns the repository name. """
    return self._repository_name

  def trigger_ref_target(self, ref_type, ref_name):
      url = repository_pipelines_url(self._namespace, self._repository_name)

      target = {
          "type": "pipeline_ref_target",
          "ref_type": ref_type,
          "ref_name": ref_name
      }

      return self._dispatcher.dispatch(url, method="POST", access_token=self._access_token,
                                       access_token_secret=self._access_token_secret,
                                       json_body=True, target=target)

  def variables(self):
    """ Returns a resource for managing the variables under the repositories pipeline configuration """
    return BitBucketRepositoryPipelinesConfigVariablesClient(self._dispatcher, self._access_token,
                                     self._access_token_secret, self._namespace,
                                     self.repository_name)

