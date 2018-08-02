""" Defines a client class for working with a specific BitBucket repository's links. """

from bitbucket.urls import repository_pipelines_config_variables_url, \
  repository_pipelines_config_variables_variable_url


class BitBucketRepositoryPipelinesConfigVariablesClient(object):
  """ Client class representing the variables for pipeliens under a repository in bitbucket.

  See https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Busername%7D/%7Brepo_slug%7D/pipelines_config/variables/
  for data structure details.
  """

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

  def all(self):
    """ Return all variables in the current repository """
    # Workaround bug https://bitbucket.org/site/master/issues/16233/api-call-to-environment-variables-end%C2%A0
    url = repository_pipelines_config_variables_url(self._namespace, self._repository_name) + "?pagelen=100"
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def get(self, variable_uuid):
    """ Retreive a repository level variable """
    url = repository_pipelines_config_variables_variable_url(self._namespace, self._repository_name, variable_uuid)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                     access_token_secret=self._access_token_secret)

  def update(self, variable_uuid, variable_name=None, variable_value=None, secured=None):
    """ Update a repository variable. Only non-null fields are updated."""
    url = repository_pipelines_config_variables_variable_url(self._namespace, self._repository_name, variable_uuid)

    data = {}
    if variable_name is not None:
      data['key'] = variable_name

    if variable_value is not None:
      data['value'] = variable_value

    if secured is not None:
      data['secured'] = secured

    return self._dispatcher.dispatch(url, method="PUT", access_token=self._access_token,
                                     access_token_secret=self._access_token_secret, json_body=True,
                                     **data)

  def delete(self, variable_uuid):
    url = repository_pipelines_config_variables_variable_url(self._namespace, self._repository_name, variable_uuid)
    return self._dispatcher.dispatch(url, method="DELETE", access_token=self._access_token,
                                     access_token_secret=self._access_token_secret)

  def create(self, variable_name, variable_value, secured):
    """ Create a variable for the current repository """
    url = repository_pipelines_config_variables_url(self._namespace, self._repository_name)
    return self._dispatcher.dispatch(url, method="POST", access_token=self._access_token,
                                     access_token_secret=self._access_token_secret, json_body=True,
                                     key=variable_name, value=variable_value, secured=secured)