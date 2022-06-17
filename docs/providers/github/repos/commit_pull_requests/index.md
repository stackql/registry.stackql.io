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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>commit_pull_requests</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.commit_pull_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `title` | `string` |  |
| `review_comment_url` | `string` |  |
| `labels` | `array` |  |
| `assignee` | `object` | Simple User |
| `updated_at` | `string` |  |
| `review_comments_url` | `string` |  |
| `head` | `object` |  |
| `html_url` | `string` |  |
| `diff_url` | `string` |  |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `commits_url` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `requested_teams` | `array` |  |
| `locked` | `boolean` |  |
| `assignees` | `array` |  |
| `active_lock_reason` | `string` |  |
| `requested_reviewers` | `array` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `user` | `object` | Simple User |
| `issue_url` | `string` |  |
| `base` | `object` |  |
| `_links` | `object` |  |
| `merged_at` | `string` |  |
| `merge_commit_sha` | `string` |  |
| `patch_url` | `string` |  |
| `url` | `string` |  |
| `body` | `string` |  |
| `comments_url` | `string` |  |
| `node_id` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `created_at` | `string` |  |
| `number` | `integer` |  |
| `state` | `string` |  |
| `statuses_url` | `string` |  |
| `closed_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_pull_requests_associated_with_commit` | `SELECT` | `commit_sha, owner, repo` |
