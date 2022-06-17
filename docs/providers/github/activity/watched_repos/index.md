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
| `clone_url` | `string` |  |
| `forks_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `merges_url` | `string` |  |
| `languages_url` | `string` |  |
| `open_issues` | `integer` |  |
| `subscribers_count` | `integer` |  |
| `has_issues` | `boolean` |  |
| `stargazers_count` | `integer` |  |
| `node_id` | `string` |  |
| `issue_comment_url` | `string` |  |
| `pushed_at` | `string` |  |
| `network_count` | `integer` |  |
| `hooks_url` | `string` |  |
| `notifications_url` | `string` |  |
| `archived` | `boolean` |  |
| `has_wiki` | `boolean` |  |
| `updated_at` | `string` |  |
| `blobs_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `pulls_url` | `string` |  |
| `compare_url` | `string` |  |
| `statuses_url` | `string` |  |
| `homepage` | `string` |  |
| `permissions` | `object` |  |
| `issues_url` | `string` |  |
| `html_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `watchers` | `integer` |  |
| `disabled` | `boolean` |  |
| `contributors_url` | `string` |  |
| `language` | `string` |  |
| `tags_url` | `string` |  |
| `created_at` | `string` |  |
| `downloads_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `svn_url` | `string` |  |
| `contents_url` | `string` |  |
| `is_template` | `boolean` |  |
| `topics` | `array` |  |
| `allow_forking` | `boolean` |  |
| `comments_url` | `string` |  |
| `forks_count` | `integer` |  |
| `stargazers_url` | `string` |  |
| `ssh_url` | `string` |  |
| `milestones_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `default_branch` | `string` |  |
| `subscription_url` | `string` |  |
| `branches_url` | `string` |  |
| `role_name` | `string` |  |
| `assignees_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `owner` | `object` | Simple User |
| `collaborators_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `visibility` | `string` |  |
| `events_url` | `string` |  |
| `commits_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `labels_url` | `string` |  |
| `deployments_url` | `string` |  |
| `license` | `object` |  |
| `mirror_url` | `string` |  |
| `size` | `integer` |  |
| `forks` | `integer` |  |
| `full_name` | `string` |  |
| `trees_url` | `string` |  |
| `url` | `string` |  |
| `subscribers_url` | `string` |  |
| `releases_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `teams_url` | `string` |  |
| `git_url` | `string` |  |
| `archive_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `fork` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `private` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `keys_url` | `string` |  |
| `git_tags_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_repos_watched_by_user` | `SELECT` | `username` | Lists repositories a user is watching. |
| `list_watched_repos_for_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user is watching. |
