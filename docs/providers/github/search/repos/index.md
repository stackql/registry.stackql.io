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
| `allow_merge_commit` | `boolean` |  |
| `keys_url` | `string` |  |
| `merges_url` | `string` |  |
| `compare_url` | `string` |  |
| `private` | `boolean` |  |
| `permissions` | `object` |  |
| `comments_url` | `string` |  |
| `hooks_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `score` | `number` |  |
| `assignees_url` | `string` |  |
| `default_branch` | `string` |  |
| `open_issues_count` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `pushed_at` | `string` |  |
| `owner` | `object` | Simple User |
| `issue_comment_url` | `string` |  |
| `created_at` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `labels_url` | `string` |  |
| `allow_rebase_merge` | `boolean` |  |
| `html_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `topics` | `array` |  |
| `temp_clone_token` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `mirror_url` | `string` |  |
| `trees_url` | `string` |  |
| `pulls_url` | `string` |  |
| `git_url` | `string` |  |
| `issues_url` | `string` |  |
| `language` | `string` |  |
| `events_url` | `string` |  |
| `downloads_url` | `string` |  |
| `full_name` | `string` |  |
| `updated_at` | `string` |  |
| `homepage` | `string` |  |
| `stargazers_count` | `integer` |  |
| `svn_url` | `string` |  |
| `subscription_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `allow_squash_merge` | `boolean` |  |
| `forks` | `integer` |  |
| `fork` | `boolean` |  |
| `open_issues` | `integer` |  |
| `has_pages` | `boolean` |  |
| `size` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `license` | `object` | License Simple |
| `git_commits_url` | `string` |  |
| `contributors_url` | `string` |  |
| `blobs_url` | `string` |  |
| `is_template` | `boolean` |  |
| `teams_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `forks_count` | `integer` |  |
| `archive_url` | `string` |  |
| `master_branch` | `string` |  |
| `git_refs_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `clone_url` | `string` |  |
| `branches_url` | `string` |  |
| `forks_url` | `string` |  |
| `contents_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `text_matches` | `array` |  |
| `milestones_url` | `string` |  |
| `deployments_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `commits_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `notifications_url` | `string` |  |
| `node_id` | `string` |  |
| `tags_url` | `string` |  |
| `releases_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `url` | `string` |  |
| `watchers` | `integer` |  |
| `statuses_url` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `languages_url` | `string` |  |
| `allow_auto_merge` | `boolean` |  |
| `archived` | `boolean` |  |
| `ssh_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `repos` | `SELECT` | `q` |
