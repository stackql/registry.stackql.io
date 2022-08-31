---
title: auto_provisioning_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - auto_provisioning_settings
  - security
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
<tr><td><b>Name</b></td><td><code>auto_provisioning_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.auto_provisioning_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `autoProvision` | `string` | Describes what kind of security agent provisioning action to take |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AutoProvisioningSettings_List` | `SELECT` | `api-version, subscriptionId` | Exposes the auto provisioning settings of the subscriptions |
| `AutoProvisioningSettings_Create` | `INSERT` | `api-version, settingName, subscriptionId` | Details of a specific setting |
| `AutoProvisioningSettings_Get` | `EXEC` | `api-version, settingName, subscriptionId` | Details of a specific setting |