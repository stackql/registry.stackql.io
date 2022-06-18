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
| `svn_url` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `size` | `integer` |  |
| `has_downloads` | `boolean` |  |
| `deployments_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `stargazers_url` | `string` |  |
| `node_id` | `string` |  |
| `labels_url` | `string` |  |
| `archived` | `boolean` |  |
| `blobs_url` | `string` |  |
| `homepage` | `string` |  |
| `has_issues` | `boolean` |  |
| `hooks_url` | `string` |  |
| `releases_url` | `string` |  |
| `html_url` | `string` |  |
| `downloads_url` | `string` |  |
| `subscription_url` | `string` |  |
| `allow_merge_commit` | `boolean` |  |
| `license` | `object` | License Simple |
| `master_branch` | `string` |  |
| `forks_url` | `string` |  |
| `milestones_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `open_issues` | `integer` |  |
| `branches_url` | `string` |  |
| `url` | `string` |  |
| `topics` | `array` |  |
| `full_name` | `string` |  |
| `language` | `string` |  |
| `allow_forking` | `boolean` |  |
| `contents_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `statuses_url` | `string` |  |
| `events_url` | `string` |  |
| `updated_at` | `string` |  |
| `contributors_url` | `string` |  |
| `private` | `boolean` |  |
| `temp_clone_token` | `string` |  |
| `fork` | `boolean` |  |
| `permissions` | `object` |  |
| `notifications_url` | `string` |  |
| `created_at` | `string` |  |
| `is_template` | `boolean` |  |
| `git_url` | `string` |  |
| `ssh_url` | `string` |  |
| `keys_url` | `string` |  |
| `score` | `number` |  |
| `forks` | `integer` |  |
| `teams_url` | `string` |  |
| `forks_count` | `integer` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `git_refs_url` | `string` |  |
| `merges_url` | `string` |  |
| `allow_rebase_merge` | `boolean` |  |
| `issues_url` | `string` |  |
| `allow_squash_merge` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `stargazers_count` | `integer` |  |
| `git_commits_url` | `string` |  |
| `tags_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `compare_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `archive_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `assignees_url` | `string` |  |
| `allow_auto_merge` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `mirror_url` | `string` |  |
| `watchers` | `integer` |  |
| `text_matches` | `array` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `trees_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `pulls_url` | `string` |  |
| `clone_url` | `string` |  |
| `languages_url` | `string` |  |
| `comments_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `commits_url` | `string` |  |
| `owner` | `object` | Simple User |
| `default_branch` | `string` |  |
| `pushed_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `repos` | `SELECT` | `q` |
