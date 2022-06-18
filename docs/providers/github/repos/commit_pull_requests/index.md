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
| `merge_commit_sha` | `string` |  |
| `locked` | `boolean` |  |
| `review_comments_url` | `string` |  |
| `commits_url` | `string` |  |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `base` | `object` |  |
| `requested_reviewers` | `array` |  |
| `body` | `string` |  |
| `diff_url` | `string` |  |
| `updated_at` | `string` |  |
| `assignees` | `array` |  |
| `url` | `string` |  |
| `comments_url` | `string` |  |
| `number` | `integer` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `requested_teams` | `array` |  |
| `active_lock_reason` | `string` |  |
| `title` | `string` |  |
| `assignee` | `object` | Simple User |
| `created_at` | `string` |  |
| `issue_url` | `string` |  |
| `_links` | `object` |  |
| `closed_at` | `string` |  |
| `merged_at` | `string` |  |
| `node_id` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `state` | `string` |  |
| `html_url` | `string` |  |
| `review_comment_url` | `string` |  |
| `labels` | `array` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `patch_url` | `string` |  |
| `user` | `object` | Simple User |
| `statuses_url` | `string` |  |
| `head` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_pull_requests_associated_with_commit` | `SELECT` | `commit_sha, owner, repo` |
