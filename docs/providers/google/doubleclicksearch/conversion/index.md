---
title: conversion
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
<tr><td><b>Name</b></td><td><code>conversion</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.doubleclicksearch.conversion</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `conversion` | `array` | The conversions being requested. |
| `kind` | `string` | Identifies this as a ConversionList resource. Value: the fixed string doubleclicksearch#conversionList. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `advertiserId, agencyId, endDate, engineAccountId, rowCount, startDate, startRow` | Retrieves a list of conversions from a DoubleClick Search engine account. |
| `insert` | `INSERT` |  | Inserts a batch of new conversions into DoubleClick Search. |
| `update` | `EXEC` |  | Updates a batch of conversions in DoubleClick Search. |
| `updateAvailability` | `EXEC` |  | Updates the availabilities of a batch of floodlight activities in DoubleClick Search. |