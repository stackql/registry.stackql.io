---
title: webResource
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
<tr><td><b>Name</b></td><td><code>webResource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.siteVerification.webResource</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The string used to identify this site. This value should be used in the "id" portion of the REST URL for the Get, Update, and Delete operations. |
| `owners` | `array` | The email addresses of all verified owners. |
| `site` | `object` | The address and type of a site that is verified or will be verified. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id` | Get the most current data for a website or domain. |
| `list` | `SELECT` |  | Get the list of your verified websites and domains. |
| `insert` | `INSERT` | `verificationMethod` | Attempt verification of a website or domain. |
| `delete` | `DELETE` | `id` | Relinquish ownership of a website or domain. |
| `getToken` | `EXEC` |  | Get a verification token for placing on a website or domain. |
| `patch` | `EXEC` | `id` | Modify the list of owners for your website or domain. This method supports patch semantics. |
| `update` | `EXEC` | `id` | Modify the list of owners for your website or domain. |
