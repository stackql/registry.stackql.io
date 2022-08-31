---
title: backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_policies
  - recovery_services_backup
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
<tr><td><b>Name</b></td><td><code>backup_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.backup_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id represents the complete path to the resource. |
| `name` | `string` | Resource name associated with the resource. |
| `type` | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
| `eTag` | `string` | Optional ETag. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Base class for backup policy. Workload-specific backup policies are derived from this class. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `BackupPolicies_List` | `SELECT` | `api-version, resourceGroupName, subscriptionId, vaultName` |