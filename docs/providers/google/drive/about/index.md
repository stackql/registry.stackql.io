---
title: about
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
<tr><td><b>Name</b></td><td><code>about</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.drive.about</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `maxImportSizes` | `object` | A map of maximum import sizes by MIME type, in bytes. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#about". |
| `user` | `object` | Information about a Drive user. |
| `maxUploadSize` | `string` | The maximum upload size in bytes. |
| `canCreateTeamDrives` | `boolean` | Deprecated - use canCreateDrives instead. |
| `driveThemes` | `array` | A list of themes that are supported for shared drives. |
| `exportFormats` | `object` | A map of source MIME type to possible targets for all supported exports. |
| `teamDriveThemes` | `array` | Deprecated - use driveThemes instead. |
| `appInstalled` | `boolean` | Whether the user has installed the requesting app. |
| `storageQuota` | `object` | The user's storage quota limits and usage. All fields are measured in bytes. |
| `importFormats` | `object` | A map of source MIME type to possible targets for all supported imports. |
| `folderColorPalette` | `array` | The currently supported folder colors as RGB hex strings. |
| `canCreateDrives` | `boolean` | Whether the user can create shared drives. |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get` | `SELECT` |  |
