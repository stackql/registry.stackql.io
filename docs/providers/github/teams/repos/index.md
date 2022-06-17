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
<tr><td><b>Name</b></td><td><code>github.teams.repos</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.repos</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `svn_url` | `string` |  |
| `full_name` | `string` |  |
| `assignees_url` | `string` |  |
| `languages_url` | `string` |  |
| `compare_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `archived` | `boolean` |  |
| `ssh_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `has_pages` | `boolean` |  |
| `role_name` | `string` |  |
| `statuses_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `html_url` | `string` |  |
| `homepage` | `string` |  |
| `pushed_at` | `string` |  |
| `labels_url` | `string` |  |
| `teams_url` | `string` |  |
| `default_branch` | `string` |  |
| `has_downloads` | `boolean` |  |
| `releases_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `deployments_url` | `string` |  |
| `blobs_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `pulls_url` | `string` |  |
| `issues_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `topics` | `array` |  |
| `open_issues_count` | `integer` |  |
| `private` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `keys_url` | `string` |  |
| `milestones_url` | `string` |  |
| `size` | `integer` |  |
| `url` | `string` |  |
| `is_template` | `boolean` |  |
| `downloads_url` | `string` |  |
| `contributors_url` | `string` |  |
| `subscription_url` | `string` |  |
| `forks` | `integer` |  |
| `has_issues` | `boolean` |  |
| `git_url` | `string` |  |
| `disabled` | `boolean` |  |
| `branches_url` | `string` |  |
| `forks_count` | `integer` |  |
| `open_issues` | `integer` |  |
| `forks_url` | `string` |  |
| `permissions` | `object` |  |
| `fork` | `boolean` |  |
| `owner` | `object` | Simple User |
| `created_at` | `string` |  |
| `template_repository` | `object` | A git repository |
| `git_tags_url` | `string` |  |
| `comments_url` | `string` |  |
| `commits_url` | `string` |  |
| `notifications_url` | `string` |  |
| `merges_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `node_id` | `string` |  |
| `events_url` | `string` |  |
| `mirror_url` | `string` |  |
| `archive_url` | `string` |  |
| `network_count` | `integer` |  |
| `subscribers_count` | `integer` |  |
| `watchers` | `integer` |  |
| `language` | `string` |  |
| `trees_url` | `string` |  |
| `visibility` | `string` |  |
| `license` | `object` |  |
| `contents_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `hooks_url` | `string` |  |
| `clone_url` | `string` |  |
| `updated_at` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `watchers_count` | `integer` |  |
| `tags_url` | `string` |  |
| `stargazers_count` | `integer` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_repos_in_org` | `org, team_slug` | Lists a team's repositories visible to the authenticated user.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/repos`. | SELECT |
| `add_or_update_repo_permissions_in_org` | `org, owner, repo, team_slug` | To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization. Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)."<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.<br /><br />For more information about the permission levels, see "[Repository permission levels for an organization](https://docs.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)". | INSERT |
| `remove_repo_in_org` | `org, owner, repo, team_slug` | If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. This does not delete the repository, it just removes it from the team.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`. | DELETE |
| `check_permissions_for_repo_in_org` | `org, owner, repo, team_slug` | Checks whether a team has `admin`, `push`, `maintain`, `triage`, or `pull` permission for a repository. Repositories inherited through a parent team will also be checked.<br /><br />You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `application/vnd.github.v3.repository+json` accept header.<br /><br />If a team doesn't have permission for the repository, you will receive a `404 Not Found` response status.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`. | EXEC |
