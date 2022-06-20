---
title: spreadsheets
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
<tr><td><b>Name</b></td><td><code>spreadsheets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.sheets.spreadsheets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `namedRanges` | `array` | The named ranges defined in a spreadsheet. |
| `properties` | `object` | Properties of a spreadsheet. |
| `sheets` | `array` | The sheets that are part of a spreadsheet. |
| `spreadsheetId` | `string` | The ID of the spreadsheet. This field is read-only. |
| `spreadsheetUrl` | `string` | The url of the spreadsheet. This field is read-only. |
| `dataSourceSchedules` | `array` | Output only. A list of data source refresh schedules. |
| `dataSources` | `array` | A list of external data sources connected with the spreadsheet. |
| `developerMetadata` | `array` | The developer metadata associated with a spreadsheet. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `spreadsheetId` | Returns the spreadsheet at the given ID. The caller must specify the spreadsheet ID. By default, data within grids will not be returned. You can include grid data one of two ways: * Specify a field mask listing your desired fields using the `fields` URL parameter in HTTP * Set the includeGridData URL parameter to true. If a field mask is set, the `includeGridData` parameter is ignored For large spreadsheets, it is recommended to retrieve only the specific fields of the spreadsheet that you want. To retrieve only subsets of the spreadsheet, use the ranges URL parameter. Multiple ranges can be specified. Limiting the range will return only the portions of the spreadsheet that intersect the requested ranges. Ranges are specified using A1 notation. |
| `create` | `INSERT` |  | Creates a spreadsheet, returning the newly created spreadsheet. |
| `batchUpdate` | `EXEC` | `spreadsheetId` | Applies one or more updates to the spreadsheet. Each request is validated before being applied. If any request is not valid then the entire request will fail and nothing will be applied. Some requests have replies to give you some information about how they are applied. The replies will mirror the requests. For example, if you applied 4 updates and the 3rd one had a reply, then the response will have 2 empty replies, the actual reply, and another empty reply, in that order. Due to the collaborative nature of spreadsheets, it is not guaranteed that the spreadsheet will reflect exactly your changes after this completes, however it is guaranteed that the updates in the request will be applied together atomically. Your changes may be altered with respect to collaborator changes. If there are no collaborators, the spreadsheet should reflect your changes. |
| `getByDataFilter` | `EXEC` | `spreadsheetId` | Returns the spreadsheet at the given ID. The caller must specify the spreadsheet ID. This method differs from GetSpreadsheet in that it allows selecting which subsets of spreadsheet data to return by specifying a dataFilters parameter. Multiple DataFilters can be specified. Specifying one or more data filters will return the portions of the spreadsheet that intersect ranges matched by any of the filters. By default, data within grids will not be returned. You can include grid data one of two ways: * Specify a field mask listing your desired fields using the `fields` URL parameter in HTTP * Set the includeGridData parameter to true. If a field mask is set, the `includeGridData` parameter is ignored For large spreadsheets, it is recommended to retrieve only the specific fields of the spreadsheet that you want. |
