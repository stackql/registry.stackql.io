---
title: watched_repos
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
<tr><td><b>Name</b></td><td><code>watched_repos</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.watched_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `ssh_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `branches_url` | `string` |  |
| `created_at` | `string` |  |
| `open_issues` | `integer` |  |
| `git_tags_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `git_refs_url` | `string` |  |
| `merges_url` | `string` |  |
| `svn_url` | `string` |  |
| `milestones_url` | `string` |  |
| `forks_count` | `integer` |  |
| `compare_url` | `string` |  |
| `permissions` | `object` |  |
| `archive_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `is_template` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `comments_url` | `string` |  |
| `contents_url` | `string` |  |
| `tags_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `deployments_url` | `string` |  |
| `pulls_url` | `string` |  |
| `pushed_at` | `string` |  |
| `has_issues` | `boolean` |  |
| `fork` | `boolean` |  |
| `trees_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `forks_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `archived` | `boolean` |  |
| `statuses_url` | `string` |  |
| `full_name` | `string` |  |
| `forks` | `integer` |  |
| `temp_clone_token` | `string` |  |
| `git_url` | `string` |  |
| `blobs_url` | `string` |  |
| `private` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `languages_url` | `string` |  |
| `teams_url` | `string` |  |
| `keys_url` | `string` |  |
| `mirror_url` | `string` |  |
| `license` | `object` |  |
| `size` | `integer` |  |
| `node_id` | `string` |  |
| `owner` | `object` | Simple User |
| `topics` | `array` |  |
| `subscription_url` | `string` |  |
| `updated_at` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `network_count` | `integer` |  |
| `subscribers_count` | `integer` |  |
| `disabled` | `boolean` |  |
| `releases_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `labels_url` | `string` |  |
| `visibility` | `string` |  |
| `commits_url` | `string` |  |
| `downloads_url` | `string` |  |
| `assignees_url` | `string` |  |
| `events_url` | `string` |  |
| `homepage` | `string` |  |
| `role_name` | `string` |  |
| `issues_url` | `string` |  |
| `hooks_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `default_branch` | `string` |  |
| `url` | `string` |  |
| `contributors_url` | `string` |  |
| `watchers` | `integer` |  |
| `html_url` | `string` |  |
| `clone_url` | `string` |  |
| `language` | `string` |  |
| `notifications_url` | `string` |  |
| `watchers_count` | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_repos_watched_by_user` | `SELECT` | `username` | Lists repositories a user is watching. |
| `list_watched_repos_for_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user is watching. |
