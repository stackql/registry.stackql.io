---
title: information_protection_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - information_protection_policies
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
<tr><td><b>Name</b></td><td><code>information_protection_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.information_protection_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `informationTypes` | `object` | The sensitivity information types. |
| `labels` | `object` | Dictionary of sensitivity labels. |
| `lastModifiedUtc` | `string` | Describes the last UTC time the policy was modified. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `version` | `string` | Describes the version of the policy. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `InformationProtectionPolicies_List` | `SELECT` | `api-version, scope` | Information protection policies of a specific management group. |
| `InformationProtectionPolicies_CreateOrUpdate` | `INSERT` | `api-version, informationProtectionPolicyName, scope` | Details of the information protection policy. |
| `InformationProtectionPolicies_Get` | `EXEC` | `api-version, informationProtectionPolicyName, scope` | Details of the information protection policy. |
