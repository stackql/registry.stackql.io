---
title: projects.deployments
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
<tr><td><b>Name</b></td><td><code>projects.deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.script.projects.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `deployments` | `array` | The list of deployments. |
| `nextPageToken` | `string` | The token that can be used in the next call to get the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deploymentId, scriptId` | Gets a deployment of an Apps Script project. |
| `list` | `SELECT` | `scriptId` | Lists the deployments of an Apps Script project. |
| `create` | `INSERT` | `scriptId` | Creates a deployment of an Apps Script project. |
| `delete` | `DELETE` | `deploymentId, scriptId` | Deletes a deployment of an Apps Script project. |
| `update` | `EXEC` | `deploymentId, scriptId` | Updates a deployment of an Apps Script project. |
