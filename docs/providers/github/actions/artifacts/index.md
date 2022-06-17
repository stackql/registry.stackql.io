---
title: artifacts
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
<tr><td><b>Name</b></td><td><code>github.actions.artifacts</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.artifacts</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` | The name of the artifact. |
| `archive_download_url` | `string` |  |
| `created_at` | `string` |  |
| `expired` | `boolean` | Whether or not the artifact has expired. |
| `url` | `string` |  |
| `size_in_bytes` | `integer` | The size in bytes of the artifact. |
| `expires_at` | `string` |  |
| `node_id` | `string` |  |
| `updated_at` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_artifact` | `artifact_id, owner, repo` | Gets a specific artifact for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. | SELECT |
| `list_artifacts_for_repo` | `owner, repo` | Lists all artifacts for a repository. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. | SELECT |
| `list_workflow_run_artifacts` | `owner, repo, run_id` | Lists artifacts for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. | SELECT |
| `delete_artifact` | `artifact_id, owner, repo` | Deletes an artifact for a workflow run. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint. | DELETE |
| `download_artifact` | `archive_format, artifact_id, owner, repo` | Gets a redirect URL to download an archive for a repository. This URL expires after 1 minute. Look for `Location:` in<br />the response header to find the URL for the download. The `:archive_format` must be `zip`. Anyone with read access to<br />the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions:read` permission to use this endpoint. | EXEC |
