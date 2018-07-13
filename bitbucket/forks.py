""" Defines a client class for working with a specific BitBucket repository's links. """

from bitbucket.urls import repository_forks_url

class BitBucketRepositoryForksClient(object):
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

  def all(self):
    """ Returns a list of the links found under the repository. """
    url = repository_forks_url(self._namespace, self._repository_name)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def create(self, owner, name,
             description=None,
             fork_policy=None,
             language=None,
             mainbranch=None,
             is_private=None,
             has_issues=None,
             has_wiki=None,
             project=None):
    """ Creates a new fork. """
    url = repository_forks_url(self._namespace, self._repository_name)

    # This is kind of ugly, but we'd otherwise have to do an inspection.
    req_args = {}

    if owner is not None:
        req_args["owner"] = owner
    if name is not None:
        req_args["name"] = description

    if description is not None:
        req_args["description"] = description
    if fork_policy is not None:
        req_args["fork_policy"] = fork_policy
    if language is not None:
        req_args["language"] = language
    if mainbranch is not None:
        req_args["mainbranch"] = mainbranch
    if is_private is not None:
        req_args["is_private"] = is_private
    if has_issues is not None:
        req_args["has_issues"] = has_issues
    if has_wiki is not None:
        req_args["has_wiki"] = has_wiki
    if project is not None:
        req_args["project"] = project

    return self._dispatcher.dispatch(url, method='POST', access_token=self._access_token,
                                     access_token_secret=self._access_token_secret,
                                     **req_args)
