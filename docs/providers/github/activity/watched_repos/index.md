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
| `trees_url` | `string` |  |
| `pulls_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `open_issues` | `integer` |  |
| `git_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `subscription_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `merges_url` | `string` |  |
| `deployments_url` | `string` |  |
| `notifications_url` | `string` |  |
| `clone_url` | `string` |  |
| `full_name` | `string` |  |
| `labels_url` | `string` |  |
| `forks_count` | `integer` |  |
| `watchers_count` | `integer` |  |
| `issues_url` | `string` |  |
| `visibility` | `string` |  |
| `stargazers_count` | `integer` |  |
| `role_name` | `string` |  |
| `has_downloads` | `boolean` |  |
| `ssh_url` | `string` |  |
| `private` | `boolean` |  |
| `language` | `string` |  |
| `homepage` | `string` |  |
| `keys_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `pushed_at` | `string` |  |
| `contributors_url` | `string` |  |
| `archived` | `boolean` |  |
| `tags_url` | `string` |  |
| `watchers` | `integer` |  |
| `topics` | `array` |  |
| `template_repository` | `object` | A git repository |
| `languages_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `blobs_url` | `string` |  |
| `commits_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `releases_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `forks_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `owner` | `object` | Simple User |
| `url` | `string` |  |
| `assignees_url` | `string` |  |
| `disabled` | `boolean` |  |
| `updated_at` | `string` |  |
| `events_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `size` | `integer` |  |
| `subscribers_count` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `network_count` | `integer` |  |
| `milestones_url` | `string` |  |
| `fork` | `boolean` |  |
| `forks` | `integer` |  |
| `mirror_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `statuses_url` | `string` |  |
| `contents_url` | `string` |  |
| `default_branch` | `string` |  |
| `branches_url` | `string` |  |
| `is_template` | `boolean` |  |
| `node_id` | `string` |  |
| `git_tags_url` | `string` |  |
| `archive_url` | `string` |  |
| `comments_url` | `string` |  |
| `compare_url` | `string` |  |
| `teams_url` | `string` |  |
| `license` | `object` |  |
| `downloads_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `subscribers_url` | `string` |  |
| `svn_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `created_at` | `string` |  |
| `hooks_url` | `string` |  |
| `html_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `permissions` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_repos_watched_by_user` | `SELECT` | `username` | Lists repositories a user is watching. |
| `list_watched_repos_for_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user is watching. |
