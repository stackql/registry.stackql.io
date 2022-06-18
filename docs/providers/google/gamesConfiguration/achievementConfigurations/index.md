---
title: achievementConfigurations
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
<tr><td><b>Name</b></td><td><code>achievementConfigurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gamesConfiguration.achievementConfigurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | The ID of the achievement. |
| `initialState` | `string` | The initial state of the achievement. |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#achievementConfiguration`. |
| `published` | `object` | An achievement configuration detail. |
| `stepsToUnlock` | `integer` | Steps to unlock. Only applicable to incremental achievements. |
| `token` | `string` | The token for this resource. |
| `achievementType` | `string` | The type of the achievement. |
| `draft` | `object` | An achievement configuration detail. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `achievementId` | Retrieves the metadata of the achievement configuration with the given ID. |
| `list` | `SELECT` | `applicationId` | Returns a list of the achievement configurations in this application. |
| `insert` | `INSERT` | `applicationId` | Insert a new achievement configuration in this application. |
| `delete` | `DELETE` | `achievementId` | Delete the achievement configuration with the given ID. |
| `update` | `EXEC` | `achievementId` | Update the metadata of the achievement configuration with the given ID. |
