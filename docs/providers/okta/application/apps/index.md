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
<tr><td><b>Name</b></td><td><code>okta.application.apps</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.application.apps</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `accessibility` | `object` |  |
| `_embedded` | `object` |  |
| `licensing` | `object` |  |
| `settings` | `object` |  |
| `features` | `array` |  |
| `status` | `string` |  |
| `visibility` | `object` |  |
| `credentials` | `object` |  |
| `signOnMode` | `string` |  |
| `lastUpdated` | `string` |  |
| `label` | `string` |  |
| `_links` | `object` |  |
| `created` | `string` |  |
| `profile` | `object` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `appId` | Fetches an application from your Okta organization by `id`. | SELECT |
| `list` | `` | Enumerates apps added to your organization with pagination. A subset of apps can be returned that match a supported filter expression or query. | SELECT |
| `insert` | `` | Adds a new application to your Okta organization. | INSERT |
| `delete` | `appId` | Removes an inactive application. | DELETE |
| `activate` | `appId` | Activates an inactive application. | EXEC |
| `deactivate` | `appId` | Deactivates an active application. | EXEC |
| `deleteall` | `appId` | Revokes all tokens for the specified application | EXEC |
| `update` | `appId` | Updates an application in your organization. | EXEC |
