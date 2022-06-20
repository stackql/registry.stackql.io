---
title: webapps
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
<tr><td><b>Name</b></td><td><code>webapps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidenterprise.webapps</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `enterpriseId, webAppId` | Gets an existing web app. |
| `list` | `SELECT` | `enterpriseId` | Retrieves the details of all web apps for a given enterprise. |
| `insert` | `INSERT` | `enterpriseId` | Creates a new web app for the enterprise. |
| `delete` | `DELETE` | `enterpriseId, webAppId` | Deletes an existing web app. |
| `update` | `EXEC` | `enterpriseId, webAppId` | Updates an existing web app. |
