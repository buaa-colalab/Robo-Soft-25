---
layout: default
---

<!-- # RoboSoft'25: The 1st International Workshop on Vision-Language in Soft Robot -->

## Overview

The rapid development of embodied intelligence, realized through robots’ interaction with the environment, has evolved from rule-based control to autonomous systems integrating deep learning and reinforcement learning. Current research in embodied intelligence predominantly focuses on rigid robotic platforms. However, the characteristics of rigid materials not only limit flexibility and increase collision risks but also render them insufficiently adaptive in unstructured and constrained environments. To address these limitations, researchers have drawn inspiration from the biological traits of mollusks, introducing flexible materials into robotic design and advancing the field of embodied intelligence centered on soft robotic platforms. Soft robots, owing to their deformable properties, offer highly adaptive and safe solutions, particularly for human-robot collaboration scenarios and tasks in complex environments. Nevertheless, their underactuated nature and strong nonlinear dynamic characteristics pose significant challenges for the design of autonomous control systems.

This workshop focuses on the multimodal perception and decision-making of soft robots, delving into and promoting cutting-edge technologies in embodied intelligence with soft robotics as the carrier. We aim to bring together researchers and practitioners to explore emerging challenges and solutions, including the design of adaptive control systems for soft robots, the integration of multimodal sensory data, and the optimization of decision-making algorithms under nonlinear dynamics.

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
    <img src="pics/speakers/Qin Jin.jpg" alt="Qin Jin" class="speaker-img">
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
## Call for Papers

This workshop aims to bring together researchers and practitioners from different disciplines to share ideas and methods on soft robot learning. We welcome research contributions as well as best-practice contributions on (but not limited to) the following topics:

- Multimodal Embodied Navigation: visual navigation, vision-language navigation, soft robot navigation
- Multimodal Embodied Manipulation: grasping, dexterous manipulation, soft-hand manipulation, tool manipulation
- Embodied Reasoning: spatial reasoning, affordance learning, task planning
- Embodied Perception: multi-modal perception, active perception
- Embodied Simulation: 2D/3D reconstruction, sim-to-real, benchmark
- Control Methods for Soft Robots: model-based/learning-based control methods

For this workshop, we accept the following type of papers：
- 4–8 pages for the main text, plus up to 2 pages for references.
- Topics include but are not limited to original ideas, perspectives, research visions, and open challenges in the themes outlined above.

Submission Website: https://openreview.net/group?id=acmmm.org/ACMMM/2025/Workshop/Robosoft

Submission templates are available on the ACM MM 2025 website.

**Submissions must adhere to the ACM MM 2025 submission policies.**

<strong><span style="color: red;">The workshop will finally select a Best Paper Award.</span></strong>  

## Challenge

To advance research in multimodal soft robot planning, we propose two challenge tasks.

This competition employs the open-source software Elastica developed by the Gazzola Lab at UIUC for soft-body dynamics modeling, establishing a benchmark platform for soft robot dynamics and interaction simulation. In this benchmark, soft robots are modeled as a single Cosserat rod freely moving in 3D space—serving as a flexible manipulator in Task 1 and a flexible mobile body in Task 2. The soft rod features an elastic Young's modulus of 10 MPa, exhibiting the typical bending stiffness of soft robots.

The actuation mechanism is realized through internal moments distributed along the rod's length, where the continuous activation function is characterized by spline curves defined by N independent control points, approaching zero at both ends of the rod. Precise control is achieved by decomposing the overall actuation into orthogonal moment functions in the local normal, binormal (inducing bending), and orthogonal directions (inducing torsion).

### Task 1: Vision-Language Manipulation for Soft Robot
**Vision-Language Manipulation** aims to endow soft robots with the ability to interact with objects based on human instructions and visual perception—a capability crucial for manufacturing and medical fields, encompassing scenarios such as object grasping, component assembly, item classification, and even surgical assistance. In this task, the soft robot must operate within a complex workspace containing various objects (e.g., cubes, spheres, cones). One end of the robot is fixed to a base, while the other end moves freely to accomplish manipulation tasks.

The system inputs include natural language instructions (specifying the object to manipulate and its target position) and multi-view visual observations. The robot must first recognize and localize the target object from visual inputs, then execute motions to transport it to the specified position. The operation is deemed successful when the object accurately reaches the target location.

<div class="video-container">
  <div class="video-item">
    <video controls class="side-by-side-video">
      <source src="videos/VLM-1.mp4" type="video/mp4">
    </video>
    <p class="video-caption">Instruction: Move the football to the basketball</p>
  </div>
  
  <div class="video-item">
    <video controls class="side-by-side-video">
      <source src="videos/VLM-2.mp4" type="video/mp4">
    </video>
    <p class="video-caption">Instruction: Move the smaller yellow roadblocks next to the larger roadblocks</p>
  </div>
</div>


### Task 2: Vision-Language Navigation for Soft Robot
**Vision-Language Navigation** requires soft robots to autonomously explore complex environments by comprehending linguistic instructions and parsing visual cues. This task holds significant importance for applications such as disaster search and rescue, as well as exploration. Within this task, the agent must process synchronized multimodal inputs comprising visual observations and natural language instructions, necessitating cross-modal alignment between the vision-language modality and soft-body dynamics modeling. Instructions are translated into continuum mechanics actions.

The solution space must jointly optimize semantic localization accuracy, deformation trajectory smoothness, and obstacle avoidance feasibility under time-varying boundary conditions. Vision-Language Navigation for soft robots establishes a new research domain in embodied intelligence, where soft robots execute navigation tasks through morphological adaptation in dynamic environments.

<div class="video-container">
  <div class="video-item">
    <video controls class="side-by-side-video">
      <source src="videos/VLN-1.mp4" type="video/mp4">
    </video>
    <p class="video-caption">Instruction: Navigate to the basketball between two footballs</p>
  </div>
  
  <div class="video-item">
    <video controls class="side-by-side-video">
      <source src="videos/VLN-2.mp4" type="video/mp4">
    </video>
    <p class="video-caption">Instruction: Navigate to the football next to the yellow cone</p>
  </div>
</div>


<style>
.wider {
  width: 90%;
  margin: 20px auto;
}
.video-container {
  display: flex;
  gap: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.video-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.side-by-side-video {
  width: 100%;
  height: auto;
  max-height: 400px;
}

.video-caption {
  color: #666;
  font-size: 0.9rem;
  text-align: left;
  margin: 0;
  padding: 5px 0;
}

@media (max-width: 768px) {
  .video-container {
    flex-direction: column;
  }
  .video-caption {
    font-size: 0.8rem;
  }
}
</style>

## Important Dates

- Paper submission deadline: July 11, 2025
- Paper notification: August 1, 2025
- Camera-ready submission: August 3, 2025
- Challenge submission deadline: July 30, 2025
- Workshop date: October 27–28, 2025


## Program Committee

<div class="speaker-grid">
  <div class="speaker">
    <img src="pics/organizers/Si Liu.jpg" alt="Si Liu" class="speaker-img">
    <p><a href="#">Si Liu</a><br>Beihang University</p>
  </div>
  <div class="speaker">
    <img src="pics/organizers/Li Wen.jpg" alt="Li Wen" class="speaker-img">
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
    <img src="pics/organizers/Hongliang Huang.jpg" alt="Hongliang Huang" class="speaker-img">
    <p><a href="#">Hongliang Huang</a><br>Beihang University</p>
  </div>
  <div class="speaker">
    <img src="pics/organizers/Xudong Liu.jpg" alt="Xudong Liu" class="speaker-img">
    <p><a href="#">Xudong Liu</a><br>Beihang University</p>
  </div>
</div>

<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
