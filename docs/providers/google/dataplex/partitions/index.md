---
title: partitions
hide_title: false
hide_table_of_contents: false
keywords:
  - partitions
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.partitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Partition values used in the HTTP URL must be double encoded. For example, url_encode(url_encode(value)) can be used to encode "US:CA/CA#Sunnyvale so that the request URL ends with "/partitions/US%253ACA/CA%2523Sunnyvale". The name field in the response retains the encoded format. |
| `etag` | `string` | Optional. The etag for this partition. |
| `location` | `string` | Required. Immutable. The location of the entity data within the partition, for example, gs://bucket/path/to/entity/key1=value1/key2=value2. Or projects//datasets//tables/ |
| `values` | `array` | Required. Immutable. The set of values representing the partition, which correspond to the partition schema defined in the parent entity. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_zones_entities_partitions_get` | `SELECT` | `name` | Get a metadata partition of an entity. |
| `projects_locations_lakes_zones_entities_partitions_list` | `SELECT` | `parent` | List metadata partitions of an entity. |
| `projects_locations_lakes_zones_entities_partitions_create` | `INSERT` | `parent` | Create a metadata partition. |
| `projects_locations_lakes_zones_entities_partitions_delete` | `DELETE` | `name` | Delete a metadata partition. |