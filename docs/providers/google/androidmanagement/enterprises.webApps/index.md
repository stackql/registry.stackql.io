---
title: enterprises.webApps
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
<tr><td><b>Name</b></td><td><code>enterprises.webApps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidmanagement.enterprises.webApps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `nextPageToken` | `string` | If there are more results, a token to retrieve next page of results. |
| `webApps` | `array` | The list of web apps. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `enterprisesId, webAppsId` | Gets a web app. |
| `list` | `SELECT` | `enterprisesId` | Lists web apps for a given enterprise. |
| `create` | `INSERT` | `enterprisesId` | Creates a web app. |
| `delete` | `DELETE` | `enterprisesId, webAppsId` | Deletes a web app. |
| `patch` | `EXEC` | `enterprisesId, webAppsId` | Updates a web app. |
