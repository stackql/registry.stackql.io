---
title: spaces.members
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
<tr><td><b>Name</b></td><td><code>spaces.members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.chat.spaces.members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `memberships` | `array` | List of memberships in the requested (or first) page. |
| `nextPageToken` | `string` | Continuation token to retrieve the next page of results. It will be empty for the last page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `membersId, spacesId` | Gets the metadata of a message attachment. The attachment data is fetched using the media API. |
| `list` | `SELECT` | `spacesId` | Lists human memberships in a space. |
