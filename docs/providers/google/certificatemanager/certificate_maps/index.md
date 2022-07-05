---
title: certificate_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_maps
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
<tr><td><b>Name</b></td><td><code>certificate_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.certificatemanager.certificate_maps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | A user-defined name of the Certificate Map. Certificate Map names must be unique globally and match pattern `projects/*/locations/*/certificateMaps/*`. |
| `description` | `string` | One or more paragraphs of text description of a certificate map. |
| `updateTime` | `string` | Output only. The update timestamp of a Certificate Map. |
| `createTime` | `string` | Output only. The creation timestamp of a Certificate Map. |
| `gclbTargets` | `array` | Output only. A list of GCLB targets which use this Certificate Map. |
| `labels` | `object` | Set of labels associated with a Certificate Map. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_certificateMaps_get` | `SELECT` | `name` | Gets details of a single CertificateMap. |
| `projects_locations_certificateMaps_list` | `SELECT` | `parent` | Lists CertificateMaps in a given project and location. |
| `projects_locations_certificateMaps_create` | `INSERT` | `parent` | Creates a new CertificateMap in a given project and location. |
| `projects_locations_certificateMaps_delete` | `DELETE` | `name` | Deletes a single CertificateMap. A Certificate Map can't be deleted if it contains Certificate Map Entries. Remove all the entries from the map before calling this method. |
| `projects_locations_certificateMaps_patch` | `EXEC` | `name` | Updates a CertificateMap. |
