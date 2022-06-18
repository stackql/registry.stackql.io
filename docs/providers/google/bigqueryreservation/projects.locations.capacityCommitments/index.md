---
title: projects.locations.capacityCommitments
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
<tr><td><b>Name</b></td><td><code>projects.locations.capacityCommitments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigqueryreservation.projects.locations.capacityCommitments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `capacityCommitments` | `array` | List of capacity commitments visible to the user. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `capacityCommitmentsId, locationsId, projectsId` | Returns information about the reservation. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all the capacity commitments for the admin project. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new capacity commitment resource. |
| `delete` | `DELETE` | `capacityCommitmentsId, locationsId, projectsId` | Deletes a assignment. No expansion will happen. Example: * Organization `organizationA` contains two projects, `project1` and `project2`. * Reservation `res1` exists and was created previously. * CreateAssignment was used previously to define the following associations between entities and reservations: `` and `` In this example, deletion of the `` assignment won't affect the other assignment ``. After said deletion, queries from `project1` will still use `res1` while queries from `project2` will switch to use on-demand mode. |
| `merge` | `EXEC` | `locationsId, projectsId` | Merges capacity commitments of the same plan into a single commitment. The resulting capacity commitment has the greater commitment_end_time out of the to-be-merged capacity commitments. Attempting to merge capacity commitments of different plan will fail with the error code `google.rpc.Code.FAILED_PRECONDITION`. |
| `patch` | `EXEC` | `capacityCommitmentsId, locationsId, projectsId` | Updates an existing reservation resource. |
| `split` | `EXEC` | `capacityCommitmentsId, locationsId, projectsId` | Splits capacity commitment to two commitments of the same plan and `commitment_end_time`. A common use case is to enable downgrading commitments. For example, in order to downgrade from 10000 slots to 8000, you might split a 10000 capacity commitment into commitments of 2000 and 8000. Then, you would change the plan of the first one to `FLEX` and then delete it. |
