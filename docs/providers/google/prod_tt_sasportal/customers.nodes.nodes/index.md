---
title: customers.nodes.nodes
hide_title: false
hide_table_of_contents: false
keywords:
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
<tr><td><b>Name</b></td><td><code>customers.nodes.nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.prod_tt_sasportal.customers.nodes.nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nodes` | `array` | The nodes that match the request. |
| `nextPageToken` | `string` | A pagination token returned from a previous call to ListNodes that indicates from where listing should continue. If the field is missing or empty, it means there is no more nodes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `customersId, nodesId` | Lists nodes. |
| `create` | `INSERT` | `customersId, nodesId` | Creates a new node. |
