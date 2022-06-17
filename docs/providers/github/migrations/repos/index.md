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
<tr><td><b>Name</b></td><td><code>github.migrations.repos</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.migrations.repos</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `git_tags_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `created_at` | `string` |  |
| `size` | `integer` |  |
| `issue_comment_url` | `string` |  |
| `svn_url` | `string` |  |
| `events_url` | `string` |  |
| `statuses_url` | `string` |  |
| `milestones_url` | `string` |  |
| `owner` | `object` | Simple User |
| `html_url` | `string` |  |
| `tags_url` | `string` |  |
| `updated_at` | `string` |  |
| `open_issues_count` | `integer` |  |
| `subscription_url` | `string` |  |
| `forks_url` | `string` |  |
| `topics` | `array` |  |
| `node_id` | `string` |  |
| `assignees_url` | `string` |  |
| `contributors_url` | `string` |  |
| `pushed_at` | `string` |  |
| `has_pages` | `boolean` |  |
| `watchers` | `integer` |  |
| `deployments_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `forks_count` | `integer` |  |
| `commits_url` | `string` |  |
| `languages_url` | `string` |  |
| `hooks_url` | `string` |  |
| `contents_url` | `string` |  |
| `license` | `object` |  |
| `network_count` | `integer` |  |
| `url` | `string` |  |
| `role_name` | `string` |  |
| `downloads_url` | `string` |  |
| `full_name` | `string` |  |
| `subscribers_count` | `integer` |  |
| `clone_url` | `string` |  |
| `visibility` | `string` |  |
| `compare_url` | `string` |  |
| `archive_url` | `string` |  |
| `disabled` | `boolean` |  |
| `template_repository` | `object` | A git repository |
| `comments_url` | `string` |  |
| `permissions` | `object` |  |
| `teams_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `pulls_url` | `string` |  |
| `archived` | `boolean` |  |
| `stargazers_count` | `integer` |  |
| `git_refs_url` | `string` |  |
| `notifications_url` | `string` |  |
| `releases_url` | `string` |  |
| `ssh_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `git_url` | `string` |  |
| `issues_url` | `string` |  |
| `is_template` | `boolean` |  |
| `private` | `boolean` |  |
| `keys_url` | `string` |  |
| `fork` | `boolean` |  |
| `has_issues` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `branches_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `merges_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `trees_url` | `string` |  |
| `labels_url` | `string` |  |
| `homepage` | `string` |  |
| `language` | `string` |  |
| `blobs_url` | `string` |  |
| `default_branch` | `string` |  |
| `watchers_count` | `integer` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `allow_forking` | `boolean` |  |
| `mirror_url` | `string` |  |
| `open_issues` | `integer` |  |
| `forks` | `integer` |  |
| `has_downloads` | `boolean` |  |
| `git_commits_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_repos_for_authenticated_user` | `migration_id` | Lists all the repositories for this user migration. | SELECT |
| `list_repos_for_org` | `migration_id, org` | List all the repositories for this organization migration. | SELECT |
| `unlock_repo_for_authenticated_user` | `migration_id, repo_name` | Unlocks a repository. You can lock repositories when you [start a user migration](https://docs.github.com/rest/reference/migrations#start-a-user-migration). Once the migration is complete you can unlock each repository to begin using it again or [delete the repository](https://docs.github.com/rest/reference/repos#delete-a-repository) if you no longer need the source data. Returns a status of `404 Not Found` if the repository is not locked. | EXEC |
| `unlock_repo_for_org` | `migration_id, org, repo_name` | Unlocks a repository that was locked for migration. You should unlock each migrated repository and [delete them](https://docs.github.com/rest/reference/repos#delete-a-repository) when the migration is complete and you no longer need the source data. | EXEC |
