---
title: user_installations
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
<tr><td><b>Name</b></td><td><code>github.apps.user_installations</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.user_installations</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | The ID of the installation. |
| `target_id` | `integer` | The ID of the user or organization this token is being scoped to. |
| `html_url` | `string` |  |
| `updated_at` | `string` |  |
| `app_slug` | `string` |  |
| `target_type` | `string` |  |
| `repository_selection` | `string` | Describe whether all repositories have been selected or there's a selection involved |
| `suspended_at` | `string` |  |
| `created_at` | `string` |  |
| `has_multiple_single_files` | `boolean` |  |
| `single_file_name` | `string` |  |
| `access_tokens_url` | `string` |  |
| `account` | `` |  |
| `suspended_by` | `object` | Simple User |
| `contact_email` | `string` |  |
| `repositories_url` | `string` |  |
| `single_file_paths` | `array` |  |
| `permissions` | `object` | The permissions granted to the user-to-server access token. |
| `app_id` | `integer` |  |
| `events` | `array` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_user_installation` | `username` | Enables an authenticated GitHub App to find the user’s installation information.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. | SELECT |
| `list_installations_for_authenticated_user` | `` | Lists installations of your GitHub App that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access.<br /><br />You must use a [user-to-server OAuth access token](https://docs.github.com/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/#identifying-users-on-your-site), created for a user who has authorized your GitHub App, to access this endpoint.<br /><br />The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.<br /><br />You can find the permissions for the installation under the `permissions` key. | SELECT |
