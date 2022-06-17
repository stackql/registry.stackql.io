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
<tr><td><b>Name</b></td><td><code>github.pulls.comments</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.comments</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | The ID of the pull request review comment. |
| `body` | `string` | The text of the comment. |
| `updated_at` | `string` |  |
| `original_commit_id` | `string` | The SHA of the original commit to which the comment applies. |
| `reactions` | `object` |  |
| `diff_hunk` | `string` | The diff of the line that the comment refers to. |
| `html_url` | `string` | HTML URL for the pull request review comment. |
| `original_position` | `integer` | The index of the original line in the diff to which the comment applies. |
| `node_id` | `string` | The node ID of the pull request review comment. |
| `position` | `integer` | The line index in the diff to which the comment applies. |
| `pull_request_review_id` | `integer` | The ID of the pull request review to which the comment belongs. |
| `original_line` | `integer` | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `created_at` | `string` |  |
| `commit_id` | `string` | The SHA of the commit to which the comment applies. |
| `url` | `string` | URL for the pull request review comment |
| `body_html` | `string` |  |
| `in_reply_to_id` | `integer` | The comment ID to reply to. |
| `body_text` | `string` |  |
| `start_line` | `integer` | The first line of the range for a multi-line comment. |
| `side` | `string` | The side of the diff to which the comment applies. The side of the last line of the range for a multi-line comment |
| `start_side` | `string` | The side of the first line of the range for a multi-line comment. |
| `author_association` | `string` | How the author is associated with the repository. |
| `path` | `string` | The relative path of the file to which the comment applies. |
| `pull_request_url` | `string` | URL for the pull request that the review comment belongs to. |
| `_links` | `object` |  |
| `user` | `object` | Simple User |
| `line` | `integer` | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `original_start_line` | `integer` | The first line of the range for a multi-line comment. |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_review_comment` | `comment_id, owner, repo` | Provides details for a review comment. | SELECT |
| `list_review_comments` | `owner, pull_number, repo` | Lists all review comments for a pull request. By default, review comments are in ascending order by ID. | SELECT |
| `list_review_comments_for_repo` | `owner, repo` | Lists review comments for all pull requests in a repository. By default, review comments are in ascending order by ID. | SELECT |
| `create_reply_for_review_comment` | `comment_id, owner, pull_number, repo, data__body` | Creates a reply to a review comment for a pull request. For the `comment_id`, provide the ID of the review comment you are replying to. This must be the ID of a _top-level review comment_, not a reply to that comment. Replies to replies are not supported.<br /><br />This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. | INSERT |
| `create_review_comment` | `owner, pull_number, repo, data__body` | <br />Creates a review comment in the pull request diff. To add a regular comment to a pull request timeline, see "[Create an issue comment](https://docs.github.com/rest/reference/issues#create-an-issue-comment)." We recommend creating a review comment using `line`, `side`, and optionally `start_line` and `start_side` if your comment applies to more than one line in the pull request diff.<br /><br />You can still create a review comment using the `position` parameter. When you use `position`, the `line`, `side`, `start_line`, and `start_side` parameters are not required.<br /><br />**Note:** The position value equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.<br /><br />This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. | INSERT |
| `delete_review_comment` | `comment_id, owner, repo` | Deletes a review comment. | DELETE |
| `update_review_comment` | `comment_id, owner, repo, data__body` | Enables you to edit a review comment. | EXEC |
