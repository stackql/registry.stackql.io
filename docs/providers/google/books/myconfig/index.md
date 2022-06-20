---
title: myconfig
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
<tr><td><b>Name</b></td><td><code>myconfig</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.books.myconfig</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getUserSettings` | `EXEC` |  | Gets the current settings for the user. |
| `releaseDownloadAccess` | `EXEC` | `cpksver, volumeIds` | Release downloaded content access restriction. |
| `requestAccess` | `EXEC` | `cpksver, nonce, source, volumeId` | Request concurrent and download access restrictions. |
| `syncVolumeLicenses` | `EXEC` | `cpksver, nonce, source` | Request downloaded content access for specified volumes on the My eBooks shelf. |
| `updateUserSettings` | `EXEC` |  | Sets the settings for the user. If a sub-object is specified, it will overwrite the existing sub-object stored in the server. Unspecified sub-objects will retain the existing value. |
