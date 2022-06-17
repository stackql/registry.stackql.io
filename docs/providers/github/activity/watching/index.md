---
title: watching
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
<tr><td><b>Name</b></td><td><code>github.activity.watching</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.watching</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `subscribed` | `boolean` | Determines if notifications should be received from this repository. |
| `url` | `string` |  |
| `created_at` | `string` |  |
| `ignored` | `boolean` | Determines if all notifications should be blocked from this repository. |
| `reason` | `string` |  |
| `repository_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_repo_subscription` | `owner, repo` |  | SELECT |
| `delete_repo_subscription` | `owner, repo` | This endpoint should only be used to stop watching a repository. To control whether or not you wish to receive notifications from a repository, [set the repository's subscription manually](https://docs.github.com/rest/reference/activity#set-a-repository-subscription). | DELETE |
| `set_repo_subscription` | `owner, repo` | If you would like to watch a repository, set `subscribed` to `true`. If you would like to ignore notifications made within a repository, set `ignored` to `true`. If you would like to stop watching a repository, [delete the repository's subscription](https://docs.github.com/rest/reference/activity#delete-a-repository-subscription) completely. | EXEC |
