---
title: regulatory_compliance_standards
hide_title: false
hide_table_of_contents: false
keywords:
  - regulatory_compliance_standards
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
<tr><td><b>Name</b></td><td><code>regulatory_compliance_standards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.regulatory_compliance_standards</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `unsupportedControls` | `integer` | The number of regulatory compliance controls of the given standard which are unsupported by automated assessments |
| `failedControls` | `integer` | The number of supported regulatory compliance controls of the given standard with a failed state |
| `passedControls` | `integer` | The number of supported regulatory compliance controls of the given standard with a passed state |
| `skippedControls` | `integer` | The number of supported regulatory compliance controls of the given standard with a skipped state |
| `state` | `string` | Aggregative state based on the standard's supported controls states |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RegulatoryComplianceStandards_List` | `SELECT` | `api-version, subscriptionId` | Supported regulatory compliance standards details and state |
| `RegulatoryComplianceStandards_Get` | `EXEC` | `api-version, regulatoryComplianceStandardName, subscriptionId` | Supported regulatory compliance details state for selected standard |
