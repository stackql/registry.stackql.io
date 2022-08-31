---
title: record_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - record_sets
  - dns
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
<tr><td><b>Name</b></td><td><code>record_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dns.record_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the record set. |
| `name` | `string` | The name of the record set. |
| `TTL` | `integer` | The TTL (time-to-live) of the records in the record set. |
| `MXRecords` | `array` | The list of MX records in the record set. |
| `etag` | `string` | The etag of the record set. |
| `fqdn` | `string` | Fully qualified domain name of the record set. |
| `SOARecord` | `object` | An SOA record. |
| `AAAARecords` | `array` | The list of AAAA records in the record set. |
| `NSRecords` | `array` | The list of NS records in the record set. |
| `TXTRecords` | `array` | The list of TXT records in the record set. |
| `PTRRecords` | `array` | The list of PTR records in the record set. |
| `ARecords` | `array` | The list of A records in the record set. |
| `provisioningState` | `string` | provisioning State of the record set. |
| `CNAMERecord` | `object` | A CNAME record. |
| `SRVRecords` | `array` | The list of SRV records in the record set. |
| `targetResource` | `object` | A reference to a another resource |
| `caaRecords` | `array` | The list of CAA records in the record set. |
| `type` | `string` | The type of the record set. |
| `metadata` | `object` | The metadata attached to the record set. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RecordSets_ListByDnsZone` | `SELECT` | `resourceGroupName, subscriptionId, zoneName` | Lists all record sets in a DNS zone. |
| `RecordSets_ListByType` | `SELECT` | `recordType, resourceGroupName, subscriptionId, zoneName` | Lists the record sets of a specified type in a DNS zone. |
| `RecordSets_CreateOrUpdate` | `INSERT` | `recordType, relativeRecordSetName, resourceGroupName, subscriptionId, zoneName` | Creates or updates a record set within a DNS zone. |
| `RecordSets_Delete` | `DELETE` | `recordType, relativeRecordSetName, resourceGroupName, subscriptionId, zoneName` | Deletes a record set from a DNS zone. This operation cannot be undone. |
| `RecordSets_Get` | `EXEC` | `recordType, relativeRecordSetName, resourceGroupName, subscriptionId, zoneName` | Gets a record set. |
| `RecordSets_ListAllByDnsZone` | `EXEC` | `resourceGroupName, subscriptionId, zoneName` | Lists all record sets in a DNS zone. |
| `RecordSets_Update` | `EXEC` | `recordType, relativeRecordSetName, resourceGroupName, subscriptionId, zoneName` | Updates a record set within a DNS zone. |
