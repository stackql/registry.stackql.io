---
title: codespaces
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
<tr><td><b>Name</b></td><td><code>github.codespaces.codespaces</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.codespaces</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `total_count` | `integer` |  |
| `codespaces` | `array` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_for_authenticated_user` | `codespace_name` | Gets information about a user's codespace.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. | SELECT |
| `list_for_authenticated_user` | `` | Lists the authenticated user's codespaces.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. | SELECT |
| `list_in_repository_for_authenticated_user` | `owner, repo` | Lists the codespaces associated to a specified repository and the authenticated user.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. | SELECT |
| `create_for_authenticated_user` | `` | Creates a new codespace, owned by the authenticated user.<br /><br />This endpoint requires either a `repository_id` OR a `pull_request` but not both.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. | INSERT |
| `create_with_pr_for_authenticated_user` | `owner, pull_number, repo, data__location` | Creates a codespace owned by the authenticated user for the specified pull request.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. | INSERT |
| `create_with_repo_for_authenticated_user` | `owner, repo, data__location` | Creates a codespace owned by the authenticated user in the specified repository.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. | INSERT |
| `delete_for_authenticated_user` | `codespace_name` | Deletes a user's codespace.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. | DELETE |
| `export_for_authenticated_user` | `codespace_name` | Triggers an export of the specified codespace and returns a URL and ID where the status of the export can be monitored.<br /><br />You must authenticate using a personal access token with the `codespace` scope to use this endpoint. | EXEC |
| `get_export_details_for_authenticated_user` | `codespace_name, export_id` | Gets information about an export of a codespace.<br /><br />You must authenticate using a personal access token with the `codespace` scope to use this endpoint. | EXEC |
| `start_for_authenticated_user` | `codespace_name` | Starts a user's codespace.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. | EXEC |
| `stop_for_authenticated_user` | `codespace_name` | Stops a user's codespace.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. | EXEC |
| `update_for_authenticated_user` | `codespace_name` | Updates a codespace owned by the authenticated user. Currently only the codespace's machine type and recent folders can be modified using this endpoint.<br /><br />If you specify a new machine type it will be applied the next time your codespace is started.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. | EXEC |
