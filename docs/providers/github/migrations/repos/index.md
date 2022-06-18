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
<tr><td><b>Id</b></td><td><code>github.migrations.repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `mirror_url` | `string` |  |
| `languages_url` | `string` |  |
| `size` | `integer` |  |
| `open_issues_count` | `integer` |  |
| `clone_url` | `string` |  |
| `fork` | `boolean` |  |
| `git_refs_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `svn_url` | `string` |  |
| `owner` | `object` | Simple User |
| `pulls_url` | `string` |  |
| `downloads_url` | `string` |  |
| `pushed_at` | `string` |  |
| `contents_url` | `string` |  |
| `assignees_url` | `string` |  |
| `blobs_url` | `string` |  |
| `teams_url` | `string` |  |
| `deployments_url` | `string` |  |
| `hooks_url` | `string` |  |
| `releases_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `watchers_count` | `integer` |  |
| `milestones_url` | `string` |  |
| `commits_url` | `string` |  |
| `subscription_url` | `string` |  |
| `created_at` | `string` |  |
| `private` | `boolean` |  |
| `statuses_url` | `string` |  |
| `permissions` | `object` |  |
| `comments_url` | `string` |  |
| `node_id` | `string` |  |
| `url` | `string` |  |
| `labels_url` | `string` |  |
| `open_issues` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `html_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `updated_at` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `visibility` | `string` |  |
| `contributors_url` | `string` |  |
| `issues_url` | `string` |  |
| `archived` | `boolean` |  |
| `trees_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `topics` | `array` |  |
| `keys_url` | `string` |  |
| `homepage` | `string` |  |
| `disabled` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `watchers` | `integer` |  |
| `stargazers_count` | `integer` |  |
| `forks_count` | `integer` |  |
| `events_url` | `string` |  |
| `language` | `string` |  |
| `forks_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `role_name` | `string` |  |
| `has_issues` | `boolean` |  |
| `merges_url` | `string` |  |
| `notifications_url` | `string` |  |
| `default_branch` | `string` |  |
| `license` | `object` |  |
| `issue_events_url` | `string` |  |
| `is_template` | `boolean` |  |
| `template_repository` | `object` | A git repository |
| `tags_url` | `string` |  |
| `ssh_url` | `string` |  |
| `forks` | `integer` |  |
| `network_count` | `integer` |  |
| `compare_url` | `string` |  |
| `full_name` | `string` |  |
| `temp_clone_token` | `string` |  |
| `branches_url` | `string` |  |
| `git_url` | `string` |  |
| `archive_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_repos_for_authenticated_user` | `SELECT` | `migration_id` | Lists all the repositories for this user migration. |
| `list_repos_for_org` | `SELECT` | `migration_id, org` | List all the repositories for this organization migration. |
| `unlock_repo_for_authenticated_user` | `EXEC` | `migration_id, repo_name` | Unlocks a repository. You can lock repositories when you [start a user migration](https://docs.github.com/rest/reference/migrations#start-a-user-migration). Once the migration is complete you can unlock each repository to begin using it again or [delete the repository](https://docs.github.com/rest/reference/repos#delete-a-repository) if you no longer need the source data. Returns a status of `404 Not Found` if the repository is not locked. |
| `unlock_repo_for_org` | `EXEC` | `migration_id, org, repo_name` | Unlocks a repository that was locked for migration. You should unlock each migrated repository and [delete them](https://docs.github.com/rest/reference/repos#delete-a-repository) when the migration is complete and you no longer need the source data. |
