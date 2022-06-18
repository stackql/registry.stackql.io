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
| `has_downloads` | `boolean` |  |
| `clone_url` | `string` |  |
| `topics` | `array` |  |
| `commits_url` | `string` |  |
| `open_issues` | `integer` |  |
| `keys_url` | `string` |  |
| `assignees_url` | `string` |  |
| `default_branch` | `string` |  |
| `events_url` | `string` |  |
| `git_url` | `string` |  |
| `languages_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `pushed_at` | `string` |  |
| `trees_url` | `string` |  |
| `blobs_url` | `string` |  |
| `homepage` | `string` |  |
| `created_at` | `string` |  |
| `issues_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `forks_url` | `string` |  |
| `mirror_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `private` | `boolean` |  |
| `watchers` | `integer` |  |
| `license` | `object` |  |
| `html_url` | `string` |  |
| `owner` | `object` | Simple User |
| `milestones_url` | `string` |  |
| `deployments_url` | `string` |  |
| `archived` | `boolean` |  |
| `role_name` | `string` |  |
| `has_pages` | `boolean` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `notifications_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `watchers_count` | `integer` |  |
| `node_id` | `string` |  |
| `forks_count` | `integer` |  |
| `hooks_url` | `string` |  |
| `forks` | `integer` |  |
| `releases_url` | `string` |  |
| `contributors_url` | `string` |  |
| `statuses_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `subscribers_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `url` | `string` |  |
| `pulls_url` | `string` |  |
| `network_count` | `integer` |  |
| `subscription_url` | `string` |  |
| `contents_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `fork` | `boolean` |  |
| `is_template` | `boolean` |  |
| `language` | `string` |  |
| `teams_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `branches_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `size` | `integer` |  |
| `issue_comment_url` | `string` |  |
| `svn_url` | `string` |  |
| `archive_url` | `string` |  |
| `comments_url` | `string` |  |
| `tags_url` | `string` |  |
| `labels_url` | `string` |  |
| `ssh_url` | `string` |  |
| `disabled` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `downloads_url` | `string` |  |
| `merges_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `updated_at` | `string` |  |
| `full_name` | `string` |  |
| `permissions` | `object` |  |
| `compare_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `visibility` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_repos_watched_by_user` | `SELECT` | `username` | Lists repositories a user is watching. |
| `list_watched_repos_for_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user is watching. |
