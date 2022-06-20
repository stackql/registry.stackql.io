---
title: systemapks.variants
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
<tr><td><b>Name</b></td><td><code>systemapks.variants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidpublisher.systemapks.variants</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `packageName, variantId, versionCode` | Returns a previously created system APK variant. |
| `list` | `SELECT` | `packageName, versionCode` | Returns the list of previously created system APK variants. |
| `create` | `INSERT` | `packageName, versionCode` | Creates an APK which is suitable for inclusion in a system image from an already uploaded Android App Bundle. |
| `download` | `EXEC` | `packageName, variantId, versionCode` | Downloads a previously created system APK which is suitable for inclusion in a system image. |
