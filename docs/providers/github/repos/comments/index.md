---
title: comments
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
<tr><td><b>Name</b></td><td><code>github.repos.comments</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.comments</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `body` | `string` |  |
| `html_url` | `string` |  |
| `commit_id` | `string` |  |
| `reactions` | `object` |  |
| `node_id` | `string` |  |
| `line` | `integer` |  |
| `created_at` | `string` |  |
| `position` | `integer` |  |
| `updated_at` | `string` |  |
| `user` | `object` | Simple User |
| `url` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `path` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_commit_comment` | `comment_id, owner, repo` |  | SELECT |
| `list_comments_for_commit` | `commit_sha, owner, repo` | Use the `:commit_sha` to specify the commit that will have its comments listed. | SELECT |
| `list_commit_comments_for_repo` | `owner, repo` | Commit Comments use [these custom media types](https://docs.github.com/rest/reference/repos#custom-media-types). You can read more about the use of media types in the API [here](https://docs.github.com/rest/overview/media-types/).<br /><br />Comments are ordered by ascending ID. | SELECT |
| `create_commit_comment` | `commit_sha, owner, repo, data__body` | Create a comment for a commit using its `:commit_sha`.<br /><br />This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. | INSERT |
| `delete_commit_comment` | `comment_id, owner, repo` |  | DELETE |
| `update_commit_comment` | `comment_id, owner, repo, data__body` |  | EXEC |
