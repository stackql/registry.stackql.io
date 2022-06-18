---
title: appadmintargets
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
<tr><td><b>Name</b></td><td><code>appadmintargets</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.appadmintargets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `category` | `string` |
| `verificationStatus` | `string` |
| `displayName` | `string` |
| `features` | `array` |
| `_links` | `object` |
| `signOnModes` | `array` |
| `status` | `string` |
| `website` | `string` |
| `lastUpdated` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list` | `SELECT` | `roleId, userId` | Lists all App targets for an `APP_ADMIN` Role assigned to a User. This methods return list may include full Applications or Instances. The response for an instance will have an `ID` value, while Application will not have an ID. |
| `insert` | `INSERT` | `appName, applicationId, roleId, userId` | Add App Instance Target to App Administrator Role given to a User |
| `delete` | `DELETE` | `appName, applicationId, roleId, userId` | Remove App Instance Target to App Administrator Role given to a User |
