---
title: repos
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
<tr><td><b>Name</b></td><td><code>repos</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `hooks_url` | `string` |  |
| `fork` | `boolean` |  |
| `language` | `string` |  |
| `allow_forking` | `boolean` |  |
| `stargazers_count` | `integer` |  |
| `issue_events_url` | `string` |  |
| `is_template` | `boolean` |  |
| `mirror_url` | `string` |  |
| `notifications_url` | `string` |  |
| `svn_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `forks_count` | `integer` |  |
| `events_url` | `string` |  |
| `statuses_url` | `string` |  |
| `git_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `forks` | `integer` |  |
| `open_issues_count` | `integer` |  |
| `deployments_url` | `string` |  |
| `default_branch` | `string` |  |
| `blobs_url` | `string` |  |
| `keys_url` | `string` |  |
| `archive_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `milestones_url` | `string` |  |
| `visibility` | `string` |  |
| `html_url` | `string` |  |
| `branches_url` | `string` |  |
| `watchers` | `integer` |  |
| `comments_url` | `string` |  |
| `size` | `integer` |  |
| `updated_at` | `string` |  |
| `network_count` | `integer` |  |
| `open_issues` | `integer` |  |
| `watchers_count` | `integer` |  |
| `issue_comment_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `temp_clone_token` | `string` |  |
| `labels_url` | `string` |  |
| `clone_url` | `string` |  |
| `forks_url` | `string` |  |
| `homepage` | `string` |  |
| `teams_url` | `string` |  |
| `languages_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `commits_url` | `string` |  |
| `ssh_url` | `string` |  |
| `pushed_at` | `string` |  |
| `has_issues` | `boolean` |  |
| `topics` | `array` |  |
| `permissions` | `object` |  |
| `contents_url` | `string` |  |
| `downloads_url` | `string` |  |
| `trees_url` | `string` |  |
| `disabled` | `boolean` |  |
| `pulls_url` | `string` |  |
| `assignees_url` | `string` |  |
| `private` | `boolean` |  |
| `compare_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `node_id` | `string` |  |
| `merges_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `has_wiki` | `boolean` |  |
| `created_at` | `string` |  |
| `tags_url` | `string` |  |
| `archived` | `boolean` |  |
| `role_name` | `string` |  |
| `full_name` | `string` |  |
| `contributors_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `url` | `string` |  |
| `license` | `object` |  |
| `template_repository` | `object` | A git repository |
| `issues_url` | `string` |  |
| `owner` | `object` | Simple User |
| `git_refs_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `has_projects` | `boolean` |  |
| `releases_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `subscription_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_repos_in_org` | `SELECT` | `org, team_slug` | Lists a team's repositories visible to the authenticated user.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/repos`. |
| `add_or_update_repo_permissions_in_org` | `INSERT` | `org, owner, repo, team_slug` | To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization. Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)."<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.<br /><br />For more information about the permission levels, see "[Repository permission levels for an organization](https://docs.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)". |
| `remove_repo_in_org` | `DELETE` | `org, owner, repo, team_slug` | If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. This does not delete the repository, it just removes it from the team.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`. |
| `check_permissions_for_repo_in_org` | `EXEC` | `org, owner, repo, team_slug` | Checks whether a team has `admin`, `push`, `maintain`, `triage`, or `pull` permission for a repository. Repositories inherited through a parent team will also be checked.<br /><br />You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `application/vnd.github.v3.repository+json` accept header.<br /><br />If a team doesn't have permission for the repository, you will receive a `404 Not Found` response status.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`. |
