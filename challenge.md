---
layout: default
---

## Leaderboard

**Registration**: 
You may register for this workshop [here](https://docs.google.com/forms/d/e/1FAIpQLSfB8juyzKzP6jKH_FEaU1uvsNvvtUHRSvgDkfoKe7vgLzBywA/viewform?usp=dialog).

**Submission**: You may submit your docker images [here](https://docs.google.com/forms/d/e/1FAIpQLSf6Nyh0vGb96X2tio6RIXlFlZ0eD95sv6HYVG9OAd411RxCzw/viewform?usp=header).
>Note: If multiple submissions are made, the latest one shall prevail.

Here are the current leaderboards:
<div style="display: flex; gap: 16px; align-items: flex-start;">

  <div style="width:49%;">
    <div style="text-align:center; font-weight:bold; margin-bottom:4px;">VLM</div>
    <iframe
      src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRxMVn-R-tdqepDwJubsEkfj8WEwa8yvFSulfPrI-2w5JVhW6EApiEAIMSniS7TLbINwGjLPpLBd4dT/pubhtml?gid=0&single=true"
      width="100%"
      height="400">
    </iframe>
  </div>

  <div style="width:49%;">
    <div style="text-align:center; font-weight:bold; margin-bottom:4px;">VLN</div>
    <iframe
      src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQcPoNHvEU0nygRiqd1oKi-mX6NAsFxiR-28oLW-3KeNsgQIydgC4Jx3gYF3UsBUidxqlAf9wYjCUAj/pubhtml?gid=0&single=true"
      width="100%"
      height="400">
    </iframe>
  </div>

</div>

*The above tables are updated every two days.

## Data Details

### Task 1: Vision-Language Manipulation for Soft Robot

<a href="#" class="btn" style="margin-bottom:10px;">Download VLM data</a>


### Task 2: Vision-Language Navigation for Soft Robot

<a href="#" class="btn" style="margin-bottom:10px;">Download VLN data</a>

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
    │   ├── actions.json
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
<summary>Example</summary>

<pre><code class="language-yaml">
objects:
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
<summary>Example</summary>

<pre><code class="language-json">[
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
| id          | The data serial number. The corresponding environmental configuration and data annotations are in subfolders named by the id within the trajectories folder. |
| target_id   | The serial number of the target object in the environment, mainly used for simulation environment construction.|
| instruction | Text guidance for the task. |

`state_actions.pkl` stores data annotations of actions executed and the soft robot's state for completing the current task.

| Keyword     | Meaning  |
| ----------- | --------------------|
| rod_time    | (n_time_steps, ), recording the time instants corresponding to the rod's positions. |
| torque_time | (n_time_steps, ), recording the time instants of applied torques.  |
| position    | (n_time_steps, 3, n_elem+1), position information of the rod at each time step. 3 denotes the number of spatial coordinates, and n_elem is the total number of rod segments (details can be found in Cosserat rod simulation methods). Positions record the start and end positions of each segment rather than the center, hence the third dimension is n_elem+1 instead of n_elem. |
| velocity    | (n_time_steps, 3, n_elem+1), velocity information of the rod at each time step, with each dimension defined as above. |

## Development Toolkit

During this workshop, we provide a base Docker image for participants to set up their environment. The image is pre-configured with dependencies for Elastica and PyTorch, and can be obtained via the link: TBD

To build base environment container, you can follow the steps below:
```
docker pull <images>
docker run -v <data_path>:/app/data -d --name <name> -it <images> /bin/bash
```

Participants are required to develop programs based on the provided base image, push the image to Docker Hub, and submit the image URL on Docker Hub. We will use this image for testing.

Specifically, we will mount the test data into the container directory `/app/data` via `docker run -v`, so **please ensure the `/app/data` directory in the image is empty.**

<style>
details summary {
  list-style: revert;
  cursor: pointer;
}
</style>