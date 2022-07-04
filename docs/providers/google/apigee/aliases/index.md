---
title: aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - aliases
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
<tr><td><b>Name</b></td><td><code>aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.aliases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `alias` | `string` | Resource ID for this alias. Values must match the regular expression `[^/]{1,255}`. |
| `certsInfo` | `object` |  |
| `type` | `string` | Type of alias. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_environments_keystores_aliases_get` | `SELECT` | `name` | Gets an alias. |
| `organizations_environments_keystores_aliases_create` | `INSERT` | `parent` | Creates an alias from a key/certificate pair. The structure of the request is controlled by the `format` query parameter: - `keycertfile` - Separate PEM-encoded key and certificate files are uploaded. Set `Content-Type: multipart/form-data` and include the `keyFile`, `certFile`, and `password` (if keys are encrypted) fields in the request body. If uploading to a truststore, omit `keyFile`. - `pkcs12` - A PKCS12 file is uploaded. Set `Content-Type: multipart/form-data`, provide the file in the `file` field, and include the `password` field if the file is encrypted in the request body. - `selfsignedcert` - A new private key and certificate are generated. Set `Content-Type: application/json` and include CertificateGenerationSpec in the request body. |
| `organizations_environments_keystores_aliases_delete` | `DELETE` | `name` | Deletes an alias. |
| `organizations_environments_keystores_aliases_csr` | `EXEC` | `name` | Generates a PKCS #10 Certificate Signing Request for the private key in an alias. |
| `organizations_environments_keystores_aliases_update` | `EXEC` | `name` | Updates the certificate in an alias. |