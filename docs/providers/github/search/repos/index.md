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
| `languages_url` | `string` |  |
| `clone_url` | `string` |  |
| `pushed_at` | `string` |  |
| `language` | `string` |  |
| `assignees_url` | `string` |  |
| `labels_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `stargazers_url` | `string` |  |
| `statuses_url` | `string` |  |
| `merges_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `milestones_url` | `string` |  |
| `comments_url` | `string` |  |
| `forks` | `integer` |  |
| `master_branch` | `string` |  |
| `ssh_url` | `string` |  |
| `trees_url` | `string` |  |
| `forks_count` | `integer` |  |
| `releases_url` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `license` | `object` | License Simple |
| `has_issues` | `boolean` |  |
| `temp_clone_token` | `string` |  |
| `subscription_url` | `string` |  |
| `forks_url` | `string` |  |
| `text_matches` | `array` |  |
| `issue_comment_url` | `string` |  |
| `downloads_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `git_tags_url` | `string` |  |
| `allow_auto_merge` | `boolean` |  |
| `issues_url` | `string` |  |
| `url` | `string` |  |
| `branches_url` | `string` |  |
| `pulls_url` | `string` |  |
| `owner` | `object` | Simple User |
| `open_issues` | `integer` |  |
| `size` | `integer` |  |
| `git_commits_url` | `string` |  |
| `notifications_url` | `string` |  |
| `topics` | `array` |  |
| `watchers` | `integer` |  |
| `subscribers_url` | `string` |  |
| `mirror_url` | `string` |  |
| `contents_url` | `string` |  |
| `fork` | `boolean` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `permissions` | `object` |  |
| `default_branch` | `string` |  |
| `allow_merge_commit` | `boolean` |  |
| `private` | `boolean` |  |
| `homepage` | `string` |  |
| `deployments_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `score` | `number` |  |
| `archive_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `compare_url` | `string` |  |
| `commits_url` | `string` |  |
| `teams_url` | `string` |  |
| `keys_url` | `string` |  |
| `node_id` | `string` |  |
| `archived` | `boolean` |  |
| `allow_rebase_merge` | `boolean` |  |
| `git_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `svn_url` | `string` |  |
| `events_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `created_at` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `tags_url` | `string` |  |
| `contributors_url` | `string` |  |
| `html_url` | `string` |  |
| `hooks_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `is_template` | `boolean` |  |
| `updated_at` | `string` |  |
| `open_issues_count` | `integer` |  |
| `git_refs_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `blobs_url` | `string` |  |
| `allow_squash_merge` | `boolean` |  |
| `full_name` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `repos` | `SELECT` | `q` |
