---
title: product_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - product_secrets
  - deployment_admin
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>product_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.deployment_admin.product_secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `description` | `string` | The secret description. |
| `secretDescriptor` | `object` | The secret type-specific descriptor. |
| `secretState` | `object` | Represents the secret state. |
| `type` | `string` | Type of Resource. |
| `provisioningState` | `string` | Provisioning state of the resource. |
| `location` | `string` | Location of the resource. |
| `secretKind` | `string` | Specifies the secret kind. |
| `expiresAfter` | `string` | The expiration period of the secret (in ISO8601 format). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProductSecrets_List` | `SELECT` | `packageId, subscriptionId` | Returns an array of product secrets. |
| `ProductSecrets_GET` | `EXEC` | `packageId, secretName, subscriptionId` | Returns the specific product secret. |
| `ProductSecrets_Set` | `EXEC` | `packageId, secretName, subscriptionId` | Imports a product secret. |
| `ProductSecrets_Validate` | `EXEC` | `packageId, secretName, subscriptionId` | Validates a product secret. |
