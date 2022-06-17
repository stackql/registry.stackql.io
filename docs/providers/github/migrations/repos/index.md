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
| `subscription_url` | `string` |  |
| `contents_url` | `string` |  |
| `full_name` | `string` |  |
| `language` | `string` |  |
| `open_issues` | `integer` |  |
| `pushed_at` | `string` |  |
| `commits_url` | `string` |  |
| `statuses_url` | `string` |  |
| `created_at` | `string` |  |
| `subscribers_count` | `integer` |  |
| `permissions` | `object` |  |
| `allow_forking` | `boolean` |  |
| `labels_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `topics` | `array` |  |
| `url` | `string` |  |
| `contributors_url` | `string` |  |
| `releases_url` | `string` |  |
| `events_url` | `string` |  |
| `hooks_url` | `string` |  |
| `role_name` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `updated_at` | `string` |  |
| `git_tags_url` | `string` |  |
| `tags_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `clone_url` | `string` |  |
| `milestones_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `compare_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `open_issues_count` | `integer` |  |
| `forks_url` | `string` |  |
| `license` | `object` |  |
| `subscribers_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `languages_url` | `string` |  |
| `node_id` | `string` |  |
| `size` | `integer` |  |
| `has_projects` | `boolean` |  |
| `merges_url` | `string` |  |
| `visibility` | `string` |  |
| `has_wiki` | `boolean` |  |
| `svn_url` | `string` |  |
| `owner` | `object` | Simple User |
| `html_url` | `string` |  |
| `archived` | `boolean` |  |
| `stargazers_url` | `string` |  |
| `blobs_url` | `string` |  |
| `pulls_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `forks_count` | `integer` |  |
| `forks` | `integer` |  |
| `private` | `boolean` |  |
| `branches_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `issue_comment_url` | `string` |  |
| `network_count` | `integer` |  |
| `trees_url` | `string` |  |
| `fork` | `boolean` |  |
| `disabled` | `boolean` |  |
| `ssh_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `notifications_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `deployments_url` | `string` |  |
| `default_branch` | `string` |  |
| `mirror_url` | `string` |  |
| `comments_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `issues_url` | `string` |  |
| `git_url` | `string` |  |
| `downloads_url` | `string` |  |
| `is_template` | `boolean` |  |
| `teams_url` | `string` |  |
| `homepage` | `string` |  |
| `watchers` | `integer` |  |
| `keys_url` | `string` |  |
| `assignees_url` | `string` |  |
| `archive_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `git_commits_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_repos_for_authenticated_user` | `SELECT` | `migration_id` | Lists all the repositories for this user migration. |
| `list_repos_for_org` | `SELECT` | `migration_id, org` | List all the repositories for this organization migration. |
| `unlock_repo_for_authenticated_user` | `EXEC` | `migration_id, repo_name` | Unlocks a repository. You can lock repositories when you [start a user migration](https://docs.github.com/rest/reference/migrations#start-a-user-migration). Once the migration is complete you can unlock each repository to begin using it again or [delete the repository](https://docs.github.com/rest/reference/repos#delete-a-repository) if you no longer need the source data. Returns a status of `404 Not Found` if the repository is not locked. |
| `unlock_repo_for_org` | `EXEC` | `migration_id, org, repo_name` | Unlocks a repository that was locked for migration. You should unlock each migrated repository and [delete them](https://docs.github.com/rest/reference/repos#delete-a-repository) when the migration is complete and you no longer need the source data. |
