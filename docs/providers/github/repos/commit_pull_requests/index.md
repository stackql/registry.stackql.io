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
| `diff_url` | `string` |  |
| `comments_url` | `string` |  |
| `patch_url` | `string` |  |
| `review_comment_url` | `string` |  |
| `review_comments_url` | `string` |  |
| `merge_commit_sha` | `string` |  |
| `assignee` | `object` | Simple User |
| `state` | `string` |  |
| `title` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `active_lock_reason` | `string` |  |
| `body` | `string` |  |
| `assignees` | `array` |  |
| `url` | `string` |  |
| `statuses_url` | `string` |  |
| `node_id` | `string` |  |
| `requested_reviewers` | `array` |  |
| `locked` | `boolean` |  |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `user` | `object` | Simple User |
| `number` | `integer` |  |
| `issue_url` | `string` |  |
| `_links` | `object` |  |
| `created_at` | `string` |  |
| `merged_at` | `string` |  |
| `labels` | `array` |  |
| `head` | `object` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `base` | `object` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `commits_url` | `string` |  |
| `html_url` | `string` |  |
| `updated_at` | `string` |  |
| `closed_at` | `string` |  |
| `requested_teams` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_pull_requests_associated_with_commit` | `SELECT` | `commit_sha, owner, repo` |
