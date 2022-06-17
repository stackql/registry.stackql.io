---
title: user
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
<tr><td><b>Name</b></td><td><code>okta.usertype.user</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.usertype.user</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `_links` | `object` |  |
| `default` | `boolean` |  |
| `created` | `string` |  |
| `displayName` | `string` |  |
| `lastUpdated` | `string` |  |
| `lastUpdatedBy` | `string` |  |
| `createdBy` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `typeId` | Fetches a User Type by ID. The special identifier `default` may be used to fetch the default User Type. | SELECT |
| `list` | `` | Fetches all User Types in your org | SELECT |
| `insert` | `` | Creates a new User Type. A default User Type is automatically created along with your org, and you may add another 9 User Types for a maximum of 10. | INSERT |
| `delete` | `typeId` | Deletes a User Type permanently. This operation is not permitted for the default type, nor for any User Type that has existing users | DELETE |
| `partialUpdate` | `typeId` | Updates an existing User Type | EXEC |
| `update` | `typeId` | Replace an existing User Type | EXEC |
