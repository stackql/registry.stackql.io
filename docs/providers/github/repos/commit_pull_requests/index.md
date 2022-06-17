---
title: commit_pull_requests
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
<tr><td><b>Name</b></td><td><code>commit_pull_requests</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.commit_pull_requests</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `merge_commit_sha` | `string` |  |
| `requested_teams` | `array` |  |
| `requested_reviewers` | `array` |  |
| `statuses_url` | `string` |  |
| `active_lock_reason` | `string` |  |
| `node_id` | `string` |  |
| `url` | `string` |  |
| `user` | `object` | Simple User |
| `issue_url` | `string` |  |
| `html_url` | `string` |  |
| `base` | `object` |  |
| `locked` | `boolean` |  |
| `_links` | `object` |  |
| `labels` | `array` |  |
| `assignees` | `array` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `closed_at` | `string` |  |
| `review_comments_url` | `string` |  |
| `commits_url` | `string` |  |
| `diff_url` | `string` |  |
| `comments_url` | `string` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `head` | `object` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `merged_at` | `string` |  |
| `created_at` | `string` |  |
| `state` | `string` |  |
| `number` | `integer` |  |
| `updated_at` | `string` |  |
| `assignee` | `object` | Simple User |
| `body` | `string` |  |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `title` | `string` |  |
| `patch_url` | `string` |  |
| `review_comment_url` | `string` |  |
## Methods
