---
title: commit_comment_reactions
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
<tr><td><b>Name</b></td><td><code>github.reactions.commit_comment_reactions</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.reactions.commit_comment_reactions</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `content` | `string` | The reaction to use |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
| `user` | `object` | Simple User |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_for_commit_comment` | `comment_id, owner, repo` | List the reactions to a [commit comment](https://docs.github.com/rest/reference/repos#comments). | SELECT |
| `create_for_commit_comment` | `comment_id, owner, repo, data__content` | Create a reaction to a [commit comment](https://docs.github.com/rest/reference/repos#comments). A response with an HTTP `200` status means that you already added the reaction type to this commit comment. | INSERT |
| `delete_for_commit_comment` | `comment_id, owner, reaction_id, repo` | **Note:** You can also specify a repository by `repository_id` using the route `DELETE /repositories/:repository_id/comments/:comment_id/reactions/:reaction_id`.<br /><br />Delete a reaction to a [commit comment](https://docs.github.com/rest/reference/repos#comments). | DELETE |
