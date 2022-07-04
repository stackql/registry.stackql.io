---
title: policysimulator
hide_title: false
hide_table_of_contents: false
keywords:
  - policysimulator
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
 Policy Simulator is a collection of endpoints for creating, running, and viewing a Replay. A `Replay` is a type of simulation that lets you see how your members' access to resources might change if you changed your IAM policy. During a `Replay`, Policy Simulator re-evaluates, or replays, past access attempts under both the current policy and your proposed policy, and compares those results to determine how your members' access might change under the proposed policy.  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>google.policysimulator</code></td></tr>
<tr><td><b>Type</b></td><td>Service</td></tr>
<tr><td><b>Title</b></td><td>Policy Simulator API</td></tr>
<tr><td><b>Description</b></td><td> Policy Simulator is a collection of endpoints for creating, running, and viewing a Replay. A `Replay` is a type of simulation that lets you see how your members' access to resources might change if you changed your IAM policy. During a `Replay`, Policy Simulator re-evaluates, or replays, past access attempts under both the current policy and your proposed policy, and compares those results to determine how your members' access might change under the proposed policy.</td></tr>
<tr><td><b>Id</b></td><td><code>policysimulator:v1.0.0</code></td></tr>
</tbody></table>

## Resources
<div class="row">
<div class="providerDocColumn">
<a href="/providers/google/policysimulator/operations/">operations</a><br />
<a href="/providers/google/policysimulator/replays/">replays</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/google/policysimulator/results/">results</a><br />
</div>
</div>