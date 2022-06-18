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
| `subscribers_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `open_issues` | `integer` |  |
| `commits_url` | `string` |  |
| `downloads_url` | `string` |  |
| `hooks_url` | `string` |  |
| `assignees_url` | `string` |  |
| `archived` | `boolean` |  |
| `archive_url` | `string` |  |
| `subscription_url` | `string` |  |
| `fork` | `boolean` |  |
| `open_issues_count` | `integer` |  |
| `subscribers_count` | `integer` |  |
| `contents_url` | `string` |  |
| `clone_url` | `string` |  |
| `comments_url` | `string` |  |
| `keys_url` | `string` |  |
| `url` | `string` |  |
| `homepage` | `string` |  |
| `git_refs_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `full_name` | `string` |  |
| `has_pages` | `boolean` |  |
| `mirror_url` | `string` |  |
| `license` | `object` |  |
| `forks_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `is_template` | `boolean` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `milestones_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `role_name` | `string` |  |
| `default_branch` | `string` |  |
| `git_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `statuses_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `pulls_url` | `string` |  |
| `private` | `boolean` |  |
| `owner` | `object` | Simple User |
| `has_issues` | `boolean` |  |
| `git_tags_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `releases_url` | `string` |  |
| `permissions` | `object` |  |
| `deployments_url` | `string` |  |
| `node_id` | `string` |  |
| `forks` | `integer` |  |
| `svn_url` | `string` |  |
| `watchers` | `integer` |  |
| `branches_url` | `string` |  |
| `ssh_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `merges_url` | `string` |  |
| `visibility` | `string` |  |
| `disabled` | `boolean` |  |
| `created_at` | `string` |  |
| `updated_at` | `string` |  |
| `network_count` | `integer` |  |
| `trees_url` | `string` |  |
| `labels_url` | `string` |  |
| `languages_url` | `string` |  |
| `notifications_url` | `string` |  |
| `forks_count` | `integer` |  |
| `size` | `integer` |  |
| `git_commits_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `topics` | `array` |  |
| `pushed_at` | `string` |  |
| `teams_url` | `string` |  |
| `tags_url` | `string` |  |
| `html_url` | `string` |  |
| `issues_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `compare_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `language` | `string` |  |
| `events_url` | `string` |  |
| `blobs_url` | `string` |  |
| `contributors_url` | `string` |  |
| `stargazers_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_repos_for_authenticated_user` | `SELECT` | `migration_id` | Lists all the repositories for this user migration. |
| `list_repos_for_org` | `SELECT` | `migration_id, org` | List all the repositories for this organization migration. |
| `unlock_repo_for_authenticated_user` | `EXEC` | `migration_id, repo_name` | Unlocks a repository. You can lock repositories when you [start a user migration](https://docs.github.com/rest/reference/migrations#start-a-user-migration). Once the migration is complete you can unlock each repository to begin using it again or [delete the repository](https://docs.github.com/rest/reference/repos#delete-a-repository) if you no longer need the source data. Returns a status of `404 Not Found` if the repository is not locked. |
| `unlock_repo_for_org` | `EXEC` | `migration_id, org, repo_name` | Unlocks a repository that was locked for migration. You should unlock each migrated repository and [delete them](https://docs.github.com/rest/reference/repos#delete-a-repository) when the migration is complete and you no longer need the source data. |
