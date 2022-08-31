---
title: pricings
hide_title: false
hide_table_of_contents: false
keywords:
  - pricings
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
<tr><td><b>Name</b></td><td><code>pricings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.pricings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `subPlan` | `string` | The sub-plan selected for a Standard pricing configuration, when more than one sub-plan is available. Each sub-plan enables a set of security features. When not specified, full plan is applied. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `deprecated` | `boolean` | Optional. True if the plan is deprecated. If there are replacing plans they will appear in `replacedBy` property |
| `freeTrialRemainingTime` | `string` | The duration left for the subscriptions free trial period - in ISO 8601 format (e.g. P3Y6M4DT12H30M5S). |
| `pricingTier` | `string` | The pricing tier value. Microsoft Defender for Cloud is provided in two pricing tiers: free and standard, with the standard tier available with a trial period. The standard tier offers advanced security capabilities, while the free tier offers basic security features. |
| `replacedBy` | `array` | Optional. List of plans that replace this plan. This property exists only if this plan is deprecated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Pricings_List` | `SELECT` | `api-version, subscriptionId` | Lists Microsoft Defender for Cloud pricing configurations in the subscription. |
| `Pricings_Get` | `EXEC` | `api-version, pricingName, subscriptionId` | Gets a provided Microsoft Defender for Cloud pricing configuration in the subscription. |
| `Pricings_Update` | `EXEC` | `api-version, pricingName, subscriptionId` | Updates a provided Microsoft Defender for Cloud pricing configuration in the subscription. |
