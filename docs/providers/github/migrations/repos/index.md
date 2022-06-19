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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.migrations.repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `notifications_url` | `string` |  |
| `commits_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `git_refs_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `language` | `string` |  |
| `network_count` | `integer` |  |
| `trees_url` | `string` |  |
| `pulls_url` | `string` |  |
| `topics` | `array` |  |
| `issue_comment_url` | `string` |  |
| `forks` | `integer` |  |
| `stargazers_url` | `string` |  |
| `html_url` | `string` |  |
| `mirror_url` | `string` |  |
| `git_url` | `string` |  |
| `is_template` | `boolean` |  |
| `contributors_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `template_repository` | `object` | A git repository |
| `homepage` | `string` |  |
| `merges_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `visibility` | `string` |  |
| `disabled` | `boolean` |  |
| `statuses_url` | `string` |  |
| `fork` | `boolean` |  |
| `stargazers_count` | `integer` |  |
| `labels_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `assignees_url` | `string` |  |
| `comments_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `default_branch` | `string` |  |
| `full_name` | `string` |  |
| `issue_events_url` | `string` |  |
| `clone_url` | `string` |  |
| `pushed_at` | `string` |  |
| `downloads_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `languages_url` | `string` |  |
| `watchers` | `integer` |  |
| `keys_url` | `string` |  |
| `compare_url` | `string` |  |
| `hooks_url` | `string` |  |
| `ssh_url` | `string` |  |
| `updated_at` | `string` |  |
| `url` | `string` |  |
| `has_pages` | `boolean` |  |
| `node_id` | `string` |  |
| `owner` | `object` | Simple User |
| `subscription_url` | `string` |  |
| `archive_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `contents_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `events_url` | `string` |  |
| `milestones_url` | `string` |  |
| `svn_url` | `string` |  |
| `created_at` | `string` |  |
| `private` | `boolean` |  |
| `branches_url` | `string` |  |
| `issues_url` | `string` |  |
| `archived` | `boolean` |  |
| `teams_url` | `string` |  |
| `role_name` | `string` |  |
| `license` | `object` |  |
| `open_issues` | `integer` |  |
| `watchers_count` | `integer` |  |
| `forks_count` | `integer` |  |
| `releases_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `size` | `integer` |  |
| `permissions` | `object` |  |
| `tags_url` | `string` |  |
| `blobs_url` | `string` |  |
| `deployments_url` | `string` |  |
| `forks_url` | `string` |  |
| `has_issues` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_repos_for_authenticated_user` | `SELECT` | `migration_id` | Lists all the repositories for this user migration. |
| `list_repos_for_org` | `SELECT` | `migration_id, org` | List all the repositories for this organization migration. |
| `unlock_repo_for_authenticated_user` | `EXEC` | `migration_id, repo_name` | Unlocks a repository. You can lock repositories when you [start a user migration](https://docs.github.com/rest/reference/migrations#start-a-user-migration). Once the migration is complete you can unlock each repository to begin using it again or [delete the repository](https://docs.github.com/rest/reference/repos#delete-a-repository) if you no longer need the source data. Returns a status of `404 Not Found` if the repository is not locked. |
| `unlock_repo_for_org` | `EXEC` | `migration_id, org, repo_name` | Unlocks a repository that was locked for migration. You should unlock each migrated repository and [delete them](https://docs.github.com/rest/reference/repos#delete-a-repository) when the migration is complete and you no longer need the source data. |
