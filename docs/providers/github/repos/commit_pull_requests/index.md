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
<tr><td><b>Name</b></td><td><code>github.repos.commit_pull_requests</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.commit_pull_requests</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `assignee` | `object` | Simple User |
| `issue_url` | `string` |  |
| `updated_at` | `string` |  |
| `comments_url` | `string` |  |
| `title` | `string` |  |
| `merge_commit_sha` | `string` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `requested_teams` | `array` |  |
| `base` | `object` |  |
| `patch_url` | `string` |  |
| `html_url` | `string` |  |
| `statuses_url` | `string` |  |
| `created_at` | `string` |  |
| `state` | `string` |  |
| `commits_url` | `string` |  |
| `assignees` | `array` |  |
| `node_id` | `string` |  |
| `merged_at` | `string` |  |
| `labels` | `array` |  |
| `body` | `string` |  |
| `_links` | `object` |  |
| `requested_reviewers` | `array` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `review_comments_url` | `string` |  |
| `url` | `string` |  |
| `locked` | `boolean` |  |
| `diff_url` | `string` |  |
| `number` | `integer` |  |
| `active_lock_reason` | `string` |  |
| `head` | `object` |  |
| `closed_at` | `string` |  |
| `user` | `object` | Simple User |
| `review_comment_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_pull_requests_associated_with_commit` | `commit_sha, owner, repo` | Lists the merged pull request that introduced the commit to the repository. If the commit is not present in the default branch, additionally returns open pull requests associated with the commit. The results may include open and closed pull requests. Additional preview headers may be required to see certain details for associated pull requests, such as whether a pull request is in a draft state. For more information about previews that might affect this endpoint, see the [List pull requests](https://docs.github.com/rest/reference/pulls#list-pull-requests) endpoint. | SELECT |
