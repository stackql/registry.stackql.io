---
title: legacy_repos
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>github.teams.legacy_repos</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.legacy_repos</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `milestones_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `private` | `boolean` |  |
| `fork` | `boolean` |  |
| `html_url` | `string` |  |
| `trees_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `language` | `string` |  |
| `svn_url` | `string` |  |
| `node_id` | `string` |  |
| `permissions` | `object` |  |
| `archive_url` | `string` |  |
| `default_branch` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `is_template` | `boolean` |  |
| `has_downloads` | `boolean` |  |
| `git_url` | `string` |  |
| `keys_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `notifications_url` | `string` |  |
| `teams_url` | `string` |  |
| `mirror_url` | `string` |  |
| `open_issues` | `integer` |  |
| `full_name` | `string` |  |
| `topics` | `array` |  |
| `has_wiki` | `boolean` |  |
| `comments_url` | `string` |  |
| `commits_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `license` | `object` |  |
| `subscribers_count` | `integer` |  |
| `compare_url` | `string` |  |
| `deployments_url` | `string` |  |
| `releases_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `contributors_url` | `string` |  |
| `url` | `string` |  |
| `forks_url` | `string` |  |
| `visibility` | `string` |  |
| `subscription_url` | `string` |  |
| `tags_url` | `string` |  |
| `contents_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `watchers` | `integer` |  |
| `size` | `integer` |  |
| `clone_url` | `string` |  |
| `downloads_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `events_url` | `string` |  |
| `pulls_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `homepage` | `string` |  |
| `languages_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `watchers_count` | `integer` |  |
| `hooks_url` | `string` |  |
| `forks_count` | `integer` |  |
| `stargazers_url` | `string` |  |
| `role_name` | `string` |  |
| `owner` | `object` | Simple User |
| `forks` | `integer` |  |
| `created_at` | `string` |  |
| `archived` | `boolean` |  |
| `updated_at` | `string` |  |
| `labels_url` | `string` |  |
| `merges_url` | `string` |  |
| `statuses_url` | `string` |  |
| `blobs_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `open_issues_count` | `integer` |  |
| `ssh_url` | `string` |  |
| `branches_url` | `string` |  |
| `issues_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `network_count` | `integer` |  |
| `disabled` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `assignees_url` | `string` |  |
| `pushed_at` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_repos_legacy` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [List team repositories](https://docs.github.com/rest/reference/teams#list-team-repositories) endpoint. | SELECT |
| `remove_repo_legacy` | `owner, repo, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a repository from a team](https://docs.github.com/rest/reference/teams#remove-a-repository-from-a-team) endpoint.<br /><br />If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. NOTE: This does not delete the repository, it just removes it from the team. | DELETE |
| `add_or_update_repo_permissions_legacy` | `owner, repo, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new "[Add or update team repository permissions](https://docs.github.com/rest/reference/teams#add-or-update-team-repository-permissions)" endpoint.<br /><br />To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization.<br /><br />Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." | EXEC |
| `check_permissions_for_repo_legacy` | `owner, repo, team_id` | **Note**: Repositories inherited through a parent team will also be checked.<br /><br />**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a repository](https://docs.github.com/rest/reference/teams#check-team-permissions-for-a-repository) endpoint.<br /><br />You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: | EXEC |
