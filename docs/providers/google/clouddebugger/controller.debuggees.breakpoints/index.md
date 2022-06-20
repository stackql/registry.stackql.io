---
title: controller.debuggees.breakpoints
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
<tr><td><b>Name</b></td><td><code>controller.debuggees.breakpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.clouddebugger.controller.debuggees.breakpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `breakpoints` | `array` | List of all active breakpoints. The fields `id` and `location` are guaranteed to be set on each breakpoint. |
| `nextWaitToken` | `string` | A token that can be used in the next method call to block until the list of breakpoints changes. |
| `waitExpired` | `boolean` | If set to `true`, indicates that there is no change to the list of active breakpoints and the server-selected timeout has expired. The `breakpoints` field would be empty and should be ignored. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `debuggeeId` | Returns the list of all active breakpoints for the debuggee. The breakpoint specification (`location`, `condition`, and `expressions` fields) is semantically immutable, although the field values may change. For example, an agent may update the location line number to reflect the actual line where the breakpoint was set, but this doesn't change the breakpoint semantics. This means that an agent does not need to check if a breakpoint has changed when it encounters the same breakpoint on a successive call. Moreover, an agent should remember the breakpoints that are completed until the controller removes them from the active list to avoid setting those breakpoints again. |
| `update` | `EXEC` | `debuggeeId, id` | Updates the breakpoint state or mutable fields. The entire Breakpoint message must be sent back to the controller service. Updates to active breakpoint fields are only allowed if the new value does not change the breakpoint specification. Updates to the `location`, `condition` and `expressions` fields should not alter the breakpoint semantics. These may only make changes such as canonicalizing a value or snapping the location to the correct line of code. |
