---
title: pull_requests
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
<tr><td><b>Name</b></td><td><code>pull_requests</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.pull_requests</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `body` | `string` |  |
| `maintainer_can_modify` | `boolean` | Indicates whether maintainers can modify the pull request. |
| `node_id` | `string` |  |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `merge_commit_sha` | `string` |  |
| `html_url` | `string` |  |
| `comments` | `integer` |  |
| `base` | `object` |  |
| `assignees` | `array` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `locked` | `boolean` |  |
| `active_lock_reason` | `string` |  |
| `review_comments_url` | `string` |  |
| `labels` | `array` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `patch_url` | `string` |  |
| `merged_by` | `object` | Simple User |
| `changed_files` | `integer` |  |
| `rebaseable` | `boolean` |  |
| `mergeable_state` | `string` |  |
| `additions` | `integer` |  |
| `merged` | `boolean` |  |
| `assignee` | `object` | Simple User |
| `created_at` | `string` |  |
| `user` | `object` | Simple User |
| `mergeable` | `boolean` |  |
| `requested_teams` | `array` |  |
| `title` | `string` | The title of the pull request. |
| `closed_at` | `string` |  |
| `state` | `string` | State of this Pull Request. Either `open` or `closed`. |
| `number` | `integer` | Number uniquely identifying the pull request within its repository. |
| `issue_url` | `string` |  |
| `review_comment_url` | `string` |  |
| `statuses_url` | `string` |  |
| `updated_at` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `comments_url` | `string` |  |
| `url` | `string` |  |
| `_links` | `object` |  |
| `commits_url` | `string` |  |
| `deletions` | `integer` |  |
| `requested_reviewers` | `array` |  |
| `head` | `object` |  |
| `review_comments` | `integer` |  |
| `commits` | `integer` |  |
| `diff_url` | `string` |  |
| `merged_at` | `string` |  |
## Methods
