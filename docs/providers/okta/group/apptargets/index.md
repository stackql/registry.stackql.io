---
title: apptargets
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
<tr><td><b>Name</b></td><td><code>okta.group.apptargets</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.group.apptargets</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `displayName` | `string` |  |
| `signOnModes` | `array` |  |
| `features` | `array` |  |
| `lastUpdated` | `string` |  |
| `status` | `string` |  |
| `website` | `string` |  |
| `verificationStatus` | `string` |  |
| `_links` | `object` |  |
| `category` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list` | `groupId, roleId` | Lists all App targets for an `APP_ADMIN` Role assigned to a Group. This methods return list may include full Applications or Instances. The response for an instance will have an `ID` value, while Application will not have an ID. | SELECT |
| `insert` | `appName, groupId, roleId` | Success | INSERT |
| `delete` | `appName, groupId, roleId` | Success | DELETE |
