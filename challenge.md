---
layout: default
---

## Challenge

To advance research in multimodal soft robot planning, we propose two challenge tasks:

### Task 1: Vision-Language Manipulation for Soft Robot

In this task, a soft robot operates within a cluttered workspace containing various objects, such as cubes, spheres, and cones. One end of the soft robot is fixed to the surface, while the other end moves freely to perform manipulation. The robot receives natural language instruction and multi-perspective visual observations as inputs. The instruction specifies the objects to be manipulated and their target locations.

<div class="figure-grid">
  <div class="figure-item">
    <img src="pics/1a.png" alt="Task 1 Example A" class="task-img">
    <p class="caption">Instruction: "pick up the cone and place it in the gray area on the right side of the workspace."</p>
  </div>
  <div class="figure-item">
    <img src="pics/1c.png" alt="Task 1 Example C" class="task-img">
    <p class="caption">Instruction: "pick up the blue cylinder on the left and place it in the gray area."</p>
  </div>
  <div class="figure-item">
    <img src="pics/1d.png" alt="Task 1 Example D" class="task-img">
    <p class="caption">Instruction: "place the blue cube in the blue area and then place the green cube in the green area."</p>
  </div>
  <div class="figure-item">
    <img src="pics/1b.png" alt="Task 1 Example B" class="task-img">
    <p class="caption">Instruction: "pick up the red cube behind the tall cone and place it in the red area."</p>
  </div>
</div>

<style>
.figure-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  gap: 15px;
  margin: 20px 0;
}
.figure-item {
  width: 45%;
  min-width: 300px;
  text-align: center;
  margin-bottom: 20px;
}
.task-img {
  max-width: 100%;
  border: 1px solid #ddd;
}
.caption {
  font-size: 0.9em;
  margin-top: 8px;
}
</style>

#### Easy-Track: Single-Object Manipulation
In the Easy-Track, each instruction involves only one object. For example, an instruction might be: "Pick up the cone and place it in the gray area on the right side of the workspace."

<div class="figure-item wider">
  <img src="pics/3.png" alt="Task 1 Easy-Track Illustration" class="task-img">
  <p class="caption">Illustration of Task 1 Easy-Track: The soft robot must reach the cone and place it in the target area while avoiding collision with the cube in between.</p>
</div>

#### Hard-Track: Multi-Object Manipulation
The Hard-Track increases complexity by involving multiple objects within a single manipulation task. For example, an instruction might be: "Pick up the red cube behind the tall cone and place it in the red area."

<div class="figure-item wider">
  <img src="pics/4.png" alt="Task 1 Hard-Track Illustration" class="task-img">
  <p class="caption">Illustration of Task 1 Hard-Track: The soft robot must first move the cone and cylinder obstacles before placing the cube in its target location.</p>
</div>

### Task 2: Vision-Language Navigation for Soft Robot

Soft robot vision-language navigation establishes a novel research field for embodied intelligence where compliant robots execute navigation tasks through morphological adaptation in dynamic environments.

<div class="figure-grid">
  <div class="figure-item">
    <img src="pics/task2-a.svg" alt="Task 2 Example A" class="task-img">
    <p class="caption">Easy-Track: Navigation in sparse obstacles example</p>
  </div>
  <div class="figure-item">
    <img src="pics/task2-b.svg" alt="Task 2 Example B" class="task-img">
    <p class="caption">Easy-Track: Different view of navigation with sparse obstacles</p>
  </div>
  <div class="figure-item">
    <img src="pics/task2-c.svg" alt="Task 2 Example C" class="task-img">
    <p class="caption">Hard-Track: Navigation in dense obstacles example</p>
  </div>
  <div class="figure-item">
    <img src="pics/task2-d.svg" alt="Task 2 Example D" class="task-img">
    <p class="caption">Hard-Track: Multiple sub-goals navigation scenario</p>
  </div>
</div>

<!-- ### Evaluation Metrics

We adopt four metrics to evaluate the performance:

1. **Success Rate (SR)**: Defined as the ratio of successfully completed tasks within the maximum steps.
   
   <p align="center">
     <img src="https://latex.codecogs.com/svg.latex?\Large&space;SR=\frac{N_{success}}{N_{total}}" alt="Success Rate Formula">
   </p>

2. **Average Collision Rate (CR)**: Measures safety performance by considering both self-collisions and environmental collisions.
   
   <p align="center">
     <img src="https://latex.codecogs.com/svg.latex?\Large&space;CR=\frac{1}{N_{total}}\sum_{i=1}^{N_{total}}\frac{N_{collision}^i}{N_{steps}^i}" alt="Collision Rate Formula">
   </p>

3. **Task Completion Efficiency (TCE)**: Evaluates the model efficiency using the normalized inverse steps.
   
   <p align="center">
     <img src="https://latex.codecogs.com/svg.latex?\Large&space;TCE=\frac{1}{N_{success}}\sum_{i=1}^{N_{success}}\frac{S_{max}-S_i}{S_{max}-S_{min}}" alt="TCE Formula">
   </p>

4. **Comprehensive Evaluation Score (CES)**: A weighted composite score incorporating the above evaluation metrics.
   
   <p align="center">
     <img src="https://latex.codecogs.com/svg.latex?\Large&space;CES=\alpha\cdot{SR}+\beta\cdot(1-CR)+\gamma\cdot{TCE}" alt="CES Formula">
   </p> -->


<style>
.wider {
  width: 90%;
  margin: 20px auto;
}
</style>