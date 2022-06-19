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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.legacy_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `merges_url` | `string` |  |
| `permissions` | `object` |  |
| `git_refs_url` | `string` |  |
| `owner` | `object` | Simple User |
| `deployments_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `pushed_at` | `string` |  |
| `issues_url` | `string` |  |
| `open_issues` | `integer` |  |
| `subscribers_count` | `integer` |  |
| `mirror_url` | `string` |  |
| `statuses_url` | `string` |  |
| `compare_url` | `string` |  |
| `watchers` | `integer` |  |
| `temp_clone_token` | `string` |  |
| `milestones_url` | `string` |  |
| `languages_url` | `string` |  |
| `pulls_url` | `string` |  |
| `fork` | `boolean` |  |
| `url` | `string` |  |
| `trees_url` | `string` |  |
| `tags_url` | `string` |  |
| `network_count` | `integer` |  |
| `stargazers_url` | `string` |  |
| `assignees_url` | `string` |  |
| `topics` | `array` |  |
| `comments_url` | `string` |  |
| `downloads_url` | `string` |  |
| `visibility` | `string` |  |
| `open_issues_count` | `integer` |  |
| `disabled` | `boolean` |  |
| `full_name` | `string` |  |
| `has_pages` | `boolean` |  |
| `hooks_url` | `string` |  |
| `notifications_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `clone_url` | `string` |  |
| `contributors_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `default_branch` | `string` |  |
| `labels_url` | `string` |  |
| `updated_at` | `string` |  |
| `subscription_url` | `string` |  |
| `contents_url` | `string` |  |
| `license` | `object` |  |
| `forks` | `integer` |  |
| `has_issues` | `boolean` |  |
| `is_template` | `boolean` |  |
| `html_url` | `string` |  |
| `ssh_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `forks_url` | `string` |  |
| `private` | `boolean` |  |
| `homepage` | `string` |  |
| `svn_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `forks_count` | `integer` |  |
| `watchers_count` | `integer` |  |
| `keys_url` | `string` |  |
| `language` | `string` |  |
| `git_url` | `string` |  |
| `node_id` | `string` |  |
| `blobs_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `archived` | `boolean` |  |
| `template_repository` | `object` | A git repository |
| `size` | `integer` |  |
| `branches_url` | `string` |  |
| `role_name` | `string` |  |
| `teams_url` | `string` |  |
| `created_at` | `string` |  |
| `has_wiki` | `boolean` |  |
| `commits_url` | `string` |  |
| `events_url` | `string` |  |
| `archive_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `releases_url` | `string` |  |
| `has_downloads` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_repos_legacy` | `SELECT` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [List team repositories](https://docs.github.com/rest/reference/teams#list-team-repositories) endpoint. |
| `remove_repo_legacy` | `DELETE` | `owner, repo, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a repository from a team](https://docs.github.com/rest/reference/teams#remove-a-repository-from-a-team) endpoint.<br /><br />If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. NOTE: This does not delete the repository, it just removes it from the team. |
| `add_or_update_repo_permissions_legacy` | `EXEC` | `owner, repo, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new "[Add or update team repository permissions](https://docs.github.com/rest/reference/teams#add-or-update-team-repository-permissions)" endpoint.<br /><br />To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization.<br /><br />Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `check_permissions_for_repo_legacy` | `EXEC` | `owner, repo, team_id` | **Note**: Repositories inherited through a parent team will also be checked.<br /><br />**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a repository](https://docs.github.com/rest/reference/teams#check-team-permissions-for-a-repository) endpoint.<br /><br />You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
