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
  
    
See also:   
[[` SHOW `]](/docs/language-spec/show) [[` DESCRIBE `]](/docs/language-spec/describe)  
* * * 
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repos</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.search.repos</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `size` | `integer` |  |
| `branches_url` | `string` |  |
| `statuses_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `keys_url` | `string` |  |
| `hooks_url` | `string` |  |
| `open_issues` | `integer` |  |
| `owner` | `object` | Simple User |
| `notifications_url` | `string` |  |
| `html_url` | `string` |  |
| `clone_url` | `string` |  |
| `score` | `number` |  |
| `subscribers_url` | `string` |  |
| `contents_url` | `string` |  |
| `tags_url` | `string` |  |
| `master_branch` | `string` |  |
| `is_template` | `boolean` |  |
| `url` | `string` |  |
| `fork` | `boolean` |  |
| `allow_auto_merge` | `boolean` |  |
| `node_id` | `string` |  |
| `allow_squash_merge` | `boolean` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `homepage` | `string` |  |
| `forks_url` | `string` |  |
| `topics` | `array` |  |
| `blobs_url` | `string` |  |
| `deployments_url` | `string` |  |
| `releases_url` | `string` |  |
| `compare_url` | `string` |  |
| `archived` | `boolean` |  |
| `watchers` | `integer` |  |
| `downloads_url` | `string` |  |
| `permissions` | `object` |  |
| `forks` | `integer` |  |
| `updated_at` | `string` |  |
| `svn_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `ssh_url` | `string` |  |
| `full_name` | `string` |  |
| `labels_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `commits_url` | `string` |  |
| `comments_url` | `string` |  |
| `events_url` | `string` |  |
| `milestones_url` | `string` |  |
| `text_matches` | `array` |  |
| `has_projects` | `boolean` |  |
| `trees_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `collaborators_url` | `string` |  |
| `merges_url` | `string` |  |
| `mirror_url` | `string` |  |
| `issues_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `allow_rebase_merge` | `boolean` |  |
| `forks_count` | `integer` |  |
| `allow_merge_commit` | `boolean` |  |
| `watchers_count` | `integer` |  |
| `git_url` | `string` |  |
| `pushed_at` | `string` |  |
| `stargazers_count` | `integer` |  |
| `assignees_url` | `string` |  |
| `license` | `object` | License Simple |
| `has_issues` | `boolean` |  |
| `languages_url` | `string` |  |
| `pulls_url` | `string` |  |
| `subscription_url` | `string` |  |
| `private` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `stargazers_url` | `string` |  |
| `archive_url` | `string` |  |
| `language` | `string` |  |
| `created_at` | `string` |  |
| `git_refs_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `default_branch` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `contributors_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `teams_url` | `string` |  |
| `open_issues_count` | `integer` |  |
## Methods
