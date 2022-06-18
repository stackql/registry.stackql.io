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
| `archived` | `boolean` |  |
| `temp_clone_token` | `string` |  |
| `fork` | `boolean` |  |
| `tags_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `homepage` | `string` |  |
| `size` | `integer` |  |
| `subscription_url` | `string` |  |
| `teams_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `pushed_at` | `string` |  |
| `comments_url` | `string` |  |
| `default_branch` | `string` |  |
| `git_url` | `string` |  |
| `forks_url` | `string` |  |
| `full_name` | `string` |  |
| `clone_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `stargazers_count` | `integer` |  |
| `watchers` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `owner` | `object` | Simple User |
| `svn_url` | `string` |  |
| `assignees_url` | `string` |  |
| `downloads_url` | `string` |  |
| `ssh_url` | `string` |  |
| `languages_url` | `string` |  |
| `forks_count` | `integer` |  |
| `releases_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `events_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `html_url` | `string` |  |
| `node_id` | `string` |  |
| `mirror_url` | `string` |  |
| `permissions` | `object` |  |
| `git_commits_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `merges_url` | `string` |  |
| `trees_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `notifications_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `forks` | `integer` |  |
| `contents_url` | `string` |  |
| `keys_url` | `string` |  |
| `visibility` | `string` |  |
| `open_issues_count` | `integer` |  |
| `stargazers_url` | `string` |  |
| `role_name` | `string` |  |
| `template_repository` | `object` | A git repository |
| `git_refs_url` | `string` |  |
| `created_at` | `string` |  |
| `open_issues` | `integer` |  |
| `has_issues` | `boolean` |  |
| `hooks_url` | `string` |  |
| `labels_url` | `string` |  |
| `compare_url` | `string` |  |
| `private` | `boolean` |  |
| `topics` | `array` |  |
| `blobs_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `pulls_url` | `string` |  |
| `milestones_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `is_template` | `boolean` |  |
| `language` | `string` |  |
| `issue_comment_url` | `string` |  |
| `updated_at` | `string` |  |
| `license` | `object` |  |
| `url` | `string` |  |
| `has_projects` | `boolean` |  |
| `deployments_url` | `string` |  |
| `network_count` | `integer` |  |
| `branches_url` | `string` |  |
| `statuses_url` | `string` |  |
| `archive_url` | `string` |  |
| `disabled` | `boolean` |  |
| `contributors_url` | `string` |  |
| `commits_url` | `string` |  |
| `issues_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_repos_for_authenticated_user` | `SELECT` | `migration_id` | Lists all the repositories for this user migration. |
| `list_repos_for_org` | `SELECT` | `migration_id, org` | List all the repositories for this organization migration. |
| `unlock_repo_for_authenticated_user` | `EXEC` | `migration_id, repo_name` | Unlocks a repository. You can lock repositories when you [start a user migration](https://docs.github.com/rest/reference/migrations#start-a-user-migration). Once the migration is complete you can unlock each repository to begin using it again or [delete the repository](https://docs.github.com/rest/reference/repos#delete-a-repository) if you no longer need the source data. Returns a status of `404 Not Found` if the repository is not locked. |
| `unlock_repo_for_org` | `EXEC` | `migration_id, org, repo_name` | Unlocks a repository that was locked for migration. You should unlock each migrated repository and [delete them](https://docs.github.com/rest/reference/repos#delete-a-repository) when the migration is complete and you no longer need the source data. |
