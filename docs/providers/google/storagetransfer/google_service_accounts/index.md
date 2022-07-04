---
title: google_service_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - google_service_accounts
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
<tr><td><b>Name</b></td><td><code>google_service_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.storagetransfer.google_service_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `subjectId` | `string` | Unique identifier for the service account. |
| `accountEmail` | `string` | Email address of the service account. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `googleServiceAccounts_get` | `SELECT` | `projectId` |
