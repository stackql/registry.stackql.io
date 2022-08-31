---
title: component_current_billing_features
hide_title: false
hide_table_of_contents: false
keywords:
  - component_current_billing_features
  - application_insights
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
<tr><td><b>Name</b></td><td><code>component_current_billing_features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.component_current_billing_features</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ComponentCurrentBillingFeatures_Get` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Returns current billing features for an Application Insights component. |
| `ComponentCurrentBillingFeatures_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Update current billing features for an Application Insights component. |
