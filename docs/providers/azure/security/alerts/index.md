---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
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
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `description` | `string` | Description of the suspicious activity that was detected. |
| `processingEndTimeUtc` | `string` | The UTC processing end time of the alert in ISO8601 format. |
| `extendedLinks` | `array` | Links related to the alert |
| `vendorName` | `string` | The name of the vendor that raises the alert. |
| `resourceIdentifiers` | `array` | The resource identifiers that can be used to direct the alert to the right product exposure group (tenant, workspace, subscription etc.). There can be multiple identifiers of different type per alert. |
| `systemAlertId` | `string` | Unique identifier for the alert. |
| `alertDisplayName` | `string` | The display name of the alert. |
| `severity` | `string` | The risk level of the threat that was detected. Learn more: https://docs.microsoft.com/en-us/azure/security-center/security-center-alerts-overview#how-are-alerts-classified. |
| `startTimeUtc` | `string` | The UTC time of the first event or activity included in the alert in ISO8601 format. |
| `techniques` | `array` | kill chain related techniques behind the alert. |
| `timeGeneratedUtc` | `string` | The UTC time the alert was generated in ISO8601 format. |
| `compromisedEntity` | `string` | The display name of the resource most related to this alert. |
| `entities` | `array` | A list of entities related to the alert. |
| `endTimeUtc` | `string` | The UTC time of the last event or activity included in the alert in ISO8601 format. |
| `alertType` | `string` | Unique identifier for the detection logic (all alert instances from the same detection logic will have the same alertType). |
| `extendedProperties` | `object` | Custom properties for the alert. |
| `remediationSteps` | `array` | Manual action items to take to remediate the alert. |
| `alertUri` | `string` | A direct link to the alert page in Azure Portal. |
| `subTechniques` | `array` | Kill chain related sub-techniques behind the alert. |
| `intent` | `string` | The kill chain related intent behind the alert. For list of supported values, and explanations of Azure Security Center's supported kill chain intents. |
| `status` | `string` | The life cycle status of the alert. |
| `correlationKey` | `string` | Key for corelating related alerts. Alerts with the same correlation key considered to be related. |
| `version` | `string` | Schema version. |
| `isIncident` | `boolean` | This field determines whether the alert is an incident (a compound grouping of several alerts) or a single alert. |
| `supportingEvidence` | `object` | Changing set of properties depending on the supportingEvidence type. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `productName` | `string` | The name of the product which published this alert (Azure Security Center, Azure ATP, Microsoft Defender ATP, O365 ATP, MCAS, and so on). |
| `productComponentName` | `string` | The name of Azure Security Center pricing tier which powering this alert. Learn more: https://docs.microsoft.com/en-us/azure/security-center/security-center-pricing |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Alerts_List` | `SELECT` | `api-version, subscriptionId` | List all the alerts that are associated with the subscription |
| `Alerts_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List all the alerts that are associated with the resource group |
| `Alerts_GetResourceGroupLevel` | `EXEC` | `alertName, api-version, ascLocation, resourceGroupName, subscriptionId` | Get an alert that is associated a resource group or a resource in a resource group |
| `Alerts_GetSubscriptionLevel` | `EXEC` | `alertName, api-version, ascLocation, subscriptionId` | Get an alert that is associated with a subscription |
| `Alerts_ListResourceGroupLevelByRegion` | `EXEC` | `api-version, ascLocation, resourceGroupName, subscriptionId` | List all the alerts that are associated with the resource group that are stored in a specific location |
| `Alerts_ListSubscriptionLevelByRegion` | `EXEC` | `api-version, ascLocation, subscriptionId` | List all the alerts that are associated with the subscription that are stored in a specific location |
| `Alerts_Simulate` | `EXEC` | `api-version, ascLocation, subscriptionId` | Simulate security alerts |
| `Alerts_UpdateResourceGroupLevelStateToActivate` | `EXEC` | `alertName, api-version, ascLocation, resourceGroupName, subscriptionId` | Update the alert's state |
| `Alerts_UpdateResourceGroupLevelStateToDismiss` | `EXEC` | `alertName, api-version, ascLocation, resourceGroupName, subscriptionId` | Update the alert's state |
| `Alerts_UpdateResourceGroupLevelStateToInProgress` | `EXEC` | `alertName, api-version, ascLocation, resourceGroupName, subscriptionId` | Update the alert's state |
| `Alerts_UpdateResourceGroupLevelStateToResolve` | `EXEC` | `alertName, api-version, ascLocation, resourceGroupName, subscriptionId` | Update the alert's state |
| `Alerts_UpdateSubscriptionLevelStateToActivate` | `EXEC` | `alertName, api-version, ascLocation, subscriptionId` | Update the alert's state |
| `Alerts_UpdateSubscriptionLevelStateToDismiss` | `EXEC` | `alertName, api-version, ascLocation, subscriptionId` | Update the alert's state |
| `Alerts_UpdateSubscriptionLevelStateToInProgress` | `EXEC` | `alertName, api-version, ascLocation, subscriptionId` | Update the alert's state |
| `Alerts_UpdateSubscriptionLevelStateToResolve` | `EXEC` | `alertName, api-version, ascLocation, subscriptionId` | Update the alert's state |
