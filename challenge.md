---
layout: default
---

<!-- # RoboSoft'25: The 1st International Workshop on Vision-Language in Soft Robot -->

## Leaderboard

**Registration**: 
All teams wishing to participate and obtain official eligibility must register [**here**](https://docs.google.com/forms/d/e/1FAIpQLSfB8juyzKzP6jKH_FEaU1uvsNvvtUHRSvgDkfoKe7vgLzBywA/viewform?usp=dialog), and may update team member information afterward. 

**Submission**: All teams may submit docker images [**here**](https://docs.google.com/forms/d/e/1FAIpQLSf6Nyh0vGb96X2tio6RIXlFlZ0eD95sv6HYVG9OAd411RxCzw/viewform?usp=header).
>Note: If multiple submissions are made, the **best** one shall prevail.

<table>
    <caption><b>VLM</b></caption>
    <tr>
      <th>Team ID</th>
      <th>Name</th>
      <th>Score</th>
      <th>Submit Time</th>
    </tr>
    <tr>
      <td>4c1593</td>
      <td>SoftVisioBots</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
</table>

<table>
    <caption><b>VLN</b></caption>
    <tr>
      <th>Team ID</th>
      <th>Name</th>
      <th>Score</th>
      <th>Submit Time</th>
    </tr>
    <tr>
      <td>4c1593</td>
      <td>SoftVisioBots</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
</table>


*The above tables are updated every two days.

## Data Details

[**Download VLM data**](https://openxlab.org.cn/datasets/JobsWei/RoboSoft2025-VLM)

[**Download VLN data**](https://openxlab.org.cn/datasets/JobsWei/RoboSoft2025-VLN)

The data directory structure is as follows:
```plaintext
release
├── annotations.json
├── scenarios
│   ├── 0
│   │   └── config.yaml
│   ├── ...
│   └── 99
└── trajectories
    ├── 0
    │   ├── actions.json (only exists for VLN tasks)
    │   ├── state_action.pkl
    │   └── visual
    │       ├── step_00000.png
    │       ├── step_00001.png
    │       └── ...
    ├── ...
    └── 99
```

`scenarios` directory stores the environmental configurations.

`trajectories` directory stores data annotations corresponding to each piece of data, with folders named by the data's id. 

`visual` directory stores visualization renderings of the task process from top-down view. The visualizations provided in the dataset are rendered every 1333 simulation time steps (i.e., 1333 time steps between two frames). For more fine-grained visualization, users can render independently. 

**File Details**

`config.yaml` contains configuration information for the simulation environment.
<details>
<summary class="example-btn">Example</summary>

<pre><code class="language-yaml">objects:
- center:
  - 0.4863890172516796
  - 0.2153593989325976
  - 3.1806980291836973
  color: ''
  mesh_path: ./assets/cylinder.stl
  scale:
  - 0.215
  - 0.215
  - 0.215
  shape: cylinder
  type: mesh_surface
- center:
  - 2.8291035111323892
  - 0.23340298631651013
  - 4.21278268891604
  density: 1.0
  radius: 0.23340298631651013
  type: sphere

rod:
  base_length: 0.5
  base_radius: 0.025
  density: 1000
  direction:
  - 0.0
  - 0.0
  - 1.0
  n_elem: 20
  normal:
  - 0.0
  - 1.0
  - 0.0
  poisson_ratio: 0.5
  start:
  - 0.0
  - 0.0
  - 0.0
  youngs_modulus: 10000000
simulator:
  collect_data: true
  final_time: 10.0
  rendering_fps: 15
  time_step: 5.0e-05
  update_interval: 1
</code></pre>
</details>

| Keyword   | Meaning                                                                                                                                                                  |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| objects   | Configurations for all objects in the environment except the soft robot, including basic types such as sphere and mesh surface.                                          |
| rod       | Configuration for the Cosserat rod simulating the soft robot; parameters are not recommended to be modified.                                                             |
| simulator | Simulator-related configurations. The maximum simulation duration can be adjusted by modifying the final_time field; other parameters are not recommended to be changed. |

`annotations.json` contains all annotation information.

<details>
<summary class="example-btn">Example</summary>

<pre><code class="language-json">// VLM
[
    {
        "id": 0,
        "target_object_id": 5,
        "target_position_id": 6,
        "instruction": "Pick up the basketball and place it in the gray zone."
    },
    {
        "id": 1,
        "target_object_id": 5,
        "target_position_id": 6,
        "instruction": "Pick up the red book and place it in the gray zone."
    }
]
// VLN
[
    {
        "id": 0,
        "target_id": 10,
        "description": "Explore the environment and find: indigo hemisphere, remember to carefully cross any potential obstacles."
    },
    {
        "id": 1,
        "target_id": 10,
        "description": "Navigate to: red cone, ensuring you avoid all obstacles to arrive safely."
    }
]

</code></pre>
</details>

| Keyword     | Meaning |
| ----------- | ---------|
| id          | The data id. The corresponding environmental configuration and data annotations are in subfolders named by the id within the trajectories folder. |
| target_id   | (VLN) ID of the target object in the environment.|
| target_object_id   | (VLM) ID of the target object in the environment.|
| target_position_id   | (VLM) ID of the target position in the environment, mainly used for simulation environment construction.|
| instruction | Text guidance for the task. |

`state_actions.pkl` stores data annotations of actions executed and the soft robot's state for completing the current task.

| Keyword     | Meaning  |
| ----------- | --------------------|
| rod_time    | (n_time_steps, ), recording the time instants corresponding to the rod's positions. |
| torque_time | (n_time_steps, ), recording the time instants of applied torques.  |
| position    | (n_time_steps, 3, n_elem+1), position information of the rod at each time step. 3 denotes the number of spatial coordinates, and n_elem is the total number of rod segments (details can be found in Cosserat rod simulation methods). Positions record the start and end positions of each segment rather than the center, hence the third dimension is n_elem+1 instead of n_elem. |
| velocity    | (n_time_steps, 3, n_elem+1), velocity information of the rod at each time step, with each dimension defined as above. |

For VLN, we have encapsulated higher-level atomic actions (i.e., move forward, turn left, turn right) and map these actions to torques for control. The atomic actions taken to complete the task in `actions.json` are formatted as `timestep: action_type`. For time steps not explicitly specified, the action from the nearest specified time step is maintained. The torques corresponding to these atomic actions are exactly the torques recorded in state_actions.pkl.

<details>
<summary class="example-btn">Example</summary>

<pre><code class="language-json">{"9000": 1, "43000": 2, "49000": 1}
</code></pre>
</details>

<style>
.example-btn {
  display: inline-block;
  padding: 4px 12px;
  background: #1e6bb8;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-weight: bold;
  cursor: pointer;
  font-size: 1em;
  margin-bottom: 10px;
}
details[open] .example-btn {
  background: #005a9e;
}
</style>

## Development Toolkit

During this workshop, we provide a base Docker image for teams to set up environment. The image is pre-configured with dependencies for Elastica and PyTorch, and can be obtained via the link: TBD (Estimated Availability Time: June 13th)

To build base environment container, you can follow the steps below:
```
docker pull <images>
docker run -v <data_path>:/app/data -d --name <name> -it <images> /bin/bash
```

Teams are required to develop programs based on the provided base image, push the image to Docker Hub, and submit the image URL on Docker Hub. We will use this image for testing.

Specifically, we will mount the test data into the container directory `/app/data` via `docker run -v`, so **please ensure the `/app/data` directory in the image is empty.**

After mounting, the following directory structure will be obtained. Teams should maintain the file layout and complete the task based on this structure.

```plaintext
/app/data
├── VLN
└── VLM
```

<style>
details summary {
  list-style: revert;
  cursor: pointer;
}
</style>