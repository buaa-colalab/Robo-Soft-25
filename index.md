---
layout: default
---

<!-- # RoboSoft'25: The 1st International Workshop on Vision-Language in Soft Robot -->

## Overview

Natural organisms, particularly soft-bodied animals, effectively explore and interact with their environments using highly redundant structures. Inspired by nature, engineers have integrated soft materials into rigid robotic joints, leading to significant advancements in the field of soft robotics. This innovative design enables robots to bend, twist, and continuously deform along their entire length. The inherently deformable nature of soft robots provides safe and adaptive solutions, especially in applications such as human-robot collaboration, search and rescue operations, and exploration and manipulation in unstructured environments.

However, soft robots are inherently underactuated, highly nonlinear mechanical systems, immersed in an elastic potential field and subject to dissipative forces that contribute to their stability. This underactuated nature, combined with the complex dynamics, presents significant challenges in controlling soft robots. These challenges have attracted researchers from various fields, including mechanical engineering, control theory, and computer science.

Recent advances in multimodal learning, particularly the integration of vision and language, offer a promising direction for improving soft robot autonomy. By leveraging vision-language models, soft robots can interpret human instructions in natural language while grounding their actions in visual perception. Therefore, this workshop focuses on multimodal soft robot planning, aiming to develop efficient control strategies that bridge the gap between high-level human intent and low-level robot execution. The ultimate goal is to enhance the adaptability and usability of soft robots in real-world applications.

## Invited Speakers

<div class="speaker-grid">
  <div class="speaker">
    <img src="pics/speakers/Cosimo Della Santina.png" alt="Cosimo Della Santina" class="speaker-img">
    <!-- https://cosimodellasantina.eu/ -->
    <p><a href="#">Cosimo Della Santina</a><br>TU Delft</p>
  </div>
  <div class="speaker">
    <img src="pics/speakers/Xiang LI.png" alt="Xiang LI" class="speaker-img">
    <!-- https://sites.google.com/view/homepageoflixiang -->
    <p><a href="#">Xiang LI</a><br>Tsinghua University</p>
  </div>
  <div class="speaker">
    <img src="pics/speakers/Shuqiang Jiang.png" alt="Shuqiang Jiang" class="speaker-img">
    <!-- https://vipl.ict.ac.cn/homepage/sqjiang/index.html -->
    <p><a href="#">Shuqiang Jiang</a><br>Chinese Academy of Sciences</p>
  </div>
  <div class="speaker">
    <img src="pics/speakers/Qin Jin.png" alt="Qin Jin" class="speaker-img">
    <!-- https://www.ruc-aim3.com/people.html -->
    <p><a href="#">Qin Jin</a><br>Renmin University of China</p>
  </div>
  <div class="speaker">
    <img src="pics/speakers/Jiebo Luo.png" alt="Jiebo Luo" class="speaker-img">
    <!-- https://scholar.google.com/citations?user=CcbnBvgAAAAJ&hl=en -->
    <p><a href="#">Jiebo Luo</a><br>University of Rochester</p>
  </div>
</div>

<style>
.speaker-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 30px;
  margin: 20px 0;
  width: 100%;
}
.speaker {
  text-align: center;
  width: 180px;
  margin-bottom: 20px;
}
.speaker-img {
  height: 180px;
  width: 180px;
  border-radius: 50%;
  object-fit: cover;
}
.speaker p {
  margin-top: 5px;
  font-size: 0.9em;
}
</style>

## Schedule

*Tentative schedule - Half-day workshop*


| Time | Event |
|-------------|-------------|
| TBD | Opening Remarks |
| TBD | Invited Talk: Cosimo Della Santina |
| TBD | Invited Talk: Xiang LI |
| TBD | Invited Talk: Shuqiang Jiang |
| TBD | Coffee Break |
| TBD | Invited Talk: Qin Jin |
| TBD | Invited Talk: Jiebo Luo |
| TBD | Invited Talk: Mohan Kankanhalli |
| TBD | Challenge Results Announcement |
| TBD | Challenge Winner Presentations |
| TBD | Paper Presentations |
| TBD | Panel Discussion & Closing Remarks |


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

## Program Committee

<div class="speaker-grid">
  <div class="speaker">
    <img src="pics/organizers/Si Liu.png" alt="Si Liu" class="speaker-img">
    <p><a href="#">Si Liu</a><br>Beihang University</p>
  </div>
  <div class="speaker">
    <img src="pics/organizers/Li Wen.png" alt="Li Wen" class="speaker-img">
    <!-- http://softrobotics.buaa.edu.cn/peoples.html -->
    <p><a href="#">Li Wen</a><br>Beihang University</p>
  </div>
  <div class="speaker">
    <img src="pics/organizers/Chen Gao.png" alt="Chen Gao" class="speaker-img">
    <!-- https://chengaopro.github.io/ -->
    <p><a href="#">Chen Gao</a><br>Beihang University</p>
  </div>
  <div class="speaker">
    <img src="pics/organizers/Ziyu Ren.png" alt="Ziyu Ren" class="speaker-img">
    <!-- http://softrobotics.buaa.edu.cn/peoples.html -->
    <p><a href="#">Ziyu Ren</a><br>Beihang University</p>
  </div>
  <div class="speaker">
    <img src="pics/organizers/LuTing Wang.png" alt="Luting Wang" class="speaker-img">
    <!-- https://scholar.google.com/citations?user=-TokIr8AAAAJ&hl=zh-CN&oi=ao -->
    <p><a href="#">Luting Wang</a><br>Beihang University</p>
  </div>
  <div class="speaker">
    <img src="pics/organizers/Jiaqi Liu.png" alt="Jiaqi Liu" class="speaker-img">
    <!-- http://softrobotics.buaa.edu.cn/peoples.html -->
    <p><a href="#">Jiaqi Liu</a><br>Beihang University</p>
  </div>
  <div class="speaker">
    <img src="pics/organizers/Heqing Yang.jpg" alt="Heqing Yang" class="speaker-img">
    <p><a href="#">Heqing Yang</a><br>Beihang University</p>
  </div>
  <div class="speaker">
    <img src="pics/organizers/Xingyu Chen.png" alt="Xingyu Chen" class="speaker-img">
    <!-- http://softrobotics.buaa.edu.cn/peoples.html -->
    <p><a href="#">Xingyu Chen</a><br>Beihang University</p>
  </div>
  <div class="speaker">
    <img src="pics/organizers/Youning Duo.png" alt="Youning Duo" class="speaker-img">
    <!-- http://softrobotics.buaa.edu.cn/peoples.html -->
    <p><a href="#">Youning Duo</a><br>Beihang University</p>
  </div>
</div>

## Challenge Technical Committee

<div class="speaker-grid">
  <div class="speaker">
    <img src="pics/organizers/Ziyu Wei.jpg" alt="Ziyu Wei" class="speaker-img">
    <p><a href="#">Ziyu Wei</a><br>Beihang University</p>
  </div>
  <div class="speaker">
    <img src="pics/placeholder.jpg" alt="Jiasheng Wu" class="speaker-img">
    <!-- http://softrobotics.buaa.edu.cn/peoples.html -->
    <p><a href="#">Jiasheng Wu</a><br>Beihang University</p>
  </div>
  <div class="speaker">
    <img src="pics/placeholder.jpg" alt="Ruipu Wu" class="speaker-img">
    <!-- http://softrobotics.buaa.edu.cn/peoples.html -->
    <p><a href="#">Ruipu Wu</a><br>Beihang University</p>
  </div>
</div>

## Call for Papers

This workshop aims to bring together researchers and practitioners from different disciplines to share ideas and methods on soft robot learning. We welcome research contributions as well as best-practice contributions on (but not limited to) the following topics:

- Multimodal robot manipulation in constrained environments.
- Multimodal navigation with mobile robots.
- Learning-based paradigms for soft robot control.
- Multimodal perception and modeling for soft-bodied robots.

All submissions must be original work not under review at any other workshop, conference, or journal. The workshop will accept papers describing completed work as well as work in progress. One submission format is accepted: full paper, which must follow the formatting guidelines of the main conference ACM MM 2025.

## Important Dates

- Paper submission deadline: July 11, 2025
- Paper notification: August 1, 2025
- Camera-ready submission: August 3, 2025
- Challenge submission deadline: July 30, 2025
- Workshop date: October 27–28, 2025

## Prizes

- Prizes for each track winner
- Best paper award

<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
