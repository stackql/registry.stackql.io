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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.watched_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `temp_clone_token` | `string` |  |
| `ssh_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `private` | `boolean` |  |
| `contents_url` | `string` |  |
| `notifications_url` | `string` |  |
| `size` | `integer` |  |
| `homepage` | `string` |  |
| `keys_url` | `string` |  |
| `default_branch` | `string` |  |
| `subscribers_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `html_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `milestones_url` | `string` |  |
| `events_url` | `string` |  |
| `updated_at` | `string` |  |
| `commits_url` | `string` |  |
| `visibility` | `string` |  |
| `mirror_url` | `string` |  |
| `releases_url` | `string` |  |
| `full_name` | `string` |  |
| `topics` | `array` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `trees_url` | `string` |  |
| `license` | `object` |  |
| `forks_count` | `integer` |  |
| `merges_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `tags_url` | `string` |  |
| `hooks_url` | `string` |  |
| `blobs_url` | `string` |  |
| `statuses_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `archive_url` | `string` |  |
| `contributors_url` | `string` |  |
| `created_at` | `string` |  |
| `comments_url` | `string` |  |
| `assignees_url` | `string` |  |
| `pulls_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `has_wiki` | `boolean` |  |
| `owner` | `object` | Simple User |
| `git_url` | `string` |  |
| `fork` | `boolean` |  |
| `compare_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `deployments_url` | `string` |  |
| `open_issues` | `integer` |  |
| `open_issues_count` | `integer` |  |
| `template_repository` | `object` | A git repository |
| `forks` | `integer` |  |
| `network_count` | `integer` |  |
| `pushed_at` | `string` |  |
| `language` | `string` |  |
| `role_name` | `string` |  |
| `subscribers_count` | `integer` |  |
| `watchers` | `integer` |  |
| `issues_url` | `string` |  |
| `forks_url` | `string` |  |
| `labels_url` | `string` |  |
| `archived` | `boolean` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `has_projects` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `teams_url` | `string` |  |
| `clone_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `has_downloads` | `boolean` |  |
| `subscription_url` | `string` |  |
| `node_id` | `string` |  |
| `issue_events_url` | `string` |  |
| `is_template` | `boolean` |  |
| `url` | `string` |  |
| `permissions` | `object` |  |
| `svn_url` | `string` |  |
| `disabled` | `boolean` |  |
| `downloads_url` | `string` |  |
| `languages_url` | `string` |  |
| `branches_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_repos_watched_by_user` | `SELECT` | `username` | Lists repositories a user is watching. |
| `list_watched_repos_for_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user is watching. |
