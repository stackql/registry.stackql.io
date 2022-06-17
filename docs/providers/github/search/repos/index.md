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
<tr><td><b>Id</b></td><td><code>github.search.repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `node_id` | `string` |  |
| `git_url` | `string` |  |
| `topics` | `array` |  |
| `open_issues` | `integer` |  |
| `size` | `integer` |  |
| `subscription_url` | `string` |  |
| `pulls_url` | `string` |  |
| `allow_squash_merge` | `boolean` |  |
| `full_name` | `string` |  |
| `permissions` | `object` |  |
| `score` | `number` |  |
| `languages_url` | `string` |  |
| `comments_url` | `string` |  |
| `milestones_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `assignees_url` | `string` |  |
| `ssh_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `temp_clone_token` | `string` |  |
| `archive_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `contributors_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `merges_url` | `string` |  |
| `watchers` | `integer` |  |
| `default_branch` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `svn_url` | `string` |  |
| `releases_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `branches_url` | `string` |  |
| `issues_url` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `has_issues` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `forks_count` | `integer` |  |
| `url` | `string` |  |
| `forks` | `integer` |  |
| `issue_events_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `forks_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `notifications_url` | `string` |  |
| `contents_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `html_url` | `string` |  |
| `tags_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `stargazers_count` | `integer` |  |
| `archived` | `boolean` |  |
| `has_wiki` | `boolean` |  |
| `owner` | `object` | Simple User |
| `blobs_url` | `string` |  |
| `deployments_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `clone_url` | `string` |  |
| `allow_rebase_merge` | `boolean` |  |
| `hooks_url` | `string` |  |
| `pushed_at` | `string` |  |
| `compare_url` | `string` |  |
| `private` | `boolean` |  |
| `teams_url` | `string` |  |
| `keys_url` | `string` |  |
| `created_at` | `string` |  |
| `fork` | `boolean` |  |
| `allow_merge_commit` | `boolean` |  |
| `mirror_url` | `string` |  |
| `statuses_url` | `string` |  |
| `events_url` | `string` |  |
| `language` | `string` |  |
| `labels_url` | `string` |  |
| `commits_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `trees_url` | `string` |  |
| `updated_at` | `string` |  |
| `allow_auto_merge` | `boolean` |  |
| `text_matches` | `array` |  |
| `homepage` | `string` |  |
| `is_template` | `boolean` |  |
| `downloads_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `license` | `object` | License Simple |
| `open_issues_count` | `integer` |  |
| `master_branch` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `repos` | `SELECT` | `q` |
