---
title: installations
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
<tr><td><b>Name</b></td><td><code>installations</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.installations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | The ID of the installation. |
| `suspended_by` | `object` | Simple User |
| `access_tokens_url` | `string` |  |
| `suspended_at` | `string` |  |
| `target_type` | `string` |  |
| `created_at` | `string` |  |
| `target_id` | `integer` | The ID of the user or organization this token is being scoped to. |
| `events` | `array` |  |
| `repositories_url` | `string` |  |
| `app_id` | `integer` |  |
| `has_multiple_single_files` | `boolean` |  |
| `permissions` | `object` | The permissions granted to the user-to-server access token. |
| `updated_at` | `string` |  |
| `repository_selection` | `string` | Describe whether all repositories have been selected or there's a selection involved |
| `contact_email` | `string` |  |
| `html_url` | `string` |  |
| `single_file_paths` | `array` |  |
| `account` | `` |  |
| `app_slug` | `string` |  |
| `single_file_name` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get_installation` | `SELECT` | `installation_id` | Enables an authenticated GitHub App to find an installation's information using the installation id.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| `get_org_installation` | `SELECT` | `org` | Enables an authenticated GitHub App to find the organization's installation information.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| `get_repo_installation` | `SELECT` | `owner, repo` | Enables an authenticated GitHub App to find the repository's installation information. The installation's account type will be either an organization or a user account, depending which account the repository belongs to.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| `list_installations` | `SELECT` |  | You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.<br /><br />The permissions the installation has are included under the `permissions` key. |
| `delete_installation` | `DELETE` | `installation_id` | Uninstalls a GitHub App on a user, organization, or business account. If you prefer to temporarily suspend an app's access to your account's resources, then we recommend the "[Suspend an app installation](https://docs.github.com/rest/reference/apps/#suspend-an-app-installation)" endpoint.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| `create_installation_access_token` | `EXEC` | `installation_id` | Creates an installation access token that enables a GitHub App to make authenticated API requests for the app's installation on an organization or individual account. Installation tokens expire one hour from the time you create them. Using an expired token produces a status code of `401 - Unauthorized`, and requires creating a new installation token. By default the installation token has access to all repositories that the installation can access. To restrict the access to specific repositories, you can provide the `repository_ids` when creating the token. When you omit `repository_ids`, the response does not contain the `repositories` key.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| `suspend_installation` | `EXEC` | `installation_id` | Suspends a GitHub App on a user, organization, or business account, which blocks the app from accessing the account's resources. When a GitHub App is suspended, the app's access to the GitHub API or webhook events is blocked for that account.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| `unsuspend_installation` | `EXEC` | `installation_id` | Removes a GitHub App installation suspension.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
