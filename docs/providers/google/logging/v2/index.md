---
title: v2
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
<tr><td><b>Name</b></td><td><code>v2</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.logging.v2</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getCmekSettings` | `EXEC` | `v2Id, v2Id1` | Gets the Logs Router CMEK settings for the given resource.Note: CMEK for the Logs Router can currently only be configured for Google Cloud organizations. Once configured, it applies to all projects and folders in the Google Cloud organization.See Enabling CMEK for Logs Router (https://cloud.google.com/logging/docs/routing/managed-encryption) for more information. |
| `updateCmekSettings` | `EXEC` | `v2Id, v2Id1` | Updates the Logs Router CMEK settings for the given resource.Note: CMEK for the Logs Router can currently only be configured for Google Cloud organizations. Once configured, it applies to all projects and folders in the Google Cloud organization.UpdateCmekSettings will fail if 1) kms_key_name is invalid, or 2) the associated service account does not have the required roles/cloudkms.cryptoKeyEncrypterDecrypter role assigned for the key, or 3) access to the key is disabled.See Enabling CMEK for Logs Router (https://cloud.google.com/logging/docs/routing/managed-encryption) for more information. |