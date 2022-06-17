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
<tr><td><b>Name</b></td><td><code>okta.user.appadmintargets</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.appadmintargets</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `_links` | `object` |  |
| `lastUpdated` | `string` |  |
| `website` | `string` |  |
| `status` | `string` |  |
| `category` | `string` |  |
| `signOnModes` | `array` |  |
| `features` | `array` |  |
| `verificationStatus` | `string` |  |
| `displayName` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list` | `roleId, userId` | Lists all App targets for an `APP_ADMIN` Role assigned to a User. This methods return list may include full Applications or Instances. The response for an instance will have an `ID` value, while Application will not have an ID. | SELECT |
| `insert` | `appName, applicationId, roleId, userId` | Add App Instance Target to App Administrator Role given to a User | INSERT |
| `delete` | `appName, applicationId, roleId, userId` | Remove App Instance Target to App Administrator Role given to a User | DELETE |