---
title: customchannels
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
<tr><td><b>Name</b></td><td><code>customchannels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.adsensehost.customchannels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier of this custom channel. This should be considered an opaque identifier; it is not safe to rely on it being in any particular format. |
| `name` | `string` | Name of this custom channel. |
| `kind` | `string` | Kind of resource this is, in this case adsensehost#customChannel. |
| `code` | `string` | Code of this custom channel, not necessarily unique across ad clients. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `adClientId, customChannelId` | Get a specific custom channel from the host AdSense account. |
| `list` | `SELECT` | `adClientId` | List all host custom channels in this AdSense account. |
| `insert` | `INSERT` | `adClientId` | Add a new custom channel to the host AdSense account. |
| `delete` | `DELETE` | `adClientId, customChannelId` | Delete a specific custom channel from the host AdSense account. |
| `patch` | `EXEC` | `adClientId, customChannelId` | Update a custom channel in the host AdSense account. This method supports patch semantics. |
| `update` | `EXEC` | `adClientId` | Update a custom channel in the host AdSense account. |
