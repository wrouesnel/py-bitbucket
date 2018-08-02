_BASE_URL_V2 = 'https://api.bitbucket.org/2.0/%s'

def request_token_url():
  """ URL for getting a request token. """
  return _BASE_URL_V2 % 'oauth/request_token/'

def authenticate_url(token):
  """ URL for performing authentication on behalf of a user. """
  return _BASE_URL_V2 % ('oauth/authenticate?oauth_token=%s' % token)

def access_token_url():
  """ URL for exchanging a verifier for an access token. """
  return _BASE_URL_V2 % 'oauth/access_token/'

def current_user_url():
  """ URL for retrieving the current authorized user. """
  return _BASE_URL_V2 % 'user'

def repositories_url():
  """ URL for retrieving repositories """
  return _BASE_URL_V2 % 'repositories'

def repositories_for_namespace_url(namespace):
  """ URL for retrieving repositories """
  return _BASE_URL_V2 % 'repositories/%s' % namespace

def repository_for_namespace_url(namespace, repository):
  """ URL for repository """
  return _BASE_URL_V2 % ('repositories/%s/%s' %  (namespace, repository))

def repository_branches_url(namespace, repository):
  """ URL for retrieiving the branches under a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/branches' % (namespace, repository))

def repository_tags_url(namespace, repository):
  """ URL for retrieiving the tags under a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/tags' % (namespace, repository))

def repository_branches_tags_url(namespace, repository):
  """ URL for retrieiving the branches and tags under a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/branches-tags' % (namespace, repository))

def repository_manifest_url(namespace, repository, revision):
  """ URL for retrieving a manifest of a revision of a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/manifest/%s' % (namespace, repository, revision))

def repository_path_contents_url(namespace, repository, revision, path):
  """ Returns the contents of the path (file or directory) under a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/src/%s/%s' % (namespace, repository, revision, path))

def repository_path_raw_contents_url(namespace, repository, revision, path):
  """ Returns the contents of the path (file or directory) under a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/raw/%s/%s' % (namespace, repository, revision, path))

def repository_deploy_keys_url(namespace, repository):
  """ Returns the list of deploy keys in a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/deploy-keys' % (namespace, repository))

def repository_deploy_key_url(namespace, repository, key_id):
  """ Returns the contents of a deploy key under a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/deploy-keys/%s' % (namespace, repository, key_id))

def repository_links_url(namespace, repository):
  """ Returns the list of links in a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/links' % (namespace, repository))

def repository_link_url(namespace, repository, link_id):
  """ Returns the contents of a link under a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/links/%s' % (namespace, repository, link_id))

def repository_forks_url(namespace, repository):
  """ Returns the contents of a link under a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/forks' % (namespace, repository))

def repository_pipelines_config_url(namespace, repository):
  """ Returns the contents of a link under a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/pipelines_config' % (namespace, repository))

def repository_pipelines_config_variables_url(namespace, repository):
  """ Returns the contents of a link under a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/pipelines_config/variables/' % (namespace, repository))

def repository_pipelines_url(namespace, repository):
  """ Returns the contents of a link under a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/pipelines/' % (namespace, repository))

def repository_branch_restrictions_url(namespace, repository):
  """ Returns the branch permissions of a repository """
  return _BASE_URL_V2 % ('repositories/%s/%s/branch-restrictions/' % (namespace, repository))

def repository_branch_restrictions_by_id_url(namespace, repository, id):
  """ Returns the contents a branch restriction under a repository """
  return _BASE_URL_V2 % ('repositories/%s/%s/branch-restrictions/%s' % (namespace, repository, id))

def repository_pipelines_config_variables_variable_url(namespace, repository, uuid):
  """ Returns the contents of a link under a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/pipelines_config/variables/%s' % (namespace, repository, uuid))

def repository_main_branch_url(namespace, repository):
  """ Returns the name of the main branch for the repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/main-branch' % (namespace, repository))

def repository_changesets_url(namespace, repository):
  """ Returns the list of changesets in a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/changesets' % (namespace, repository))

def repository_changeset_url(namespace, repository, node_id):
  """ Returns the contents of a changeset under a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/changesets/%s' % (namespace, repository, node_id))

def account_profile_url(accountname):
  """ Returns the account profile information for the given account. """
  return _BASE_URL_V2 % ('users/%s' % accountname)

def repository_webhooks_url(namespace, repository):
  """ Returns the list of webhooks in a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/hooks' % (namespace, repository))

def repository_webhook_url(namespace, repository, service_id):
  """ Returns the contents of a webhook under a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/hooks/%s' % (namespace, repository, service_id))

def repository_branch_url(namespace, repository, branch_name):
  """ URL for retrieiving a specific branch under a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/refs/branches/%s' % (namespace, repository,
                                                                  branch_name))
def repository_tag_url(namespace, repository, tag_name):
  """ URL for retrieiving a specific tag under a repository. """
  return _BASE_URL_V2 % ('repositories/%s/%s/refs/tags/%s' % (namespace, repository, tag_name))

