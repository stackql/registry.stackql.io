---
title: apicategories
hide_title: false
hide_table_of_contents: false
keywords:
  - apicategories
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
<tr><td><b>Name</b></td><td><code>apicategories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.apicategories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `message` | `string` | Description of the operation. |
| `requestId` | `string` | ID that can be used to find request details in the log files. |
| `status` | `string` | Status of the operation. |
| `data` | `object` | the Api category resource. |
| `errorCode` | `string` | ID that can be used to find errors in the log files. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_sites_apicategories_get` | `SELECT` | `name` | Gets a category on the portal. |
| `organizations_sites_apicategories_list` | `SELECT` | `parent` | Lists the categories on the portal. |
| `organizations_sites_apicategories_create` | `INSERT` | `parent` | Creates a new category on the portal. |
| `organizations_sites_apicategories_delete` | `DELETE` | `name` | Deletes a category from the portal. |
| `organizations_sites_apicategories_patch` | `EXEC` | `name` | Updates a category on the portal. |
