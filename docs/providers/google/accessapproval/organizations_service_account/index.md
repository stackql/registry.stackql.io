---
title: organizations_service_account
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations_service_account
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
<tr><td><b>Name</b></td><td><code>organizations_service_account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.accessapproval.organizations_service_account</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the Access Approval service account. Format is one of: * "projects/{project}/serviceAccount" * "folders/{folder}/serviceAccount" * "organizations/{organization}/serviceAccount" |
| `accountEmail` | `string` | Email address of the service account. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_getServiceAccount` | `SELECT` | `name` |