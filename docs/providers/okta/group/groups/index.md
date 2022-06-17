---
title: groups
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
<tr><td><b>Name</b></td><td><code>okta.group.groups</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.group.groups</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `lastUpdated` | `string` |  |
| `_links` | `object` |  |
| `_embedded` | `object` |  |
| `lastMembershipUpdated` | `string` |  |
| `objectClass` | `array` |  |
| `created` | `string` |  |
| `profile` | `object` |  |
| `type` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `groupId` | Fetches a group from your organization. | SELECT |
| `list` | `` | Enumerates groups in your organization with pagination. A subset of groups can be returned that match a supported filter expression or query. | SELECT |
| `insert` | `` | Adds a new group with `OKTA_GROUP` type to your organization. | INSERT |
| `delete` | `groupId` | Removes a group with `OKTA_GROUP` type from your organization. | DELETE |
| `update` | `groupId` | Updates the profile for a group with `OKTA_GROUP` type from your organization. | EXEC |