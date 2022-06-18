---
title: projects.androidApps.sha
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
<tr><td><b>Name</b></td><td><code>projects.androidApps.sha</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.firebase.projects.androidApps.sha</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list` | `SELECT` | `androidAppsId, projectsId` | Lists the SHA-1 and SHA-256 certificates for the specified AndroidApp. |
| `create` | `INSERT` | `androidAppsId, projectsId` | Adds a ShaCertificate to the specified AndroidApp. |
| `delete` | `DELETE` | `androidAppsId, projectsId, shaId` | Removes a ShaCertificate from the specified AndroidApp. |
