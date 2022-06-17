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
<tr><td><b>Name</b></td><td><code>github.repos.deployment_statuses</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.deployment_statuses</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `description` | `string` | A short description of the status. |
| `log_url` | `string` | The URL to associate with this status. |
| `creator` | `object` | Simple User |
| `url` | `string` |  |
| `state` | `string` | The state of the status. |
| `node_id` | `string` |  |
| `updated_at` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `environment` | `string` | The environment of the deployment that the status is for. |
| `created_at` | `string` |  |
| `repository_url` | `string` |  |
| `target_url` | `string` | Deprecated: the URL to associate with this status. |
| `environment_url` | `string` | The URL for accessing your environment. |
| `deployment_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_deployment_status` | `deployment_id, owner, repo, status_id` | Users with pull access can view a deployment status for a deployment: | SELECT |
| `list_deployment_statuses` | `deployment_id, owner, repo` | Users with pull access can view deployment statuses for a deployment: | SELECT |
| `create_deployment_status` | `deployment_id, owner, repo, data__state` | Users with `push` access can create deployment statuses for a given deployment.<br /><br />GitHub Apps require `read & write` access to "Deployments" and `read-only` access to "Repo contents" (for private repos). OAuth Apps require the `repo_deployment` scope. | INSERT |
