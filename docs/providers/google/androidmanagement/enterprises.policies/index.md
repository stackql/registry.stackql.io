---
title: enterprises.policies
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
<tr><td><b>Name</b></td><td><code>enterprises.policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidmanagement.enterprises.policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `nextPageToken` | `string` | If there are more results, a token to retrieve next page of results. |
| `policies` | `array` | The list of policies. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `enterprisesId, policiesId` | Gets a web app. |
| `list` | `SELECT` | `enterprisesId` | Lists policies for a given enterprise. |
| `delete` | `DELETE` | `enterprisesId, policiesId` | Deletes a web app. |
| `patch` | `EXEC` | `enterprisesId, policiesId` | Updates a web app. |
