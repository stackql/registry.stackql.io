---
title: keystores
hide_title: false
hide_table_of_contents: false
keywords:
  - keystores
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
<tr><td><b>Name</b></td><td><code>keystores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.keystores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Resource ID for this keystore. Values must match the regular expression `[\w[:space:]-.]{1,255}`. |
| `aliases` | `array` | Output only. Aliases in this keystore. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_environments_keystores_get` | `SELECT` | `name` | Gets a keystore or truststore. |
| `organizations_environments_keystores_create` | `INSERT` | `parent` | Creates a keystore or truststore. - Keystore: Contains certificates and their associated keys. - Truststore: Contains trusted certificates used to validate a server's certificate. These certificates are typically self-signed certificates or certificates that are not signed by a trusted CA. |
| `organizations_environments_keystores_delete` | `DELETE` | `name` | Deletes a keystore or truststore. |
