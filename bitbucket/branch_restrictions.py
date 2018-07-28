""" Defines a client class for working with a specific BitBucket repository's links. """

# We use requests so use requests.compat to handle py2-to-3 compatibility
import requests.compat
from enum import Enum

from bitbucket.urls import repository_branch_restrictions_url, repository_branch_restrictions_by_id_url


class BitBucketRepositoryBranchRestrictionsClient(object):
  """ Client class representing the variables for branch restrictions under the repository in bitbucker
  """

  class RestrictionKind(Enum):
    """ Provides some helpers for setting restriction kind """
    require_passing_builds_to_merge = "require_passing_builds_to_merge"
    force = "force"
    require_all_dependencies_merged = "require_all_dependencies_merged"
    push = "push"
    require_approvals_to_merge = "require_approvals_to_merge"
    enforce_merge_checks = "enforce_merge_checks"
    restrict_merges = "restrict_merges"
    reset_pullrequest_approvals_on_change = "reset_pullrequest_approvals_on_change"
    delete = "delete"

  UPDATEABLE_FIELDS = set(["kind", "pattern", "users", "groups", "value"])

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
    """ Return all branch restrictions in the current repository """
    url = repository_branch_restrictions_url(self._namespace, self._repository_name)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def get(self, id):
    """ Retrieve a specific branch restriction """
    url = repository_branch_restrictions_by_id_url(self._namespace, self._repository_name, id)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                     access_token_secret=self._access_token_secret)

  def update(self, id, **kwargs):
    """ Update a repository variable. Only specified fields are updated. This function will
    handle an update that consists of the output of a GET request for the rule ID and discard fields
    which aren't needed sensibly.
    """
    url = repository_branch_restrictions_by_id_url(self._namespace, self._repository_name, id)

    # Filter the input so GET requests yield nice updates for users
    data = {}
    for field in self.UPDATEABLE_FIELDS:
      if field in kwargs:
          data[field] = kwargs[field]

    return self._dispatcher.dispatch(url, method="PUT", access_token=self._access_token,
                                     access_token_secret=self._access_token_secret, json_body=True,
                                     **data)

  def delete(self, id):
    url = repository_branch_restrictions_by_id_url(self._namespace, self._repository_name, id)
    return self._dispatcher.dispatch(url, method="DELETE", access_token=self._access_token,
                                     access_token_secret=self._access_token_secret)

  def create(self, kind, pattern, users=None, groups=None, value=None):
    """ Create a variable for the current repository """
    users = [] if users is None else users
    groups = [] if groups is None else groups

    url = repository_branch_restrictions_url(self._namespace, self._repository_name)
    return self._dispatcher.dispatch(url, method="POST", access_token=self._access_token,
                                     access_token_secret=self._access_token_secret, json_body=True,
                                     kind=kind, pattern=pattern, users=users, groups=groups, value=value)