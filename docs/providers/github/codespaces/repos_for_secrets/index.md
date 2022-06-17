---
title: repos_for_secrets
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
<tr><td><b>Name</b></td><td><code>github.codespaces.repos_for_secrets</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.repos_for_secrets</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `repositories` | `array` |  |
| `total_count` | `integer` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_repositories_for_secret_for_authenticated_user` | `secret_name` | List the repositories that have been granted the ability to use a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. | SELECT |
| `add_repository_for_secret_for_authenticated_user` | `repository_id, secret_name` | Adds a repository to the selected repositories for a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. | INSERT |
| `remove_repository_for_secret_for_authenticated_user` | `repository_id, secret_name` | Removes a repository from the selected repositories for a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. | DELETE |
| `set_repositories_for_secret_for_authenticated_user` | `secret_name, data__selected_repository_ids` | Select the repositories that will use a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. | EXEC |
