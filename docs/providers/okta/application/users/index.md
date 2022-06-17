---
title: users
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
<tr><td><b>Name</b></td><td><code>okta.application.users</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.application.users</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `passwordChanged` | `string` |  |
| `profile` | `object` |  |
| `syncState` | `string` |  |
| `scope` | `string` |  |
| `externalId` | `string` |  |
| `lastUpdated` | `string` |  |
| `credentials` | `object` |  |
| `_embedded` | `object` |  |
| `created` | `string` |  |
| `statusChanged` | `string` |  |
| `status` | `string` |  |
| `_links` | `object` |  |
| `lastSync` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `appId, userId` | Fetches a specific user assignment for application by `id`. | SELECT |
| `list` | `appId` | Enumerates all assigned [application users](#application-user-model) for an application. | SELECT |
| `insert` | `appId` | Assigns an user to an application with [credentials](#application-user-credentials-object) and an app-specific [profile](#application-user-profile-object). Profile mappings defined for the application are first applied before applying any profile properties specified in the request. | INSERT |
| `delete` | `appId, userId` | Removes an assignment for a user from an application. | DELETE |
| `update` | `appId, userId` | Updates a user's profile for an application | EXEC |
