---
title: management.uploads
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
<tr><td><b>Name</b></td><td><code>management.uploads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analytics.management.uploads</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | A unique ID for this upload. |
| `customDataSourceId` | `string` | Custom data source Id to which this data import belongs. |
| `errors` | `array` | Data import errors collection. |
| `kind` | `string` | Resource type for Analytics upload. |
| `status` | `string` | Upload status. Possible values: PENDING, COMPLETED, FAILED, DELETING, DELETED. |
| `uploadTime` | `string` | Time this file is uploaded. |
| `accountId` | `string` | Account Id to which this upload belongs. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `accountId, customDataSourceId, uploadId, webPropertyId` | List uploads to which the user has access. |
| `list` | `SELECT` | `accountId, customDataSourceId, webPropertyId` | List uploads to which the user has access. |
| `deleteUploadData` | `EXEC` | `accountId, customDataSourceId, webPropertyId` | Delete data associated with a previous upload. |
| `uploadData` | `EXEC` | `accountId, customDataSourceId, webPropertyId` | Upload data for a custom data source. |
