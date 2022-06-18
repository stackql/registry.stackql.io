---
title: projects
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
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquery.projects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `etag` | `string` | A hash of the page of results |
| `kind` | `string` | The type of list. |
| `nextPageToken` | `string` | A token to request the next page of results. |
| `projects` | `array` | Projects to which you have at least READ access. |
| `totalItems` | `integer` | The total number of projects in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list` | `SELECT` |  | Lists all projects to which you have been granted any project role. |
| `getServiceAccount` | `EXEC` | `projectId` | Returns the email address of the service account for your project used for interactions with Google Cloud KMS. |
