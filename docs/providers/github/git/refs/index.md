---
title: refs
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
<tr><td><b>Name</b></td><td><code>github.git.refs</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.git.refs</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `node_id` | `string` |  |
| `object` | `object` |  |
| `ref` | `string` |  |
| `url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_ref` | `owner, ref, repo` | Returns a single reference from your Git database. The `:ref` in the URL must be formatted as `heads/&#x7B;branch name&#x7D;` for branches and `tags/&#x7B;tag name&#x7D;` for tags. If the `:ref` doesn't match an existing ref, a `404` is returned.<br /><br />**Note:** You need to explicitly [request a pull request](https://docs.github.com/rest/reference/pulls#get-a-pull-request) to trigger a test merge commit, which checks the mergeability of pull requests. For more information, see "[Checking mergeability of pull requests](https://docs.github.com/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)". | SELECT |
| `create_ref` | `owner, repo, data__ref, data__sha` | Creates a reference for your repository. You are unable to create new references for empty repositories, even if the commit SHA-1 hash used exists. Empty repositories are repositories without branches. | INSERT |
| `delete_ref` | `owner, ref, repo` |  | DELETE |
| `update_ref` | `owner, ref, repo, data__sha` |  | EXEC |
