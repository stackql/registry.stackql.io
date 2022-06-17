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
<tr><td><b>Name</b></td><td><code>github.activity.watched_repos</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.watched_repos</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `languages_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `temp_clone_token` | `string` |  |
| `owner` | `object` | Simple User |
| `allow_forking` | `boolean` |  |
| `commits_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `mirror_url` | `string` |  |
| `subscription_url` | `string` |  |
| `labels_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `license` | `object` |  |
| `git_commits_url` | `string` |  |
| `language` | `string` |  |
| `full_name` | `string` |  |
| `comments_url` | `string` |  |
| `forks_url` | `string` |  |
| `archive_url` | `string` |  |
| `forks_count` | `integer` |  |
| `node_id` | `string` |  |
| `pulls_url` | `string` |  |
| `downloads_url` | `string` |  |
| `default_branch` | `string` |  |
| `homepage` | `string` |  |
| `contributors_url` | `string` |  |
| `forks` | `integer` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `git_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `size` | `integer` |  |
| `issues_url` | `string` |  |
| `deployments_url` | `string` |  |
| `open_issues` | `integer` |  |
| `role_name` | `string` |  |
| `releases_url` | `string` |  |
| `contents_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `is_template` | `boolean` |  |
| `fork` | `boolean` |  |
| `notifications_url` | `string` |  |
| `watchers` | `integer` |  |
| `branches_url` | `string` |  |
| `keys_url` | `string` |  |
| `permissions` | `object` |  |
| `assignees_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `hooks_url` | `string` |  |
| `statuses_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `disabled` | `boolean` |  |
| `pushed_at` | `string` |  |
| `merges_url` | `string` |  |
| `milestones_url` | `string` |  |
| `compare_url` | `string` |  |
| `visibility` | `string` |  |
| `archived` | `boolean` |  |
| `subscribers_count` | `integer` |  |
| `events_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `tags_url` | `string` |  |
| `blobs_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `created_at` | `string` |  |
| `issue_events_url` | `string` |  |
| `topics` | `array` |  |
| `stargazers_url` | `string` |  |
| `private` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `html_url` | `string` |  |
| `ssh_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `svn_url` | `string` |  |
| `updated_at` | `string` |  |
| `clone_url` | `string` |  |
| `teams_url` | `string` |  |
| `trees_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `network_count` | `integer` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_repos_watched_by_user` | `username` | Lists repositories a user is watching. | SELECT |
| `list_watched_repos_for_authenticated_user` | `` | Lists repositories the authenticated user is watching. | SELECT |
