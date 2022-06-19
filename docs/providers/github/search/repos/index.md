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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.search.repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `mirror_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `homepage` | `string` |  |
| `branches_url` | `string` |  |
| `license` | `object` | License Simple |
| `hooks_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `comments_url` | `string` |  |
| `topics` | `array` |  |
| `permissions` | `object` |  |
| `open_issues_count` | `integer` |  |
| `subscribers_url` | `string` |  |
| `allow_auto_merge` | `boolean` |  |
| `watchers` | `integer` |  |
| `svn_url` | `string` |  |
| `text_matches` | `array` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `releases_url` | `string` |  |
| `milestones_url` | `string` |  |
| `size` | `integer` |  |
| `collaborators_url` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `clone_url` | `string` |  |
| `full_name` | `string` |  |
| `pulls_url` | `string` |  |
| `forks_url` | `string` |  |
| `open_issues` | `integer` |  |
| `has_projects` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `deployments_url` | `string` |  |
| `subscription_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `stargazers_url` | `string` |  |
| `allow_merge_commit` | `boolean` |  |
| `private` | `boolean` |  |
| `watchers_count` | `integer` |  |
| `forks` | `integer` |  |
| `stargazers_count` | `integer` |  |
| `allow_rebase_merge` | `boolean` |  |
| `contents_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `archived` | `boolean` |  |
| `git_refs_url` | `string` |  |
| `pushed_at` | `string` |  |
| `is_template` | `boolean` |  |
| `assignees_url` | `string` |  |
| `statuses_url` | `string` |  |
| `node_id` | `string` |  |
| `has_downloads` | `boolean` |  |
| `git_tags_url` | `string` |  |
| `languages_url` | `string` |  |
| `html_url` | `string` |  |
| `issues_url` | `string` |  |
| `downloads_url` | `string` |  |
| `owner` | `object` | Simple User |
| `events_url` | `string` |  |
| `labels_url` | `string` |  |
| `tags_url` | `string` |  |
| `forks_count` | `integer` |  |
| `created_at` | `string` |  |
| `updated_at` | `string` |  |
| `default_branch` | `string` |  |
| `keys_url` | `string` |  |
| `archive_url` | `string` |  |
| `teams_url` | `string` |  |
| `blobs_url` | `string` |  |
| `allow_squash_merge` | `boolean` |  |
| `score` | `number` |  |
| `url` | `string` |  |
| `git_url` | `string` |  |
| `ssh_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `fork` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `compare_url` | `string` |  |
| `notifications_url` | `string` |  |
| `language` | `string` |  |
| `merges_url` | `string` |  |
| `trees_url` | `string` |  |
| `commits_url` | `string` |  |
| `contributors_url` | `string` |  |
| `master_branch` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `repos` | `SELECT` | `q` |
