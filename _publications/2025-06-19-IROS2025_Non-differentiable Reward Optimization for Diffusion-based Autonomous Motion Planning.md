---
title: "Non-differentiable Reward Optimization for Diffusion-based Autonomous Motion Planning"
collection: publications
category: conferences
# permalink: /publication/2025-06-18-CVPR2025_Multi-modal Knowledge Distillation-based Human Trajectory Forecasting.md
excerpt: 'Giwon Lee\*, Daehee Park\*, Jaewoo Jeong\*, Kuk-Jin Yoon (\* denotes equal contribution)'
date: 2025-06-19
venue: 'IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)'
# slidesurl: 'http://academicpages.github.io/files/slides1.pdf'
# paperurl: 'https://openaccess.thecvf.com/content/CVPR2025/papers/Jeong_Multi-modal_Knowledge_Distillation-based_Human_Trajectory_Forecasting_CVPR_2025_paper.pdf'
# bibtexurl: 'http://academicpages.github.io/files/bibtex1.bib'
# citation: 'Your Name, You. (2009). &quot;Paper Title Number 1.&quot; <i>Journal 1</i>. 1(1).'
---
Safe and effective motion planning is crucial for autonomous robots. Diffusion models excel at capturing complex agent interactions, a fundamental aspect of decisionmaking in dynamic environments. Recent studies have successfully applied diffusion models to motion planning, demonstrating their competence in handling complex scenarios and accurately predicting multi-modal future trajectories. Despite their effectiveness, diffusion models have limitations in training objectives, as they approximate data distributions rather than explicitly capturing the underlying decision-making dynamics. However, the crux of motion planning lies in non-differentiable downstream objectives, such as safety (collision avoidance) and effectiveness (goal-reaching), which conventional learning algorithms cannot directly optimize. In this paper, we propose a reinforcement learning-based training scheme for diffusion motion planning models, enabling them to effectively learn non-differentiable objectives that explicitly measure safety and effectiveness. Specifically, we introduce a reward-weighted dynamic thresholding algorithm to shape a dense reward signal, facilitating more effective training and outperforming models trained with differentiable objectives. State-of-the-art performance on pedestrian datasets (CrowdNav, ETH-UCY) compared to various baselines demonstrates the versatility of our approach for safe and effective motion planning.