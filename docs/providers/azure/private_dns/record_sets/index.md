---
title: record_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - record_sets
  - private_dns
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
<tr><td><b>Id</b></td><td><code>azure.private_dns.record_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the record set. |
| `name` | `string` | The name of the record set. |
| `isAutoRegistered` | `boolean` | Is the record set auto-registered in the Private DNS zone through a virtual network link? |
| `type` | `string` | The type of the record set. |
| `txtRecords` | `array` | The list of TXT records in the record set. |
| `etag` | `string` | The ETag of the record set. |
| `mxRecords` | `array` | The list of MX records in the record set. |
| `cnameRecord` | `object` | A CNAME record. |
| `soaRecord` | `object` | An SOA record. |
| `ttl` | `integer` | The TTL (time-to-live) of the records in the record set. |
| `aRecords` | `array` | The list of A records in the record set. |
| `ptrRecords` | `array` | The list of PTR records in the record set. |
| `aaaaRecords` | `array` | The list of AAAA records in the record set. |
| `metadata` | `object` | The metadata attached to the record set. |
| `fqdn` | `string` | Fully qualified domain name of the record set. |
| `srvRecords` | `array` | The list of SRV records in the record set. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RecordSets_List` | `SELECT` | `privateZoneName, resourceGroupName, subscriptionId` | Lists all record sets in a Private DNS zone. |
| `RecordSets_ListByType` | `SELECT` | `privateZoneName, recordType, resourceGroupName, subscriptionId` | Lists the record sets of a specified type in a Private DNS zone. |
| `RecordSets_CreateOrUpdate` | `INSERT` | `privateZoneName, recordType, relativeRecordSetName, resourceGroupName, subscriptionId` | Creates or updates a record set within a Private DNS zone. |
| `RecordSets_Delete` | `DELETE` | `privateZoneName, recordType, relativeRecordSetName, resourceGroupName, subscriptionId` | Deletes a record set from a Private DNS zone. This operation cannot be undone. |
| `RecordSets_Get` | `EXEC` | `privateZoneName, recordType, relativeRecordSetName, resourceGroupName, subscriptionId` | Gets a record set. |
| `RecordSets_Update` | `EXEC` | `privateZoneName, recordType, relativeRecordSetName, resourceGroupName, subscriptionId` | Updates a record set within a Private DNS zone. |
