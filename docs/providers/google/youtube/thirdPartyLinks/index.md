---
title: thirdPartyLinks
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
<tr><td><b>Name</b></td><td><code>thirdPartyLinks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.youtube.thirdPartyLinks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `etag` | `string` | Etag of this resource |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#thirdPartyLink". |
| `linkingToken` | `string` | The linking_token identifies a YouTube account and channel with which the third party account is linked. |
| `snippet` | `object` | Basic information about a third party account link, including its type and type-specific information. |
| `status` | `object` | The third-party link status object contains information about the status of the link. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list` | `SELECT` | `part` | Retrieves a list of resources, possibly filtered. |
| `insert` | `INSERT` | `part` | Inserts a new resource into this collection. |
| `delete` | `DELETE` | `linkingToken, type` | Deletes a resource. |
| `update` | `EXEC` | `part` | Updates an existing resource. |
