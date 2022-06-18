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
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `assignees` | `array` |  |
| `statuses_url` | `string` |  |
| `url` | `string` |  |
| `_links` | `object` |  |
| `created_at` | `string` |  |
| `assignee` | `object` | Simple User |
| `user` | `object` | Simple User |
| `updated_at` | `string` |  |
| `state` | `string` |  |
| `diff_url` | `string` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `active_lock_reason` | `string` |  |
| `html_url` | `string` |  |
| `body` | `string` |  |
| `issue_url` | `string` |  |
| `title` | `string` |  |
| `closed_at` | `string` |  |
| `requested_teams` | `array` |  |
| `base` | `object` |  |
| `node_id` | `string` |  |
| `number` | `integer` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `commits_url` | `string` |  |
| `merged_at` | `string` |  |
| `patch_url` | `string` |  |
| `locked` | `boolean` |  |
| `requested_reviewers` | `array` |  |
| `head` | `object` |  |
| `comments_url` | `string` |  |
| `review_comments_url` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `review_comment_url` | `string` |  |
| `merge_commit_sha` | `string` |  |
| `labels` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_pull_requests_associated_with_commit` | `SELECT` | `commit_sha, owner, repo` |
