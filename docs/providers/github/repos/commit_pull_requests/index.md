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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.commit_pull_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `body` | `string` |  |
| `html_url` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `requested_teams` | `array` |  |
| `locked` | `boolean` |  |
| `created_at` | `string` |  |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `url` | `string` |  |
| `state` | `string` |  |
| `commits_url` | `string` |  |
| `patch_url` | `string` |  |
| `active_lock_reason` | `string` |  |
| `diff_url` | `string` |  |
| `labels` | `array` |  |
| `comments_url` | `string` |  |
| `closed_at` | `string` |  |
| `number` | `integer` |  |
| `review_comment_url` | `string` |  |
| `title` | `string` |  |
| `user` | `object` | Simple User |
| `node_id` | `string` |  |
| `merge_commit_sha` | `string` |  |
| `updated_at` | `string` |  |
| `_links` | `object` |  |
| `base` | `object` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `statuses_url` | `string` |  |
| `assignee` | `object` | Simple User |
| `merged_at` | `string` |  |
| `assignees` | `array` |  |
| `requested_reviewers` | `array` |  |
| `issue_url` | `string` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `review_comments_url` | `string` |  |
| `head` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_pull_requests_associated_with_commit` | `SELECT` | `commit_sha, owner, repo` |
