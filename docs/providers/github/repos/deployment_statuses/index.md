---
title: deployment_statuses
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
<tr><td><b>Name</b></td><td><code>deployment_statuses</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.deployment_statuses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `description` | `string` | A short description of the status. |
| `url` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `state` | `string` | The state of the status. |
| `node_id` | `string` |  |
| `environment_url` | `string` | The URL for accessing your environment. |
| `creator` | `object` | Simple User |
| `created_at` | `string` |  |
| `deployment_url` | `string` |  |
| `environment` | `string` | The environment of the deployment that the status is for. |
| `log_url` | `string` | The URL to associate with this status. |
| `target_url` | `string` | Deprecated: the URL to associate with this status. |
| `repository_url` | `string` |  |
| `updated_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get_deployment_status` | `SELECT` | `deployment_id, owner, repo, status_id` | Users with pull access can view a deployment status for a deployment: |
| `list_deployment_statuses` | `SELECT` | `deployment_id, owner, repo` | Users with pull access can view deployment statuses for a deployment: |
| `create_deployment_status` | `INSERT` | `deployment_id, owner, repo, data__state` | Users with `push` access can create deployment statuses for a given deployment.<br /><br />GitHub Apps require `read & write` access to "Deployments" and `read-only` access to "Repo contents" (for private repos). OAuth Apps require the `repo_deployment` scope. |
