---
title: private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources
  - recovery_services
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
<tr><td><b>Name</b></td><td><code>private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services.private_link_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier of the resource. |
| `name` | `string` | Name of the resource. |
| `requiredZoneNames` | `array` | The private link resource Private link DNS zone name. |
| `type` | `string` | e.g. Microsoft.RecoveryServices/vaults/privateLinkResources |
| `groupId` | `string` | e.g. f9ad6492-33d4-4690-9999-6bfd52a0d081 (Backup) or f9ad6492-33d4-4690-9999-6bfd52a0d082 (SiteRecovery) |
| `requiredMembers` | `array` | [backup-ecs1, backup-prot1, backup-prot1b, backup-prot1c, backup-id1] |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PrivateLinkResources_List` | `SELECT` | `api-version, resourceGroupName, subscriptionId, vaultName` |
| `PrivateLinkResources_Get` | `EXEC` | `api-version, privateLinkResourceName, resourceGroupName, subscriptionId, vaultName` |
