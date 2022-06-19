---
title: apps
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
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.application.apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `name` | `string` |
| `features` | `array` |
| `settings` | `object` |
| `status` | `string` |
| `signOnMode` | `string` |
| `created` | `string` |
| `label` | `string` |
| `_embedded` | `object` |
| `profile` | `object` |
| `visibility` | `object` |
| `licensing` | `object` |
| `credentials` | `object` |
| `accessibility` | `object` |
| `_links` | `object` |
| `lastUpdated` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `appId` | Fetches an application from your Okta organization by `id`. |
| `list` | `SELECT` |  | Enumerates apps added to your organization with pagination. A subset of apps can be returned that match a supported filter expression or query. |
| `insert` | `INSERT` |  | Adds a new application to your Okta organization. |
| `delete` | `DELETE` | `appId` | Removes an inactive application. |
| `activate` | `EXEC` | `appId` | Activates an inactive application. |
| `deactivate` | `EXEC` | `appId` | Deactivates an active application. |
| `deleteall` | `EXEC` | `appId` | Revokes all tokens for the specified application |
| `update` | `EXEC` | `appId` | Updates an application in your organization. |
