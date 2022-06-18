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
<tr><td><b>Name</b></td><td><code>legacy_repos</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.legacy_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `blobs_url` | `string` |  |
| `network_count` | `integer` |  |
| `git_tags_url` | `string` |  |
| `releases_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `language` | `string` |  |
| `temp_clone_token` | `string` |  |
| `clone_url` | `string` |  |
| `statuses_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `role_name` | `string` |  |
| `homepage` | `string` |  |
| `forks_count` | `integer` |  |
| `tags_url` | `string` |  |
| `subscription_url` | `string` |  |
| `mirror_url` | `string` |  |
| `deployments_url` | `string` |  |
| `languages_url` | `string` |  |
| `pushed_at` | `string` |  |
| `hooks_url` | `string` |  |
| `keys_url` | `string` |  |
| `contents_url` | `string` |  |
| `owner` | `object` | Simple User |
| `stargazers_count` | `integer` |  |
| `has_projects` | `boolean` |  |
| `updated_at` | `string` |  |
| `downloads_url` | `string` |  |
| `default_branch` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `git_refs_url` | `string` |  |
| `git_url` | `string` |  |
| `archive_url` | `string` |  |
| `visibility` | `string` |  |
| `forks_url` | `string` |  |
| `trees_url` | `string` |  |
| `forks` | `integer` |  |
| `created_at` | `string` |  |
| `labels_url` | `string` |  |
| `watchers` | `integer` |  |
| `svn_url` | `string` |  |
| `license` | `object` |  |
| `subscribers_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `node_id` | `string` |  |
| `teams_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `is_template` | `boolean` |  |
| `disabled` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `compare_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `private` | `boolean` |  |
| `template_repository` | `object` | A git repository |
| `stargazers_url` | `string` |  |
| `milestones_url` | `string` |  |
| `assignees_url` | `string` |  |
| `archived` | `boolean` |  |
| `comments_url` | `string` |  |
| `open_issues` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `html_url` | `string` |  |
| `issues_url` | `string` |  |
| `topics` | `array` |  |
| `collaborators_url` | `string` |  |
| `url` | `string` |  |
| `branches_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `full_name` | `string` |  |
| `commits_url` | `string` |  |
| `contributors_url` | `string` |  |
| `fork` | `boolean` |  |
| `events_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `notifications_url` | `string` |  |
| `ssh_url` | `string` |  |
| `size` | `integer` |  |
| `pulls_url` | `string` |  |
| `merges_url` | `string` |  |
| `permissions` | `object` |  |
| `git_commits_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `issue_events_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_repos_legacy` | `SELECT` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [List team repositories](https://docs.github.com/rest/reference/teams#list-team-repositories) endpoint. |
| `remove_repo_legacy` | `DELETE` | `owner, repo, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a repository from a team](https://docs.github.com/rest/reference/teams#remove-a-repository-from-a-team) endpoint.<br /><br />If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. NOTE: This does not delete the repository, it just removes it from the team. |
| `add_or_update_repo_permissions_legacy` | `EXEC` | `owner, repo, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new "[Add or update team repository permissions](https://docs.github.com/rest/reference/teams#add-or-update-team-repository-permissions)" endpoint.<br /><br />To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization.<br /><br />Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `check_permissions_for_repo_legacy` | `EXEC` | `owner, repo, team_id` | **Note**: Repositories inherited through a parent team will also be checked.<br /><br />**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a repository](https://docs.github.com/rest/reference/teams#check-team-permissions-for-a-repository) endpoint.<br /><br />You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
